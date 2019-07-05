#!/usr/bin/env python
# coding: utf-8

# @author: Samy Bencherif (1998)
# @region: North Carolina
# @copyright: May 2019
# @file: nc98ge
# @title: NCurses wrapper for Graphical Expressions
# @description: Provides minimal graphics support to systems that
# support only 8 color text mode.

import curses
import sys
import os
from datetime import datetime

"""
HINT: If you are losing grip on reality, press CTRL+C, type reset,
press ENTER, then dream on.
"""


BLACK   = 1
RED     = 2
GREEN   = 3
YELLOW  = 4
BLUE    = 5
MAGENTA = 6
CYAN    = 7
WHITE   = 8

class Program:

    def __init__(self, stdscr):
        self.finished = False
        self.stdscr = stdscr
        self.fillchar = " "

        self.w = None
        self.h = None

        self.logfile = open("log.txt", "at")

    def key(self, k):
        pass

    # rendering functions

    def clear(self, fill=BLACK):
        #self.stdscr.clear()

        self.rect(self.w//2, self.h//2, self.w, self.h, fill)

    def cols(self, rcount):
        return round( rcount * 41 / 24. )

    def rows(self, ccount):
        """
        Convert length measured in columns to rows
        based on screen measurements.
        """

        return round( ccount * 24 / 41. )

    def pix(self, x, y, col):
        try:
            self.stdscr.addstr(y, x, self.fillchar,
                    curses.color_pair(col))
        except:
            # don't complain if pixel is not rendered
            # or is in bottom right corner
            pass

    def print(self, x, y, msg):
        try:
            bw = min(self.w - x, len(msg))
            self.stdscr.addstr(y, x, msg[:bw], BLACK)
        except:
            pass

    def rect(self, x, y, w, h, col):
        # screen dimensions
        SH, SW = self.stdscr.getmaxyx()

        # center rect
        x -= w//2
        y -= h//2

        # bounded x
        bx = max(0, x)

        # bounded width
        bw  = min(w, SW-x) - (bx-x)

        by = max(0, y)

        bh  = min(h, SH-y) - (by-y)

        if bw > 0:
            for i in range(by, by+bh):
                try:
                    self.stdscr.addstr(i, bx, self.fillchar * bw,
                            curses.color_pair(col))
                except:
                    # all cases are covered by bounding
                    # except wrapping on bottom right
                    pass

    def circ(self, x, y, r, col):
        rh = self.rows(r)
        for i in range(-rh, rh+1):
            self.rect(x, y+i, round(2*(max(0, r**2-self.cols(i)**2))**.5), 1,
                    col)

    def log(self, msg):
        self.logfile.write("[%s] %s\n" % (
                datetime.strftime(
                    datetime.now(),
                    "%b %d %I:%M %p"
                ),
                msg
            )
        )

    def quickReport(self, tb):

            if tb.tb_next:
                self.quickReport(
                        tb.tb_next
                        )

            sys.stderr.write("Error on line %s of %s." % (
                    tb.tb_lineno,
                    os.path.basename(tb.tb_frame.f_code.co_filename)
                )
            )
            sys.stderr.write("\n")

    def endProg(self, err=None):

        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()

        curses.endwin()

        self.logfile.close()

        if err:
            sys.stderr.write(str(err)[0].upper())
            sys.stderr.write(str(err)[1:])
            sys.stderr.write(".")
            sys.stderr.write("\n")
            self.quickReport(err.__traceback__)
            sys.exit(1)
        else:
            sys.exit()

def execute(program, fdlay=1):

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    curses.start_color()

    for i in range(8):
        if i == WHITE-1:
            curses.init_pair(i+1, BLACK-1, i)
        else:
            curses.init_pair(i+1, WHITE-1, i)

    curses.halfdelay(fdlay)

    curses.curs_set(0)

    prg = program(stdscr)

    prg.h, prg.w = prg.stdscr.getmaxyx()

    try:
        prg.begin()
    except Exception as ex:
        prg.endProg(err=ex)

    k = -1

    while not prg.finished:
        try:
            prg.h, prg.w = prg.stdscr.getmaxyx()
            prg.update()
        except Exception as ex:
            prg.endProg(err=ex)

        stdscr.refresh()

        if k != -1:
            try:
                prg.key(k)
            except Exception as ex:
                prg.endProg(err=ex)

        k = -1

        try:
            k = stdscr.getkey()
        except KeyboardInterrupt:
            prg.endProg()
            pass
        except:
            pass # no input

    prg.endProg()
