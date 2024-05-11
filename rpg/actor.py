#from object import *
import time

class Actor():
    def __init__(self, x = 0, y = 0, z = 0, **params):
        '''def __init__(self, name, category, x, y, z, sprite, **params):
        dnd_class, level, race, strange, agi, con, inteligence, wiz, charizma, - убрал эти параметры'''
        '''self.act_name = name # имя персонажа
        self.act_category = category
        self.act_hp = hp
        self.act_ac = ac
        self.act_speed = speed
        self.act_alive = True       
        self.act_loot = () # список, хранящий экземпляры класса Item
        self.act_text = None # текстовое сообщение, которое будет у нпс
        self.act_dnd_class = dnd_class # текстовое значение, обозначение класса ("warrior" "wizard" "cleric")
        self.act_level = level # числовое значение, обозначающее уровень персонажа
        self.act_race = race # текстовое значение, обозначающее расу персонажа("human" "elf" "dwarf")
        self.act_str = strange # числовое значение, обозначающее показатель храктеристики "сила"
        self.act_agi = agi # числовое значение, обозначающее показатель храктеристики "ловкость"
        self.act_con = con # числовое значение, обозначающее показатель храктеристики "телосложение"
        self.act_inteligence = inteligence # числовое значение, обозначающее показатель храктеристики "интеллект"
        self.act_wiz = wiz # числовое значение, обозначающее показатель храктеристики "мудрость"
        self.act_charizma = charizma # числовое значение, обозначающее показатель храктеристики "харизма"
        self.act_inventory = () # список, хранящий в себе множество экземпляров классов Item
        self.act_list_spells = () # список, хранящий в себе множество экземпляров классов Spell'''
        self.pos_x = x #  числовое значение обозначающее расположение на экране, по координате x
        self.pos_y = y #  числовое значение обозначающее расположение на экране, по координате y
        self.pos_z = z #  числовое значение обозначающее расположение на экране, по координате z
        #self.sprite = sprite  # спрайт персонажа, в будущем будет хранить в себе текущий кадр анимации.

    def read_text(self, text):
        '''вывод содержимого поля act_text экземпляра класса Actor на экран'''
    def open_inventory(self, inventory):
        '''вывод содержимого поля act_inventory экземпляра класса Actor на экран'''

    def open_list_spells(self, spells):
        '''вывод содержимого поля act_list_spells экземпляра класса Actor на экран'''

    def target_use_spell(self, spell, target):
        ''' вызов метода cast\_spell экземпляра класса Spell'''

    def target_use_item(self, item, target):
        ''' вызов метода use\_item экземпляра класса Item'''
    def position_update(self, x, y, speed, sprite):
        '''изменяет координаты персонажа'''
        while self.pos_x != x or self.pos_y != y:
            if x > self.pos_x:
                self.pos_x+=speed
            if x < self.pos_x:
                self.pos_x-=speed
            if y > self.pos_y:
                self.pos_y+=speed
            if y < self.pos_y:
                self.pos_y-=speed
            sprite.update(self.pos_x, self.pos_y)