#include <iostream>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();
    int t;
    cin>>t;
    int n;
    string s;
    while(t--)
    {
        cin>>n;
        cin>>s;
        for (int i=0; i<s.size(); i++)
        {
            if (s.at(i)=='U')
            {
                s.at(i)='D';
            }
            else if (s.at(i)=='D')
            {
                s.at(i)='U';
            }
        }
        cout <<s<<endl;
    }
}
