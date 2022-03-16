import datetime


class Item:
    __item_id = 0
    __item_list = dict()

    def __init__(self, title, specification, price) -> None:
        Item.__item_id += 1
        self.__id = Item.__item_id
        self.title = title
        self.specification = specification
        self.price = price
        self.__created = datetime.datetime.now()
        self.__update = None
        Item.__item_list[self.__id] = self

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if type(title) == str:
            self.__title = title
        else:
            raise ValueError("Please be advised, that title has to be string")

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification):
        if type(specification) == str:
            self.__specification = specification
        else:
            raise ValueError(
                "Please be advised, that specification has to be string")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) != int and price < 0:
            raise ValueError("Price cannot be less than zero")
        else:
            self.__price = price

    @staticmethod
    def get_item_by_id(id):
        for item in Item.__item_list.keys():
            if item == id:
                return Item.__item_list[item]
        raise ValueError('Item has not found')
