import sys

from lolcode_terminal import LOLCodeTerminal

def main(args):
    """ Program entry point for the Python LOLCode Parser """
    print args
    terminal = LOLCodeTerminal()
    terminal.run()

if __name__ == "__main__":
    main(sys.argv[1:])