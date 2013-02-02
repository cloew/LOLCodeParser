from lolcode_parser import LOLCodeParser

class LOLCodeFileReader:
    """ Class to parse LOL Code Files """
    
    def __init__(self):
        """ Create the LOL Code Parser """
        self.parser = LOLCodeParser()
        
    def parseFile(self, filename):
        """ Parse the given file """
        file = self.openFile(filename)
        for line in file.readlines():
            self.parser.parse(line)
        # Generate Output File
        
    def openFile(self, filename):
        """ Return the opened file """
        return open(filename, 'r')