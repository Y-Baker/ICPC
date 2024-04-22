#include <iostream>
#include <algorithm>

#define endl "\n"
#define ll long long
#define int long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int binary_search(int left, int right, int k, int x, ll ps[]) {
    int maxx = -1, to_fill, have;
    int l = left, r = right;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (mid > left) {
            to_fill = (x + 1)* mid;
            have = ps[x];
        } else {
            to_fill = x * mid;
            if (x == 0) {
                have = 0;
            } else {
                have = ps[x - 1];
            }
        }
        if (to_fill - have <= k) {
            maxx = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return maxx;
}

int32_t main() {
    fastIO();
    int t, n, k;
    cin >> t;

    while (t--) {
        cin >> n >> k;
        int arr[n];
        ll ps[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        sort(arr, arr + n);
        ps[0] = arr[0];
        for (int i = 1; i < n; i++) {
            ps[i] = ps[i - 1] + arr[i];
        }
        ll x = (ps[n - 1] + k) / n;
        if (x > arr[n - 1]) {
            cout << x << endl;
        } else {
            int maxx, last = -1;
            int ptr = n - 1;
            while (ptr >= 0) {
                int to_fill = (ptr) * arr[ptr];
                int have = ps[ptr - 1];
                if (to_fill - have <= k || ptr == 0) {
                    if (last == -1) {
                        maxx = arr[ptr];
                    } else {
                        maxx = binary_search(arr[ptr], last, k, ptr, ps);
                    }
                    break;
                } else {
                    last = arr[ptr];
                    ptr--;
                }
            }
            cout << maxx << endl;
        }
        
    }
}
