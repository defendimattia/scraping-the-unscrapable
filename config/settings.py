from dotenv import load_dotenv
import os

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
USER_AGENT = os.getenv("USER_AGENT")

# Timeout e scroll
TIMEOUT = 15  # massimo tempo di attesa per il caricamento di un elemento
SCROLL_TIMEOUT = 10
