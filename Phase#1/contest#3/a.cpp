#include <iostream>
#include <iostream>
#include <vector>
#include <cmath>
#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}


bool isSquare(int i) {
    int root = static_cast<int>(sqrt(i));
    return i == root * root;
}

int main() {
    fastIO();
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int count = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (isSquare(arr[i] * arr[j])) {
                count++;
            }
        }
    }

    cout << count << endl;

    return 0;
}
