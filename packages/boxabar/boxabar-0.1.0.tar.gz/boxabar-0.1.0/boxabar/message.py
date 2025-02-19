import datetime


class Message:
    """Xabarlar uchun asosiy sinf"""

    def __init__(self, text, sender, recipient, subject=None):
        self.text = text
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.created_at = datetime.datetime.now()
        self.status = "NEW"

    def __str__(self):
        if self.subject:
            return f"[{self.subject}] {self.text[:30]}..."
        return f"{self.text[:30]}..."

    def mark_as_sent(self):
        """Xabarni yuborilgan deb belgilash"""
        self.status = "SENT"
        self.sent_at = datetime.datetime.now()

    def mark_as_delivered(self):
        """Xabarni yetkazilgan deb belgilash"""
        self.status = "DELIVERED"
        self.delivered_at = datetime.datetime.now()

    def mark_as_read(self):
        """Xabarni o'qilgan deb belgilash"""
        self.status = "READ"
        self.read_at = datetime.datetime.now()

    def to_dict(self):
        """Xabarni lug'at ko'rinishida qaytarish"""
        result = {
            "text": self.text,
            "sender": self.sender,
            "recipient": self.recipient,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

        if self.subject:
            result["subject"] = self.subject

        if hasattr(self, "sent_at"):
            result["sent_at"] = self.sent_at.isoformat()

        if hasattr(self, "delivered_at"):
            result["delivered_at"] = self.delivered_at.isoformat()

        if hasattr(self, "read_at"):
            result["read_at"] = self.read_at.isoformat()

        return result
