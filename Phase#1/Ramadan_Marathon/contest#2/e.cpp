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

    int t;
    cin >> t;
    while (t--)
    {
        int a, b;
        cin >> a >> b;
        string s("");

        if (a >= b)
        {
            s = "0";
            --a;
        }
        else
        {
            s = "1";
            --b;
        }

        while (a > 0 || b > 0)
        {
            if (s.back() == '0')
            {
                if (b > 0)
                {
                    s += '1';
                    --b;
                }
                else if (a > 0)
                {
                    s += '0';
                    --a;
                }
            }
            else if (s.back() == '1')
            {
                if (a > 0)
                {
                    s += '0';
                    --a;
                }
                else if (b > 0)
                {
                    s += '1';
                    --b;
                }
            }
        }

        cout << s << endl;
    }
}
