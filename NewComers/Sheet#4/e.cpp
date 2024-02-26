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
    string s;
    
    while (t--)
    {
        cin >> s;
        int counter = 0;
        int l = 0;
        int r = s.size() - 1;
        while (l < r)
        {
            if (s.at(l) == '1' && s.at(r) == '1')
            {

                for (int j = l; j <= r; j++)
                {
                    if (s.at(j) == '0')
                        counter++;
                }
                break;
            }
            else
            {
                if (s.at(r) != '1')
                {
                    r--;
                }
                if (s.at(l) != '1')
                {
                    l++;
                }
            }
        }
        cout << counter << endl;
    }
}