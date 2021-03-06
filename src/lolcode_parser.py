import Statements
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
        line = self.removeCommentFromLine(line)
        if line != "":
            statement = FindMatchingStatement(line, self.variableTable)
            if statement is not None:
                self.statements.append(statement)
        self.printVariables()
        
    def getCCodeLines(self):
        """ Return the C Code lines of the Parser's Statements """
        cCodeLines = []
        for statement in self.statements:
            cCodeLines.append(statement.toCCode())
        return cCodeLines
        
    def removeCommentFromLine(self, line):
        """ Removes comments from the given line and returns it """
        return line.split("BTW")[0].strip()
        
    def printVariables(self):
        """ Print variables """
        for variable in self.variableTable.variables:
            print variable.type, variable.name