from pyrogram import Client, filters
import requests
import random

api_id = 26480985 #--Add your Api Id here
api_hash = '56c935fae1c5c86ba5a3af655f8caa9d' #--Enter Api Hash Here

token = '7195594057:AAHfeGa1M11mAVFOo8SfUDYPZG-vIAx8_Ow' #--Enter Bot Token Here.

emojis = ["馃憤", "馃憥", "鉂わ笍", "馃敟", "馃グ", "馃憦", "馃榿", "馃", "馃く", "馃槺", "馃が", "馃槩", "馃帀", "馃ぉ", "馃ぎ", "馃挬", "馃檹", "馃憣", "馃晩", "馃ぁ", "馃ケ", "馃ゴ", "馃槏", "馃惓", "鉂も�嶐煍�", "馃寶", "馃尛", "馃挴", "馃ぃ", "鈿★笍", "馃崒", "馃弳", "馃挃", "馃え", "馃槓", "馃崜", "馃嵕", "馃拫", "馃枙", "馃槇", "馃槾", "馃槶", "馃", "馃懟", "馃懆鈥嶐煉�", "馃憖", "馃巸", "馃檲", "馃槆", "馃槰", "馃", "鉁嶏笍", "馃", "馃", "馃巺", "馃巹", "鈽冿笍", "馃拝", "馃お", "馃椏", "馃啋", "馃挊", "馃檳", "馃", "馃槝", "馃拪", "馃檴", "馃槑", "馃懢", "馃し鈥嶁檪", "馃し", "馃し鈥嶁檧", "馃槨"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message()
async def react_to_message(client, message):
    chat_id = message.chat.id
    message_id = message.id
    
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    
    url = f'https://api.telegram.org/bot{token}/setMessageReaction'

    # Parameters for the request
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': [{
            "type": "emoji",
            "emoji": random_emoji
        }]
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        print("Reaction set successfully!")
        print("Response content:", response.content)
    else:
        print(f"Failed to set reaction. Status code: {response.status_code}")
        print("Response content:", response.content)
    
app.run()
