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

    int tt;
	cin >> tt;
	while (tt--) {
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		int even = 0;
		for (int i = 0; i < n; i++) {
			even += (a[i] % 2 == 0);
		}
		cout << min(even, n - even) << '\n';
	}
	return 0;
}
