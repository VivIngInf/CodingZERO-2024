#include <stdio.h>
#define dim 5

int main(){
    int somma = 0;
    int array[dim] = {5,3,6,3,1};
    for(int i = 0; i<dim; i++) {
        somma = somma+array[i];
    }
    printf("Risultato = %d",somma);
    return 0;
}