from Statements.statement_factory import __statementClasses

class ProgramExitStatement:
    """ Represents the Program Exit Statement """
    
    def __init__(self):
        """  """
        
    def isValidStatement(self, statementString, variableTable):
        """ Returns if the string is a valid statement """
        # May want this to throw an exception if the statement looks almost proper, but fails for some reason
        return statementString == "KTHXBYE!"
        
    def toCCode(self):
        """ Translates the statement to C Code """
        return "return 0;\n}"
        
__statementClasses.append(ProgramExitStatement) # Register with the Statement Factory