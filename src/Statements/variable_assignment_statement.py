from Variables.variable import Variable

import re

class VariableAssignmentStatement:
    """ Represents the Variable Assignment Statement """
    types = ["INT"]
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variableTable):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        validStatement = re.match(r".+, I HAVE .+? TO PUT IN YOU", statementString)
        
        if validStatement:
            self.checkValidVariable(statementString, variableTable)
            self.checkValidValue(statementString)
            print self.variable, self.value
        return validStatement
        
    def toCCode(self):
        """ Translates the statement to C Code """
        return ""
        
    def checkValidVariable(self, statementString, variableTable):
        """ Checks if the variable in the statement is a valid variable """
        variableName = self.getVariableName(statementString)
        self.variable = variableTable.getVariableWithName(variableName)
        if self.variable is None:
            print variableName, "is not a recognized variable"
            
    def checkValidValue(self, statementString):
        """ Checks if the value is a valid value """
        valueHalf = statementString.split(", I HAVE ")[1]
        self.value = valueHalf.split(" TO PUT IN YOU")[0].strip()
        # Should check if the value is a proper value for the variable type
    
    def getVariableName(self, statementString):
        """ Returns the variable name in the given statement string """
        return statementString.split(",")[0]