import os
import sys

statementsDirectory = os.path.dirname(__file__)

for modulename in os.listdir(statementsDirectory):
    if modulename.endswith(".py") and modulename != "__init__.py":
        print modulename
        try:
            module = __import__(statementsDirectory, fromlist=[modulename[:-3]])
            module = getattr(module, modulename[:-3])
        except ImportError as error:
            print "Couldn't import", modulename
            print error
            continue

        # for attr in dir(module):
            # classAttribute = getattr(module, attr)
            # #print classAttribute
            # if hasattr(classAttribute, "isValidStatement"):
                # print "Has Valid Statement"
                # # do whatever