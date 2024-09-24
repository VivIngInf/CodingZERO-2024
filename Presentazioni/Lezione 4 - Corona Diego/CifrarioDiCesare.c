#include <stdio.h>
#include <string.h>

int main() {
    char scritta[100];
    int chiave = 0;

    // Input
    printf("Inserire Stringa: ");
    scanf("%99[^\n]", scritta);
    printf("Inserire chiave: ");
    scanf("%d", &chiave);

    // Cifrario
    for(int i = 0; i < strlen(scritta); i++) {
        if (scritta[i] >= 'a' && scritta[i] <= 'z') {
            scritta[i] = ((scritta[i] - 'a' + chiave) % 26) + 'a';
        } else if (scritta[i] >= 'A' && scritta[i] <= 'Z') {
            scritta[i] = ((scritta[i] - 'A' + chiave) % 26) + 'A';
        }
    }

    // Output
    printf("Stringa cifrata: %s\n", scritta);

    return 0;
}