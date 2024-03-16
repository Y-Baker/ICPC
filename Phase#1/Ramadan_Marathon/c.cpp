#include <iostream>
#include <map>
#define endl "\n"
#define int long long
using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int32_t main() {
    fastIO();

    int n, n_q;
    cin >> n >> n_q;

    int arr[n];
    int sum = 0;
    int flag = -1;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        sum += arr[i];
    }

    map <int, int> mp;

    while (n_q--)
    {
        int op;
        cin >> op;
        if (op == 2) {
            int x;
            cin >> x;
            flag = x;
            sum = n * x;
            mp.clear();
        } else {
            int x, y;
            cin >> x >> y;
            x -= 1;
            if (flag == -1) {
                // arr doesn't change
                sum += (y - arr[x]);
                arr[x] = y;
            } else {
                // arr changes
                if (mp[x] == 0) {
                    // first time
                    sum -= flag;
                    sum += y;
                    mp[x] = y;
                } else {
                    // after first time
                    sum -= mp[x];
                    sum += y;
                    mp[x] = y;
                }
            }
        }
        cout << sum << endl;
    }
    
}
