import sys
from pathlib import Path
from time import sleep

sys.path.append(str(Path(__file__).parent.parent))
from src import ytils


def test_printer():
    from src.ytils import printer

    print("Line 1")
    print("Line 2")
    sleep(1)
    printer.Cursor.up(2)
    printer.Cursor.column(3)
    print("Hello World")
    sleep(1)
    printer.Cursor.down(3)
    print("Zebra", end="")
    sleep(3)
    printer.Cursor.beginning()
    print("Bebra")
    # for i in range(20):
    #     print(f"{i}    ", end="\r")
    #     sleep(0.5)
    
    input('Enter a 5 letter word: ')
    printer.Cursor.up(1)
    print('words go here          ')
    # print('\x1b[1A' + 'words go here          ')

        


if __name__ == "__main__":
    test_printer()
