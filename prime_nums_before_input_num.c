#include <stdio.h>

int main(int argc, char const *argv[])
{
    int userNumber;
    int primeNum;
    int subPrimeNum;

    float reminder;
    char sreminder[20];

    int isPrime;
    int c;


    printf("Introduce un numero entero mayor a 1: ");
    scanf("%d", &userNumber);

    printf("Numeros primos anteriores a %d: \n", userNumber);

    for (primeNum = 2; primeNum < userNumber; primeNum++)
    {   
        isPrime = 1;
        c = 0;
        for (subPrimeNum = 1; subPrimeNum <= primeNum; subPrimeNum++)
        {
            reminder = primeNum % subPrimeNum;

            if (reminder == 0)
            {
                c++;
            }
            if (c > 2)
            {
                isPrime = 0;
                break;
            }
            
        }
        if (isPrime == 1)
        {
            printf("%d\n", primeNum);
        }
    }
    return 0;
}
