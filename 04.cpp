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
using std::pair;

void get_lines(vector<string> &lines, string filename)
{
    string         line;
    std::ifstream  f(filename);

    while (std::getline(f, line))
        if (line.size() > 0)
            lines.push_back(line);
}

vector<pair<long, long>> get_neighbors(size_t w, size_t h, pair<long, long> c)
{
    vector<pair<long, long>> ret;

    for (int i = -1; i <= 1; ++i) {
        for (int j = -1; j <= 1; ++j) {
            auto new_x = c.first + i;
            auto new_y = c.second + j;
            if ((i == 0 && j == 0) || new_x < 0 || new_x >= w || new_y < 0 || new_y >= h)
                continue;

            ret.push_back(std::make_pair(new_x, new_y));
        }
    }

    return ret;
}

void solve(vector<string> &lines, long &silver, long &gold)
{
    long ret = 0;
    size_t w = lines[0].size();
    size_t h = lines.size();

    bool fstep = true;

    while (true) {
        long removed = 0;
        for (size_t x = 0; x != w; ++x) {
            for (size_t y = 0; y != h; ++y) {
                if (lines[y][x] != '@')
                    continue;

                auto neighbors = get_neighbors(w, h, std::make_pair(x, y));
                size_t ctr = 0;
                for (auto &n : neighbors)
                    if (lines[n.second][n.first] == '@')
                        ++ctr;

                if (ctr < 4) {
                    lines[y][x] = '.';
                    ++removed;
                }
            }
        }

        if (fstep) {
            silver = removed;
            fstep = false;
        }

        if (removed == 0)
            break;

        gold += removed;
    }
}

int main()
{
    vector<string> lines;
    get_lines(lines, "inputs/04.txt");

    long silver = 0;
    long gold   = 0;

    solve(lines, silver, gold);

    cout << silver << "\n";
    cout << gold   << "\n";

    return 0;
}
