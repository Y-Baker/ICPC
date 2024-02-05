#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;
    if (n >= 0) {
        cout << n / 10 << endl;
        return 0;
    }
    cout << (n % 10 == 0 ? n / 10 : ((n / 10) - 1)) << endl;
}
