#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int deliver_mail(map<int, int> data, int car_cap) {
    int distance {0};
    for (auto iter = data.rbegin(); iter != data.rend();) {
        distance += 2*(iter->first);
        int& num_lets = iter->second;
        if (num_lets > car_cap) {
            num_lets -= car_cap;
            continue;
        }
        else if (num_lets < car_cap) {
            int let_left = car_cap - num_lets;
            num_lets = 0;
            ++iter;
            do {
                if (let_left >= iter->second) {
                    let_left -= iter->second;
                    iter->second = 0;
                    ++iter;
                }
                else if (let_left < iter->second) {
                    iter->second = iter->second - let_left;
                    let_left = 0;
                }
            }
            while (let_left > 0 && iter!= data.rend());
            continue;
        }
        else if (num_lets = car_cap) {
            num_lets = 0;
            ++iter;
            continue;
        }
    }
    return distance;
}

int main() {
    vector<int> allnums;
    map<int, int> neg_adds, pos_adds;

    int num_add, car_cap, num;

    cin >> num_add >> car_cap;

    while (cin >> num) {
        allnums.push_back(num);
    }

    for (int it = 0; it < allnums.size(); it += 2){
        if (allnums[it] > 0) {
            pos_adds.insert(pair<int, int>(allnums[it], allnums[it+1]));
        }
        else neg_adds.insert(pair<int, int>(-allnums[it], allnums[it+1]));
    }

    int total_distance = deliver_mail(neg_adds, car_cap) + deliver_mail(pos_adds, car_cap);

    cout << total_distance;
}