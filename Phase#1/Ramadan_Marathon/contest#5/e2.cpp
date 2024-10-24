#include<bits/stdc++.h>
using namespace std;

#define long long ll;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

const int maxn = 1000005;
int t;
int n, k, m[maxn], b[maxn], cnt1[maxn], cnt2[maxn], ans1 = 0, ans2 = 0;

int main() {
    fastIO();
    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
        cin >> m[i];
        if (m[i] > k) continue;
        else {
            cnt1[m[i]]++;
            ans1 += cnt1[k - m[i]];
        }
    }

    for (int i = 1; i <= n; i++) {
        cin >> b[i];
        if (b[i] > k) continue;
        else {
            cnt2[b[i]]++;
            ans2 += cnt2[k - b[i]];
        }
    }

    // cout << ans1 << " " << ans2 << endl;

    if (ans1 > ans2) return cout << "Mahmoud", 0;
    if (ans1 == ans2) return cout << "Draw", 0;
    return cout << "Bashar", 0;
}
