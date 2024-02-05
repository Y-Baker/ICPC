#include <iostream>
#include <vector>

using namespace std;

vector<string> splitString(int n, int p, int q, const string& s) {
    for (int i = 0; i <= n / p; ++i) {
        int remainingLength = n - i * p;
        if (remainingLength % q == 0) {
            int j = remainingLength / q;
            vector<string> partition;
            for (int k = 0; k < i; ++k) {
                partition.push_back(s.substr(k * p, p));
            }
            for (int k = 0; k < j; ++k) {
                partition.push_back(s.substr(i * p + k * q, p));
            }
            return partition;
        }
    }
    return {};
}

int main() {

}
