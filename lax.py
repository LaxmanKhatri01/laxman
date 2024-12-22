#include<stdio.h>
int main() {

    int number1, number2,sum;
    printf("Enter two integers: ");
    sum= number1 + number2;
    printf("%d + %d", number1,number2,sum);
    int num3,div;
    printf("\n\nEnter a number to divide:");
    scanf("%d",&num3);
    div=sum/num3;
    printf("dividion:%d",div);
    return 0;
}