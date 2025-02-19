# Telegram Transfer

一个基于 Telethon 的 Telegram 文件传输工具，支持文件夹上传、下载和同步功能。

## 特性

- 文件夹上传、下载和同步
- 断点续传功能
- 增量同步支持
- 实时进度显示
- 文件完整性验证
- 会话管理支持

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/ooopus/telegramTransfer.git
cd telegramTransfer
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置：
创建一个 `config.json` 文件（你可以从 `config.json.example` 复制）：
```json
{
    "api": {
        "id": "your_api_id",
        "hash": "your_api_hash"
    }
}
```

API ID 和 Hash 可以从 https://my.telegram.org 获取。

## 使用方法

### 基本命令

```bash
# 上传文件夹
python -m telegramTransfer upload /path/to/folder --to username
# 上传并启用增量同步
python -m telegramTransfer upload /path/to/folder --to username --sync

# 下载文件夹
python -m telegramTransfer download /path/to/folder --from username
# 下载并启用增量同步
python -m telegramTransfer download /path/to/folder --from username --sync
```

### 命令参数

- `folder`: 要处理的文件夹路径
- `--to`: 目标用户/频道，支持以下格式：
  - 数字 ID（例如：4639628806）
  - 用户名（例如：@username）
  - Topic Group 链接（例如：https://t.me/c/2257928502/2）
- `--from`: 源用户/频道，支持与 --to 相同的格式
- `--caption`: 文件描述模板
- `--session`: 指定会话名称
- `--new-session`: 强制创建新会话
- `--api-id`: Telegram API ID
- `--api-hash`: Telegram API Hash
- `--sync`: 启用增量同步模式

### 高级功能

1. 断点续传：
   - 传输中断后重新运行命令即可从断点处继续

2. 增量同步：
   - 仅传输发生变更的文件
   - 支持文件修改检测
   - 保持目录结构

3. 会话管理：
   - 多账号支持
   - 会话持久化
   - 自动登录

## 注意事项

1. 首次使用需要进行登录验证
2. 建议使用稳定的网络连接
3. 大文件传输可能受到 Telegram 限制
4. 请遵守 Telegram 服务条款