/* Esercizio 1: Scrivere la calcolatrice migliorata sfruttando le funzioni*/
#include <stdio.h>

float Somma(float a, float b);
float Differenza(float a, float b);
float Prodotto(float a, float b);
float Divisione(float a, float b);

int main(){
    float a = 0, b = 0, s = 0, dif = 0, p = 0;
    printf("Inserire primo valore: ");
    scanf("%f",&a);
    printf("Inserire secondo valore: ");
    scanf("%f",&b);

    s = Somma(a,b);
    dif = Differenza(a,b);
    p = Prodotto(a,b);

    printf("a+b=%f\na-b=%f\na*b=%f\n",s,dif,p);
    Divisione(a,b);
    return 0;
}

float Somma(float a, float b){
    return a+b;
}
float Differenza(float a, float b){
    return a-b;
}
float Prodotto(float a, float b){
    return a*b;
}
float Divisione(float a, float b){
    if(b == 0 && a == 0) printf("a/b e' indefinito\n");
    else if(b == 0) printf("a/b non calcolabile\n");
    else printf("a/b=%f\n",a/b);
}