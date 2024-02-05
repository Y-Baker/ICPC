#include <iostream>
using namespace std;

int main() {
    string s;
    int times;
    cin >> s;

    while (s.size() > 1)
    {
        times++;
        int sum = 0;
        for (int i = 0; i < s.size(); i++)
            sum += s[i] - '0';
        s = to_string(sum);
    }
    cout << times << endl;
}
