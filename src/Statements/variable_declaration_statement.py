import re

class VariableDeclarationStatement:
    """ Represents the Variable Declaration Statement """
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variables):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        return re.match(r"I HAZ .+? .+", statementString)
        
    def toCCode(self):
        """ Translates the statement to C Code """