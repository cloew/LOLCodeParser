from Variables.variable import Variable

import re

class VariableDeclarationStatement:
    """ Represents the Variable Declaration Statement """
    types = ["INT"]
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variableTable):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        validStatement = re.match(r"I HAZ .+? .+", statementString)
        
        if validStatement:
            self.addVariableToVariableList(statementString, variableTable)
        return validStatement
        
    def toCCode(self):
        """ Translates the statement to C Code """
		return "{0} {1};\n".format(self.variable.type.lower(), self.varable.name)
		    
        
    def addVariableToVariableList(self, statementString, variableTable):
        """ Returns the variable name in the given statement string """
        statementPieces = statementString.split()
        type = self.getVariableType(statementPieces)
        name = self.getVariableName(statementString, type)
        self.variable = Variable(name, type)
        variableTable.addVariable(self.variable)
    
    def getVariableName(self, statementString, type):
        """ Returns the variable name in the given statement string """
        return statementString.split(type)[1].strip()
    
    def getVariableType(self, statementPieces):
        """ Returns the variable type in the given statement string """
        for type in VariableDeclarationStatement.types:
            if type in statementPieces:
                return type
        # Should throw an exception if it does not have a valid type