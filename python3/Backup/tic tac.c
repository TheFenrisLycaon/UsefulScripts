#include <stdio.h>
void decide(char);
int main(void)
{
	int temp,i,j,k;
	char u1, u2, x, a[3][3]={'-','-','-','-','-','-','-','-','-'};
	printf("Lets Play Tic Tac Toe\nInput Numbers to place your characters according to the T9 format\n");
	printf("First User's Character Is:");
	scanf("%c",&u1);
	printf("Second User's Character Is:");
	scanf("%c",&u2);
	for (i=0; i<9; i++)
	{
		printf("Enter Position");
		scanf("%d",&temp);
		
		switch(temp)
		{
			case(1):
				if(a[0][0]=='0' && i%2 == 0)
					a[0][0] = u1;
				else if (a[0][0] == '0' && i%2 != 0)
					a[0][0] = u2;
				else
					printf ("Position already occupied");
			case(2):
				if(a[1][0]=='0' && i%2 == 0)
					a[1][0] = u1;
				else if (a[1][0] == '0' && i%2 != 0)
					a[1][0] = u2;
				else
					printf ("Position already occupied");
			case(3):
				if(a[2][0]=='0' && i%2 == 0)
					a[2][0] = u1;
				else if (a[2][0] == '0' && i%2 != 0)
					a[2][0] = u2;
				else
					printf ("Position already occupied");
			case(4):
				if(a[0][1]=='0' && i%2 == 0)
					a[0][1] = u1;
				else if (a[0][1] == '0' && i%2 != 0)
					a[0][1] = u2;
				else
					printf ("Position already occupied");
			case(5):
				if(a[1][1]=='0' && i%2 == 0)
					a[1][1] = u1;
				else if (a[1][1] == '0' && i%2 != 0)
					a[1][1] = u2;
				else
					printf ("Position already occupied");
			case(6):
				if(a[2][1]=='0' && i%2 == 0)
					a[2][1] = u1;
				else if (a[2][1] == '0' && i%2 != 0)
					a[2][1] = u2;
				else
					printf ("Position already occupied");
			case(7):
				if(a[0][2]=='0' && i%2 == 0)
					a[0][2] = u1;
				else if (a[0][2] == '0' && i%2 != 0)
					a[0][2] = u2;
				else
					printf ("Position already occupied");
			case(8):
				if(a[1][2]=='0' && i%2 == 0)
					a[1][2] = u1;
				else if (a[1][2] == '0' && i%2 != 0)
					a[1][2] = u2;
				else
					printf ("Position already occupied");
			case(9):
				if(a[2][2]=='0' && i%2 == 0)
					a[2][2] = u1;
				else if (a[2][2] == '0' && i%2 != 0)
					a[2][2] = u2;
				else
					printf ("Position already occupied");
			default :
				printf ("Invalid Input");
		}
		for(j=0; j<3;j++)
		{
			for(k=0; k<3; k++)
				printf("%c\t",&a[j][k]);
		}
		printf("\n")
		
	}
}