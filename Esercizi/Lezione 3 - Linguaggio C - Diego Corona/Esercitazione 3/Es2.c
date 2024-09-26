/* Esercizio 2: Scrivere un programma che sommi n numeri in input dall’utente, 
dove n viene sempre scelto dall’utente, sfruttando le funzioni*/
#include <stdio.h>

int Sommatore(int n){
    int a = 0;
    int somma = 0;

    for(int i = 0; i<n; i++){
        printf("Numero %d: ",i+1);
        scanf("%d",&a);
        somma += a;
    }

    return n;
}
int main(){
    int n = 0;

    printf("Quanti numeri vuoi sommare?\n");
    scanf("%f",&n);

    printf("Somma = %d\n",Sommatore(n));
    return 0;
}