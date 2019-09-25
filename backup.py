import sys
import os
import docker
client = docker.from_env();
for container in client.containers.list(all=True):
   print "***** Start backup the container : " +container.name+ " *****"
   if sys.argv[0] is  not None:
       os.system("sh backup-container.sh "+ container.id + " "+ container.name + " "+ sys.argv[0])
   os.system("sh backup-container.sh "+ container.id + " "+ container.name)
   print "***** End backup the container : "+ container.name+ " *****"
