#include <iostream>;

using namespace std;

int main(void) {
	/* 1st algorithm */
	int ans[128];
	int n, n4, count;
	count = 0;
	cout << "enter: ";
	cin >> n;
	double sum = 0;
	double sumd = 0;

	for (int i = 0; i < 128; i++) {
		n *= n;
		
		n4 = n / 100 % 10000;
		ans[i] = n4;
		n = n4;
	}
	for (int i = 0; i < 128; i++) {

		cout << (double)ans[i]/10000 << endl;
		sum += (double)ans[i] / 10000;
		count++;	
	}

	for (int i = 0; i < 128; i++) {
		sumd += (double)((double)ans[i] / 10000 - (double)sum / count) * ((double)ans[i] / 10000 - (double)sum / count)  / count;
	}
	cout << "amount: " << count << endl;
	cout <<"mr: " << (double)sum / count << endl;
	cout << "dr: " << sumd << endl;
	cout << "sigma: " << sqrt(sumd) << endl;

	/* 2nd algorithm */

	int n1, n2, n3;
	int ans2[128];
	int count2 = 0;
	n1 = ans[126];
	n2 = ans[127];
	cout << "using last 2 elements for start of 2nd algorythm: " << n1 << " " << n2 << endl;
	double sum2 = 0;
	double sumd2 = 0;

	for (int i = 0; i < 128; i++) {
		n3 = n1 * n2;
		//n3 = n3 / 100 % 10000;
		if (n3 / 1000000 == 0) { //if number is 6 digits length - take middle part (374748 - > 7474) 
								 //if number is 5 ligits length - take left side (37474 -> 3747)
			n3 = n3 / 10 % 10000;
			ans2[i] = n3;
			n1 = n2;
			n2 = n3;
		}
		else {
			n3 = n3 / 100 % 10000;
			ans2[i] = n3;
			n1 = n2;
			n2 = n3;
		}
	}

	for (int i = 0; i < 128; i++) {
		
			cout << (double)ans2[i]/10000 << endl;
			sum2 += (double)ans2[i] / 10000;
			count2++;
	}

	for (int i = 0; i < 128; i++) {
		sumd2 += (double)((double)ans2[i] / 10000 - (double)sum2 / count2) * ((double)ans2[i] / 10000 - (double)sum2 / count2)  / count2;
	}

	cout << "amount: " << count2 << endl;
	cout <<"mr: " << (double)sum2 / count2 << endl;
	cout << "dr: " << sumd2 << endl;
	cout << "sigma: " << sqrt(sumd2) << endl;

	return 0;
}

