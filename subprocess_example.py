import os
from multiprocessing import Pool

'''
processes = ('C:\\Users\\patelvi\\PycharmProjects\\NCE\\1.py',
             'C:\\Users\\patelvi\\PycharmProjects\\NCE\\2.py')
'''
processes =(
    'C:\\Users\\patelvi\\PycharmProjects\\NCE\\14.py',
    'C:\\Users\\patelvi\\PycharmProjects\\NCE\\15.py',
    'C:\\Users\\patelvi\\PycharmProjects\\NCE\\16.py')


def run_process(process):
    os.system('python {}'.format(process))

if __name__ == '__main__':

    pool = Pool(processes=3)
    pool.map(run_process, processes)




'''
import subprocess

subprocess.call(['python','C:\\Users\\patelvi\\PycharmProjects\\NCE\\12.py'])
subprocess.call(['python','C:\\Users\\patelvi\\PycharmProjects\\NCE\\13.py'])
'''