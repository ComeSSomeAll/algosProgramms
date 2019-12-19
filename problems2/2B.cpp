#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Person
{
	string country, name;
	int place;
};

void StableQuickSort(vector<Person> &p, int l, int r)
{
	int i = l, j = r, e = p[(l + r) / 2].place;
	string m = p[(l + r) / 2].country;
	while (i <= j)
	{
		while (p[i].country < m || p[i].country == m && p[i].place < e) i++;
		while (p[j].country > m || p[j].country == m && p[j].place > e) j--;
		if (i <= j)
			swap(p[i++], p[j--]);
	}
	if (l < j) StableQuickSort(p, l, j);
	if (i < r) StableQuickSort(p, i, r);
}

int main()
{
	ifstream fin("race.in");
	ofstream fout("race.out");
	int n;
	fin >> n;
	vector<Person> p;
	p.resize(n);
	for (int i = 0; i < n; i++)
	{
		fin >> p[i].country >> p[i].name;
		p[i].place = i + 1;
	}
	StableQuickSort(p, 0, n - 1);
	string curCountry = "";
	for (int i = 0; i < n; i++)
	{
		if (p[i].country != curCountry)
		{
			curCountry = p[i].country;
			fout << "=== " << curCountry << " ===" << endl;
		}
		fout << p[i].name << endl;
	}
	return 0;
}