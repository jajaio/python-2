from player import Player

class Game():
    def __init__(self):
        print('Welcome to the game')
            self.player=Player()
        
    def run(self):
        self.player.show_stats()
        while True:
            action=input('What do you wanna do?')
        
if __name__=='__main__':
    agame=Game()
    agame.run()
