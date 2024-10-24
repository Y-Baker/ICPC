#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#define endl "\n"
#define ll long long

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}



vector<int> prime_factors(int n) {
    vector<int> factors;
    
    while (n % 2 == 0) {
        factors.push_back(2);
        n /= 2;
    }

    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
    }
    
    if (n > 2) {
        factors.push_back(n);
    }
    
    return factors;
}


int main() {
    fastIO();
    int t;
    cin >> t;
    while (t--)
    {
        int a, c;
        cin >> a >> c;
        if (a > c) {
            swap(a, c);
        }
        vector <int> vec1 = prime_factors(a);
        vector <int> vec2 = prime_factors(c);

        sort(vec1.begin(), vec1.end());
        sort(vec2.begin(), vec2.end());
        int p = 0;
        for (int i = 0; i < max(vec1.size(), vec2.size()); i++) {
            if (vec1[p] == vec2[p]) {
                p++;
            } else {
                break;
            }
        }
        if (p < vec1.size()) {
            cout << -1 << endl;
        } else {
            ll ans = 1;
            for (int i = p; i < vec2.size(); i++) {
                ans *= vec2[i];
            }
            cout << ans << endl;
        }
    }
}
