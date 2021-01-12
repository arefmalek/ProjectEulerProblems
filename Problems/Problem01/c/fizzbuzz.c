#include <stdio.h>

int fb(int input)
{
	int fact_1 = 5;
	int fact_2 = 3;

	int factors[2];
	//I made an array because I wanted this code to be reusable
	//with more than one factor (as if I'll ever touch it again lol)

	factors[0] = fact_1;
	factors[1] = fact_2;

	for(int i = 0; i < sizeof(factors); i++)
	{
		if (input % factors[i] == 0)
		{
			return input;
		}
	}
	return 0;
}
int main()
{
	//got a lil lazy and didn't modularize this code, but it works just fine
	int limit = 1000;
	int answer = 0;

	for(int i = 0; i < limit; i++)
	{
		answer += fb(i);
	}
	
	printf("%d\n", answer);
	return 0;

}
