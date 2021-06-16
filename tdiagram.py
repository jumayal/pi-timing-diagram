import curses


class TDiagram:
    def __init__(self, name, pin, sw, sh):
        self.sw = sw
        self.sh = sh
        self.name = name
        self.win = curses.newwin(2, self.sw, pin * 3, 0)
        self.binary = []

    def read(self, b):
        self.buffer = b
        if len(self.binary) > self.sw:
            self.binary.pop(0)
        self.binary.append(b)

    def write(self):
        # self.wind.clear()
        prev = 0
        self.win.addstr(1, 0, self.name)
        x = 10
        for b in self.binary:
            if prev != b:
                self.win.addstr(1, x, "|")
                x = x + 1
            if b == 0:
                y = 1
            else:
                y = 0
            self.win.addstr(y, x, "_")
            prev = b
            x = x + 1
        self.win.refresh()
