import datetime
from item import Item


class Item_Catalog:
    __catalog_id = 0
    __catalog_list = dict()

    def __init__(self):
        Item_Catalog.__catalog_id += 1
        self.__id = Item_Catalog.__catalog_id
        self.__title = Item.title
        self.__specification = Item.specification
        self.__price = Item.price
        self.__created = datetime.datetime.now()
        self.__update = None
        Item_Catalog.__catalog_list[self.__id] = self

    @staticmethod
    def get_item_by_price(price):
        for product in Item_Catalog.__catalog_list:
            if product.price == price:
                return price
        raise ValueError('Item has not found')

    @staticmethod
    def get_item_by_tittle(tittle):
        for item in Item_Catalog.__catalog_list:
            if item.tittle == tittle:
                return item
        raise ValueError('Item has not found')

    @staticmethod
    def get_item_by_specification(specfication):
        for item in Item_Catalog.__catalog_list:
            if item.specification == specfication:
                return item
        raise ValueError('Item has not found')

    def __str__(self):
        return str(self.__id) + ' ' + self.__title + ' ' + str(self.price) + " " + self.__specification
