#include <iostream>
#include <fstream>
#include <string>
#include <range/v3/all.hpp>
using namespace std;

string * get_file(string fname) {
  ifstream file (fname);
  static string line;
  getline(file, line);
  return & line;
}

void parse_file(string * crypt) {
  auto split = crypt
      | std::ranges::views::split(',');
      | std::ranges::views::transform([](auto&& str) {
      return std::string_view(&*str.begin(),str::ranges::distance(str));
      });
  cout << * crypt;
}

/*
void parse_file(string crypt) {

  std::string delimiter = ",";
  for (int i=0; i<=crypt.length(); i++){
    std::string token = crypt.substr(0, crypt.find(delimiter));
    cout << token;
  }
}
*/

int main() {
  string * crypt = get_file("/Users/dude/fun/project_euler/data/p059_cipher.txt");
  cout << * crypt;
  parse_file(* crypt);
  return 0;
}
