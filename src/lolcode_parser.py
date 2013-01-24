from Statements.statement_factory import FindMatchingStatement

class LOLCodeParser:
    """ Parses LOL Code lines """
    
    def parse(self, line):
        """ Parse the line of LOLCode """
        line = line.strip()
        FindMatchingStatement(line)
        