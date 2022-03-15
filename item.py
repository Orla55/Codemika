import datetime


class Item:
    __item_id = 0
    __item_list = dict()

    def __init__(self, title, price) -> None:
        Item.__item_id += 1
        self.__id = Item.__item_id
        self.__title = title
        self.price = price
        self.__created = datetime.datetime.now()
        self.__update = None
        Item.__item_list[self.__id] = self

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = price

    @staticmethod
    def get_item_by_id(id):
        for item in Item.__item_list.keys():
            if item == id:
                return Item.__item_list[item]
        raise ValueError('Item has not found')

    @staticmethod
    def get_item_by_price(price):
        for product in Item.__item_list:
            if product.price == price:
                return price
        raise ValueError('Item has not found')

    @staticmethod
    def get_item_by_tittle(tittle):
        for item in Item.__item_list:
            if item.tittle == tittle:
                return item
        raise ValueError('Item has not found')

    def __str__(self):
        return str(self.__id) + ' ' + self.__title + ' ' + str(self.price)
