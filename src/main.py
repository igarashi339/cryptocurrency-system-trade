'''
システムトレードのエントリポイント。
'''

from src.common.common import CryptoType, TickerInfo, ExchangeType, WebAPIErrorCode
from src.web_handler.exchange_handler import ExchangeHandler
from src.util.config_reader import ConfigReader
from src.util.api_key_reader import APIKeyReader
import pprint
import time
import codecs

if __name__=='__main__':
    handler = ExchangeHandler(ExchangeType.ZAIF)
    handler.load_api_key()
    handler.fetch_balance()
