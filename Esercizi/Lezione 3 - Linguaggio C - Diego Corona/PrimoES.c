#include <stdio.h>

int main(){
    // Dichiarazione Variabile
    float a = 0, b = 0;
    float somma = 0;
    float differenza = 0;
    float prodotto = 0;
    float divisione = 0;

    //Input
    printf("Inserire A:\n");
    scanf("%f",&a);
    printf("Inserire B: ");
    scanf("%f",&b);

    //Operazioni
    somma = a + b;
    differenza=a-b;
    prodotto = a*b;
    divisione = a/b;

    //Output
    printf("Somma = %f\n",somma);
    printf("%f - %f = %f\n",a,b,differenza);
    printf("Prodotto = %f\nDivisione = %f\n", prodotto, divisione);
    return 0;
}