class Postcard:
    def __init__(self, picture: str, author: str, address: str, stamp: bool):
        """
        Класс содержит базовую информацию об открытке.
        :param picture: Отражает, что изображено на открытке.
        :param author: Автор картинки (художник или фотограф).
        :param address: Адрес назначения.
        :param stamp: Наличие марки.
        """
        self.picture = picture
        self.author = author
        self.address = address
        self.stamp = stamp

        if not isinstance(picture, str):
            raise TypeError("Изображение должно быть типа str")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть типа str")
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть типа str")
        if not isinstance(stamp, bool):
            raise TypeError("Марка должна быть типа bool")

    def __str__(self):
        return f"{self.__class__.__name__} Открытка {self.picture}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(picture={self.picture!r}, author={self.author!r}," \
               f" address={self.address!r}, stamp={self.stamp})"

    @property
    def picture(self) -> str:
        """
        Возвращает состояние атрибута picture
        :return: изображение на открытке.
        """
        return self.picture

    @picture.setter
    def picture(self, value):
        """
        Изменяет состояние атрибута picture
        :param value: новое значение атрибута picture
        """
        self.picture = value

    @property
    def author(self) -> str:
        """
        Возвращает состояние атрибута author
        :return: автора открытки.
        """
        return self.author

    @author.setter
    def author(self, value):
        """
        Изменяет состояние атрибута author
        :param value: новое значение атрибута author
        """
        self.author = value

    @property
    def address(self) -> str:
        """
        Возвращает состояние атрибута address
        :return: адрес открытки.
        """
        return self.address

    @address.setter
    def address(self, value):
        """
        Изменяет состояние атрибута address
        :param value: новое значение атрибута address
        """
        self.address = value

    @property
    def stamp(self) -> bool:
        """
        Возвращает состояние атрибута stamp
        :return:наличии марки на открытки.
        """
        return self.stamp

    @stamp.setter
    def stamp(self, value):
        """
        Изменяет состояние атрибута stamp
        :param value: новое значение атрибута stamp
        """
        self.stamp = value

    def change_address(self, adr: str):
        """
        Функция меняет адрес назначения для открытки.
        :param adr: Новый адрес отправки на открытки.
        """
        if not isinstance(adr, str):
            raise TypeError("Адрес на открытке должен быть типа str")
        self.address = adr

    def is_stamp(self):
        """
        Функция проверяет, есть ли на открытке марка.
        """
        if self.stamp is True:
            print("Марка приклеена")
        else:
            print("Марки нет")


class ArtPostcard(Postcard):
    def __init__(self, picture: str, author: str, museum: str, address: str, stamp: bool):
        """
        Этот класс иллюстрирует открытки с произведениями искусства.
        :param picture:
        :param author:
        :param museum: название музея, где располагается предмет искусства.
        :param address:
        :param stamp:
        """
        super(ArtPostcard, self).__init__(picture=picture, author=author, address=address, stamp=stamp)
        self.museum = museum

        if not isinstance(museum, str):
            raise TypeError("Название музея должно быть типа str")

    def __str__(self):
        return f"{self.__class__.__name__} Открытка {self.picture}. Автор {self.author}. Музей {self.museum}."

    def __repr__(self):
        return f"{self.__class__.__name__}(picture={self.picture!r}, author={self.author!r}," \
               f" address={self.address!r}, stamp={self.stamp}, museum={self.museum})"

    @property
    def museum(self) -> str:
        """
        Возвращает состояние атрибута museum
        :return: название музея
        """
        return self.museum

    @museum.setter
    def museum(self, value):
        """
        Изменяет состояние атрибута museum
        :param value: новое значение атрибута museum
        """
        self._museum = value

    def change_address(self, adr: str):
        """
        Функция меняет адрес назначения для открытки.
        Мы хотим отправлять открытки с искусством только заграницу.
        Представим, что все иностранные адреса написаны в верхнем регистре.
        Чтобы поменять адрес, нужно проверить, является ли он иностранным.
        Для этого воспользуемся функцией isupper.
        :param adr: Новый адрес отправки на открытки.
        :return:
        """
        if not isinstance(adr, str):
            raise TypeError("Адрес на открытке должен быть типа str")

        if adr.isupper() is True:
            self.address = adr
        else:
            print("Этот адрес не является иностранным")


card = Postcard("Кот в мешке", "Вася Пупкин", 'ул. Бассееная,д.3', True)
print(f"{card.__str__()}\n{card.__repr__()}")
card.change_address("Пушкинская, 10")
print(card.address)
card.is_stamp()

print("")
art_card = ArtPostcard("Кот в мешке", "Вася Пупкин", 'Эрарта', 'ул. Бассееная,д.3', True)
print(f"{art_card.__str__()}\n{art_card.__repr__()}")
art_card.change_address("Пушкинская, 10")
art_card.change_address("TIME SQUARE 10")
print(art_card.address)
art_card.is_stamp()
