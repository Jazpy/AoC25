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

long solve(vector<string> &lines, size_t d)
{
    long ret = 0;

    for (auto &e : lines) {
        string composed = "";
        size_t look_pos = 0;
        for (size_t curr_d = 0; curr_d != d; ++curr_d) {
            char m = '0';
            for (size_t i = look_pos; i != e.length() - ((d - curr_d) - 1); ++i) {
                if (e[i] > m) {
                    m = e[i];
                    look_pos = i + 1;
                }
            }

            composed += string(1, m);
        }

        ret += std::stol(composed);
    }

    return ret;
}

int main()
{
    vector<string> lines;
    get_lines(lines, "inputs/03.txt");

    long silver = solve(lines, 2);
    long gold   = solve(lines, 12);

    cout << silver << "\n";
    cout << gold   << "\n";

    return 0;
}
