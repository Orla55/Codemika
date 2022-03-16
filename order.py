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

    # добавление списка товаров в ItemList и соответствующего каталога

    def add_list_of_item(self, item_list, catalog):
        assert type(
            item_list) == list, "На вход должен подавать список товаров (list<Item>)"
        assert len(item_list) != 0, "Список должен содержать хотя бы один элемент"

        for item in item_list:
            assert type(
                item) == Item, "Некорректный тип элемента списка. Все элементы должны относится к классу Item"
            self.add_item(item, catalog)


# class Item_Catalog:
#     __catalog_id = 0
#     __catalog_list = dict()

#     def __init__(self, description):
#         self.description = description
#         self.__id = Catalog.__id
#         Catalog.__id += 1
#         self.item_list = None
#         self.catalog_list = list()

#     # -----------------------------------------------------------
#     @property
#     def id(self):
#         return self.__id

#     @property
#     def description(self):
#         return self.__description

#     @description.setter
#     def description(self, description):
#         assert type(description) == str, "Описание каталога должно быть строкой!"
#         self.__description = description

#     @property
#     def catalog_list(self):
#         return self.__catalog_list

#     @catalog_list.setter
#     def catalog_list(self, catalog_list):
#         assert type(catalog_list) == Catalog or type(catalog_list) == list, "На вход должен подавать элемент типа Catalog или List()"

#         if type(catalog_list) == Catalog: # в случае одного элемента
#             self.__catalog_list = [catalog_list]
#         else: # в случае списка
#             catalog_list_dst = list() # создание списка для заполнения его каталогами
#             for catalog in catalog_list:
#                 assert type(catalog) == Catalog, "Некорректный элемент списка! Все элементы списка должны относится к классу Catalog"
#                 catalog_list_dst.append(catalog)
#             self.__catalog_list = catalog_list_dst

#     @property
#     def item_list(self):
#         return self.__item_list

#     @item_list.setter
#     def item_list(self, item_list):
#         assert type(item_list) == ItemList or item_list == None, "Список товаров должен относится к классу ItemList или None"
#         self.__item_list = item_list

#     # -----------------------------------------------------------

#     # добавление подкаталога
#     def add_subcatalog(self, catalog):
#         assert type(catalog) == Catalog, "На вход должен подаваться аргумент типа Catalog"
#         self.__catalog_list.append(catalog)
