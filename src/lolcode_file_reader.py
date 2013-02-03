from lolcode_parser import LOLCodeParser

class LOLCodeFileReader:
    """ Class to parse LOL Code Files """
    
    def __init__(self):
        """ Create the LOL Code Parser """
        self.parser = LOLCodeParser()
        
    def parseFile(self, filename):
        """ Parse the given file """
        inputFile = self.openLOLCodeFile(filename)
        for line in inputFile.readlines():
            self.parser.parse(line)
        self.generateOutputFile()
        
    def generateOutputFile(self):
        """ Generate Output File """
        cCodeLines = self.parser.getCCodeLines()
        outputFile = open("out.c", 'w')
        outputFile.writelines(cCodeLines)
        
    def openLOLCodeFile(self, filename):
        """ Return the opened file """
        return open(filename, 'r')