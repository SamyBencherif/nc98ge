
import nc98ge

from nc98ge import BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

"""

color key

  1+     BLUE
  1-     MAGENTA
  0      BLACK
  i+     RED
  i-     YELLOW
  1+i+   GREEN
  1-i+   CYAN
  1+i-   GREEN
  1-i-   CYAN

  labels + axis   WHITE

"""

class Game(nc98ge.Program):

    def begin(self):
        self.window = (-3, -2, 2, 2)
        self.gridColor = WHITE

        self.fn = lambda x: x

    def key(self, k):

        self.log(k)

    def drawGrid(self):


        # horizontal axis
        self.rect(self.w//2, self.h//2, self.w, 1, WHITE)


        for x in range(self.w+1):

            xi = x/float(self.w)
            xw = self.window[0] + xi * (self.window[2] - self.window[0])
            xin = (x+1)/float(self.w)
            xwn = self.window[0] + xin * (self.window[2] - self.window[0])
            xinn = (x+2)/float(self.w)
            xwnn = self.window[0] + xinn * (self.window[2] - self.window[0])
            # vertical axis
            if xw < 0 and xwnn > 0:
                self.rect(x, self.h//2, 1, self.h, self.gridColor)
            elif round(xwn % 1) == 1 and round(xwnn % 1) == 0:
                # numbers
                self.print(x, self.h//2 -2, str(round(xwn)))

            # vertical tick
            if round(xw % 1) == 1 and round(xwnn % 1) == 0:
                self.rect(x, self.h//2, 1, 3, self.gridColor)


    def colorBlock(self, x0, y0, x1, y1, c0, c1, on, off):
        #self.rect((x0+x1)//2, (y0+y1)//2, x1-x0, y1-y0, c0)

        i = 0
        o = 0
        for y in range(y0, y1+1):
            for x in range(x0, x1+1):
                i = i % (on + off)
                self.pix(x, y, c0 if i < on else c1)
                i += 1
            o += 1
            i = -o

    def update(self):

        self.clear()

        # note: not drawing function, testing gradient
        for i in range(3):
            self.colorBlock(int(i*self.w/3),0,
                    int(i*self.w/3+self.w/3),self.h,RED,BLACK,1,i)
        self.drawGrid()

nc98ge.execute(Game)
