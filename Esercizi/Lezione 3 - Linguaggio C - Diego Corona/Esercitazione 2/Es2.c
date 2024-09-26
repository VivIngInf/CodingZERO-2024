/* Esercizio 2: Scrivere un programma che sommi n numeri in input dall’utente, 
dove n viene sempre scelto dall’utente */
#include <stdio.h>

int main(){
    int n = 0;
    int somma = 0;
    int a = 0;

    printf("Quanti numeri vuoi sommare?\n");
    scanf("%f",&n);

    for(int i = 0; i<n; i++){
        printf("Numero %d: ",i+1);
        scanf("%d",&a);
        somma += a;
    }

    printf("Somma = %d\n",somma);
    return 0;
}