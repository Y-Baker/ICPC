#include <iostream>
#include <vector>
#include <algorithm>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, n, n_queries, query;
    cin >> t;
    while(t--) {
        cin >> n >> n_queries;
        vector<int> v(n);

        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }
        sort(v.begin(), v.end(), greater<int>());
        for (int i = 1; i < n; i++) {
            v[i] += v[i - 1];
        }

        for (int i = 0; i < n_queries; i++) {
            cin >> query;

            if (query > v[n - 1]) {
                cout << -1 << endl;
            } else if (query == v[n - 1]){
                cout << n << endl;
            } else {
                auto it = lower_bound(v.begin(), v.end(), query);
                int ans = it - v.begin();
                cout << ans + 1 << endl;
            }
        }
    }
}
