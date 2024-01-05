#include <iostream>
using namespace std;

bool isPowerOfTwo(int n)
{
    return (n > 0) && ((n & (n - 1)) == 0);
}

int main()
{
    int N;
    cin >> N;

    if (isPowerOfTwo(N))
    {
        cout << "Output: Yes" << endl;
    }
    else
    {
        cout << "Output: No" << endl;
    }
    return 0;
}