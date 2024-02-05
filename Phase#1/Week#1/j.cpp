#include <iostream>
#include <deque>
#define endl "\n"

using namespace std;
bool compare(deque<int> &q, string &t);

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    string s, t;
    deque<int> q;
    cin >> s >> t;

    int n = s.size();
    if (n != t.size()) {
        cout << "No" << endl;
        return 0;
    }
    if (s == t) {
        cout << "Yes" << endl;
        return 0;
    }
    for (int i = 0; i < n; i++) {
        q.push_back(s[i]);
    }
    for (int i = 0; i < n; i++) {
        q.push_front(q.back());
        q.pop_back();
        if (compare(q, t)) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}


bool compare(deque<int> &q, string &t) {
    for (int i = 0; i < q.size(); i++) {
        if (q[i] != t[i]) {
            return false;
        }
    }
    return true;
}
