#include<iostream>
#include<vector>
#include<bits/stdc++.h>
using namespace std;

vector< int > A(100+1);
int T(int k, int i)
{
    if(k<=0 || i==0)
    return 0;
    if(A[i] > k){
        return T(k, i-1);
    }
    return max(T(k-A[i], i-1 ) + A[i], T(k,i+1));
}
int main()
{
    freopen("intput.txt","r",stdin);
    int n, s= 0;
    cin>>n;
    for(int i= 1; i<= n; i++)
    {
        cin>>A[i];
        s+=A[i];
    }
}

