#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int NOI = 0;
    long long savings = 0;
    cin >> NOI;
    vector<int> prices;
    int price;
    while (cin >> price) {
        prices.push_back(price);
    }

    sort(prices.begin(), prices.end(), greater<>());

    for (int i = 2; i < prices.size(); i += 3) {
        if (i % 3 == 2)
            savings += prices[i];
    }

    cout << savings << endl;
}
