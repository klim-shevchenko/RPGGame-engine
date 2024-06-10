from rpg.object import Object
from rpg.game import Game
from rpg.rectangle import Rectangle

class Portal(Object):
    def __init__(self, x, y, width, height, area, team_x, team_y):
        ''' 
        Создает портал в новую зону

        :param x: координата x портала
        :param y: координата y портала
        :param width: ширина портала
        :param height: высота портала
        :param area: имя зоны куда будет переход
        :param team_x: местоположение команды в новой зоне
        :param team_y: местоположение команды в новой зоне
        '''
        self.states = None
        self.sprite = None
        self.category = 'portal'
        super().__init__(x, y, 0)
        self.rectangle = Rectangle(x, y, width, height)
        self.area = area
        self.team_x = team_x
        self.team_y = team_y
        self.visible = False

    def actor_in(self, actor):
        '''
        Проверяет находится ли персонаж внутри портала

        :param actor: проверяемый персонаж
        '''
        if actor.category == "pc":
            Game.game.set_area(self.area)
            Game.game.set_team(self.team_x, self.team_y, 100)
            actor.stop_move()
