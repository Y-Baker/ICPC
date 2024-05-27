#include <iostream>
#include <vector>
#include <algorithm>
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

    int n;
    cin >> n;

    vector<vector<ll>> arr(2);
    vector<ll> arr1(n+1);
    vector<ll> arr2(n+1);

    arr[0] = arr1;
    arr[1] = arr2;

    for (int i = 1; i <= n; i++) {
        int x;
        cin >> x;
        arr[0][i] = x;
        arr[1][i] = x;
    }
    sort(arr[1].begin(), arr[1].end());

    for (int i = 2; i <= n; i++) {
        arr[0][i] += arr[0][i-1];
        arr[1][i] += arr[1][i-1];
    }

    int m, t, l, r;
    cin >> m;

    while (m--) {
        cin >> t >> l >> r;
        t--, l--;
        cout << arr[t][r] - arr[t][l] << endl;
    }
}
