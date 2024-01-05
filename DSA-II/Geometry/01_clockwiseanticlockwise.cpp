// Clockwise or Anticlockwise
#include <iostream>
using namespace std;

class Point
{
public:
    float x;
    float y;
};

float cross(Point p1, Point p2, Point p0)
{
    return ((p1.x-p0.x)*(p2.y-p0.y) - (p1.y-p0.y)*(p2.x-p0.x));
}
int main()
{
    Point p1, p2, p0;
    cout << "P1" << endl;
    cin >> p1.x >> p1.y;
    cout << "P2\n";
    cin >> p2.x >> p2.y;
    cout << "P0\n";
    cin >> p0.x >> p0.y;

    float result=cross(p1,p2,p0);
    if(result>0){
        cout<<"P1 is clockwise from P2"<<endl;
    }
    else if(result<0)
    {
        cout<<"P1 is anticlockwise from P2"<<endl;
    }
    else{
        cout<<"Points are Collinear"<<endl;
    }
}