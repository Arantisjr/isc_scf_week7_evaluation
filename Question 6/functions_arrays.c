#include <stdio.h>
int large_value(int arr[],int size){
    int max = arr[0];//assumes the first value of the array is the largest
    for (int i=1;i<size;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}
int main(){
    int n;
  printf("Enter the number of elements:\n");
  scanf("%d",&n);

  if(n<=0){
    printf("invalid number, number must be greater than zero\n");
    return 1;
  }

  int arr[n];//declaring an array of size n to store the intergers
  printf("Enter %d numbers:\n",n);
  for(int i=0; i<n;i++){
    scanf("%d",arr[i]);
  }
int largest_num = large_value(arr,n);
printf("the largest numbers from the list is: ",largest_num);
    return 0;
}