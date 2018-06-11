#include<iostream>
#include<unistd.h>
#include <cstdlib>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
int main(int argc, char** argv)
{
	std::string current = getcwd(NULL,0);
	std::string params = "python3 ";
	try
	{
		std::string main = argv[1];
		std::string params = "python3 "+current+"/bot.py ";
		if(main == "--setup")
		{
			params = "python3 "+current+"/setup.py ";
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
		std::string curstr = "python3 "+current+"/bot.py";
		system(curstr.c_str());
	}
}
