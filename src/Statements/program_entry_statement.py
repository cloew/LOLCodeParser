
class ProgramEntryStatement:
    """ Represents the Program Entry Statement """
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        return statementString == "HAI!"
        
    def toCCode(self):
        """ Translates the statement to C Code """