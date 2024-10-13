#include <stdio.h>
//Firma funzione handling
void handling(char c, float a, float b);

//Funzione somma
void somma(float a, float b){
    float s = a + b;
    printf("%f + %f = %f\n", a, b, s);
}
//Funzione differenza
void dif(float a, float b){
    float dif = a - b; 
    printf("%f - %f = %f\n", a, b, dif);
}
//Funzione prodotto
void prod(float a, float b){
    float p = a * b;
    printf("%f * %f = %f\n", a, b, p);
}
//Funzione divisione
void div(float a, float b){
    if (b == 0 && a == 0) printf("0/0 è indefinito\n");
    else if(b == 0) printf("%f/0 non calcolabile\n", a);
        else {
            float d = a / b;
            printf("%f / %f = %f\n", a, b, d);
        }
}

int main(){
    float a = 0, b = 0;
    char ripeti = 'n', oper = 's';
    do {
        //input numeri
        printf("Inserire il primo numero: ");
        scanf("%f", &a);
        printf("Inserire il secondo numero: ");
        scanf("%f", &b);
        //richiesta operazione da fare
        printf("Scegliere qual operazione eseguire tra + , - , * , /  (s/d/p/f) ");
        scanf("\n%c", &oper);
        //richiamo funzione 
        handling(oper, a, b);
        
        printf("Vuoi ripertere il programma? s/n ");
        scanf("\n%c", &ripeti);
    } while ( ripeti == 's' || ripeti == 'S'); //loop programma
    
    return 0;
}

// Funzione handling operazioni a scelta dall'utente 
void handling(char c, float a, float b){
    switch (c) {
        case 's':
            somma(a,b);
            break;
        case 'd':
            dif(a,b);
            break;
        case 'p':
            prod(a,b);
            break;
        case 'f':
            div(a,b);
            break;
        default:
            printf("Scegliere nuovamente che operazione eseguire ");
            scanf("\n%c", &c);
            handling(c, a, b);
    }
}