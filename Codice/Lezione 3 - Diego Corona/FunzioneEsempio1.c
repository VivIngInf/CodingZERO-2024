#include <stdio.h>

int somma(int a, int b);
int Sommabase(int a, int b);
int main(){
    char s = 'n';
    scanf("\n%c",&s);
    return 0;
}

int Somma(int a, int b){
    int somma = Sommabase(a,b);
    return somma;
}

int Sommabase(int a, int b) {
    for(int i = 0; i<b; i++) {
        a++;
    }
    return a;
}