API = None


class SAPI:
    def __init__(self, api):
        global API
        API = api


class Main():
    world = None
    shell = None

    def __init__(self):
        global API
        # 生成世界
        lib_world = API(['get', 'lib', 'world'])
        self.world = lib_world.World()
        self.world.generate()
        # 进入自定义命令行
        lib_shell = API(['get', 'lib', 'shell'])
        self.shell = lib_shell.Shell()
        self.shell.cmdloop()
