import datetime
import re


class User:
    __user_id = 0
    __users_list = dict()

    def __init__(self, name, surname, phone, email) -> None:
        User.__user_id += 1
        self.__id = User.__user_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.__created = datetime.datetime.now()
        self.__update = None
        self.__last_visit = self.__created
        User.__users_list[self.__id] = self

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        regex = re.compile(r"([А-ЯЁ]|[а-яё])|([A-Z]|[a-z])")
        if re.match(regex, name):
            self.__name = name
        else:
            print("Invalid name")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        regex = re.compile(r"([А-ЯЁ]|[а-яё])|([A-Z]|[a-z])")
        if re.match(regex, surname):
            self.__surname = surname
        else:
            print("Invalid surname")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        regex = re.compile(
            r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$")
        if re.match(regex, phone):
            self.__phone = phone
        else:
            print("Invalid phone")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        regex = re.compile(
            r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        if re.fullmatch(regex, email):
            self.__email = email
        else:
            print("Invalid email")

    def __str__(self) -> str:
        return str(self.__id) + " " + self.name + " " + self.surname + " " + self.phone + " " + self.__email

    @staticmethod
    def get_user_by_id(id):
        for key in User.__users_list:
            if key == id:
                return User.__users_list[key]
        raise ValueError("User has not found")

    @staticmethod
    def get_user_by_phone(phone):
        for value in User.__users_list.values():
            value = str(value)
            if phone in value:
                return value
        raise ValueError("User has not found")

    @staticmethod
    def get_user_by_email(email):
        for value in User.__users_list.values():
            value = str(value)
            if email in value:
                return value
        raise ValueError("User has not found")


user1 = User("Dmitry", "Kolobov", '+79052541525', "danasan@akak.ru")
user2 = User("Alex", "Yashin", '+79052541515', "danan@akak.ru")
print(User.get_user_by_phone('danan@akak.ru'))
