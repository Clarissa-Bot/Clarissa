#include<iostream>
#include <cstdlib>
using namespace std;
int main(int argc, char** argv)
{
	std::string params = "py -3 ";
	try
	{
		std::string main = argv[1];
		std::string params = "py -3 bot.py ";
		if(main == "--setup")
		{
			params = "py -3 setup.py ";
			for(int i = 2; i < argc; i++)
			{
				params = params + argv[i] + " ";
			}
		}else
		{
			for(int i = 1; i < argc; i++)
			{
				params = params + argv[i] + " ";
			}
		}
		system(params.c_str());
	}catch(std::logic_error)
	{
		system("py -3 bot.py");
	}
}