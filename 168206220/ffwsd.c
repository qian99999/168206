
#include <stdio.h>
int main()
{
   int a,b,c,d;
    for(a=1;a>=0;a--) 
        for(b=1;b>=0;b--) //1:��С͵ 0:����
            for(c=1;c>=0;c--)
                for(d=1;d>=0;d--)
                    if(((a==0)+(d==1)+(b==1)+(d==0)==1)&&(a+b+c+d==1)) //4�˵�˵������1����ģ���ֻ��һ��С͵
                    {
                        printf("A: %d, B: %d, C: %d, D: %d\n", a, b, c, d);
						if(a==1){
							printf("a��С͵");
						}
						if(b==1){
							printf("b��С͵");
						}
						if(c==1){
							printf("c��С͵");
						}
						if(d==1){
							printf("d��С͵");
						}
                    }
    return 0;

}