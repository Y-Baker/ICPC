#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int main() {
    int t = 1;
    // cin >> t;

    for (int _ = 0; _ < t; ++_) {
        int n;
        cin >> n;
        vector<tuple<int, int, int>> listt(n);

        for (int i = 0; i < n; ++i) {
            int a, b;
            cin >> a >> b;
            listt[i] = make_tuple(a, b, i + 1);
        }

        sort(listt.begin(), listt.end(), [](const tuple<int, int, int>& x, const tuple<int, int, int>& y) {
            double ratio_x = get<0>(x) / static_cast<double>(get<1>(x) + get<0>(x));
            double ratio_y = get<0>(y) / static_cast<double>(get<1>(y) + get<0>(y));
            if (ratio_x == ratio_y) {
                return (get<0>(x) + get<1>(x)) < (get<0>(y) + get<1>(y));
            }
            return ratio_x > ratio_y;
        });

        for (const auto& item : listt) {
            cout << get<2>(item) << " ";
        }
        cout << endl;
    }

    return 0;
}
