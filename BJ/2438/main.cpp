#include <iostream>

using namespace std;

int main(int argv, char* argc[]){
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++){
        // Perfectly elegant 
        string output(i, '*');
        cout << output << endl;
    }
}