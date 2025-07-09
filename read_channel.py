from telethon.sync import TelegramClient

# Replace with your actual values
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
channel = 'https://t.me/YOUR_CHANNEL'  # or '@channelusername'

# Create the client and connect
with TelegramClient('session_name', api_id, api_hash) as client:
    for message in client.iter_messages(channel, limit=10):
        print(f"{message.date} | {message.sender_id} | {message.text}\n")