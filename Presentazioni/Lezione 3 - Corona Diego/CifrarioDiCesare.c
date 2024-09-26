#include <stdio.h>
#include <string.h>

int main()
{
    char cypherText[100];
    int chiave = 0;

    // --- INPUT ---
    printf("Inserire messaggio cifrato: ");
    scanf("%99[^\n]", cypherText);
    printf("Inserire chiave: ");
    scanf("%d", &chiave);

    // --- ALGORITMO DI DECIFRATURA ---
    for (int i = 0; i < strlen(cypherText); i++)
    {
        if (cypherText[i] >= 'a' && cypherText[i] <= 'z')
        {
            cypherText[i] = ((cypherText[i] - 'a' + chiave) % 26) + 'a';
        }
        else if (cypherText[i] >= 'A' && cypherText[i] <= 'Z')
        {
            cypherText[i] = ((cypherText[i] - 'A' + chiave) % 26) + 'A';
        }
    }

    // --- OUTPUT ---
    printf("Stringa cifrata: %s\n", cypherText);

    return 0;
}

// Credits to Giulio Cesare, sei stato un vero chad