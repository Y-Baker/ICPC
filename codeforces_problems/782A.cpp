#include <iostream>
#include <unordered_set>
#include <algorithm>
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

    int n, x, size;
    cin >> n;

    unordered_set<int> set;
    int maxx = 1;

    for (int i = 0; i < 2 * n; i++) {
        cin >> x;
        if (set.count(x) == 1) {
            set.erase(x);
        } else {
            set.insert(x);
        }
        size = set.size();
        maxx = max(maxx, size);
    }
    cout << maxx << endl;
}
