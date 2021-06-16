import curses
from curses import wrapper
from curses import textpad
from tdiagram import TDiagram

def main (stdscr):
    curses.curs_set(0)
    sh,sw = stdscr.getmaxyx()
    first = TDiagram(0,sw,sh)
    first.read(1)
    first.read(1)
    first.read(0)
    first.write()
    second = TDiagram(1,sw,sh)
    second.read(1)
    second.read(1)
    second.read(0)
    second.read(1)
    second.write()
    while(1):
        continue

    # box = [[3,3],[sh-3,sw-3]]
    # textpad.rectangle(stdscr,box[0][0],box[0][1],box[1][0],box[1][1])
    # stdscr.refresh()
    # stdscr.getch()



wrapper(main)


# #End Curses
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()
# curses.endwin()