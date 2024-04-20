#include <iostream>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

bool isPrime(int n) {
    if (n == 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    fastIO();

    int n;
    cin >> n;

    int cnt = 0;
    int re[n];
    for (int i = 3; i <= 55555 && cnt < n; i+=5) {
        if (isPrime(i)) {
            re[cnt++] = i;
        }
    }
    for (int i = 0; i < n; i++) {
        cout << re[i] << " ";
    }
}
