#!/usr/bin/env python3

from nc98ge import Program, execute, WHITE, CYAN

# refactor

class Block:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def activated(self):
        pass

class MyGame(Program):

    def begin(self):
        self.blocks = []
        self.blocks.append(Block(-5, 0, CYAN))


    def update(self):
        self.clear()
        self.pix(self.w//2, self.h//2, WHITE)
        self.pix(self.w//2+1, self.h//2, WHITE)

        for barrier in self.barriers:
            self.pix(*barrier, CYAN)
            barrier = (barrier[0]+1, barrier[1])
            self.pix(*barrier, CYAN)

    def key(self, k):
        if k == "w":
            for b in self.barriers:
                if b[0] == self.x and b[1] == self.y - 1:
                    return
            self.y -= 1
        if k == "s":
            for b in self.barriers:
                if b[0] == self.x and b[1] == self.y + 1:
                    return
            self.y += 1
        if k == "a":
            for b in self.barriers:
                if b[1] == self.y and b[0] == self.x - 2:
                    return
            self.x -= 2
        if k == "d":
            for b in self.barriers:
                if b[1] == self.y and b[0] == self.x + 2:
                    return
            self.x += 2

execute (MyGame)
