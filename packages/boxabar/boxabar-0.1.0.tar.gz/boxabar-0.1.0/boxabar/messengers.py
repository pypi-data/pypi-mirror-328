from abc import ABC, abstractmethod
from .message import Message
from .utils import log_message


class BaseMessenger(ABC):
    """Xabar yuboruvchilar uchun asosiy sinf"""

    def __init__(self, config=None):
        self.config = config or {}
        self.sent_messages = []

    @abstractmethod
    def send(self, message):
        """Xabar yuborish metodi"""
        pass

    def get_history(self):
        """Yuborilgan xabarlar tarixini qaytarish"""
        return self.sent_messages


class SMSMessenger(BaseMessenger):
    """SMS xabarlarni yuborish uchun sinf"""

    def send(self, message):
        """SMS xabar yuborish"""
        if not isinstance(message, Message):
            message = Message(
                text=message,
                sender=self.config.get("default_sender", "Unknown"),
                recipient=self.config.get("default_recipient", "Unknown"),
            )

        # SMS yuborish logikasi
        print(f"SMS yuborilmoqda: {message.recipient} raqamiga")
        print(f"Matn: {message.text}")

        # Xabarni yuborilgan deb belgilash
        message.mark_as_sent()
        self.sent_messages.append(message)

        # Xabarni jurnaliga yozish
        log_message(message, messenger_type="SMS")

        return True


class EmailMessenger(BaseMessenger):
    """Email xabarlarni yuborish uchun sinf"""

    def send(self, message):
        """Email xabar yuborish"""
        if not isinstance(message, Message):
            message = Message(
                text=message,
                sender=self.config.get("default_sender", "noreply@example.com"),
                recipient=self.config.get("default_recipient", "user@example.com"),
                subject=self.config.get("default_subject", "Boxabar xabarnomasi"),
            )

        if not message.subject:
            message.subject = "Boxabar xabarnomasi"

        # Email yuborish logikasi
        print(f"Email yuborilmoqda: {message.recipient} manziliga")
        print(f"Mavzu: {message.subject}")
        print(f"Matn: {message.text}")

        # Xabarni yuborilgan deb belgilash
        message.mark_as_sent()
        self.sent_messages.append(message)

        # Xabarni jurnaliga yozish
        log_message(message, messenger_type="Email")

        return True


class TelegramMessenger(BaseMessenger):
    """Telegram xabarlarni yuborish uchun sinf"""

    def __init__(self, config=None):
        super().__init__(config)
        self.bot_token = config.get("bot_token", "")
        if not self.bot_token:
            raise ValueError("Telegram bot uchun token talab qilinadi!")

    def send(self, message):
        """Telegram xabar yuborish"""
        if not isinstance(message, Message):
            message = Message(
                text=message,
                sender=self.config.get("bot_username", "BoxabarBot"),
                recipient=self.config.get("chat_id", ""),
                subject=None,
            )

        # Telegram yuborish logikasi
        print(f"Telegram xabar yuborilmoqda: {message.recipient} chat ID ga")
        print(f"Bot: {self.config.get('bot_username', 'BoxabarBot')}")
        print(f"Matn: {message.text}")

        # Xabarni yuborilgan deb belgilash
        message.mark_as_sent()
        self.sent_messages.append(message)

        # Xabarni jurnaliga yozish
        log_message(message, messenger_type="Telegram")

        return True
