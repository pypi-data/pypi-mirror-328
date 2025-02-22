from market import *
from client import *
import requests
from datetime import datetime
from enums import *
from enum import Enum

root="https://api.elections.kalshi.com/trade-api/v2"
demoRoot="https://demo-api.kalshi.co/trade-api/v2"

class Environment(Enum):
    DEMO = "demo",
    PROD = "prod"

class KalshiMarket(Market):
    """ A market on Kalshi
    """
    title: str # The listed title of the market
    rules: str # The listed rules to the market. Used to identify differences between seemingly similar markets
    open: bool # Whether this market is open to orders
    open_time: datetime # the time this market opened
    close_time: datetime #the time this market closes, used to calculate returns
    book: OrderBook # The orderbook of this market. Not automatically refreshed

    last_refreshed_data: datetime # the last time the data has been refreshed
    last_refreshed_book: datetime

    ticker: str # the ticker used as id on kalshi
    environment: Environment # demo or prod

    def __init__(self, ticker, demo=Environment.PROD):
        super().__init__()
        self.ticker = ticker
        self.demo = demo

    def _get_api_root(self) -> str:
        """ Gets the api root URL for endpoints
        """
        if self.demo == Environment.PROD:
            return demoRoot
        else:
            return root

    def refresh_data(self) -> None:
        apiRoot = self._get_api_root()
        data = requests.get(f"{apiRoot}/markets/{self.ticker}")

        if data.status_code != 200:
            raise KalshiRequestError(f"Recieved status code {data.status_code} instead of 200. Ticker: {self.ticker}")
        
        dataJSON = data.json()['market']
        self.title = dataJSON['title']
        self.rules = dataJSON['rules_primary']
        self.open = True if dataJSON['status']=="active" else False
        self.open_time = datetime.fromisoformat(dataJSON['open_time'][0:-1])
        self.close_time = datetime.fromisoformat(dataJSON['close_time'][0:-1])

        self.last_refreshed_data = datetime.now()

    def refresh_book(self) -> None:
        apiRoot = self._get_api_root()
        data = requests.get(f"{apiRoot}/markets/{self.ticker}/orderbook")

        if data.status_code != 200:
            raise KalshiRequestError(f"Recieved status code {data.status_code} instead of 200. Ticker: {self.ticker}")
        
        dataJSON = data.json()['orderbook']
        self.book.update_book(dataJSON['YES'], dataJSON['NO'])


# TODO: test
# example code from kalshi demo: https://github.com/Kalshi/kalshi-starter-code-python/blob/main/clients.py
#                                https://github.com/Kalshi/kalshi-starter-code-python/blob/main/main.py
#                                https://trading-api.readme.io/reference/api-keys
class KalshiClient(Client):
    """ A single client on Kalshi. Uses HTTP connections
    """
    key_id: str
    private_key: str
    environment: Environment
    

class KalshiOrder(Order):
    """ An order on Kalshi
    """
    client: Client
    market: Market
    placed_price: float # price per share when the order was placed
    quantity: float
    side: Side
    
    def __init__(self, client, market, placed_price, quantity, side):
        super().__init__(client, market, placed_price, quantity, side)
    
class KalshiRequestError(Exception):
    pass