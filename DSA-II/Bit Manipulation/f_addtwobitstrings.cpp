#include <iostream>
using namespace std;

string addBitStrings(string A, string B)
{
    int i = A.size() - 1;
    int j = B.size() - 1;
    int carry = 0;
    string result = "";

    while (i >= 0 || j >= 0 || carry)
    {
        // Add the values of current bits and the carry
        int sum = carry;
        if (i >= 0)
            sum += (A[i] - '0');
        if (j >= 0)
            sum += (B[j] - '0');

        // Append the current bit to the result string
        result = char(sum % 2 + '0') + result;

        // Update carry for the next calculation
        carry = sum / 2;

        // Move to the next bits in the input strings
        i--;
        j--;
    }

    return result;
}

int main()
{
    string A = "1101";
    string B = "111";
    string result = addBitStrings(A, B);
    cout << "Output: " << result << endl;
    return 0;
}