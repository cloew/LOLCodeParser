from Statements.statement_factory import FindMatchingStatement
from Variables.variable_table import VariableTable

class LOLCodeParser:
    """ Parses LOL Code lines """
    
    def __init__(self):
        """ Construct the LOLCodeParser """
        self.variableTable = VariableTable()
        self.statements = []
    
    def parse(self, line):
        """ Parse the line of LOLCode """
        line = line.strip()
        if line != "":
            statement = FindMatchingStatement(line, self.variableTable)
            if statement is not None:
                self.statements.append(statement)
        self.printVariables()
        print self.statements
        
    def printVariables(self):
        """ Print variables """
        for variable in self.variableTable.variables:
            print variable.type, variable.name