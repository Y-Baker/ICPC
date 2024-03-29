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

    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        long long sum = 0;
        int maxx = -1;
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
            maxx = max(maxx, arr[i]);
            sum += arr[i];
        }
        sum -= maxx;
        if (maxx == 0) {
            cout << 0 << endl;
        } else if (sum >= maxx) {
            cout << 1 << endl;
        } else {
            cout << maxx - sum << endl;
        }

    }
}
