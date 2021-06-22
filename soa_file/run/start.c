#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char * argv[]){

	char input_port[1024];

	sprintf(input_port,"python build.py %s",argv[1]);

	system(input_port);

	while(1){

		system("pkill -9 run");
		system("./run &");
		sleep(10);

	}

	return 0;

}


