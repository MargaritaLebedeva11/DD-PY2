class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super(PaperBook, self).__init__(name=name, author=author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r}"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if not pages <= 2000:
            """В условии ограничения не даны.
            Подумала, что книг с настолько большим количеством страниц
            практически не существует."""
            raise ValueError


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super(AudioBook, self).__init__(name=name, author=author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if not duration <= 100:
            raise ValueError
