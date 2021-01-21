#include <stdio.h>
#include <stdlib.h>

int fibonacci(int limit)
{
	int f1 = 0;
	int f2 = 1;

	int temp = f1;
	int answer = 0;

	while (f2 < limit)
	{
		temp = f2;
		f2 += f1;
		f1 = temp;

		if (f2 % 2 == 0)
		{
			answer += f2;
			printf("%d, ", f2);
		}
	}

	printf("\n");

	return answer;
}

int main(int argc, char **argv)
{
	long n = strtol(argv[1], NULL, 10);
	printf("first %ld fib numbers %d\n", n, fibonacci(n));
}
