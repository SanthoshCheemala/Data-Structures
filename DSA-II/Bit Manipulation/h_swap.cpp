#include<iostream>
using namespace std;
int main()
{
	int n,m;
	cin>>n>>m;
	n=n^m;
	m=n^m;
	n=n^m;
	cout<<n<<m;
return 0;
}
