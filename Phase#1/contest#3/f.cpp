#include <iostream>
#include <vector>

#define int long long
using namespace std;

int32_t main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n, q;
        cin >> n >> q;

        vector<int> arr(n);
        for (int j = 0; j < n; j++) {
            cin >> arr[j];
        }

        for (int j = 0; j < q; j++) {
            int l, r, k;
            cin >> l >> r >> k;

            int s = 0;
            for (int x = 0; x < l - 1; x++) {
                s += arr[x];
            }
            for (int x = r; x < n; x++) {
                s += arr[x];
            }
            s += k * (r - l + 1);

            if (s % 2 == 1) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }

    return 0;
}
