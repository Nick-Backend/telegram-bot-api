
import requests
from config  import TOKEN

class Bot:
    def __init__(self, token: str) -> None:
        self.url = f"https://api.telegram.org/bot{token}"

    def get_me(self):
        get_me_url = f"{self.url}/getMe"
        response = requests.get(get_me_url)

        return response.json() 
   

    def get_update(self):
        get_update_url = f"{self.url}/getUpdates"
        response = requests.get(get_update_url)

        return response.json()



    def send_message(self, chat_id: int, text: str):
        get_send_massage_url = f"{self.url}/sendMessage"

        params ={
            "chat_id": chat_id,
            "text": text
        }
        requests.get(get_send_massage_url, params=params)

    def send_voice(self, chat_id: int, file_id: str):
        url = f"{self.url}/sendVoice"
        params = {
            "chat_id": chat_id,
            "voice": file_id
        }
        requests.get(url, params=params)

    def send_photo(self, chat_id: int, file_id: str):
        url = f"{self.url}/sendPhoto"
        params = {
            "chat_id": chat_id,
            "photo": file_id
        }

        requests.get(url, params=params)



    def echo(self):
        offset = 0

        while True:
            response = requests.get(
                f"{self.url}/getUpdates",
                params={"offset": offset, "timeout": 30}
            ).json()

            for update in response["result"]:
                offset = update["update_id"] + 1

                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]

                if "text" in message:
                    self.send_message(chat_id, message["text"])

                elif "photo" in message:
                    file_id = message["photo"][-1]["file_id"]
                    self.send_photo(8416278601, file_id)

                elif "voice" in message:
                    file_id = message["voice"]["file_id"]
                    self.send_voice(8416278601, file_id)

    
bot = Bot(TOKEN)

bot.send_message(chat_id = 8416278601, text = "Salom bu bot ishga tushdi")
# pprint(bot.get_me())
# pprint(bot.get_update())
bot.echo()








