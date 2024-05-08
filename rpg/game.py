from rpg.area import *
from rpg.graphics import *
from rpg.sprite import *
from rpg.actor import *
class Game():
    def __init__(self, canvas, **params):
        self.rpg_dict_of_area = {} # словарь, хранящий в себе множество экземпляров класса Area, {number - ключ : name Area - значение}
        self.team_of_pc = [] # список, хранящий в себе имена экземпляров класса Actor с параметром category = "pc"
        self.canvas = canvas # графика

    def new_area(self, name, area):
        ''' добавляет новую зону в список
         param name - имя зоны area - класс area()'''
        self.rpg_dict_of_area[name] = area

    def set_area(self, name):
        ''' устанавливает текущую зону, загружает графику зоны
         param name - имя зоны '''
        if name in self.rpg_dict_of_area:
            area = self.rpg_dict_of_area[name]
            self.canvas.clear_all()
            for sprite in area.sprites:
                sprite.update(sprite.x, sprite.y)
                self.canvas.add_sprite(sprite, sprite.x, sprite.y, sprite.z)

    def new_actor(self, name, category,  x, y, z, sprite, **params):
        ''' создёт класс, потомок от Actor и создаёт поле из параметров, и установление их в начальные значения '''
        name = type(category, (Actor,), {})
        return name(name, category, x, y, z, sprite)

    def new_item(self, name, **params):
        ''' добавляет новый предмет '''
        self

    def new_spell(self, name, **params):
        ''' добавляет новое заклинание '''
        self


    def add_pc_to_team(self, pc):
        ''' добавдяет персонажа в команду '''
        self

    def remove_pc_from_team(self, pc):
        ''' удаляет персонажа из команды '''
        self

    def start_script(script):
        ''' активирует скрипт '''
        script

    def stop_thread(script):
        '''остановливает скрипт '''
        script
