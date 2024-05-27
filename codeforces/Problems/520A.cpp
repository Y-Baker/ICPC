#include <iostream>
#include <unordered_set>

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

    string s;
    cin >> s;

    unordered_set<char> set;

    for (char c : s) {
        c = tolower(c);
        set.insert(c);
        if (set.size() == 26) {
            cout << "YES" << endl;
            return 0;
        }
    }
    cout << "NO" << endl;
}
