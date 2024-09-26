/* Esercizio 3: Scrivere un programma che sommi
numeri in input dall’utente finché non digita 0 sfruttando le funzioni*/
#include <stdio.h>

void Sommatore(int *somma) {
    int n = 0;

    do{
        printf("Numero da sommare: ");
        scanf("%d",&n);
        *somma += n;
    }while(n!=0);
}

int main(){
    int somma = 0;

    Sommatore(&somma);

    printf("Somma = %d\n",somma);
    return 0;
}