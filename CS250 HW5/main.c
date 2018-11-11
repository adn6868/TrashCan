#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "snippet_list.h"

#define MAX_ACTION_LENGTH 1000
#define MAX_LINE_LENGTH 5000
  
int main (int argc , char* argv[])
{
  //read file
  char *snippet_file = argv[1];
  read_file(snippet_file);
  
  print_list();
  
  // perform actions
  /*char action[MAX_ACTION_LENGTH]; 
  printf("Enter action: \n1.%s\n2.%s\n3.%s\n4.%s\n","list","add","remove"
   ,"exit");
  scanf("%s", action);
  printf("\n");

  if (strcmp ( action, "list") == 0 ){
    display_list();
    } else if ( strcmp ( action, "add" ) == 0) {
    char line[MAX_LINE_LENGTH];
    printf("Enter name\n:");
    fgets(line, MAX_LINE_LENGTH, stdin);
    
    printf("Enter address\n:");
    printf("Enter city\n:");
    printf("Enter state\n:");
    printf("Enter zip\n:");
    
    add_snippet( name, addr, city, state, zip);
    
    } else if ( strcmp ( action, "remove" ) == 0 ) {
    
    remove_snippet();
  } else {
    terminate();
  }*/
  return 0;
}

