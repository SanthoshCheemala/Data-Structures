#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int CalculateTotalLength(vector<pair<int, int>> &segments)
{
    int n = segments.size();
    if (n == 0)
    {
        return 0; // Handle the case with no segments.
    }

    vector<pair<int, bool>> points(n * 2);

    for (int i = 0; i < n; i++)
    {
        points[i * 2] = make_pair(segments[i].first, false);
        points[i * 2 + 1] = make_pair(segments[i].second, true);
    }

    // Sort the points by their x-coordinate.
    sort(points.begin(), points.end());

    int result = 0;
    int count = 0;

    for (int i = 0; i < n * 2; i++)
    {
        if (count)
        {
            result += (points[i].first - points[i - 1].first);
        }
        count += (points[i].second) ? -1 : 1;
    }

    return result;
}

int main()
{
    int num;
    cout << "Enter the number of segments: ";
    cin >> num;

    vector<pair<int, int>> segments;
    for (int i = 0; i < num; i++)
    {
        int start, end;
        cout << "Enter start and end points for segment " << i + 1 << ": ";
        cin >> start >> end;
        segments.push_back(make_pair(start, end));
    }

    int total_length = CalculateTotalLength(segments);
    cout << "Total length covered by segments: " << total_length << endl;

    return 0;
}