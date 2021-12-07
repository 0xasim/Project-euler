#include <iostream>
#include <cmath>
using namespace std;

unsigned int* x(int lim){
  unsigned int* pantagonals = new unsigned int[lim];
  //unsigned int pantagonals[lim];
  
  for(int n = 1; n < lim; n++){
    pantagonals[n] = n * (3 * n - 1) / 2;
  }
  return pantagonals;
}

// The segfault is intentional
int y(int lim) {

	unsigned int i,j, pc[lim];
	float rez,rez2;

	for (i = 1;;i++) {
		pc[i] = (i * ( 3 * i - 1)) / 2;

		for (j = 1 ; j < i ; j++) {
			rez = (sqrt(1 + 3 * 8 * (pc[i] + pc[j]) ) + 1) / 6;
			rez2 = (sqrt(1 + 3 * 8 * (pc[i] - pc[j]) ) + 1) / 6;

			if (rez - (int) rez < 0.00001 && rez2 - (int) rez2 < 0.00001) {
				printf("%d\n" , (int) pc[i] -   pc[j]);
			}
		}
	}
	return 0;
}

int main() {
  unsigned int *o;
  int lim = pow(10, 2);
  o = x(lim);
  for (int i=0; i<lim; i++){
      cout << o[i] << ", ";
  }
  delete[] o;
  y(lim);
}
