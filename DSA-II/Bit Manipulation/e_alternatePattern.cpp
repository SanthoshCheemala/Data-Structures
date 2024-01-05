#include <iostream>
using namespace std;

bool hasAlternatePattern(int n)
{
    int num = n ^ (n >> 1);
    while (num)
    {
        if ((num & 1) == 0)
        {
            return false;
        }
        num = num >> 1;
    }
    return true;
}

int main()
{
    int n;
    cin >> n;
    if (hasAlternatePattern(n))
    {
        cout << "Yes" << endl;
    }
    else
    {
        cout << "No" << endl;
    }
    return 0;
}