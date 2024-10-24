#include <iostream>
#include <vector>
#define endl "\n"
#define ll long long

using namespace std;

// wrong answer on test 18

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

char getChar(int lower, int upper=-1, vector<int> costs={}) {
    if (upper == -1) {
        upper = lower;
    }
    if (lower > upper) {
        swap(lower, upper);
    }
    for (int i = 0; i < 26; i++) {
        if (costs[i] >= lower && costs[i] <= upper) {
            return (char)('a' + i);
        }
    }
    return 'a';
}

void get_cost(string s, vector<int> costs) {
    int cost = 0;
    for (int i = 1; i < s.size(); i++) {
        cost += abs(costs[s[i] - 'a'] - costs[s[i - 1] - 'a']);
    }
    cout << cost << endl;
    cout << s << endl;
}

int main() {
    fastIO();
    string s;
    cin >> s;
    int n = s.size();
    vector<int> costs(26);
    for (int i = 0; i < 26; i++) {
        cin >> costs[i];
    }

    int start = 0;
    while (s[start] == '?') {
        start++;
        if (start == n) {
            cout << 0 << endl;
            string re = "";
            for (int i = 0; i < n; i++) {
                re += 'a';
            }
            cout << re << endl;
            return 0;
        }
    }

    char x;
    if (start > 0) {
        x = getChar(costs[s[start] - 'a'],  -1, costs);
        for (int i = start - 1; i >= 0; i--) {
            s[i] = x;
        }
    }

    int l = start;
    int r;
    while (l < n) {
        while (l+1 < n && s[l+1] != '?') {
            l++;
        }
        if (l == n) break;
        r = l + 1;
        while (r < n && s[r] == '?') {
            r++;
        }
        if (r == n) {
            x = getChar(costs[s[l] - 'a'], -1, costs);
            for (int i = l + 1; i < n; i++) {
                s[i] = x;
            }
            break;
        }
        x = getChar(costs[s[l] - 'a'], costs[s[r] - 'a'], costs);
        for (int i = l + 1; i < r; i++) {
            s[i] = x;
        }
        l = r;
    }
    get_cost(s, costs);
}
