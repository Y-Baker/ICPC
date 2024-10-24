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
pair<int, int> findMax(string s, int n, unordered_map<char, pair<int, int>> op) {
    int x = 0, y = 0;
    for (int i = 0; i < n; i++) {
        x += op[s[i]].first;
        y += op[s[i]].second;
    }
    return make_pair(x, y);
}

bool checkCloser(int x, int y, int targetX, int targetY, char c) {
    if (c == 'N') {
        if (y < targetY) {
            return true;
        }
    }
    else if (c == 'S') {
        if (y > targetY) {
            return true;
        }
    }
    else if (c == 'E') {
        if (x < targetX) {
            return true;
        }
    }
    else if (c == 'W') {
        if (x > targetX) {
            return true;
        }
    }
    return false;
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        string s;
        cin >> s;

        unordered_map<char, pair<int, int>> op;
        op['N'] = make_pair(0, 1);
        op['S'] = make_pair(0, -1);
        op['E'] = make_pair(1, 0);
        op['W'] = make_pair(-1, 0);

        if (n & 1) {
            cout << "NO" << endl;
            continue;
        }

        pair<int, int> maxx = findMax(s, n, op);
        if (maxx.first & 1 || maxx.second & 1) {
            cout << "NO" << endl;
            continue;
        }
        int targetX = maxx.first / 2;
        int targetY = maxx.second / 2;

        string re = "";
        bool flag = false;

        int x = 0, y = 0;
        if (targetX == 0 && targetY == 0) {
            bool flags[4] = {false, false, false, false};
            int idxs[4] = {-1, -1, -1, -1};

            for (int i = 0; i < n; i++) {
                if (s[i] == 'N') {
                    flags[0] = true;
                    idxs[0] = i;
                }
                else if (s[i] == 'S') {
                    flags[1] = true;
                    idxs[1] = i;
                }
                else if (s[i] == 'E') {
                    flags[2] = true;
                    idxs[2] = i;
                }
                else if (s[i] == 'W') {
                    flags[3] = true;
                    idxs[3] = i;
                }
                if (flags[0] && flags[1] && flags[2] && flags[3]) {
                    break;
                }
            }

            if (flags[0] && flags[1]) {
                re = string(n, 'R');
                re[idxs[0]] = 'H';
                re[idxs[1]] = 'H';
                if (n == 2) {
                    cout << "NO" << endl;
                } else {
                    cout << re << endl;
                }
                continue;
            }
            else if (flags[2] && flags[3]) {
                re = string(n, 'R');
                re[idxs[2]] = 'H';
                re[idxs[3]] = 'H';
                if (n == 2) {
                    cout << "NO" << endl;
                } else {
                    cout << re << endl;
                }
                continue;
            }
            else {
                cout << "NO" << endl;
                continue;
            }
        }
        bool flagR = false;
        bool flagH = false;
        for (int i = 0; i < n; i++) {
            if (flag) {
                re += string(n - i, 'R');
                flagR = true;
                break;
            }
            if (checkCloser(x, y, targetX, targetY, s[i])) {
                re += 'H';
                flagH = true;
                x += op[s[i]].first;
                y += op[s[i]].second;
            }
            else {
               re += 'R';
               flagR = true;
            }
            if (x == targetX && y == targetY) {
                flag = true;
            }
        }
        if (flagR && flagH) {
            cout << re << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}
