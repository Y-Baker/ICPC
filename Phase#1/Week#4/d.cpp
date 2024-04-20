#include <iostream>
#include <cmath>
#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}
bool isPrime(ll n) {
    if (n < 2) return false;
    for (ll i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

bool isTPrime(ll n) {
    if (n < 4) return false;
    ll i;
    for (i = 2; i * i < n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    if (i * i == n) {
        return true;
    }
    return false;
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while (t--) {
        ll n;
        cin >> n;
        ll root = sqrt(n);
        if (root * root == n && isPrime(root)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
