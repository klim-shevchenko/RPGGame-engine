from rpg.area import *
from rpg.graphics import *
from rpg.sprite import *
class game():
    def __init__(self, **params):
        self.rpg_dict_of_area = {} # параметр - словарь, хранящий в себе множество экземпляров класса Area, {number - ключ : name Area - значение}
        self.team_of_pc = [] # параметр - список, хранящий в себе имена экземпляров класса Actor с параметром category = "pc"

    def new_area(self, name):
        ''' метод отвечающий за создание класса, потомка от Area и создание поля из параметров, и установление их в начальные значения '''
        self.rpg_dict_of_area[name] = area()

    def set_area(self, name, canvas):
        ''' метод отвечающий за размещение экземпляра класса Area в поле rpg\_dict\_of\_area класса game '''
        if name in self.rpg_dict_of_area:
            canvas.clear_all()
            canvas.add_sprite(name.sprite, name.sprite.x, name.sprite.y, name.sprite.z)
            canvas.update()

    def new_item(self, name, **params):
        ''' метод отвечающий за создание класса, потомка от Item и создание поля из параметров, и установление их в начальные значения '''
        self

    def new_spell(self, name, **params):
        ''' метод отвечающий за создание класса, потомка от Spell и создание поля из параметров, и установление их в начальные значения '''
        self

    def new_actor(self, name, **params):
        ''' метод отвечающий за создание класса, потомка от Actor и создание поля из параметров, и установление их в начальные значения '''
        self

    def add_pc_to_team(self, pc):
        ''' метод отвечающий за добавление имени экземпляра класса Actor с параметром category = "pc" в список team\_of\_pc, хранящий имена всех игровых персонажей '''
        self

    def remove_pc_from_team(self, pc):
        ''' метод отвечающий за удаление имени экземпляра класса Actor с параметром category = "pc" в список team\_of\_pc, хранящий имена всех игровых персонажей '''
        self

    def start_script(script):
        ''' метод отвечающий за активацию скрипта '''
        script

    def stop_thread(script):
        ''' метод отвечающий за прекращение действий скрипта '''
        script
