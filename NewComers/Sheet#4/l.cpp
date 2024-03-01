#include <iostream>

#define endl "\n"

using namespace std;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main()
{
    fastIO();

    string s, t;
    cin >> s >> t;

    bool op = true;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] != t[i])
        {
            if (op)
            {
                op = false;
                i++;
                if (i >= s.size())
                {
                    cout << "No" << endl;
                    return 0;
                }
                if (s[i] == t[i - 1] && s[i - 1] == t[i])
                    continue;
                else
                {
                    cout << "No" << endl;
                    return 0;
                }
            }
            else
            {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
}
