
import nc98ge

class Game(nc98ge.Program):

    def begin(self):
        self.y = 0

    def update(self):
        pix(0, self.y, RED)
        self.y += 1

nc98ge.execute(Game)
