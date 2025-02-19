from typing import Any


class ElectronicDevice:
    """Базовый класс для электронных устройств."""

    def init(self, brand: str, model: str, battery_life: int):
        """
        Инициализирует объект электронного устройства.

        :param brand: Бренд устройства
        :param model: Модель устройства
        :param battery_life: Время работы от аккумулятора в часах
        """
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def power_on(self) -> str:
        """Метод включения устройства."""
        return f"{self.brand} {self.model} включается..."

    def power_off(self) -> str:
        """Метод выключения устройства."""
        return f"{self.brand} {self.model} выключается..."

    def str(self) -> str:
        """Возвращает строковое представление устройства."""
        return f"Устройство: {self.brand} {self.model}, Автономность: {self.battery_life} часов"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return f"ElectronicDevice(brand={self.brand!r}, model={self.model!r}, battery_life={self.battery_life})"


class Smartphone(ElectronicDevice):
    """Дочерний класс для смартфонов."""

    def init(self, brand: str, model: str, battery_life: int, os: str, camera_megapixels: int):
        """
        Инициализирует объект смартфона.

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_life: Время работы от аккумулятора в часах
        :param os: Операционная система смартфона
        :param camera_megapixels: Разрешение камеры в мегапикселях
        """
        super().init(brand, model, battery_life)
        self.os = os
        self.camera_megapixels = camera_megapixels

    def take_photo(self) -> str:
        """Метод для съёмки фото."""
        return f"{self.brand} {self.model} делает фото с камерой {self.camera_megapixels} МП."

    def str(self) -> str:
        """Возвращает строковое представление смартфона."""
        return f"Смартфон: {self.brand} {self.model}, ОС: {self.os}, Камера: {self.camera_megapixels} МП, Автономность: {self.battery_life} часов"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return (f"Smartphone(brand={self.brand!r}, model={self.model!r}, battery_life={self.battery_life}, "
                f"os={self.os!r}, camera_megapixels={self.camera_megapixels})")


class Laptop(ElectronicDevice):
    """Дочерний класс для ноутбуков."""

    def init(self, brand: str, model: str, battery_life: int, processor: str, ram: int):
        """
        Инициализирует объект ноутбука.

        :param brand: Бренд ноутбука
        :param model: Модель ноутбука
        :param battery_life: Время работы от аккумулятора в часах
        :param processor: Тип процессора
        :param ram: Объём оперативной памяти в ГБ
        """
        super().init(brand, model, battery_life)
        self.processor = processor
        self.ram = ram

    def run_program(self, program_name: str) -> str:
        """Метод для запуска программы."""
        return f"Запуск {program_name} на {self.brand} {self.model} с процессором {self.processor} и {self.ram} ГБ ОЗУ."

    def str(self) -> str:
        """Возвращает строковое представление ноутбука."""
        return f"Ноутбук: {self.brand} {self.model}, Процессор: {self.processor}, ОЗУ: {self.ram} ГБ, Автономность: {self.battery_life} часов"

    def repr(self) -> str:
        """Возвращает строку, представляющую объект в коде."""
        return (f"Laptop(brand={self.brand!r}, model={self.model!r}, battery_life={self.battery_life}, "
                f"processor={self.processor!r}, ram={self.ram})")