//Intersection of two lines

#include <iostream>
using namespace std;

class Point
{
public:
    float x, y;
};

Point point_of_intersection(float a1, float b1, float c1, float a2, float b2, float c2)
{
    Point P;
    P.x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1);
    P.y = (a2 * c1 - a1 * c2) / (a1 * b2 - a2 * b1);
    return P;
}

int main()
{
    float a1, b1, c1, a2, b2, c2;
    cout << "Enter coefficients for the first line (a1, b1, c1): ";
    cin >> a1 >> b1 >> c1;

    cout << "Enter coefficients for the second line (a2, b2, c2): ";
    cin >> a2 >> b2 >> c2;

    Point intersection = point_of_intersection(a1, b1, c1, a2, b2, c2);

    cout << "(X,Y) = " << intersection.x << "," << intersection.y << endl;

    return 0;
}