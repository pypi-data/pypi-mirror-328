"""FileTransferManager类实现

处理文件夹级别的传输操作，包括上传、下载和同步功能。
"""

import os
import json
from typing import Dict, List, Any, Tuple, Optional
from pathlib import Path
from datetime import datetime

from telethon.tl.types import Message
from telethon.tl.custom import Dialog
from tqdm import tqdm
from loguru import logger

from .client import TelegramTransferClient

class FileTransferManager:
    """文件传输管理器
    
    处理文件夹级别的传输操作，包括：
    - 文件夹上传
    - 文件夹下载
    - 文件夹同步
    - 断点续传
    - 进度追踪
    """
    
    def __init__(self, client: TelegramTransferClient):
        """初始化传输管理器
        
        Args:
            client: TelegramTransferClient实例
        """
        self.client = client
        # 默认使用脚本所在目录
        default_state_file = os.path.join(os.path.dirname(__file__), 'transfer_state.json')
        # 从配置中获取自定义路径
        self.state_file = self.client.config.get('state', {}).get('file', default_state_file)
        self.state_file = os.path.expanduser(self.state_file)
        self.load_state()
        
    def load_state(self):
        """加载传输状态"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                self.state = json.load(f)
        else:
            self.state = {}
            
    def save_state(self):
        """保存传输状态"""
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        
        # 转换datetime对象为ISO格式字符串
        def datetime_handler(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
        
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, default=datetime_handler)
            
    def _get_transfer_key(self, folder_path: str, target: str) -> str:
        """生成传输任务的唯一标识"""
        return f"{folder_path}:{target}"
        
    def _create_progress_callback(self, desc: str, total: int):
        """创建进度回调函数
        
        Args:
            desc: 进度条描述
            total: 总大小
            
        Returns:
            callable: 进度回调函数
        """
        pbar = tqdm(total=total, desc=desc, unit='B', unit_scale=True)
        last_value = [0]
        
        def callback(current, total):
            update_size = current - last_value[0]
            pbar.update(update_size)
            last_value[0] = current
            
        return callback
        
    async def upload_folder(self,
                          folder_path: str,
                          target: str,
                          caption_template: str = None) -> Dict[str, Any]:
        """上传文件夹
        
        Args:
            folder_path: 文件夹路径
            target: 目标用户/频道
            caption_template: 文件描述模板
            
        Returns:
            Dict: 上传结果统计
        """
        folder_path = os.path.expanduser(folder_path)
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"路径不是文件夹: {folder_path}")
            
        # 扫描文件夹
        files_info = self.client.scan_folder(folder_path)
        if not files_info:
            logger.warning("文件夹为空")
            return {'success': [], 'failed': []}
            
        # 获取未完成的传输
        transfer_key = self._get_transfer_key(folder_path, target)
        uploaded = self.state.get(transfer_key, {}).get('uploaded', [])
        
        # 准备上传
        success = []
        failed = []
        
        for rel_path, info in files_info.items():
            if rel_path in uploaded:
                logger.info(f"跳过已上传的文件: {rel_path}")
                success.append(rel_path)
                continue
                
            file_path = os.path.join(folder_path, rel_path)
            # 添加文件结构元数据
            metadata = {
                'original_path': rel_path,
                'size': info['size'],
                'mtime': info['mtime'].isoformat()
            }
            caption = json.dumps(metadata) if not caption_template else caption_template.format(
                path=rel_path,
                size=info['size'],
                mtime=info['mtime'].isoformat()
            )
            
            try:
                # 创建进度回调
                callback = self._create_progress_callback(
                    f"上传 {rel_path}",
                    info['size']
                )
                
                # 上传文件
                await self.client.upload_file(
                    file_path,
                    target,
                    caption=caption,
                    progress_callback=callback
                )
                
                success.append(rel_path)
                uploaded.append(rel_path)
                
                # 保存进度
                self.state[transfer_key] = {
                    'uploaded': uploaded,
                    'last_update': datetime.now().isoformat()
                }
                self.save_state()
                
            except Exception as e:
                logger.error(f"上传失败 {rel_path}: {str(e)}")
                failed.append(rel_path)
                
        return {
            'success': success,
            'failed': failed
        }
        
    async def download_folder(self,
                            source: str,
                            download_path: str,
                            limit: int = None) -> Dict[str, Any]:
        """下载文件夹
        
        Args:
            source: 源用户/频道
            download_path: 下载路径
            limit: 获取消息数量限制
            
        Returns:
            Dict: 下载结果统计
        """
        download_path = os.path.expanduser(download_path)
        os.makedirs(download_path, exist_ok=True)
        
        # 获取对话
        entity = await self.client.get_entity_by_id_or_username(source)
        messages = await self.client.get_file_messages(entity, limit)
        
        if not messages:
            logger.warning("没有找到文件消息")
            return {'success': [], 'failed': []}
            
        # 获取未完成的传输
        transfer_key = self._get_transfer_key(source, download_path)
        downloaded = self.state.get(transfer_key, {}).get('downloaded', [])
        
        # 准备下载
        success = []
        failed = []
        
        for message in messages:
            if not message.file:
                continue
                
            try:
                # 尝试从caption中解析元数据
                metadata = None
                if message.message:
                    try:
                        metadata = json.loads(message.message)
                    except json.JSONDecodeError:
                        pass
                
                # 确定文件名和路径
                if metadata and 'original_path' in metadata:
                    file_name = metadata['original_path']
                    file_path = os.path.join(download_path, file_name)
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                else:
                    file_name = message.file.name or f"file_{message.id}"
                    file_path = os.path.join(download_path, file_name)
                
                if file_name in downloaded:
                    logger.info(f"跳过已下载的文件: {file_name}")
                    success.append(file_name)
                    continue
                
                # 创建进度回调
                callback = self._create_progress_callback(
                    f"下载 {file_name}",
                    message.file.size
                )
                
                # 下载文件
                await self.client.download_file(
                    message,
                    file_path,
                    progress_callback=callback
                )
                
                success.append(file_name)
                downloaded.append(file_name)
                
                # 保存进度
                self.state[transfer_key] = {
                    'downloaded': downloaded,
                    'last_update': datetime.now().isoformat()
                }
                self.save_state()
                
            except Exception as e:
                logger.error(f"下载失败 {file_name}: {str(e)}")
                failed.append(file_name)
                
        return {
            'success': success,
            'failed': failed
        }
        
    async def sync_folder(self,
                         folder_path: str,
                         target: str,
                         sync_mode: str = 'to',
                         caption_template: str = None) -> Dict[str, Any]:
        """同步文件夹
        
        Args:
            folder_path: 文件夹路径
            target: 目标用户/频道
            sync_mode: 同步模式，'to'表示上传到远程，'from'表示从远程下载
            caption_template: 文件描述模板
            
        Returns:
            Dict: 同步结果统计
        """
        folder_path = os.path.expanduser(folder_path)
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"路径不是文件夹: {folder_path}")
            
        # 获取本地文件状态
        local_state = self.client.scan_folder(folder_path)
        
        # 获取远程文件状态
        entity = await self.client.get_entity_by_id_or_username(target)
        messages = await self.client.get_file_messages(entity)
        remote_state = {}
        
        for msg in messages:
            if not msg.file or not msg.message:
                continue
            try:
                metadata = json.loads(msg.message)
                if 'original_path' in metadata:
                    remote_state[metadata['original_path']] = {
                        'size': msg.file.size,
                        'mtime': datetime.fromisoformat(metadata['mtime']),
                        'message_id': msg.id
                    }
            except json.JSONDecodeError:
                continue
        
        # 比较差异
        local_files = set(local_state.keys())
        remote_files = set(remote_state.keys())
        
        # 需要处理的文件
        to_download = remote_files - local_files  # 远程有但本地没有
        to_upload = local_files - remote_files    # 本地有但远程没有
        to_delete_local = local_files - remote_files if sync_mode == 'from' else set()
        to_delete_remote = remote_files - local_files if sync_mode == 'to' else set()
        
        success = []
        failed = []
        deleted = []
        
        # 处理文件同步
        if sync_mode == 'from':
            # 下载远程文件到本地
            for rel_path in to_download:
                try:
                    msg_id = remote_state[rel_path]['message_id']
                    message = await self.client.client.get_messages(entity, ids=msg_id)
                    if not message or not message.file:
                        continue
                        
                    file_path = os.path.join(folder_path, rel_path)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    
                    callback = self._create_progress_callback(
                        f"下载 {rel_path}",
                        message.file.size
                    )
                    
                    await self.client.download_file(
                        message,
                        file_path,
                        progress_callback=callback
                    )
                    
                    success.append(rel_path)
                    
                except Exception as e:
                    logger.error(f"下载失败 {rel_path}: {str(e)}")
                    failed.append(rel_path)
            
            # 删除本地多余文件
            for rel_path in to_delete_local:
                try:
                    file_path = os.path.join(folder_path, rel_path)
                    os.remove(file_path)
                    deleted.append(rel_path)
                except Exception as e:
                    logger.error(f"删除本地文件失败 {rel_path}: {str(e)}")
                    
        else:  # sync_mode == 'to'
            # 上传本地文件到远程
            for rel_path in to_upload:
                try:
                    file_path = os.path.join(folder_path, rel_path)
                    info = local_state[rel_path]
                    
                    metadata = {
                        'original_path': rel_path,
                        'size': info['size'],
                        'mtime': info['mtime'].isoformat()
                    }
                    caption = json.dumps(metadata) if not caption_template else caption_template.format(
                        path=rel_path,
                        size=info['size'],
                        mtime=info['mtime'].isoformat()
                    )
                    
                    callback = self._create_progress_callback(
                        f"上传 {rel_path}",
                        info['size']
                    )
                    
                    await self.client.upload_file(
                        file_path,
                        target,
                        caption=caption,
                        progress_callback=callback
                    )
                    
                    success.append(rel_path)
                    
                except Exception as e:
                    logger.error(f"上传失败 {rel_path}: {str(e)}")
                    failed.append(rel_path)
            
            # 删除远程多余文件
            for rel_path in to_delete_remote:
                try:
                    msg_id = remote_state[rel_path]['message_id']
                    await self.client.client.delete_messages(entity, [msg_id])
                    deleted.append(rel_path)
                except Exception as e:
                    logger.error(f"删除远程文件失败 {rel_path}: {str(e)}")
        
        # 保存同步状态
        self.state[self._get_transfer_key(folder_path, target)] = {
            'files': local_state if sync_mode == 'to' else remote_state,
            'last_update': datetime.now().isoformat()
        }
        self.save_state()
        
        return {
            'success': success,
            'failed': failed,
            'deleted': deleted
        }
