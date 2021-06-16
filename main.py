import getopt
import sys
import curses
from curses import wrapper
from curses import textpad
from tdiagram import TDiagram


def main(stdscr):
    argumentList = sys.argv[1:]
    options = "hdbac"  # heater display battery accelerometer camera
    long_options = ["Heater", "Display", "Battery", "Accelerometer", "Camera"]
    state = 0
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Heater"):
                state = 1
                numWindows = 8  # Heater interrupt, flip-flop reset,6 pwm pins

            elif currentArgument in ("-d", "--Display"):
                state = 2
                numWindows = 2  # DVI low power, Backlight enable

            elif currentArgument in ("-b", "--Battery"):
                state = 3
                numWindows = 3

            elif currentArgument in ("-a", "--Accelerometer"):
                state = 4
                numWindows = 1

            elif currentArgument in ("-c", "--Camera"):
                state = 5
                numWindows = 2

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    if(state == 0):
        sys.exit()

    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    gpioList = []
    if(state == 1):
        TMP_ALERT = TDiagram("TMP_ALERT", 0, sw, sh)
        RESET = TDiagram("RESET", 1, sw, sh)
        PWM = []
        for i in range(0, 5):
            PWM.append(TDiagram("HEATER"+str(i+2), i+2, sw, sh))

        TMP_ALERT.read(0)
        TMP_ALERT.read(0)
        TMP_ALERT.read(0)
        TMP_ALERT.read(1)
        TMP_ALERT.read(0)
        RESET.read(0)
        RESET.read(0)
        RESET.read(0)
        RESET.read(1)
        RESET.read(0)
        RESET.read(0)
        TMP_ALERT.write()
        RESET.write()
        while 1:
            continue


if __name__ == "__main__":
    wrapper(main)


# #End Curses
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()
# curses.endwin()
