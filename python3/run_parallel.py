import os
import subprocess
import time
from multiprocessing.pool import Pool

##############
#Config
##############

output_dir = "output"
parallelism = 2

def f(command_tuple):
    # Commands is a list of tuples where each tuple contains the command and the file to save the output to
    command, file = command_tuple
    print(f'Running:{command}, output:{file}')
    start_time = time.time()
    with open(file, 'a') as fp:
        subprocess.run(command, stdout=fp, stderr=fp, shell=True)
    end_time = time.time()
    print(f'Finished:{command}, output:{file}, time:{end_time - start_time} sec')


if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Define commands to run here
    commands = [(f"python3 main.py {i}", f"{output_dir}/nohup.{i}.out") for i in range(20)]
    # Commands is a list of tuples where each tuple contains the command and the file to save the output to
    print(f"{len(commands)} Commands will be run \n{commands}")
    print(f"Parallelism = {parallelism}")
    with Pool(parallelism) as p:
        print(p.map(f, commands))
