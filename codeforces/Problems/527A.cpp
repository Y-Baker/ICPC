#include <iostream>

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

    ll big, small;
    cin >> big >> small;
    ll ans = 0;

    while (small > 0) {
        ll times = big / small;
        big -= small * times;
        ans += times;
        if (small > big) {
            ll tmp = small;
            small = big;
            big = tmp;
        }
    }
    cout << ans << endl;
}
