#!bin/sh
VOLUME_NAME=$1
CONTAINER_NAME=$2
PATH=$3
VOLUME_DESTIMATION=$4
if [ -z $VOLUME_NAME ]
then
   echo "Error : Missing volume name parameters"
   exit 1
fi

if [ -z $CONTAINER_NAME ]
then
   echo "Error : Missing Container name parameters"
   exit 1
fi

if [ -z $PATH ]
then
   $PATH = "./data-backup"
fi

if [ -z $VOLUME_DESTINATION]
then
   echo "Error: Missing volume container destintion parameter"
   exit 1
fi

/usr/bin/docker run --rm --volumes-from "$CONTAINER_NAME" -v  "{$PATH}:/{$CONTAINER_NAME}" ubuntu tar cvf  "{$VOLUME_NAME}-backup.tar" "{$VOLUME_DESTINATION}"
