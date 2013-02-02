from Variables.variable import Variable

import re

class VariableAssignmentStatement:
    """ Represents the Variable Assignment Statement """
    types = ["INT"]
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variables):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        validStatement = re.match(r".+, I HAVE .+? TO PUT IN YOU", statementString)
        
        if validStatement:
            """ """
            #self.addVariableToVariableList(statementString, variables)
        return validStatement
        
    def toCCode(self):
        """ Translates the statement to C Code """
    
    def getVariableName(self, statementString, type):
        """ Returns the variable name in the given statement string """
        return statementString.split(type)[1]
    
    def getVariableType(self, statementPieces):
        """ Returns the variable type in the given statement string """
        for type in VariableDeclarationStatement.types:
            if type in statementPieces:
                return type
        # Should throw an exception if it does not have a valid type