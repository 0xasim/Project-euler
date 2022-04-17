#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  string data;
  ifstream myfile ("/Users/dude/fun/project_euler/data/p059_cipher.txt");
  getline(myfile, data);
  myfile.close();
  cout << data;
  return 0;
}
