#include <iostream>
using namespace std;

int main()
{
    int freq[3] = {0};
    for (int i = 0; i < 3; i++) {
        char line[3];
        for (int j = 0; j < 3; j++) {
            cin >> line[j];
        }
        switch (line[1])
        {
        case '>':
            freq[line[0] - 'A']++;
            break;
        case '<':
            freq[line[2] - 'A']++;
            break;
        default:
            break;
        }
    }
    if (freq[0] == freq[1] || freq[1] == freq[2] || freq[0] == freq[2]) {
        cout << "Impossible" << endl;
        return 0;
    }
    char result[3];
    for (int i = 0; i < 3; i++) {
        result[freq[i]] = 'A' + i;
    }
    cout << result[0] << result[1] << result[2];
}
