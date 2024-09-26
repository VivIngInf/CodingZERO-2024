// Algoritmo Cifrario di Cesare
// Implementazione ~ Diego Corona
// Commenti ~ Daniele Orazio Susino

#include <stdio.h>  // Libreria che permette di interfacciarci con l'utente e chiedere input e mandare output
#include <string.h> // Libreria che ci permette di manipolare le stringhe

int main() // La funzione principale di un programma C, deve ritornare obbligatoriamente un intero.
{
    char cypherText[100]; // L'array di caratteri (stringa ) che conterrà il cyphertext, ovvero il messaggio da decifrare
    int chiave = 0;       // La chiave di decifratura dell'algoritmo (valore intero)

    // --- INPUT ---
    printf("Inserire messaggio cifrato: "); // Scriviamo a schermo "Inserire messaggio cifrato: "
    scanf("%99[^\n]", cypherText);          // Leggiamo ciò che scrive l'utente e lo mettiamo dentro l'array scritta
    printf("Inserire chiave: ");            // Scriviamo a schermo "Inserire chiave: "
    scanf("%d", &chiave);                   // Leggiamo la chiave e la inseriamo all'interno della variabile chiave

    // --- ALGORITMO DI DECIFRATURA ---
    // Inizializziamo i = 0 perché dobbiamo partire dalla prima lettera dunque
    // partiamo dalla posizione dell'array 0.
    // Andremo avanti nel ciclo per tutta la lunghezza della scritta (strlen)
    // Andremo avanti una lettera alla volta (i++)
    for (int i = 0; i < strlen(cypherText); i++)
    {
        // Vogliamo shiftare le posizioni solamente delle lettere,
        // dunque dobbiamo dire che se i caratteri sono compresi tra
        // a e z li possiamo shiftare.
        // Questo permette di mantenere spazi e numeri (essendo caratteri verrebbero shiftati anche loro altrimenti).
        if (cypherText[i] >= 'a' && cypherText[i] <= 'z')
        {
            // La lettera del messaggio cifrato sarà uguale alla lettera risultante dal calcolo seguente:
            // Prendi la lettera in posizione i, sottrai il carattere 'a' (passiamo quindi da numero ascii ad alfabeto italiano)
            // aggiungi la chiave (quindi spostiamo di tante posizioni quanto è la chiave)
            // Eseguiamo il modulo 26 perché così se eccediamo la dimensione dell'alfabeto facciamo il giro e ricominciamo dalla a
            // Riaggiungiamo il carattere 'a' per riportarlo in codifica ascii.

            cypherText[i] = ((cypherText[i] - 'a' + chiave) % 26) + 'a';
        }
        // Stessa cosa per quanto riguarda le lettere maiuscole
        else if (cypherText[i] >= 'A' && cypherText[i] <= 'Z')
        {
            cypherText[i] = ((cypherText[i] - 'A' + chiave) % 26) + 'A';
        }
    }

    // --- OUTPUT ---
    printf("Stringa cifrata: %s\n", cypherText); // Manda in output "Stringa cifrata: " ed il contenuto di cypherText

    return 0; // Ritorniamo 0 per far capire al sistema operativo che il programma è andato a buon fine.
}

// Credits to Giulio Cesare, sei stato un vero chad