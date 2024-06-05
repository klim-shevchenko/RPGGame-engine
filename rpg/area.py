class Area():
    def __init__(self, **params):
        self.area_zone = params # параметр определяющий особенности конкретной зоны
        self.list_of_objects = [] # список, хранящий в себе множество экземпляров классов Item
        self.list_of_actors = []  # список, хранящий в себе множество экземпляров классов Actor
        self.sprites = [] # список, хранящий в себе множество экземпляров класов Sprite
        self.rectangles = None # список, хранящий в себе множетво прямоугольников

    def add_sprite(self, sprite, x, y, z):
        '''добавляет спрайт в зону
        param sprite - экземпляр спрайта, x y z - коодринаты'''
        sprite.x = x
        sprite.y = y
        sprite.z = z
        self.sprites.append(sprite)

    def add_object(self, obj, x, y, z):
        ''' добавляет объект в зону
        param obj - объект, x y z - коодринаты '''
        obj.pos_x = x
        obj.pos_y = y
        obj.pos_z = z
        if not obj.category:
            self.list_of_objects.append(obj)
        else:
            self.list_of_actors.append(obj)
        self.add_sprite(obj.sprite, obj.pos_x, y, z)

    def add_rect(self, rec):
        ''' добавляет прямоугольник в зону'''
        self.rectangles = rec

    def check_obj_sprite(self):
        ''' проверяет координаты объекта '''
        self

    def update(self):
        '''изменяет проверяет изменение всех персонажей в зоне'''
        for actor in self.list_of_actors:
            if actor.rectangle.is_in(self.rectangles):
                actor.update() # требуется закомментировать, если выбран вариант animate_sprite
                '''actor.anim_update()''' # требуется раскомментировать, если выбран вариант animate_sprite
            else:
                actor.stop_move()