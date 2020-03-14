

    #include <stdio.h>
    #include <stdlib.h>
    int main() {
        char sentence[1000];
        // creating file pointer to work with files
        FILE *fptr;
        //char* file="";
        // opening file in writing mode
        fptr = fopen("/sys/program.txt", "w");
        // exiting program 
        
        printf("Enter a sentence:\n");
        fgets(sentence, sizeof(sentence), stdin);
        fprintf(fptr, "%s", sentence);
        fclose(fptr);
        return 0;
    }