#include <iostream>

#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int countFactors(ll n, int p) {
    int cnt = 0;
    while (n % p == 0) {
        cnt++;
        n /= p;
    }
    return cnt;
}

int main() {
    fastIO();

    int t;
    cin >> t;

    while (t--) {
        ll n, m;
        cin >> n >> m;

        int factorsOf2 = countFactors(n, 2) + countFactors(m, 2);
        int factorsOf5 = countFactors(n, 5) + countFactors(m, 5);

        ll maxZeros = min(factorsOf2, factorsOf5);
        ll bestPrice = n * m / (1LL << (factorsOf2 - maxZeros) * (factorsOf5 - maxZeros));

        cout << bestPrice << endl;
    }

    return 0;
}