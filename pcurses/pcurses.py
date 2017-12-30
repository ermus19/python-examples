import curses

screen = curses.initscr()

screen.border(0)
screen.addstr(12, 25, "Hello World!")
screen.refresh()
screen.getch()

curses.endwin()