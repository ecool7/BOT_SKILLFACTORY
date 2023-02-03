import json
import requests
from config import keys

class CovertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount  ):
        if quote == base:
            raise ConvertionExceptions(f'Нельзя перевести одинаковые валюты {base} ')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработаь валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработать валюту {base}')
        quote_ticker, base_ticker = keys[quote], keys[base]

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceptions(f'Не удалось обработать количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')

        total_base = json.loads(r.content)[keys[base]]
        return total_base