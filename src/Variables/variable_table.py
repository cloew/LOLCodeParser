
class VariableTable:
    """ Represents the table of variables """
    
    def __init__(self):
        """ Start the variable list """
        self.variables = []
        
    def addVariable(self, variable):
        """ Adds the variable to the variable list """
        self.variables.append(variable)
        
    def getVariableWithName(self, name):
        """ Returns the variable with the given name or None if it is not found """
        foundVariable = None
        for variable in self.variables:
            if name == variable.name:
                foundVariable = variable
                break
        return foundVariable