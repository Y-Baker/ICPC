#include <iostream>
#include <unordered_set>
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

    int n, m, x;
    cin >> n >> m;

    int arr[n];
    for (int i = 0; i < n; i++) cin >> arr[i];

    unordered_set<int> set;

    for (int i = n - 1; i >= 0; i--) {
        set.insert(arr[i]);
        arr[i] = set.size();
    }

    while (m--) {
        cin >> x;
        x--;
        cout << arr[x] << endl;
    }
}
