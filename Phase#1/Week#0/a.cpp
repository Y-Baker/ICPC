#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        int size;
        cin >> size;

        int arr[size];
        int longest = 0, streak = 0;
        for (int i = 0; i < size; i++)
        {
            cin >> arr[i];
            if (arr[i] == 0)
            {
                streak++;
            }
            else
            {
                if (streak > longest)
                {
                    longest = streak;
                }
                streak = 0;
            }
        }
        if (streak > longest)
        {
            longest = streak;
        }
        cout << longest << endl;
    }
}
