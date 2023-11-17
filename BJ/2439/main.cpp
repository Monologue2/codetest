#include <iostream>
#include <iomanip> // Input Output Manipulator

using namespace std;

// output format
// std::left, std::right, std::internal

int main(int argc, char* argv[]){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;

    for(int i = 1; i <= N; i++){
        string output(i, '*');
        cout << std::setw(N) << output << '\n';
    }
}