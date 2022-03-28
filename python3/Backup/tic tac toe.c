#include <stdio.h>
void main(void)
{
    char user1, user2, setup[3][3]={'-','-','-','-','-','-','-','-','-'};
    int i,j;
    printf("Lets Play TIc Tac Toe...\nHow To Play:\n1. Winning And Losing is similar to the normal game\n2. Entering you input is via num pad which goes left to right and then top to bottom\nFor Example:\n1\t2\t3\n4\t5\t6\n7\t8\t9");
    printf("\nWhat character does the first user want:\n");
    scanf("%s", &user1);
    printf("What character does the second user want:\n");
    scanf("%s", &user2);
    printf("Society needs equality !!!\nWhy will User 1 go first everytime ?!!\nThis Time... To Promote Equality\nUser two goes first:\n");
    for(i=0; i<3;i++)
    {
        for(j=0; j<3; j++)
        {
            printf("%c\t", setup[i][j]);
        }
        printf("\n");
    }

    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            a:
            if(a[i][j] != '0')
            {
                printf("The position is already occupied. try another one :: ");
                goto:
            }
            else scanf("%c", temp]);
        }
    }
}
