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
 
    int t;
    cin >> t;
 
    while (t--) {
        ll a, b;
        cin >> a >> b;
 
        ll x = a ^ b;
        ll l = x|a, r = x^b;
        if (l == r) {
            cout << x << endl;
        } else {
            cout << -1 << endl;
        }
 
    }
}
