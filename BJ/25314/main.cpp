#include <iostream>

using namespace std;

int main(int argc, char** argv){
    int N;
    cin >> N;

    N /= 4;

    for(int i = 0; i < N; i++){
        cout << "long ";
    }
    cout << "int";
}