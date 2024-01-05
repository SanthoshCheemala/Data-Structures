#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
class Point
{
public:
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
};
double euclideanDistance(Point A, Point B)
{
    return sqrt(pow(A.x - B.x, 2) + pow(A.y - B.y, 2));
}
int main()
{
    int n;
    cin >> n;
    vector<Point> points;
    for (int i = 0; i < n; ++i)
    {
        int x, y;
        cin >> x >> y;
        points.emplace_back(x, y);
    }
    int count = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            double euclideanDist = euclideanDistance(points[i], points[j]);
            int manhattanDist = abs(points[i].x - points[j].x) + abs(points[i].y - points[j].y);
            if (fabs(euclideanDist - manhattanDist) < 1e-9)
            {
                count++;
            }
        }
    }
    cout << count << endl;
    return 0;
}