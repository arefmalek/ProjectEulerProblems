#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    long int number = atol(argv[1]);
    
    int limit = ((int) sqrt(number)) + 1;
    //time to learn memset :^)
    int sieve[limit];
    memset(sieve, 0, limit*sizeof(int));

    int answer = 2;
    //just do sieves to only get the prime factors
    for (int l = 2; l < limit; l++)
    {
	if (sieve[l] == 0)
        {
            if (number % l == 0) {
                number /= l;
                answer = l;
            }
            for (int j = 2*l; j < limit; j += j) sieve[j] = 1;
        }
    }

    printf("%d\n", answer);
    return 0;
}
