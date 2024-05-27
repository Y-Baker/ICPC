#include <iostream>
#include <deque>

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
        long long n, k, x;
        cin >> n >> k >> x;
        long long nn = n * (n + 1) / 2;
        long long lowerK = k * (k + 1) / 2;
        long long upperk = nn - (n - k) * (n - k + 1) / 2;
        if (x >= lowerK && x <= upperk)
        {
            cout << "YES\n";
        }
        else
            cout << "NO\n";
    }
}
