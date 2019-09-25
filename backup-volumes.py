import sys
import subprocess
import os
import docker
import json
client = docker.from_env();
for container in client.containers.list():
   output = subprocess.Popen(["docker", "inspect" ,  container.short_id], stdout=subprocess.PIPE).stdout.read()
   print "**************************************"
   joutput =  json.JSONDecoder().decode(output)
   if len(joutput[0]["Mounts"]) > 0:
       print joutput[0]["Mounts"]

