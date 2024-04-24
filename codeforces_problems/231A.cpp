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

    int n, ans=0;
    cin >> n;

    while (n--) {
        bool a[3];
        cin >> a[0] >> a[1] >> a[2];
        int cntZ = 0;
        for (bool one : a) {
            if (!one) {
                cntZ++;
            }
        }
        if (cntZ <= 1) {
            ans++;
        }
    }
    cout << ans << endl;
}
