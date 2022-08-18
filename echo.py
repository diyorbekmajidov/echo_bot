import requests
TOKEN = '5468504239:AAFnCFuZH99q0HYYF0iux_DGPrZoyFLwk9A'

# send Message
def send_message(chat_id:int, text:str):
    payload = {
        "chat_id":chat_id ,
        "text":text
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url, params=payload)

# send Photo
def send_Photo(chat_id:int, photo):
    payload = {
        'chat_id':chat_id ,
        'photo':photo
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    requests.get(url,params=payload)

# send Document
def send_document(chat_id:int,document):
    payload={
        'chat_id':chat_id ,
        'document':document
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    requests.get(url,params=payload)

# send dice
def send_dice(chat_id,emoji):
    payload = {
        'chat_id':chat_id ,
        'emoji':emoji
    }
    url=f'https://api.telegram.org/bot{TOKEN}/sendDice'
    requests.get(url,params=payload)


# get Updates 
def get_updates():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    result1 = requests.get(url)
    data = result1.json()['result'][-1]
    update_id = data['update_id']
    text = data['message'].get('text')
    photo = data['message'].get('photo')
    document = data['message'].get('document')
    emoji=data['message'].get('emoji')
    chat_id = data['message']['chat']['id']
    return chat_id, document, text, photo, update_id,emoji


# Last update id
last_update_id = -1 
# send message through loop 
while True:
    chat_id, document, text, photo, update_id, emoji = get_updates()
    if last_update_id != update_id:
        if text !=None:
            send_message(chat_id,text)
        elif photo !=None:
            photo=photo[0]['file_id']
            send_Photo(chat_id,photo)
        elif document != None:
            document = document['file_id']
            send_document(chat_id,document)
        elif emoji!=None:
            emoji=emoj['dice']
            send_dice(chat_id, emoji)
        last_update_id=update_id



