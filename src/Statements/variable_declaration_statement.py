from Variables.variable import Variable

import re

class VariableDeclarationStatement:
    """ Represents the Variable Declaration Statement """
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variables):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        validStatement = re.match(r"I HAZ .+? .+", statementString)
        
        if validStatement:
            self.addVariableToVariableList(statementString, variables)
        return validStatement
        
    def toCCode(self):
        """ Translates the statement to C Code """
        
    def addVariableToVariableList(self, statementString, variables):
        """ Returns the variable name in the given statement string """
        name = self.getVariableName(statementString)
        type = self.getVariableType(statementString)
        variables.append(Variable(name, type))
    
    def getVariableName(self, statementString):
        """ Returns the variable name in the given statement string """
        return "x"
    
    def getVariableType(self, statementString):
        """ Returns the variable type in the given statement string """
        return "INT"