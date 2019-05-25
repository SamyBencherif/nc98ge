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

class Program:

    def __init__(self, stdscr):
        self.stdscr = stdscr

def execute(program):
    
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    prg = program(stdscr)
    prg.begin()

    while not prg.finished():
        prg.update()

    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

    curses.endwin()
