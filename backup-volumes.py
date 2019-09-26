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

client = docker.from_env();
for container in client.containers.list():
   print "**************************************"
   volumes = getVolumeByContainer(container)
   print(volumes)
