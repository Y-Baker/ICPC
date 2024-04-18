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
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        ll summ = 0;
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            summ += arr[i];
        }

        ll l = 0, r = summ;
        bool re = false;
        while (l <= r) {
            ll mid = l + (r - l) / 2;
            if (mid * mid == summ) {
                re = true;
                break;
            } else if (mid * mid < summ) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        if (re) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

// 0 0 0 0
// 0 1 1 0
// 0 1 1 0
// 0 0 0 0 