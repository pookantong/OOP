#include<stdio.h>
#include<string.h>

int main()
{
    char a[8];
    int b = 0;
    float sum = 0, g[3];
    printf("  GPA 2 \n");
    printf("Enter your grade : ");
    scanf("%[^\n]s",a);
    for (int i = 0; i < strlen(a); i++)
    {
        if (i%3 == 0){
            switch (a[i])
            {
                case 'A':
                    g[i/3] = 4;
                    break;
                case 'B':
                    g[i/3] = 3;
                    break;
                case 'C':
                    g[i/3] = 2;
                    break;
                case 'D':
                    g[i/3] = 1;
                    break;
                case 'F':
                    g[i/3] = 0;
                    break;
            }
        }
        else if (i%3 == 1){
            sum += g[(i-1)/3]*(a[i] - '0');
            b += (a[i] - '0');
        }
    }
    
    printf ("Computer : %.2f \n",g[0]);
    printf ("Science : %.2f \n",g[1]);
    printf ("English : %.2f \n",g[2]);
    printf("%.2f",sum/b);

    return 0;
}