class Retail:
    def __init__(self, item, units, price):
        self.__item = item
        self.__units = units
        self.__price = price

    def set__item(self, item):
        self.__item = item

    def set__units(self, units):
        self.__units = units

    def set__price(self, price):
        self.__price = price

    def get__item(self):
        return self.__item

    def get__units(self):
        return self.__units

    def get__price(self):
        return self.__price
