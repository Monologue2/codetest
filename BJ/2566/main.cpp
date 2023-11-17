#include <iostream>

using namespace std;

int main(int argc, char* argv[]){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int row, col;
    int max = 0;

    for(int i = 1; i <= 9; i++){
        for(int j = 1; j <= 9; j++){
            int N;
            cin >> N;
            if(N >= max){
                row = i;
                col = j;
                max = N;
            }
        }
    }

    cout << max << '\n' << row << ' ' << col << '\n';
}