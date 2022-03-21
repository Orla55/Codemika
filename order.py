import datetime
from item import Item
from catalog import Item_Catalog


class OrderList:
    __order_id = 0  # static field
    __oredr_list = dict()

    def __init__(self, title, price, specification):
        self.__id = OrderList.__order_id
        OrderList.__order_id += 1
        self.title = title
        self.price = price
        self.specification = specification
        self.__created = datetime.datetime.now()
        self.__update = None
        OrderList.__oredr_list[self.__id] = self

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title == Item_Catalog.get_item_by_tittle(title):
            self.__title = title
        else:
            raise ValueError("Item has not found")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price == Item_Catalog.get_item_by_price(price):
            self.__price = price
        else:
            raise ValueError("Item has not found")

    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification):
        if specification == Item_Catalog.get_item_by_specification(specification):
            self.__specification = specification
        else:
            raise ValueError("Item has not found")

    def show_catalog(self):
        print(OrderList.__oredr_list)
