Boxabar - bu turli xil xabar yuborish usullarini (SMS, Email, Telegram) qo'llab-quvvatlovchi Python kutubxonasi.

## O'rnatish

```bash
pip install boxabar
```

## Foydalanish usuli

### SMS xabar yuborish

```python
from boxabar import SMSMessenger, Message

# Messenger yaratish
sms = SMSMessenger(config={
    'default_sender': '+998901234567'
})

# Xabar yuborish
xabar = Message(
    text="Salom, bu test xabar!",
    sender="+998901234567",
    recipient="+998901234568"
)
sms.send(xabar)

# Yoki qisqaroq usul
sms.send("Bu ham test xabar")
```

### Email xabar yuborish

```python
from boxabar import EmailMessenger

email = EmailMessenger(config={
    'default_sender': 'noreply@example.com',
    'default_subject': 'Muhim xabar'
})

email.send("Bu email xabar matni")
```

### Telegram xabar yuborish

```python
from boxabar import TelegramMessenger

telegram = TelegramMessenger(config={
    'bot_token': '12345:ABCdefGHIjklMNOpqrSTUvwxYZ',
    'bot_username': 'BoxabarTestBot',
    'chat_id': '123456789'
})

telegram.send("Telegram orqali yuborilgan xabar")
```
