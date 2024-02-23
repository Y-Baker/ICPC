#include <iostream>
#include <set>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int t, n;
    string str;
    cin >> t;

    while(t--) {
        set<char> s1;
        set<char> s2;
        cin >> n;
        cin >> str;

        int maxx = 0, count = 0;
        int start = 0, start_max;

        int dis[n];
        for (int i = n - 1; i >= 0; i--) {
            s1.insert(str[i]);
            dis[i] = s1.size();
        }
        for (int i = 0; i < n - 1; i++) {
            s2.insert(str[i]);
            maxx = max(maxx, int(s2.size() + dis[i + 1]));
        }
        cout << maxx << endl;
    }
}
