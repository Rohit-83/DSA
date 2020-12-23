#include<iostream>
using namespace std;

int binarysearch(int n,int arr[n], int key){
    int s=0;
    int e=n;
    while(s<=e){
        int mid = (s+e)/2;
        if (arr[mid]==key){
            return mid;
        }
        else if (arr[mid]<key){
            s=mid+1;
        }
        else{
            e=mid-1;
        }
    }
    return -1;
}
int main(){
    int n;
    cout<<"enter the size of array:"<<endl;
    cin>>n;
    int arr[n];
    cout<<"enter array element:";
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
    int key ;
    cout<<"enter key value:";
    cin>> key;
    cout<<binarysearch(n,arr,key);
    return 0;
}