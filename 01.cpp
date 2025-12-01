#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <regex>
#include <ctype.h>
#include <cmath>

using std::cout;
using std::vector;
using std::string;
using std::map;

void get_lines(vector<string> &lines, string filename)
{
  string         line;
  std::ifstream  f(filename);

  while (std::getline(f, line))
    if (line.size() > 0)
      lines.push_back(line);
}

int mod(int a) {
    int r = a % 100;
    return (r < 0) ? r + 100 : r;
}

int main()
{
  vector<string> lines;
  get_lines(lines, "inputs/01.txt");

  long real_pos = 50;
  long silver = 0;
  long gold   = 0;
  for (auto &e : lines) {
    int prev_dial = mod(real_pos);
    long movement = e[0] == 'R' ? std::stoi(e.substr(1)) : -std::stoi(e.substr(1));

    real_pos += movement;
    int dial_pos = mod(real_pos);

    gold += abs(movement) / 100;
    if (dial_pos != 0 && prev_dial != 0) {
      if (movement < 0 && dial_pos > prev_dial)
        gold += 1;
      if (movement > 0 && dial_pos < prev_dial)
        gold += 1;
    }

    if (prev_dial != 0 && dial_pos == 0)
      gold += 1;

    if (dial_pos == 0)
      silver += 1;

  }

  cout << silver << "\n";
  cout << gold   << "\n";

  return 0;
}
