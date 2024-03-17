#include <iostream>

#define endl "\n"
#define ll long long
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
        int n, n_q;
        cin >> n >> n_q;
        int arr[n + 1];
        arr[0] = 0;
        for (int i = 1; i <= n; i++) {
            ll x;
            cin >> x;
            arr[i] = 0;
            while (x > 1) {
                arr[i]++;
                if (x & 1 == 1) {
                    x--;
                } else {
                    x /= 2;
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            arr[i] += arr[i - 1];
        }
        while (n_q--) {
            int l, r;
            cin >> l >> r;
            cout << arr[r] - arr[l - 1] << endl;
        }
    }
    return 0;
}
