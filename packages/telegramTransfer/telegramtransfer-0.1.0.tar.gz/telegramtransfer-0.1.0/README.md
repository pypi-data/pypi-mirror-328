# Telegram Transfer

A Telegram file transfer tool based on Telethon, supporting folder upload, download, and synchronization.

## Features

- Folder upload, download, and sync
- Resume broken transfers
- Incremental synchronization
- Real-time progress display
- File integrity verification
- Session management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ooopus/telegramTransfer.git
cd telegramTransfer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the application:

Create a `config.json` file in the project directory (you can copy from `config.json.example`):
```json
{
    "api": {
        "id": "your_api_id",
        "hash": "your_api_hash"
    }
}
```

You can obtain API ID and Hash from https://my.telegram.org

## Usage

### Basic Commands

```bash
# Upload folder
python -m telegramTransfer upload /path/to/folder --to username
# Upload with sync mode enabled
python -m telegramTransfer upload /path/to/folder --to username --sync

# Download folder
python -m telegramTransfer download /path/to/folder --from username
# Download with sync mode enabled
python -m telegramTransfer download /path/to/folder --from username --sync
```

### Command Arguments

- `folder`: Path to the folder to process
- `--to`: Target user/channel, supports the following formats:
  - Numeric ID (e.g., 4639628806)
  - Username (e.g., @username)
  - Topic Group Link (e.g., https://t.me/c/2257928502/2)
- `--from`: Source user/channel, supports the same formats as --to
- `--caption`: File description template
- `--session`: Specify session name
- `--new-session`: Force create new session
- `--api-id`: Telegram API ID
- `--api-hash`: Telegram API Hash
- `--sync`: Enable incremental sync mode

### Advanced Features

1. Resume Broken Transfers:
   - Simply rerun the command to continue from the last point

2. Incremental Sync:
   - Only transfer changed files
   - Support file modification detection
   - Maintain directory structure

3. Session Management:
   - Multiple account support
   - Session persistence
   - Automatic login

## Notes

1. First-time use requires login verification
2. Stable network connection recommended
3. Large file transfers may be subject to Telegram limitations
4. Please comply with Telegram's Terms of Service