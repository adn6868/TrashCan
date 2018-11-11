#define MAX_SNIPPETS 1000
#define MAX_STRING_SIZE 1000
#define MAX_NAME_LENGTH 1000
#define MAX_ADDRESS_LENGTH 1000
#define MAX_CITY_LENGTH 1000
#define STATE_LENGTH 1000

void read_file(char *snippet_file);
void print_list(void);
void add_snippet( char a_name[], char an_addr[], char a_city[], char a_state[],
		  int a_zip);
