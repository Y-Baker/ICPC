#include <bits/stdc++.h>

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
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        string strNum = to_string(n);
        bool valid = false;
        if (((strNum[0]-'0')+(strNum[1]-'0')+(strNum[2]-'0')) == 16 && ((strNum[3]-'0')+(strNum[4]-'0')+(strNum[5]-'0')) == 16) valid = true;
        if (!valid) {
            int str = 100000, end = 100199;
            while (!(n >= str && n <= end)) {
                str += 200;
                end += 200;
            }
            cout << str << ' ' << end << endl;
            for (int i = str; i <= end; i++) {
                string strNum = to_string(i);
                if (((strNum[0]-'0')+(strNum[1]-'0')+(strNum[2]-'0')) == 16 && ((strNum[3]-'0')+(strNum[4]-'0')+(strNum[5]-'0')) == 16) {
                    valid = true;
                    cout << i << endl;
                    break;
                }
            }
        }
        cout << (valid ? "YES" : "NO") << endl;
    }
}
