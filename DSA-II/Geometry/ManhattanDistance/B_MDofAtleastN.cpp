
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> points;

    if (N % 2 != 0)
    {
        points.push_back(make_pair(0, 0));
        points.push_back(make_pair(0, N));
        points.push_back(make_pair(N, 0));
        points.push_back(make_pair(N, N));
    }
    else
    {
        points.push_back(make_pair(0, 0));
        points.push_back(make_pair(0, N));
        points.push_back(make_pair(N, 0));
        points.push_back(make_pair(N, N));
        points.push_back(make_pair(N / 2, N / 2));
    }

    // Print the points
    cout << "Points with Manhattan distance of at least " << N << ":" << endl;
    for (const pair<int, int> &point : points)
    {
        cout << "(" << point.first << ", " << point.second << ")" << endl;
    }

    return 0;
}