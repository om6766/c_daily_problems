#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n1,s,n,d,sum=0;
    scanf("%d %d",&n,&d);
    n1=n/10+1;
    s=d;
    for(int i=1;i<=n1;i++){
        if(s<=n){
            sum=sum+s;
            s+=10;
        }
        
    }
    if(sum!=0){
        printf("%d",sum);
        }
    else{
        printf("-1");
    }
    return 0;
}