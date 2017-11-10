import time
import datetime
# Only run if the user types in "start"
# Loop until we reach 60 seconds running
while 1:
        now = datetime.datetime.now()
	print ">>>>>>>>> flush at " + str(now) 
	# Sleep for a minute
	time.sleep(60)
