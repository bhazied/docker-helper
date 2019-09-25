#!bin/bash
CONTAINER_ID=$1
CONTAINER_NAME=$2
PATH=$3
if [ -z $CONTAINER_ID ]
then
   echo "Error : Missing container id parameters"
   exit 1
fi

if [ -z $CONTAINER_NAME ]
then
   echo "Error : Missingy Container name parameters"
   exit 1
fi

if [ -z $PATH ]
then
   $PATH = "./"
fi

/usr/bin/docker commit -p "$CONTAINER_ID"  "${CONTAINER_NAME}-backup"
/usr/bin/docker save  -o "${CONTAINER_NAME}-backup.tar"  "${PATH}${CONTAINER_NAME}-backup"

