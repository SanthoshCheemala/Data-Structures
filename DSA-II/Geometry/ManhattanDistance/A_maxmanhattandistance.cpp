// Max Manhattan distance between a distinct pair from N coordinates
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
class Point
{
public:
    float x, y;
};

float max_manhattan_distance(Point point[], int N)
{
    vector<float> sum(N), diff(N);
    for (int i = 0; i < N; i++)
    {
        sum[i] = point[i].x + point[i].y;
        diff[i] = (point[i].x - point[i].y);
    }
    sort(sum.begin(), sum.end());
    sort(diff.begin(), diff.end());

    float maximum = max(abs(sum[N - 1] - sum[0]), abs(diff[N - 1] - diff[0]));
    return maximum;
}
int main()
{
    int N; // Number of points
    cout << "Enter Number of Points" << endl;
    cin >> N;

    Point points[N];

    for (int i = 0; i < N; i++)
    {
        cout << "Enter Point" << i + 1 << endl;
        cin >> points[i].x >> points[i].y;
    }

    float maximum = max_manhattan_distance(points, N);
    cout << "Maximum distance\t" << maximum;
}