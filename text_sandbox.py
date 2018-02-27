# coding=utf-8
"""MODULE DOC"""
import os
import glob
import time
import importlib

import json


class TextSandbox:
    """CLASS DOC"""
    lib = {}  # 官方/功能性/深层次 补丁/升级
    mod = {}  # 功能特性 可临时开关
    dlc = {}  # 非功能性数据更新
    prototype = {}  # 基类

    def __init__(self):
        pass

    def api(self, cmd):
        if cmd[0] == 'get':
            if cmd[1] == 'lib':
                return self.lib[cmd[2]]

    def load(self):
        """加载一切可能加载的东西"""
        lib_file_list = glob.glob('libs/*.py')
        prototype_list = glob.glob('prototypes/*.py')
        mod_file_list = glob.glob('mods/*.py')
        dlc_folder_list = glob.glob('dlcs/*')
        for lib_file_path in lib_file_list:
            lib_name = os.path.splitext(os.path.basename(lib_file_path))[0]
            print('[INFO]载入Lib:{}...'.format(lib_name), end='')
            self.lib[lib_name] = importlib.import_module(
                lib_file_path.split('.')[0].replace('\\', '.'))
            self.lib[lib_name].SAPI(self.api)
            print('OK')
        for prototype_file_path in prototype_list:
            prototype_name = os.path.splitext(
                os.path.basename(prototype_file_path))[0]
            print('[INFO]载入Prototype:{}...'.format(prototype_name), end='')
            self.prototype[prototype_name] = importlib.import_module(
                prototype_file_path.split('.')[0].replace('\\', '.'))
            self.prototype[prototype_name].SAPI(self.api)
            print('OK')
        for mod_file_path in mod_file_list:
            mod_name = os.path.splitext(os.path.basename(mod_file_path))[0]
            print('[INFO]载入Mod:{}...'.format(mod_name), end='')
            self.mod[mod_name] = importlib.import_module(
                mod_file_path.split('.')[0].replace('\\', '.'))
            self.mod[mod_name].SAPI(self.api)
            print('OK')
        for dlc_folder_path in dlc_folder_list:
            dlc_name = os.path.splitext(os.path.basename(dlc_folder_path))[0]
            print('[INFO]载入DLC:{}...'.format(dlc_name), end='')
            self.dlc[dlc_name] = importlib.import_module(
                dlc_folder_path.split('.')[0].replace('\\', '.'))
            self.dlc[dlc_name].SAPI(self.api)
            print('OK')
        time.sleep(10)

    def show_intro(self):
        """显示开场文字"""
        os.system('title 文字沙盒：开发版')
        os.system('cls')
        print('文字沙盒')
        time.sleep(1)

    def show_main_menu(self):
        """显示主菜单"""
        os.system('cls')
        print('文字沙盒')
        print()
        print('[ENTER]开始游戏')
        print()
        i = input('>')
        # shell = self.lib['shell'].Shell()
        # shell.cmdloop()
        while True:
            if i == '':
                os.system('cls')
                self.lib['main'].Main()
                break
            else:
                print(2)
                break


if __name__ == "__main__":
    # name_db = {}
    # with open('dlcs/default/db/LN.txt', 'r', encoding='utf8') as last_name_file:
    #     data = last_name_file.readlines()
    #     name_db['姓'] = []
    #     for each in data:
    #         if each[:-1] != '':
    #             name_db['姓'].append(each[:-1])
    # with open('dlcs/default/db/Man.txt', 'r', encoding='utf8') as last_name_file:
    #     data = last_name_file.read()
    #     name_db['男名'] = []
    #     for each in data:
    #         name_db['男名'].append(each)
    # with open('dlcs/default/db/Woman.txt', 'r', encoding='utf8') as last_name_file:
    #     data = last_name_file.read()
    #     name_db['女名'] = []
    #     for each in data:
    #         name_db['女名'].append(each)
    # print(name_db)
    # with open('dlcs/default/db/names.json', 'w') as dbfile:
    #     dbfile.write(json.dumps(name_db))
    # with open('dlcs/default/db/names.json', 'r') as dbfile:
    #     data = json.loads(dbfile.read())
    #     print(data)
    #     print(data['姓'][0] + data['男名'][0] + data['男名'][1])

    TEXT_SANDBOX = TextSandbox()
    TEXT_SANDBOX.load()
    TEXT_SANDBOX.show_intro()
    TEXT_SANDBOX.show_main_menu()
