#constrain number of concurrent child processes

from subprocess import Popen
from itertools import islice

max_workers = 2 # no more than 2 concurren
processes = (Popen(cmd, shell=True) for cmd
running_processes = list(islice(processes,
    while running_processes:
        for i, process in enumerate(running_pro
            if process.poll() is not None: # t
                running_processes[i] = next(pro
                if running_processes[i] is None
                del running_processes[i]
                break
