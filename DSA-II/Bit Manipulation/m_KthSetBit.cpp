#include <iostream>
using namespace std;

void help(int n, int k)
{
    int index = 1;
    int count = 0;
    while (n)
    {
        if (n & 1 == 1)
        {
            count++;
            if (count == k)
            {
                cout << index;
                return;
            }
        }
        index++;
        n = n >> 1;
    }
}
int main()
{
    int n, k;
    cin >> n >> k;
    help(n, k);
}