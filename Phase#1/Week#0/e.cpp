#include <iostream>
#include <algorithm>
using namespace std;

int main()

{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        sort(arr, arr + n);
        int last = arr[0], i;
        for (i = 1; i < n; i++)
        {
            if (arr[i] == last)
            {
                cout << "NO" << endl;
                break;
            }
            last = arr[i];
        }
        if (i == n)
        {
            cout << "YES" << endl;
        }
    }
}

