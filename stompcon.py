import time
import sys
import stomp

# conn = stomp.Connection([('13.95.109.53', 61613)])
# conn.connect('admin', 'admin', wait=True)
# #conn.subscribe(destination='/queue/test', id=1, ack='auto')
# conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
# time.sleep(2)
# conn.disconnect()

from datetime import datetime, timedelta

# date = datetime.today().strftime('%Y%m%d')[2:]

date = (datetime.today()- timedelta(days=5)).strftime('%Y%m%d')[2:]
print(date)