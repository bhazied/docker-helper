import sys
import subprocess
import os
import docker
import json

def getVolumeByContainer(container):
   output = subprocess.Popen(["docker", "inspect" ,  container.short_id], stdout=subprocess.PIPE).stdout.read()
   joutput = json.JSONDecoder().decode(output)
   volumes = []
   if len(joutput[0]["Mounts"]) > 0:
       for volume in joutput[0]["Mounts"]:
           volumes.append(volume)
   return volumes

def saveVolumeByContainer(containerName, volumes):
   for volume in volumes:
      if argv[0] is not None:
         os.system("sh backup-volumes.sh "+ volume["Name"]+ " "+ containerName+ " "+ volume["Destination"]+ " " argv[0])
      os.system("sh backup-volumes.sh "+ volume["Name"]+ " "+ containerName+ " "+ volume["Destination"])

client = docker.from_env();
for container in client.containers.list():
   print "******** volumes for "+container.name+"  *********"
   volumes = getVolumeByContainer(container)
   print(volumes)
   saveVolumeByContainer(container.name, volumes)
