# import threading
# import Queue
# import subprocess
# import time

# # def getstatusoutput(command):
# #     process = Popen(command, stdout=PIPE)
# #     out, _ = process.communicate()
# #     return (process.returncode, out)

# # thread class to run a command
# class ExampleThread(threading.Thread):
#   def __init__(self, cmd, queue, *args, **kwargs):
#     super(ExampleThread, self).__init__(*args, **kwargs)
#     self.cmd = cmd
#     self.queue = queue

#   def run(self, *args, **kwargs):
#     # execute the command, queue the result
#     print('thread starting')
#     super(ExampleThread, self).run(*args, **kwargs)
#     print('threat has ended')

# def sleeper (cmd, style):
#   print('we are sleeping for {} seconds as {}'.format(cmd, style))
#   process = subprocess.Popen(cmd, stdout = subprocess.PIPE)
#   out, _ = process.communicate()
#   time.sleep(2)   

# result_queue = Queue.Queue()

# # define the commands to be run in parallel, run them
# # cmds = ['date; ls -l; sleep 1; date',
# #         'date; sleep 5; date',
# #         'date; df -h; sleep 3; date',
# #         'date; hostname; sleep 2; date',
# #         'date; uname -a; date',
# #        ]
# cmds = ['pwd',
#         'pwd',
#         'pwd',
#         'pwd',
#         'pwd',
#        ]

# for cmd in cmds:
#     thread = ExampleThread(cmd, result_queue, target = sleeper, args = [cmd, 'yellow'])
#     thread.start()

# # print results as we get them
# while threading.active_count() > 1 or not result_queue.empty():
#   while not result_queue.empty():
#     (cmd, output, status) = result_queue.get()
#     print('%s:' % cmd)
#     print(output)
#     print('='*60)
#     time.sleep(1)

import threading
import Queue
# import commands
import subprocess
import time

# thread class to run a command
class ExampleThread(threading.Thread):
    def __init__(self, cmd, queue):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.queue = queue

    def run(self):
        # execute the command, queue the result
        process = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
        stdout, stderr = process.communicate()
        # (status, output) = commands.getstatusoutput(self.cmd)
        self.queue.put((self.cmd, stdout, process.returncode, stderr))

# queue where results are placed
result_queue = Queue.Queue()

# define the commands to be run in parallel, run them
cmds = ['date; ls -l; sleep 1; date',
        'date; sleep 5; date',
        'date; df -h; sleep 3; date',
        'date; hostname; sleep 2; date',
        'date; uname -a; date',
       ]

for cmd in cmds:
    thread = ExampleThread(cmd, result_queue)
    thread.start()

# print results as we get them
while threading.active_count() > 1 or not result_queue.empty():
    while not result_queue.empty():
        (cmd, output, status, stderr  ) = result_queue.get()
        print('%s:' % cmd)
        print(output)
        print('='*60)
    time.sleep(1)