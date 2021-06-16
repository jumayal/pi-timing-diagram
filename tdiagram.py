import curses


class TDiagram:
    def __init__(self, pin, sw, sh):
        self.sw = sw
        self.sh = sh
        self.win = curses.newwin(5, self.sw, pin * 3, 0)
        self.binary = []

    def read(self, b):
        if len(self.binary) > self.sw:
            self.binary.pop(0)
        self.binary.append(b)

    def write(self):
        # self.wind.clear()
        x = 0
        prev = 0
        for b in self.binary:
            if prev != b:
                self.win.addstr(2, x, "|")
                x = x + 1
            if b == 0:
                y = 2
            else:
                y = 1
            self.win.addstr(y, x, "_")
            prev = b
            x = x + 1
        self.win.refresh()
