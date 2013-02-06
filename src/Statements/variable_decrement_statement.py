from Statements.statement_factory import __statementClasses
from Variables.variable import Variable

import re

class VariableDecrementStatment:
    """ Increments a Variable by a given number or 1 by defult"""
    
    def __init__(self):
        """ """
    
    def isValidStatement(self, statementString, variableTable):
        """ Returns if the string is a valid statement """
        validStatement = re.match(r".+, IM SHRINKIN YA BY .+", statementString)
        
        if not validStatement: #Maybe increase by 1
            validStatement = re.match(r".+, IM SHRINKIN YA", statementString)
            self.decrement = True
        else:
            self.decrement = False
        
        if validStatement:
            self.checkValidVariable(statementString, variableTable)
            self.checkValidValue(statementString)
            print self.variable, self.value
        return validStatement
    
    def toCCode(self):
        if self.decrement:
            return "{0}--;\n".format(self.variable.name)
        else:
            return "{0} -= {1};\n".format(self.variable.name, self.value)
        
    def checkValidVariable(self, statementString, variableTable):
        """ Checks if the variable in the statement is a valid variable """
        variableName = self.getVariableName(statementString)
        self.variable = variableTable.getVariableWithName(variableName)
        if self.variable is None:
            print variableName, " is not a recognized variable"
    
    def checkValidValue(self, statementString):
        """ Checks to see if the value is a valid value"""
        if not self.decrement:
            self.value = statementString.split(", IM SHRINKIN YA BY ")[1].strip()
        else:
            self.value = 1
        
    def getVariableName(self, statementString):
        """ Return the variable name in the given statment"""
        return statementString.split(",")[0]
        
__statementClasses.append(VariableDecrementStatment) # Register with the Statement Factory