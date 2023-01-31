import requests # Mesaj Göndermek İçin Gerekli Olan Modül
import cv2# Kamera Modülü

bot_token = "" # Botfather Dan Aldığınız Bot Tokeni
chat_id = "" # chat id öğrenmek için https://t.me/chatIDrobot bu bota mesaj atın size geri dönüş olarak chat id vericek. Sistemi kullanamdan önce botu başlatmayı unutmayın.
kayıt_yolu = "D:/Poyraz/test.jpg" #Buraya Fotoğrafın Çekildikten sonra kaydedilceği yeri yazın bunun sebebi kaydetmeden göndermezsiniz. Örnek: C:/Poyraz/python.jpg özellikle yolun sonuna dosyaismi.jpg yazmayı unutmayın.



camera = cv2.VideoCapture(0)# Video çekmeye başla
return_value,image = camera.read()# İlk fotğrafı al
cv2.imwrite(kayıt_yolu, image)# Dosyayı Kaydet

camera.release()# ?
cv2.destroyAllWindows()# Tüm ekranları kapat

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
