#include <iostream>
#include <vector>
using namespace std;
vector<int> convertBinary(int n)
{
    vector<int> temp;
    while (n > 0)
    {
        int remainder = n % 2;
        temp.insert(temp.begin(), remainder);
        n = n / 2;
    }
    if (temp.empty())
    {
        temp.push_back(0);
    }
    return temp;
}
int calculateXOR(int n)
{
    vector<int> BinaryDigits = convertBinary(n);
    int count_0s = 0, count_1s = 0;
    for (int i : BinaryDigits)
    {
        if (i == 0)
            count_0s++;
        else
            count_1s++;
    }
    int XORresult = count_0s ^ count_1s;
    return XORresult;
}
int main()
{
    int n;
    cin >> n;
    cout << calculateXOR(n) << endl;
    return 0;
}