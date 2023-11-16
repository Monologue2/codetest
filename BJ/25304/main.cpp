#include <iostream>

using namespace std;

int main(int argc, char** argv){
    int bill, N;
    int price = 0;

    cin >> bill >> N;
    for(int i = 0; i < N; i++){
        int tmp, amount;
        cin >> tmp >> amount;
        price += tmp * amount;
    }

    if (price != bill){
        cout << "No" << endl;
    }else{
        cout << "Yes" << endl;
    }
}