#include <iostream>
#include <algorithm>
#include <map>
#define endl "\n"
#define ll long long
using namespace std;
int caloperation(int x, map<ll, ll> &mp);

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
        int n, n_q;
        cin >> n >> n_q;

        ll arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        map<ll, ll> mp;  // (num, op)

        mp[1] = 0;
        mp[2] = 1;
        for (int i = 3; i <= 1000000; i++) {
            mp[i] = 1 + (i % 2 == 0 ? mp[i / 2] : mp[i - 1]);
        }

        while (n_q--) {
            int l, r;
            cin >> l >> r;
            l -= 1;
            r -= 1;

            int total = 0;
            for (int i = l; i <= r; i++) {
                total += caloperation(arr[i], mp);
            }
            cout << total << endl;
        }
    }
    return 0;
}

int caloperation(int x, map<ll, ll> &mp) {
    if (mp.find(x) != mp.end()) {
        return mp[x];
    } else if (x == 1) {
        return 0;
    } else if (x & 1 == 0) {
        return 1 + caloperation(x / 2, mp);
    } else {
        return 1 + caloperation(x - 1, mp);
    }
}
