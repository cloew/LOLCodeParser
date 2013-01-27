from Statements.statement_factory import FindMatchingStatement

class LOLCodeParser:
    """ Parses LOL Code lines """
    
    def __init__(self):
        """ Construct the LOLCodeParser """
        self.variables = []
    
    def parse(self, line):
        """ Parse the line of LOLCode """
        line = line.strip()
        FindMatchingStatement(line, self.variables)
        self.printVariables()
        
    def printVariables(self):
        """ Print variables """
        for variable in self.variables:
            print variable.type, variable.name