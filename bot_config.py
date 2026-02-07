import os
from dotenv import load_dotenv

load_dotenv()

settings = {
    'token_telegram': os.getenv('TELEGRAM_TOKEN'),
    'token_discord': os.getenv('DISCORD_TOKEN', '')  # Leave empty if not using Discord
}
