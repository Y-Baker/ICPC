#include <iostream>
#include <cmath>
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

    while (t--)
    {
        int n, m, k;
        cin >> n >> m >> k;

        if (m <= 1) {
            cout << "NO" << endl;
            continue;
        }
        int x = ceil((double)n / m);
        int re = n - x;
        if (re > k) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    
}
