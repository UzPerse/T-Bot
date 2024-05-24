import requests
import telegram



def send_message_to_telegram(message, image_url):
    TOKEN = "6641628674:AAFzzIoJ2Ua0041wJQ5UL3veT0UbWBPb2bo"
    chat_id = "5915618084"
   
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}&photo={image_url}&caption={message}"
    print(requests.get(url).json()) 
