from player import Player
import monster as m
class Game():
    def __init__(self):
        print('Welcome to the game')
        self.player=Player()
    
    def run(self):
        self.player.show_stats()
        while True:
            self.player.show_stats()
            action=input('What do you wanna do?')
            if action=="stats":
                self.player.show_stats()
            elif action=="save":
                pass
            elif action=="exit":
                input("Bye!")
                exit()
            elif action=="monster":
                count=1

                
    

if __name__=='__main__':
    agame=Game()
    agame.run()
