import cmd


class SAPI:
    def __init__(self, api):
        pass


class Shell(cmd.Cmd):
    prompt = '>'

    def emptyline(self):
        print('emptyline')

    def do_aaa(self, arg):
        print(arg)

    def preloop(self):
        print('preloop')

    def postloop(self):
        print('postloop')

    # def precmd(self, line):
    #     print('precmd', line)
    #     self.onecmd(line)

    def postcmd(self, stop, line):
        print('postcmd', stop, line)

    def default(self):
        print('default')
