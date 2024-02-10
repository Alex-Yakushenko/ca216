from cmd import Cmd
import os

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
    
        print ("Hello, %s" % name)



    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit
    
    def do_dir(self, args=None):
        '''lists files in the directory'''
        args = args.split(" ")
        if len(args) == 1:
            path = args[0]
        elif len(args) == 2:
            option = args[0]
            option = args[1]
        else:
            path = "."
        print(path)
        files = os.listdir(path)
        for name in files:
            print(name)




if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')