class Stationery:
    atr_title = 'Картина гения'
    def draw(self):
        print('Сходи купи чем-можно нарисовать')

class Pen(Stationery):
    def draw(self):
        print('Нарисуй ручкой куб')

class Pencil(Stationery):
    def draw(self):
        print('Нарисуй карандашом график')

class Handle(Stationery):
    def draw(self):
        print('Нарисуй маркером сам придумай что')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
