class BoxabarError(Exception):
    """Boxabar kutubxonasi uchun asosiy xato sinfi"""

    pass


class MessageDeliveryError(BoxabarError):
    """Xabar yetkazib berish xatosi"""

    pass


class InvalidConfigurationError(BoxabarError):
    """Noto'g'ri sozlash xatosi"""

    pass


class RecipientNotFoundError(BoxabarError):
    """Qabul qiluvchi topilmadi xatosi"""

    pass
