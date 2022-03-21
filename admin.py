from user import User
from item import Item
import datetime


class Administrator(User, Item):
    def __init__(self, name, surname, phone, email) -> None:
        super().__init__(name, surname, phone, email)
        self.role = ""

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        if type(self) == Administrator:
            self.__role = "admin"

        else:
            self.__role = ""

    # def create_item_catlog(self, title, specification, price):
    #     self.title = title
    #     self.specification = specification
    #     self.price = price

    # def change_item_catalog(self, title, specification, price):
    #     self.title = title
    #     self.specification = specification
    #     self.price = price
    #     item_update_time = datetime.datetime.now()


admin = Administrator("Dmitry", "Kolobov", '+79052541525', "danasan@akak.ru")
admin.create_item_catlog("Tovar narodnogog", "Some specification", 2345,)
