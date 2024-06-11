from rpg.area import *
from rpg.graphics import *
from rpg.sprite import *
from rpg.actor import *
from rpg.adnd_actor import Adnd_actor
import threading

class Game():
    def __init__(self, canvas, window, **params):
        '''
        Класс системы управления игрой

        :param canvas: класс графической системы
        :param window: окно на которое будет выводится игра
        '''
        self.rpg_dict_of_area = {} # словарь, хранящий в себе множество экземпляров класса Area, {number - ключ : name Area - значение}
        self.team_of_pc = [] # список, хранящий в себе имена экземпляров класса Actor с параметром category = "pc"
        self.canvas = canvas # графика
        self.root = window # окно для графики
        self.current_area = None # параметр хранящий, текущую зону
        self.scripts = {}  # Словарь для хранения запущенных сценариев
        self.events = {} # Словарь для хранения запущенных event`ов сценариев
        self.canvas.bind("<Button-1>", self.mouse_left_click)
        Game.game = self

    def new_area(self, name, area):
        '''
        Добавляет новую зону в список

        :param name: имя зоны
        :param area: класс area
        '''
        self.rpg_dict_of_area[name] = area

    def set_area(self, name):
        '''
        Устанавливает текущую зону, загружает графику зоны.

        :param name: имя зоны
        '''
        if name in self.rpg_dict_of_area:
            if self.current_area is not None:
                self.current_area.exit_script()
                for pc in self.team_of_pc:
                    self.current_area.remove_object(pc)
            self.current_area = self.rpg_dict_of_area[name]
            self.canvas.clear_all()
            self.current_area.load_sprites()
            for pc in self.team_of_pc:
                self.current_area.add_object(pc, pc.pos_x, pc.pos_y, pc.pos_z)

    def new_actor(self, name, **params):
        '''
        Создаёт класс, потомок от Actor и создаёт поле из параметров, и установление их в начальные значения.

        :param name: название нового класса
        :param params: поля нового класса
        '''
        class_attributes = {}
        for key, value in params.items():
            class_attributes[key] = value
        return type(name, (Actor,), class_attributes)

    def add_pc_to_team(self, pc):
        '''
        Добавдяет персонажа в команду
        :param pc: персонаж, которого нужно добавить в команду
        '''
        if pc.category == "pc":
            self.team_of_pc.append(pc)
        else: print('попытка добавить персонажа в команду не успешна')

    def remove_pc_from_team(self, pc):
        ''' удаляет персонажа из команды '''
        if pc.category == "pc":
            self.team_of_pc.remove(pc)
        else:
            print('попытка удалить персонажа из команды не успешна')

    def start_script(self, script_function, script_name, *args):
        '''
        Запускает сценарий в отдельном потоке с возможностью остановки и передачи аргументов.

        :param: script_function: Функция, содержащая код сценария.
        :param: script_name: Имя сценария.
        :param: args: Дополнительные аргументы, которые нужно передать в сценарий.
        '''
        # Создание потока для сценария
        e = threading.Event()
        self.events[script_name] = e

        def func(e, args):
            while not e.is_set():
                script_function(*args)

        # Создание потока для сценария
        script_thread = threading.Thread(target=func, args=(e, args))
        script_thread.daemon = True
        script_thread.start()

        # Добавление потока в словарь активных сценариев
        self.scripts[script_name] = script_thread

    def stop_script(self, script_name):
        '''
        Останавливает сценарий по имени

        :param: script_name: имя сценария, который нужно остановить
        '''
        # Проверка существования сценария
        if script_name in self.scripts:
            # Если сценарий существует, прерываем его выполнение
            self.events[script_name].set()
            # Убираем сценарий из словаря активных сценариев
            del self.scripts[script_name]
            del self.events[script_name]
            print(f"Сценарий {script_name} остановлен.")
        else:
            # Если сценарий не существует
            print(f"Сценарий {script_name} не существует.")

    def set_team(self, x, y, z):
        '''
        Устанавливает координаты персонажей команды

        :param x: координата x
        :param y: координата y
        :param z: координата z
        '''
        for elememt in self.team_of_pc:
            elememt.pos_x = x
            elememt.pos_y = y
            elememt.pos_z = z

    def update(self):
        '''
        Вызывается в таймере для обновления всех переменных в текущей зоне

        '''
        self.current_area.update()
        self.canvas.update()

    def mouse_left_click(self, event):
        for actor in self.current_area.objects:
            if actor.category == 'enemy':
                if actor.rectangle.is_point_inside(event.x, event.y):
                    actor.on_click()
        for actor in self.current_area.objects:
            if actor.category == 'pc':
                actor.search_position(event.x, event.y)

    def new_item(self, name, **params):
        '''
        Создаёт класс, потомок от Item и создаёт поле из параметров, и установление их в начальные значения.

        :param name: название нового класса
        :param params: поля нового класса
        '''
        '''item_attributes = {}
        for key, value in params.items():
            item_attributes[key] = value
        new_item = type(name, (Item,), item_attributes)
        # Добавление нового предмета в словарь игры
        self.items[name] = new_item
        return new_item'''

    def new_spell(self, name, **params):
        ''' добавляет новое заклинание '''
        self

    def timer(self):
        '''
        Таймер дожен вызывать метод update постоянно

        '''
        self.update()
        self.root.after(50, self.timer)

def new_actor(self, name, **params):
        '''
        Создаёт класс, потомок от Actor и создаёт поле из параметров, и установление их в начальные значения.

        :param name: название нового класса
        :param params: поля нового класса
        '''
        class_attributes = {}
        for key, value in params.items():
            class_attributes[key] = value
        return type(name, (Adnd_actor,), class_attributes)

