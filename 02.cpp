#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
#include <cmath>
#include <unordered_set>
#include <boost/algorithm/string.hpp>

using std::cout;
using std::vector;
using std::string;
using std::pair;
using std::unordered_set;

void get_lines(vector<string> &lines, string filename)
{
    string         line;
    std::ifstream  f(filename);

    while (std::getline(f, line))
        if (line.size() > 0)
            lines.push_back(line);
}

long num_digits(long n)
{
    long ret = 0;
    while (n) {
        n /= 10;
        ++ret;
    }

    return ret;
}

long solve_silver(long start, long end)
{
    long ret = 0;
    long start_digits = num_digits(start);
    long end_digits = num_digits(end);

    vector<long> valid_digits;
    for (long s = start_digits; s <= end_digits; ++s) {
        if (s % 2 == 0)
            valid_digits.push_back(s);
    }

    if (!valid_digits.size())
        return 0;

    for (auto &e : valid_digits) {
        long hd = e / 2;
        long lo = pow(10, hd - 1);
        long hi = pow(10, hd) - 1;

        for (long repeat = lo; repeat <= hi; ++repeat) {
            long id = repeat * long(pow(10, hd)) + repeat;

            if (id > end)
                break;

            if (id > start)
                ret += id;
        }
    }

    return ret;
}

vector<pair<long, long>> get_mult_pairs(long d) {
    vector<pair<long, long>> ret;
    ret.push_back(std::make_pair(1, d));

    for (long f = 2; f <= d / 2; ++f) {
        for (long s = 2; s <= d / 2; ++s) {
            if (f * s == d)
                ret.push_back(std::make_pair(f, s));
        }
    }

    return ret;
}

long solve_gold(long start, long end)
{
    long ret = 0;
    unordered_set<long> counted;

    for (long d = num_digits(start); d <= num_digits(end); ++d) {
        if (d == 1)
            continue;

        auto pairs = get_mult_pairs(d);

        for (auto &e : pairs) {
            long lo = pow(10, e.first - 1);
            long hi = pow(10, e.first) - 1;

            for (long repeat = lo; repeat <= hi; ++repeat) {
                long id = repeat;
                for (long i = 1; i != e.second; ++i) {
                    id *= long(pow(10, e.first));
                    id += repeat;
                }

                if (id > end)
                    break;

                if (id >= start && counted.find(id) == counted.end()) {
                    ret += id;
                    counted.insert(id);
                }
            }
        }
    }

    return ret;
}

int main()
{
    vector<string> lines;
    vector<string> toks;
    get_lines(lines, "inputs/02.txt");
    boost::split(toks, lines[0], boost::is_any_of("-,"), boost::token_compress_on);

    long silver = 0;
    long gold   = 0;

    for (size_t i = 0; i != toks.size(); i += 2) {
        long start = std::stol(toks[i]);
        long end = std::stol(toks[i + 1]);

        silver += solve_silver(start, end);
        gold += solve_gold(start, end);
    }

    cout << silver << "\n" << gold << "\n";

    return 0;
}
