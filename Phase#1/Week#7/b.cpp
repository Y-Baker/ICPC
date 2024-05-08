#include <iostream>
#include <algorithm>
#include <vector>

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

    int n, m;
    cin >> n >> m;

    vector<int> arr1(n);
    vector<int> arr2(m);

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> arr2[i];
    }

    sort(arr1.begin(), arr1.end());
    sort(arr2.begin(), arr2.end());

    if (n > m) {
        swap(arr1, arr2);
        swap(n, m);
    }

    int minn = 1e9;

    for (int i : arr1) {
        auto it = lower_bound(arr2.begin(), arr2.end(), i);
        if (it != arr2.end()) {
            minn = min(minn, abs(i - *it));
        }
        if (it != arr2.begin()) {
            it--;
            minn = min(minn, abs(i - *it));
        }
    }

    cout << minn << endl;
}
