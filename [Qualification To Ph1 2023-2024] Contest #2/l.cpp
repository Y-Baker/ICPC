#include <iostream>
using namespace std;

int main()
{
    string situation;
    cin >> situation;

    int strick = 0;
    for (int i = 1; i < situation.size(); i++)
    {
        if (situation[i] == situation[i - 1])
            strick++;
        else
            strick = 0;
        if (strick == 6)
        {
            cout << "YES";
            return (0);
        }
    }
    cout << "NO";
    return (0);
}
