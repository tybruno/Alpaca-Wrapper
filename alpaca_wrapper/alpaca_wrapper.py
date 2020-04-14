import alpaca_trade_api as tradeapi
import threading
import time
import datetime
import os

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(
    base_url=APCA_API_BASE_URL,
    key_id=API_KEY,
    secret_key=API_SECRET
)