#include<bits/stdc++.h>

#define endl "\n"
#define ll long long
#define all(v) v.begin(),v.end()

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();
    int t = 1;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        int q;
        cin >> q;

        while (q--) {
            bool valid = true;
            string x;
            cin >> x;

            if (x.length() != n) {
                cout << "NO" << endl;
                continue;
            }
            unordered_map<int, char> mp;
            unordered_map<char, int> mp2;

            for (int i = 0; i < n; i++) {
                if (mp2.find(arr[i]) != mp2.end()) {
                    if (mp2[arr[i]] != x[i]) {
                        valid = false;
                        break;
                    }
                }
                else {
                    mp2[arr[i]] = x[i];
                }
                if (mp.find(x[i]) != mp.end()) {
                    if (mp[x[i]] != arr[i]) {
                        valid = false;
                        break;
                    }
                }
                else {
                    mp[x[i]] = arr[i];
                }
            }
            cout << (valid ? "YES" : "NO") << endl;
        }
    }

    return 0;
}
