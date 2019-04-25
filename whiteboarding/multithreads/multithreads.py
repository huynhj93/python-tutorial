import threading
import time


def sleeper (n, name) :
    print ("I am {}. Going to sleep for 5 seconds".format(name))
    time.sleep(n)
    print (" {} has woken up from sleep \n".format(name))

# t = threading.Thread(target = sleeper, name = 'thread1', args = (5, "thread1"))

# t.start()
# t.join()
print('hello')
print('hello')


threads_list = []

start = time.time()

for i in range (5) :
  t = threading.Thread(target = sleeper, name = 'thread{}'.format(i), args = (5, "thread{}".format(i)))
  threads_list.append(t)
  t.start()
  print('{} has started'.format(t.name))



for t in threads_list :
  t.join()

end = time.time()

print('time taken: {}'.format(end-start))
print('All five threads have finished')