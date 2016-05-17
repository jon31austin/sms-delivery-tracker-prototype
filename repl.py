import cmd 
from delivery import *

class REPL(cmd.Cmd):

    delivery = Delivery()
    prompt = "> "
    
    def preloop(self): 
        print self.delivery.initial_prompt

    
    def default(self, line): 
        if line == ":quit":
            return True 
        else: 
            response = self.delivery.process_input(line)
            print response 
            
if __name__ == '__main__':
    repl = REPL()
    repl.cmdloop() 