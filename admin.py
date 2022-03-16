from user import User


class Administrator(User):
    def __init__(self, name, surname, phone, email) -> None:
        super().__init__(name, surname, phone, email)
