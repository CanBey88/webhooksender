import requests

def send_webhook_message():
    webhook_url = input("Webhook URL'sini girin: ")
    message = input("Göndermek istediğiniz mesajı girin: ")

    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, json=payload, headers=headers)
        response.raise_for_status()  # HTTP isteği başarılıysa devam et, değilse hata fırlat
        print("Mesaj başarıyla gönderildi!")
    except Exception as e:
        print("Mesaj gönderme başarısız. Hata:", str(e))
        if response.status_code != 200:
            print("HTTP İsteği Durumu:", response.status_code)
            print("API Hata Mesajı:", response.json())

# Webhook URL'si ve mesajı kullanıcıdan alarak konsola yazdırma işlemini gerçekleştirin
send_webhook_message()
