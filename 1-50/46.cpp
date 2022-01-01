#include <iostream>
#include <cmath>
using namespace std;

bool isprime(int n) {
	if (n <= 1) return 0;
	for (int j = 2; j <= int(sqrt(n) + 1); j++){
		if (n % j == 0) return 0;
	}
	return 1;
};

int falseConj(int lim){
	
	int i,pc[1500],j,z;
	double x;

	for (i = 3,j = 0;i < lim; i +=2) {
		if (isprime(i)) 
			pc[j++] = i;

		else

			for (z = 0; z < j ; z++) {
				x = sqrt((i - pc[z]) / 2);
				if (x - (int) x < 0.00001)
					break;
			}
  
		if (z == j) break;
	}
	return i;
}

int main() {
	int r = falseConj(pow(10, 4));
	printf("%d\n", r);
}
