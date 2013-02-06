# from Statements.program_entry_statement import ProgramEntryStatement
# from Statements.program_exit_statement import ProgramExitStatement
# from Statements.variable_assignment_statement import VariableAssignmentStatement
# from Statements.variable_declaration_statement import VariableDeclarationStatement
#from Statements.variable_increment_statement import VariableIncrementStatment
__statementClasses = []

def FindMatchingStatement(statementString, variableTable):
    """ Find a statement that matches a statement string """
    for statementClass in __statementClasses:
        statement = statementClass()
        if statement.isValidStatement(statementString, variableTable):
            print "Valid Statement"
            return statement
            break
    else:
        print "No matching Statement"
        return None
