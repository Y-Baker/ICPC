#include <iostream>
using namespace std;

int main()
{
    string target;
    cin >> target;

    string cards[5];
    for (int i = 0; i < 5; i++)
        cin >> cards[i];

    for (int i = 0; i < 5; i++)
    {
        if (target[0] == cards[i][0] || target[1] == cards[i][1])
        {
            cout << "YES";
            return (0);
        }
    }
    cout << "NO";
}
