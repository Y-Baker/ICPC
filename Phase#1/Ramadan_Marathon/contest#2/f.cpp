#include <iostream>
#include <vector>
#define endl "\n"
#define int long long
using namespace std;
int maxsubarray(vector<int> a, int n);

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int32_t main() {
    fastIO();
    int n;

    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << maxsubarray(a, n) << endl;
}


int maxsubarray(vector<int> a, int n) {
    int maxsum = a[0];
    int sum = a[0];
    for (int i = 1; i < n; i++) {
        sum = max(a[i], sum + a[i]);
        maxsum = max(maxsum, sum);
    }
    return maxsum;
}