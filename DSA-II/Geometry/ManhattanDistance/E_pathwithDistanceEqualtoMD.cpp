#include <cmath>
#include <iostream>
using namespace std;
class Point
{
public:
    float x, y;
};
int fact(int n)
{
    if (n == 1)
    {
        return 1;
    }
    else
        return n * fact(n - 1);
}
int main()
{
    Point p1, p2;

    cout << "Enter Point 1" << endl;
    cin >> p1.x >> p1.y;
    cout << "Enter Point 2" << endl;
    cin >> p2.x >> p2.y;

    float m = abs(p1.x - p2.x);
    float n = abs(p1.y - p2.y);

    int ans = fact(m + n) / (fact(n) * fact(m));

    cout << "ans:\t" << ans;
}