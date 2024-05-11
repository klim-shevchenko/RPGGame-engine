from rpg.area import *
from rpg.graphics import *
from rpg.sprite import *
from rpg.actor import *
class Game():
    def __init__(self, canvas, **params):
        self.rpg_dict_of_area = {} # словарь, хранящий в себе множество экземпляров класса Area, {number - ключ : name Area - значение}
        self.team_of_pc = [] # список, хранящий в себе имена экземпляров класса Actor с параметром category = "pc"
        self.canvas = canvas # графика
        self.current_area = None # параметр хранящий, текущую зону

    def new_area(self, name, area):
        ''' добавляет новую зону в список
         param name - имя зоны area - класс area()'''
        self.rpg_dict_of_area[name] = area

    def set_area(self, name):
        ''' устанавливает текущую зону, загружает графику зоны.
         param name - имя зоны.'''
        if name in self.rpg_dict_of_area:
            self.current_area = self.rpg_dict_of_area[name]
            self.canvas.clear_all()
            for sprite in self.current_area.sprites:
                sprite.update(sprite.x, sprite.y)
                self.canvas.add_sprite(sprite, sprite.x, sprite.y, sprite.z)

    def new_actor(self, name, **params):
        ''' создёт класс, потомок от Actor и создаёт поле из параметров, и установление их в начальные значения.
        params name - название нового класса, **params - поля нового класса
        return - новый класс '''
        class_attributes = {}
        for key, value in params.items():
            class_attributes[key] = value
        return type(name, (Actor,), class_attributes)

    def new_item(self, name, **params):
        ''' добавляет новый предмет '''
        self

    def new_spell(self, name, **params):
        ''' добавляет новое заклинание '''
        self


    def add_pc_to_team(self, pc):
        ''' добавдяет персонажа в команду '''
        if pc.category == "pc":
            self.team_of_pc.append(pc)
        else: print('попытка добавить персонажа в команду не успешна')

    def remove_pc_from_team(self, pc):
        ''' удаляет персонажа из команды '''
        self

    def start_script(script):
        ''' активирует скрипт '''
        script

    def stop_thread(script):
        '''остановливает скрипт '''
        script
    def set_team(self, area, x, y, z):
        ''' устанавливает команду. '''
        for elememt in self.team_of_pc:
            if elememt in area.list_of_actors:
                elememt.pos_x = x
                elememt.pos_y = y
                elememt.pos_z = z
                elememt.sprite.update(elememt.pos_x, elememt.pos_y)
            else:
                area.add_object(elememt, x, y, z)
                self.canvas.add_sprite(elememt.sprite, elememt.sprite.x, elememt.sprite.y, elememt.sprite.z)