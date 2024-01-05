#include <iostream>
#include <vector>
#include <algorithm>

using namespace std; 

vector<vector<float>> transpose(const vector<vector<float>> &L)
{
    int rows = L.size();
    int cols = L[0].size();
    vector<vector<float>> T(cols, vector<float>(rows));

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            T[j][i] = L[i][j];
        }
    }

    return T;
}

void minimizeMD(const vector<vector<float>> &L, int K, int N)
{
    vector<vector<float>> T = transpose(L);
    vector<vector<float>> M;

    for (int i = 0; i < K; i++)
    {
        sort(T[i].begin(), T[i].end());
    }

    for (int i = 0; i < K; i++)
    {
        cout << T[i][(N + 1) / 2 - 1] << ' ';
    }
    cout << endl;
}

int main()
{
    int N, K;
    cout << "Enter the value of N: ";
    cin >> N;
    cout << "Enter the value of K: ";
    cin >> K;

    vector<vector<float>> L;

    for (int i = 0; i < N; i++)
    {
        vector<float> P;
        cout << "Enter the coordinates: " << endl;
        for (int j = 0; j < K; j++)
        {
            float coordinate;
            cin >> coordinate;
            P.push_back(coordinate);
        }
        L.push_back(P);
    }

    minimizeMD(L, K, N);

    return 0;
}