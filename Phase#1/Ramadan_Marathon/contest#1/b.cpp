#include <iostream>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        int arr[n];
        int mapp[2] = {0, 0};
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (arr[i] % 3 == 0)
            {
                count++;
            }
            else
            {
                mapp[arr[i] % 3 - 1]++;
            }
        }

        int cnt = count + min(mapp[0], mapp[1]) + (max(mapp[0], mapp[1]) - min(mapp[0], mapp[1])) / 3;
        cout << cnt << endl;
    }
    
}
