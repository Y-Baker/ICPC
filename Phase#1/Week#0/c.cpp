#include <iostream>
using namespace std;


int main()
{
    int n;
    cin >> n;

    int input[3*n];
    int freq[n] = {0};

    for (int i = 0; i < 3*n; i++)
    {
        cin >> input[i];
        freq[input[i] - 1]++;
        if (freq[input[i] - 1] == 2)
        {
            cout << input[i] << ' ';
        }
    }

}
