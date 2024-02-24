#include <iostream>
#include <unordered_map>

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
    string s;
    unordered_map<string, int> database;
    cin >> t;

    while(t--) {
        cin >> s;
        auto it = database.find(s);
        if (it == database.end()) {
            database.insert({s, 0});
            cout << "OK" << endl;
        }
        else {
            it->second++;
            cout << it->first << it->second << endl;
        }
    }
}
