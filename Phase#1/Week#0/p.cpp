#include <iostream>

#define endl "\n"

using namespace std;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main()
{
    fastIO();
    int max, winner, idx_max = -1, idx_winner = -1;

    int size;
    cin >> size;
    int arr[size];
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    if (arr[1] > arr[0])
    {
        max = arr[1];
        idx_max = 1;
        winner = arr[0];
        idx_winner = 0;
    }
    else
    {
        max = arr[0];
        idx_max = 0;
        winner = arr[1];
        idx_winner = 1;
    }

    for (int i = 2; i < size; i++)
    {
        if (arr[i] > max) {
            winner = max;
            idx_winner = idx_max;
            max = arr[i];
            idx_max = i;
        } else if (arr[i] > winner) {
            winner = arr[i];
            idx_winner = i;
        }
    }

    cout << idx_winner + 1 << endl;
}
