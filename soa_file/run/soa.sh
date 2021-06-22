#!/bin/bash

if (( $EUID != 0 )); then

    echo "Please run the script with root privileges."
    exit

fi

clear
clear

echo '''
  ███████╗ ██████╗  █████╗ 
  ██╔════╝██╔═══██╗██╔══██╗
  ███████╗██║   ██║███████║
  ╚════██║██║   ██║██╔══██║
  ███████║╚██████╔╝██║  ██║
  ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ v1.0.0 / Developer : ENNP
'''

echo "  *******************************************************"
echo "  **                github.com/ennp/soa                **"
echo "  *******************************************************"
echo "  **        Check for ../../front_end.zip files        **"
echo "  *******************************************************"
echo "  **      SOA stop -> 'Port number to use : stop'      **"
echo "  *******************************************************"
printf "\n"

printf "  Port number to use : "
read -r port

if [ $port == "stop" ];
then
	./stop
	printf "\n  SOA STOP complete COMPLETE , Thank you for using SOA.\n\n"
else
	pkill -9 start
	./start $port 2>&1 > /dev/null &
	
	printf "\n  Check out your memory."
	printf "\n  [ ./run : 2 , ./start : 1 ]\n\n"
fi
