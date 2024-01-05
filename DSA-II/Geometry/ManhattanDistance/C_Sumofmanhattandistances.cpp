
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int distancesum(vector<int> &arr)
{
    sort(arr.begin(), arr.end());

    int res = 0, sum = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        res += (arr[i] * i - sum);
        sum += arr[i];
    }

    return res;
}

int totaldistancesum(vector<int> &x, vector<int> &y)
{
    return distancesum(x) + distancesum(y);
}

int main()
{
    int n;
    cout << "Enter the number of points: ";
    cin >> n;

    vector<int> x(n);
    vector<int> y(n);

    cout << "Enter the x and y coordinates of the points:" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> x[i] >> y[i];
    }

    cout << "Total Manhattan distance sum: " << totaldistancesum(x, y) << endl;
    return 0;
}