
#include <stdio.h>
int main()
{
   int a,b,c,d;
    for(a=1;a>=0;a--) 
        for(b=1;b>=0;b--) //1:是小偷 0:不是
            for(c=1;c>=0;c--)
                for(d=1;d>=0;d--)
                    if(((a==0)+(d==1)+(b==1)+(d==0)==1)&&(a+b+c+d==1)) //4人的说法中有1个真的，且只有一个小偷
                    {
                        printf("A: %d, B: %d, C: %d, D: %d\n", a, b, c, d);
						if(a==1){
							printf("a是小偷");
						}
						if(b==1){
							printf("b是小偷");
						}
						if(c==1){
							printf("c是小偷");
						}
						if(d==1){
							printf("d是小偷");
						}
                    }
    return 0;

}