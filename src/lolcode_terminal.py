
class LOLCodeTerminal:
    """ Acts as an in-console LOLCode Parser and initerpreter. """
    # I figured this could be a good way for us to start out with our Parsing
    # and what not -- CML
    # Also, LOLCodeTerminal may be a poor name for this
    
    def __init__(self):
        """ Do magic Initialization stuffz """
        
    def run(self):
        """ Runs the Interactive LOLCode Terminal Session """
        self.running = True
        while self.running:
            self.printLine()
            self.getAndValidateInput()
        
    def printLine(self):
        """ Prints the line header for the Interactive LOLCOde Terminal """
        print ">>>",
    
    def getAndValidateInput(self):
        """ Gets Validates input from the terminal """
        input = self.getInput()
        self.validateInput(input)
    
    def getInput(self):
        """ Waits for input and returns it """
        return raw_input()
    
    def validateInput(self, input):
        """ Validates input from the terminal """
        if input.upper() == "KTHXBYE":
            self.running = False
