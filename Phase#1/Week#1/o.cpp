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

    int t;
    cin >> t;
    string s;

    while(t--) {
        cin >> s;
        if (s.size() % 2 != 0 || s[0] == ')' || s[s.size() - 1] == '(') {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
}
