import os
import subprocess
import time
from multiprocessing.pool import Pool

output_dir = "output"
parallelism = 2


def f(command_tuple):
    # Commands is a list of tuples where each tuple contains the command and the file to save the output to
    command, file = command_tuple
    print 'Running:%s, output:%s' % (command, file)
    start_time = time.time()
    with open(file, 'a') as fp:
        subprocess.call(command, stdout=fp, stderr=fp, shell=True)
    end_time = time.time()
    print "Finished:%s, output:%s, time:%s sec" % (command, file, end_time - start_time)


if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    commands = [("python main.py %s" % i, "%s/nohup.%s.out" % (output_dir, i)) for i in range(20)]
    # Commands is a list of tuples where each tuple contains the command and the file to save the output to
    print("%s Commands will be run \n%s" % (len(commands), commands))
    print("Parallelism = %s" % parallelism)
    p = Pool(parallelism)
    print(p.map(f, commands))
