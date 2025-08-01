class MixinLog:
    """ Класс-миксин для товаров """
    def __init__(self):
        """ Инициализирует класс-миксин """
        super().__init__()
        print(repr(self))

    def __repr__(self):
        """Выводит информацию о созданном объекте в консоль"""
        return f'{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})'
