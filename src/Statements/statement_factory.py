from Statements.program_entry_statement import ProgramEntryStatement
from Statements.program_exit_statement import ProgramExitStatement
from Statements.variable_declaration_statement import VariableDeclarationStatement

__statementClasses = [ProgramEntryStatement,
                      ProgramExitStatement,
                      VariableDeclarationStatement]

def FindMatchingStatement(statementString, variables):
    """ Find a statement that matches a statement string """
    for statementClass in __statementClasses:
        statement = statementClass()
        if statement.isValidStatement(statementString, variables):
            print "Valid Statement"
            break
    else:
        print "No matching Statement"