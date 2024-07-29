#include<bits/stdc++.h>
#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void doOperation(vector<int> &a, int n) {
    for (int i = 0; i < a.size(); i++) {
        a[i] = abs(a[i] - n);
    }
}
int main() {
    fastIO();

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        if (n == 1) {
            cout << 1 << endl << a[0] << endl;
            continue;
        }
        sort(a.begin(), a.end());
        if (a[n - 1] == a[0]) {
            cout << 1 << endl << a[0] << endl;
            continue;
        }
        vector<int> ans;
        while (*max_element(a.begin(), a.end()) > 0) {
            if (ans.size() > 40) {
                break;
            }
            int a1 = -1, a2 = -1;
            for (int x : a) {
                if (a1 == -1 && x != 0) {
                    a1 = x;
                } else if (a1 != -1 && x != 0) {
                    a2 = x;
                    break;
                }
            }
            if (a2 != -1 && (a1 % 2) != (a2 % 2)) {
                break;
            }
            int min_val = *min_element(a.begin(), a.end());
            int max_val = *max_element(a.begin(), a.end());
            int x = (min_val + max_val) / 2;
            ans.push_back(x);
            doOperation(a, x);
        }
        if (*max_element(a.begin(), a.end()) > 0) {
            cout << -1 << endl;
            continue;
        }
        if (ans.size() > 40) {
            cout << -1 << endl;
            continue;
        }
        cout << ans.size() << endl;
        for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
        cout << endl;
    }
}
