#include<iostream>
#include <cstdlib>
using namespace std;
int main(int argc, char** argv)
{
	std::string params = "python ";
	try
	{
		std::string main = argv[1];
		std::string params = "python bot.py ";
		if(main == "--setup")
		{
			params = "python setup.py ";
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
		system("python bot.py");
	}
}