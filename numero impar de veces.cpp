
#include <iostream>
#include <stdio.h>

using namespace std;

int v1[100],v2[100],v3[100],n,n1,c=0,c1=0;

int main()
{
    cout<<"Digite el numero de elementos del arreglo: ";
    cin>>n1;

    for (int i=0; i<n1; i++){
        
        cout<<i+1<<". Digite un numero del arreglo ";
        cin>>v1[i];
        v2[i]=v1[i];
    }

    for (int j=0; j<n1; j++){
      c=0;
      for (int k=0; k<n1; k++){
          
        if (v1[j]==v2[k]){
            c++;
            v3[j]=c;
        }
      }
    }
      
     for (int l=0; l<n1; l++){
          
        if (v3[l]%2!=0){
            c1=l;
        }
        
     }
    cout<<"Elemento encontrado valido"<<v1[c1];
    return 0;
}