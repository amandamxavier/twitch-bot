import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
NICKNAME = os.getenv('NICKNAME')
CHANNELS = os.getenv('CHANNELS').split(',')
BOTS = os.getenv('BOTS').split(',')
BOTS.append(NICKNAME)
