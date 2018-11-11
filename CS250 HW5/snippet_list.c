#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#include "snippet_list.h"

#define MAX_SNIPPETS 1000
#define MAX_LINE_LENGTH 1000
struct snippet {
  char name[MAX_NAME_LENGTH];
  char addr[MAX_ADDRESS_LENGTH];
  char city[MAX_CITY_LENGTH];
  char state[STATE_LENGTH];
  unsigned int zip;
};

static struct snippet *snippet_list[MAX_SNIPPETS];
static int n_snippets = 0;
void read_file (char *snippet_file)
{
   // open file
  FILE *fp;
  fp = fopen(snippet_file, "r");

  if ( fp == NULL ) {
    printf("file not found");
    exit(-1);
  }
 
  char name[MAX_NAME_LENGTH];
  char addr[MAX_ADDRESS_LENGTH];
  char city[MAX_CITY_LENGTH];
  char state[STATE_LENGTH];
  unsigned int zip;
  
  char line[MAX_LINE_LENGTH];
  char *token;
  fgets(line, MAX_LINE_LENGTH,fp);
  sscanf(line, "%d\n", &n_snippets);

  while ( fgets(line, MAX_LINE_LENGTH,fp)) {
    token = strtok(line,":\n\t");
    strcpy ( name, token);
    token = strtok(NULL, ":\n\t");
    strcpy ( addr, token);
    token = strtok(NULL, ":\n\t");
    strcpy ( city, token);
    token = strtok(NULL, ":\n\t");
    strcpy ( state, token);
    token = strtok(NULL, ":\n\t");
    sscanf(line, "%d", &zip);
    add_snippet( name, addr, city, state, zip);
  }
}

void add_snippet( char a_name[], char an_addr[], char a_city[],char a_state[]
		  , int a_zip)
{
  if ( n_snippets == MAX_SNIPPETS ){
    return;
  }
  
  struct snippet *new_snippet = (struct snippet*) malloc ( sizeof ( struct snippet));
  
  strcpy ( new_snippet -> name , a_name);
  strcpy ( new_snippet -> addr , an_addr);
  strcpy ( new_snippet -> city , a_city);
  strcpy ( new_snippet -> state , a_state);
  new_snippet -> zip = a_zip;
 
   snippet_list[n_snippets] = new_snippet;
  n_snippets ++;

}

void print_list()
{
  int i;
  for (i = 0; i < n_snippets; i++) {
     printf ("%s\n%s.\n%s, %s %d\n\n", snippet_list[i] -> name,
	     snippet_list[i] -> addr,
	     snippet_list[i] -> city,
	     snippet_list[i] -> state,
	     snippet_list[i] -> zip);
  }
}


void remove ( char substring[] )
{
  int i;
  for ( i = 0 ; i< n_snippets; i++ ){
    strcat((( ( snippet_list[i] -> name,
		snippet_list[i] -> addr)
		snippet_list[i] -> city)
		snippet_list[i] -> state)
		snippet_list[i] -> zip);
    
    if ( strstr ( name, substring) != NULL) {
      remove_at_pos(i);
    }
  }
}
void remove_at_pos (int pos ) 
{
  free(snippet_list[pos]);
  int i;
  for ( i = pos ; i < ( n_snippets - 1) ; i++ ) {
    snippet_list[i] = snippet_list[i+1];
  }
}







	   

	  

	   
		 


	 
	  


	   



	   
