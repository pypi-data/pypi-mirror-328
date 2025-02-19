import os
import json
import datetime
import logging

# Jurnallashni sozlash
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="boxabar.log",
)
logger = logging.getLogger("boxabar")


def log_message(message, messenger_type=None):
    """Xabarni jurnaliga yozish"""
    logger.info(f"Xabar: {messenger_type or 'Unknown'} orqali yuborildi")
    logger.info(f"Kimdan: {message.sender}")
    logger.info(f"Kimga: {message.recipient}")
    logger.info(f"Matn: {message.text[:100]}...")

    # JSON formatida saqlash
    try:
        os.makedirs("logs", exist_ok=True)
        log_file = os.path.join(
            "logs", f"messages_{datetime.date.today().isoformat()}.json"
        )

        # Mavjud jurnalni o'qish
        messages = []
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                try:
                    messages = json.load(f)
                except json.JSONDecodeError:
                    messages = []

        # Yangi xabar qo'shish
        messages.append(
            {
                "timestamp": datetime.datetime.now().isoformat(),
                "messenger_type": messenger_type,
                "message": message.to_dict(),
            }
        )

        # Jurnalni saqlash
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Jurnallashda xato: {e}")


def format_message(message, format_type="plain"):
    """Xabarni formatlash"""
    if format_type == "plain":
        return message.text

    elif format_type == "html":
        html = f"<div class='boxabar-message'>"
        if message.subject:
            html += f"<h2>{message.subject}</h2>"
        html += f"<p>{message.text}</p>"
        html += f"<div class='boxabar-footer'>"
        html += f"<span>Kimdan: {message.sender}</span>"
        html += f"<span>Kimga: {message.recipient}</span>"
        html += f"<span>Vaqt: {message.created_at.strftime('%Y-%m-%d %H:%M:%S')}</span>"
        html += f"</div></div>"
        return html

    elif format_type == "markdown":
        md = ""
        if message.subject:
            md += f"## {message.subject}\n\n"
        md += f"{message.text}\n\n"
        md += f"*Kimdan:* {message.sender}  \n"
        md += f"*Kimga:* {message.recipient}  \n"
        md += f"*Vaqt:* {message.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        return md

    elif format_type == "dict":
        return message.to_dict()

    else:
        raise ValueError(f"Noma'lum format turi: {format_type}")
