#include <iostream>
using namespace std;

void help(int n, int m)
{
    int x = n ^ m;
    int count = 1;
    while (x)
    {
        if ((x & 1) == 0)
            count++;
        else
            break;
        x = x >> 1;
    }
    cout << count;
}
int main()
{
    int n, m;
    cin >> n >> m;
    help(n, m);
}