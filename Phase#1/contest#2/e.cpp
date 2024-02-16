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

    string s, t;
    cin >> s >> t;

    int s_idx = s.size() - 1;
    int t_idx = t.size() - 1;

    while(s[s_idx] == t[t_idx] && s_idx >= 0 && t_idx >= 0) {
        s_idx -= 1;
        t_idx -= 1;
    }

    cout << s_idx + t_idx + 2 << endl;
}
