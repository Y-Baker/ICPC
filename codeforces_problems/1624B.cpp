#include <iostream>
#include <vector>
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
        int a, b, c;
        cin >> a >> b >> c;

        bool flag = false;
        for (int i = 0; i < 3; ++i) {
            if (i == 0) {
                int x = 2 * b - c;
                if (x % a == 0 && x / a > 0) {
                    flag = true;
                    break;
                }
            }
            if (i == 1) {
                double x = (a + c) / 2.0;
                if (x == int(x) && int(x) > 0 && int(x) % b == 0) {
                    flag = true;
                    break;
                }
            }
            if (i == 2) {
                int x = 2 * b - a;
                if (x % c == 0 && x / c > 0) {
                    flag = true;
                    break;
                }
            }
        }
        if(flag) cout <<"YES\n";
        else cout<<"NO\n";
        
    }

    return 0;
}
