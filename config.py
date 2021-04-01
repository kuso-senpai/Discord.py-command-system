"""
Einstellungen für den Bot
"""

import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
color = 0x00FFFF
prefix = "!"