import sys

from lolcode_file_reader import LOLCodeFileReader
from lolcode_terminal import LOLCodeTerminal

def main(args):
    """ Program entry point for the Python LOLCode Parser """
    if len(args) > 0:
        fileReader = LOLCodeFileReader()
        fileReader.parseFile(args[0])
    else:
        terminal = LOLCodeTerminal()
        terminal.run()

if __name__ == "__main__":
    main(sys.argv[1:])