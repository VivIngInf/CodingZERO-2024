/* Esercizio 3: Scrivere un programma che sommi
numeri in input dall’utente finché non digita 0 */
#include <stdio.h>

int main(){
    int n = 0;
    int somma = 0;

    do{
        printf("Numero da sommare: ");
        scanf("%d",&n);
        somma += n;
    }while(n!=0);

    printf("Somma = %d\n",somma);
    return 0;
}