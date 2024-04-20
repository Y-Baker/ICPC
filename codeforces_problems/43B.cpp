#include <iostream>
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

    unordered_map<char, int> map;
    string s1, s2;

    getline(cin, s1);
    getline(cin, s2);

    for (char c : s1) {
        if (c != ' ')
            map[c]++;
    }

    for (char c : s2) {
        if (c == ' ') continue;
        if (map[c] == 0) {
            cout << "NO" << endl;
            return 0;
        }
        map[c]--;
    }
    cout << "YES" << endl;
}
