class Game():
    show_top_score=0
    def __init__(self,player_name):
        self.player_name=player_name
    @staticmethod
    def show_help():
        print("帮助信息")
    @classmethod
    def show_top_score(cls):
        print("历史最高得:%d分"%cls.show_top_score)
    def start_game(self):
        print("%s开始游戏了"%self.player_name)
Game.show_top_score()
Game.show_help()
game=Game("小明")
#只访问类属性时就用类方法，如果既要访问类属性与实例属性，则用实例方法
