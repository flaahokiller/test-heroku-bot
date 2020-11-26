from pyrogram import Client

API_ID = input("API_ID: ")
print("Now API_HASH")
API_HASH = input("API_HASH: ")

with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as app:
    print(app.export_session_string())
