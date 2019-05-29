
import nc98ge

from nc98ge import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

class Game(nc98ge.Program):

    def begin(self):
        self.window = (-2, -2, 2, 2)

    def key(self, k):

        self.log(k)

    def drawGrid(self):


        for x in range(self.w+1):

            xi = x/float(self.w)

            xw = self.window[0] + xi * (self.window[2] - self.window[0])

            # horizontal axis
            self.rect(self.w//2, self.h//2, self.w, 1, WHITE)

        # vertical axis
        self.rect(self.w//2, self.h//2, self.cols(1), self.h, WHITE)

    def update(self):

        self.clear()

        self.drawGrid()

nc98ge.execute(Game)
