#include <iostream>
#include <algorithm>
#include <unordered_map>

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

    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    unordered_map<char, int> mp;

    for (int i = 0; i < n; i++) {
        mp[s[i]]++;
    }

    for (char c = 'a'; c <= 'z'; c++) {
        if (mp[c] >= k) {
            mp[c] -= k;
            k = 0;
            break;
        } else {
            k -= mp[c];
            mp[c] = 0;
        }
    }

    string str = "";

    for (int i = n - 1; i >= 0; i--) {
        if (mp[s[i]] > 0) {
            str += s[i];
            mp[s[i]]--;
        }
    }

    reverse(str.begin(), str.end());

    cout << str << endl;
}
