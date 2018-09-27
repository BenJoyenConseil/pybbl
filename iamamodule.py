import os


def execute_read_write():
    print('Path iamamodule :{}'.format(os.getcwd()))
    from iamapackage.lib import read_data, write_data
    read_data()
    write_data()