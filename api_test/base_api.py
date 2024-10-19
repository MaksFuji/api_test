"""Описание базового класса АПИ BaseAPI"""
from abc import ABC

class BaseAPI(ABC):
    """Абстрактный класс инициализации АПИ"""
    def __init__(self) -> None:
        pass


    def load_json(self):
        """Получение объекта Python из json"""


    def to_json(self) -> str:
        """Преобразование в json"""


    def to_dict(self) -> dict:
        """Преобразование в словарь Python"""
