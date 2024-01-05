#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

float calculateMinkowski(vector<double> p1, vector<double> p2, int m, int dimension)
{
    float sum = 0.0;
    for (int i = 0; i < dimension; i++)
    {
        sum += abs(pow(p1[i] - p2[i], m));
    }
    sum = pow(sum, 1.0 / m);
    return sum;
}
int main()
{
    int dimension;
    cout << "Enter Dimension" << endl;
    cin >> dimension;

    vector<double> point1(dimension);
    vector<double> point2(dimension);

    cout << "Enter Point P1" << endl;
    for (int i = 0; i < dimension; i++)
    {
        cin >> point1[i];
    }

    cout << "Enter Point P2" << endl;
    for (int i = 0; i < dimension; i++)
    {
        cin >> point2[i];
    }

    int m;
    cout << "Enter 'm'" << endl;
    cin >> m;

    float distance = calculateMinkowski(point1, point2, m, dimension);
    cout << "Distance" << distance;
}