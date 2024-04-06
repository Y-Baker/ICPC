#include <iostream>
#include <vector>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();

    int n;
    cin >> n;

    int arr[n];
    vector<int> dp[n];
    int cnt = 0;
    for (int i = 1; i < n; i++) {
        cin >> arr[i]; 
    }
}
