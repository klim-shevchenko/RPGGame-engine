from rpg.area import *
from rpg.graphics import *
from rpg.sprite import *
class Game():
    def __init__(self, **params):
        self.rpg_dict_of_area = {} # параметр - словарь, хранящий в себе множество экземпляров класса Area, {number - ключ : name Area - значение}
        self.team_of_pc = [] # параметр - список, хранящий в себе имена экземпляров класса Actor с параметром category = "pc"

    def new_area(self, name):
        ''' добавляет новую зону в список
         param name - имя зоны '''
        self.rpg_dict_of_area[name] = Area()

    def set_area(self, name):
        ''' устанавливает текущую зону, загружает графику зоны
         param name - имя зоны '''
        if name in self.rpg_dict_of_area:
            area = self.rpg_dict_of_area[name]
            for sprite in area.sprites:
                sprite.update()

    def new_item(self, name, **params):
        ''' добавляет новый предмет '''
        self

    def new_spell(self, name, **params):
        ''' добавляет новое заклинание '''
        self

    def new_actor(self, name, **params):
        ''' добавляет нового персонажа '''
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
