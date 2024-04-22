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
    int n;
    cin >> n;

    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }

    sort(a.begin(), a.end());

    int l = 0, r = 0, start = a[0].first;
    while (l < n) {
        int tmp = l + 1;
        if (tmp >= n) {
            cout << start << " " << a[r].second << endl;
            break;
        }
        if (a[tmp].first > a[r].second) {
            cout << start << " " << a[r].second << endl;
            start = a[tmp].first;
            l = tmp;
            r = tmp;
        } else {
            l = tmp;
            if (a[tmp].second > a[r].second) {
                r = tmp;
            }
        }
    }
}
