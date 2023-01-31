import requests # Module required to send a message
import cv2# Camera Module

bot_token = "1833604651:AAH2zP7mxtvQ-hYSDcsFVWmrla7lsWj8Xpw" #Bot Token You Got From Bot Father
chat_id = "1480907457" # Chat id to learn https://t.me/chatıdrobot this boat message will give you a return to chat id.Don't forget to start the bot before using the system.
kayıt_yolu = "D:/Poyraz/test.jpg" #Write the place where the photo is taken here after taking the photo, you will not send it without saving it.Example: C: /poyraz/python.jpg, especially at the end of the road filename.jpg.



camera = cv2.VideoCapture(0)# startShootingVideos
return_value,image = camera.read()# Take the first photo
cv2.imwrite(kayıt_yolu, image)# Save the file

camera.release()# ?
cv2.destroyAllWindows()# Turn off all screens

with open(kayıt_yolu, 'rb') as f:
    files = {'photo': f}
    data = {'chat_id': chat_id}
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    response = requests.post(url, data=data, files=files)
    if response.status_code == 200:
        message = "Yeni Giriş Tespit Edildi Windows PC"
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': message}
        requests.post(url, data=data)
    else:
        exit