/* Esercizio 1: Scrivere la calcolatrice migliorata */
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

    printf("a+b=%f\na-b=%f\na*b=%f\n",s,dif,p);
    if(b == 0 && a == 0) printf("a/b e' indefinito\n");
    else if(b == 0) printf("a/b non calcolabile\n");
    else {
        div = a/b;
        printf("a/b=%f\n",div);
    }
    return 0;
}