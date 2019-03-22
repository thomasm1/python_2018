# threading example:
import threading
import Queue
import commands
import time

# thread class to run a command
class ExampleThread(threading.Thread):
    def __init__(self, cmd, queue):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.queue = queue
        
    def run(self):
         # execute the command, queue the re
         (status, output) = commands.getstat
         self.queue.put((self.cmd, output,

# queue where results are placed
result_queue = Queue.Queue()

# define the commands to be run in paralle
cmds = ['date; ls -l; sleep 1; date',
        'date; sleep 5; date',
        'date; df -h; sleep 3; date',
        'date; hostname; sleep 2; date',
        'date; uname -a; date',
       ]
for cmd in cmds:
    thread = ExampleThread(cmd, result_queu
    thread.start()

# print results as we get them
while threading.active_count() > 1 or not
    while not result_queue.empty(): 
       (cmd, output, status) = result_queue
        print('%s:' % cmd)  
    
     
