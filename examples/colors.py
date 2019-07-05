
import nc98ge

from nc98ge import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

class Game(nc98ge.Program):

    def begin(self):
        self.x = 0
        self.y = 0

    def key(self, k):
        #self.log(k)
        if k == "KEY_UP":
            self.y -= 1
        if k == "KEY_DOWN":
            self.y += 1
        if k == "KEY_RIGHT":
            self.x += 1
        if k == "KEY_LEFT":
            self.x -= 1

    def update(self):

        self.clear()

        self.print(3,3,"Use Left/Right Arrow Keys.")

        self.circ(self.w//2, self.h//2, self.x, BLUE)

        self.pix(0,0, BLACK)
        self.pix(1,0, RED)
        self.pix(2,0, YELLOW)
        self.pix(3,0, BLUE)
        self.pix(4,0, MAGENTA)
        self.pix(5,0, CYAN)
        self.pix(6,0, WHITE)

        s = "(%s, %s)" % (self.x, self.y)
        self.print(self.w-len(s), 0, s)

nc98ge.execute(Game)
