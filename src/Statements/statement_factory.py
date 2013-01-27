from Statements.program_entry_statement import ProgramEntryStatement
from Statements.program_exit_statement import ProgramExitStatement

__statementClasses = [ProgramEntryStatement,
                      ProgramExitStatement]

def FindMatchingStatement(statementString, variables):
    """ Find a statement that matches a statement string """
    for statementClass in __statementClasses:
        statement = statementClass()
        if statement.isValidStatement(statementString, variables):
            print "Valid Statement"
            break
    else:
        print "No matching Statement"