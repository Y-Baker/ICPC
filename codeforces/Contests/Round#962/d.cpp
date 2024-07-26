#include <iostream>
#include <algorithm>

using namespace std;

int count_triplets(int n, int x) {
    int count = 0;
    for (int a = 1; a <= x; ++a) {
        for (int b = 1; b <= x - a; ++b) {
            if (a * b > n) {
                break;
            }
            int max_c = max((n - a * b) / (a + b), 0);
            max_c = min(max_c, x - a - b);
            if (max_c == 0) {
                continue;
            }
            count += max(max_c, 0);
        }
    }
    return count;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, x;
        cin >> n >> x;
        cout << count_triplets(n, x) << endl;
    }

    return 0;
}
