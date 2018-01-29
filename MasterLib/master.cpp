#include "master.h"
#include "stdafx.h"
#include "stdio.h"
void fib(int n)
{
	//n is the number of terms wanted by the user
	if (n <= 0)
	{
		printf("Please enter a valid input [positive integer]");
		return;
	}
	int first = 0, second = 1;
	if (n == 1)
	{
		printf("Fibonacci Series is 0");
	}
	else if (n == 2)
	{
		printf("Fibonacci Series is 0 1");
	}
	else
	{
		int i;
		printf("Fibonacci Series is ");
		for (i = 0; i < n - 2; i++)
		{
			first = second;
			second = first + second;
			printf("%d %d", first, second);
		}
	}
}
