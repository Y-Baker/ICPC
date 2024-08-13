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
    int t;
    cin >> t;
    while (t--) {
        string s, t;
        cin >> s >> t;

        string res = "";
        bool flag = false;
        int p1 = 0, p2 = 0;

        while (p1 < s.length()) {
            if (p2 == t.length()) {
                break;
            }
            if (s[p1] == t[p2]) {
                p2++;
            } else {
                if (s[p1] == '?') {
                    res += t[p2];
                    p2++;
                    p1++;
                    continue;
                }
            }
            res += s[p1];
            p1++;
        }

        if (p2 >= t.length()) {
            flag = true;
            for (int i = p1; i < s.length(); i++) {
                if (s[i] == '?') {
                    res += 'a';
                } else {
                    res += s[i];
                }
            }
        }

        if (!flag) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
            cout << res << endl;
        }
    }

    return 0;
}
