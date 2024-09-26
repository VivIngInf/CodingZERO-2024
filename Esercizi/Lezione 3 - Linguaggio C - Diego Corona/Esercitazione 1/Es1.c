/* Esercizio 1: Scrivere un programma che dati in
input 2 numeri faccia le 4 operazioni fondamentali */
#include <stdio.h>

int main(){
    float a = 0, b = 0, s = 0, dif = 0, p = 0, div = 0;
    printf("Inserire primo valore: ");
    scanf("%f",&a);
    printf("Inserire secondo valore: ");
    scanf("%f",&b);

    s = a+b;
    dif = a-b;
    p = a*b;
    div = a/b;

    printf("a+b=%f\na-b=%f\na*b=%f\na/b=%f\n",s,dif,p,div);
    return 0;
}