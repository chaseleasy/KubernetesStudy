import time
import socket
while True:
    with open('/data/wwwroot/index.html','w') as f:
       f.write('time: {} create by: {}  '.format(str(time.time()),socket.gethostname()) )
    time.sleep(10)
    print('正在进行下一次等待')


