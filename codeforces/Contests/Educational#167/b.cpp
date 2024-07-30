#include <iostream>
#include <string>

#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}


bool isSubsequence(const string& root, const string& s, int i, int j) {
    if (j == 0) {
        return true;
    }
    if (i == 0) {
        return false;
    }

    if (s[j - 1] == root[i - 1]) {
        return isSubsequence(root, s, i - 1, j - 1);
    }

    return isSubsequence(root, s, i - 1, j);
}

void getLargest(const string& a, const string& b) {
    int maxx = 0;
    for (int i = 0; i < b.length(); i++) {
        for (int j = i; j < b.length(); j++) {
            string ss = b.substr(i, j - i + 1);
            if (a == ss || isSubsequence(a, ss, a.length(), ss.length())) {
                if (ss.length() > maxx) {
                    maxx = ss.length();
                }
            } else {
                break;
            }
        }
    }

    if (maxx == 0) {
        cout << a.length() + b.length() << endl;
    } else {
        cout << a.length() + b.length() - maxx << endl;
    }
}

int main() {
    fastIO();
    int t;
    cin >> t;

    while (t--) {
        string a, b;
        cin >> a >> b;

        getLargest(a, b);
    }

    return 0;
}
