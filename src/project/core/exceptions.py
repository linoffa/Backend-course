from typing import Final


class PassengerNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "User с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


# class PassengerAlreadyExists(BaseException):
#     _ERROR_MESSAGE_TEMPLATE: Final[str] = "Пользователь с почтой '{email}' уже существует"
#
#     def __init__(self, email: str) -> None:
#         self.message = self._ERROR_MESSAGE_TEMPLATE.format(email=email)
#         super().__init__(self.message)
