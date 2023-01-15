import doctest


class Bag:
    def __init__(self, volume: float, material: str):
        """
        Создание и подготовка к работе объекта "Мешок"
        :param volume: Объем мешка
        :param material: Материал мешка
        """

        if not isinstance(volume, (int, float)):
            raise TypeError("Объем мешка должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем мешка должен быть положительным числом")
        self.volume = volume

        if not isinstance(material, str):
            raise TypeError("Материал мешка должен быть типа string")
        self.material = material

    def cat_in_bag(self) -> bool:
        """
        Функция проверяет, есть ли кот в мешке
        :return: Есть ли кот в мешке
        """
        ...

    def add_cat(self, cat: float) -> None:
        """
        Функция кладет кота в мешок
        :param cat: Объем кота
        :return ValueError: Если объем кота будет больше, чем объем мешка
        """
        if not isinstance(cat, (int, float)):
            raise TypeError("Объем кота должен быть типа int или float")
        if cat <= 0:
            raise ValueError("Объем кота должен быть положительным числом")


class Cat:
    def __init__(self, weight: float, fur: bool, color: str, age: int, gender: str):
        """
        Создание и подготовка объекта "Кот"
        :param weight: Вес кота
        :param fur: Наличие шерсти
        :param color: Расцветка кота
        :param age: Возраст кота
        :param gender: Пол кота
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес кота должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес кота должен быть положительным числом")
        self.weight = weight

        if not isinstance(fur, bool):
            raise TypeError("Наличие шерсти должно быть типа bool")
        self.fur = fur

        if not isinstance(color, str):
            raise TypeError("Цвет шерсти кота должен быть типа str")
        self.color = color

        if age <= 0:
            raise ValueError("Возраст кота должен быть положительным числом")
        self.age = age

        if not isinstance(gender, str):
            raise TypeError("Пол кота должен быть типа str")
        self.gender = gender

    def is_fur(self):
        """
        Функция проверяет, лысый кот или нет
        :return: Если кот лысый, то расцветка устанавливается "Бежевый"
        """
        ...

    def paint_cat(self, clr: str):
        """
        Функция меняет раскраску кота
        :param clr: Цвет кота
        :return:
        """
        if not isinstance(clr, str):
            raise TypeError("Цвет шерсти кота должен быть типа str")

    def feed_cat(self, food):
        """
        Функция кормит кота. Вес корма прибавляется к весу кота.
        :param food: Вес корма
        :return ValueError: Если вес корма больше веса кота
        """
        if not isinstance(food, (int, float)):
            raise TypeError("Вес корма должен быть типа int или float")
        if food <= 0:
            raise ValueError("Вес корма должен быть положительным числом")


class CatsHome:
    def __init__(self, width: float, depth: float, height: float, material: str, pillow: bool):
        """
        Создание и подготовка к работе объекта "Дом для кота"
        :param width: ширина
        :param depth: длина
        :param height: высота
        :param pillow: Наличие мягкой подушки в домике
        :param material: Материал домика
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина дома должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина дома должна быть положительным числом")
        self.width = width

        if not isinstance(depth, (int, float)):
            raise TypeError("Длина дома должна быть типа int или float")
        if depth <= 0:
            raise ValueError("Длина дома должна быть положительным числом")
        self.depth = depth

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дома должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дома должна быть положительным числом")
        self.height = height

        if not isinstance(pillow, bool):
            raise TypeError("Наличие мягкой подушки должно быть типа bool")
        self.pillow = pillow

        if not isinstance(material, str):
            raise TypeError("Материал дома кота должен быть типа str")

    def build_floor(self, cnt: int):
        """
        Функция строит новые этажи домика (на случае, если появятся ещё котики)
        :param cnt: Количество новых этажей
        :return: cnt * height
        """
        if not isinstance(cnt, int):
            raise TypeError("Количество этажей должно быть типа int")
        if cnt <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")

    def get_pillow(self) -> bool:
        """
        Функция кладет подушечку в домик
        :return: Если подушка уже в домике, функция возвращает False
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass