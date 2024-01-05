// Count of numbers (x) smaller than or equal to n such that n+x = n^x
#include <iostream>
using namespace std;

int countZeroBits(int n)
{
    int count = 0;
    while (n)
    {
        if ((n & 1) == 0)
        {
            count++;
        }
        n = n >> 1;
    }
    return count;
}
int countNumbers(int n)
{
    int zeroBits = countZeroBits(n);
    return 1 << zeroBits;
}
int main()
{
    int n;
    cin >> n;
    cout << countNumbers(n) << endl;
}