from config import all_keys

class ConvertionExeption(Exception):
    pass
class Convertor():
    @staticmethod
    def convert(quote, base, amount):

        try:
            quote = all_keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту "{quote}"')
        try:
            base = all_keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту "{base}"')

        try:
            amount = float(int(amount))
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество "{amount}"')