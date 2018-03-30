#include <iostream>

int main(){
	int N=0;
	std::cin >> N;
	int num,score;
//	int result[N]=0;
	int *result = new int[N+2] ();
	for(int i=0;i<N;++i){
		std::cin >> num >> score;
		result[num] += score;
	}
	int max = -1,indx = 0;
	for(int i=0;i<N+2;++i){
		if( result[i]>=max){
			max = result[i];
			indx = i;
		}
	}
	std::cout<<indx<<" "<<max<<std::endl;
}

