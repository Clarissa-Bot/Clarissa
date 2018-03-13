#include<iostream>
#include <cstdlib>
using namespace std;
void run(int argc, char** argv)
{
	std::string main = argv[1];
	if(main == "install")
	{
		std::string second = argv[2];
		std::string sys = "py -3 bot.py --install-app ";
		sys = sys + second;
		std::string result = "";
		for(int i = 3; i < argc; i++)
		{
			result = result + " " + argv[i];
		}
		sys = sys + " " + result;
		system(sys.c_str());
	}else if( main == "run" )
	{
		std::string second = argv[2];
		std::string sys = "py -3 bot.py --run-app ";
		sys = sys + second;
		std::string result = "";
		for(int i = 3; i < argc; i++)
		{
			result = result + " " + argv[i];
		}
		sys = sys + " " + result;
		system(sys.c_str());
	}else if( main == "make" )
	{
		std::string second = argv[2];
		std::string sys = "py -3 bot.py --make-app ";
		sys = sys + second;
		std::string result = "";
		for(int i = 3; i < argc; i++)
		{
			result = result + " " + argv[i];
		}
		sys = sys + " " + result;
		system(sys.c_str());
	}else if( main == "compile" or main == "build")
	{
		std::string second = argv[2];
		std::string sys = "py -3 bot.py --build-app ";
		sys = sys + second;
		sys = sys + " "+second;
		std::string result = "";
		for(int i = 3; i < argc; i++)
		{
			result = result + " " + argv[i];
		}
		sys = sys + " " + result;
		system(sys.c_str());
	}else
	{
		cout << "Clarissa Package Manager Help Menu:" <<endl;
		cout << "\tcompile: [FOR DEVELOPERS] Compiles Clarissa Application to .cpk" <<endl;
		cout << "\t\tEx: cpk compile [APP_NAME]" <<endl;
		cout << "\tinstall: Installs a Clarissa Package (.cpk) from a directory" <<endl;
		cout << "\t\tEx: cpk install [CPK_DIR]" << endl;
		cout << "\tmake: [FOR DEVELOPERS] builds a sample application" <<endl;
		cout << "\t\tEx: cpk make [APP_NAME]" << endl;
		cout << "\trun: Runs installed app" << endl;
		cout << "\t\tEx: cpk run [APP_NAME] [optional: --python]" <<endl;
	}
}
int main(int argc, char** argv)
{
	try
	{
		run(argc, argv);
	}catch( std::logic_error err)
	{
		cout << "Clarissa Package Manager Help Menu:" <<endl;
		cout << "\tinstall: Installs a Clarissa Package (.cpk) from a directory" <<endl;
		cout << "\t\tEx: cpk install [CPK_DIR]" << endl;
		cout << "\trun: Runs installed app" << endl;
		cout << "\t\tEx: cpk run [APP_NAME]" <<endl;
		cout << "\tmake: [FOR DEVELOPERS] builds a sample application" <<endl;
		cout << "\t\tEx: cpk make [APP_NAME]" << endl;
		cout << "\tcompile: [FOR DEVELOPERS] Compiles Clarissa Application to .cpk" <<endl;
		cout << "\t\tEx: cpk compile [APP_NAME]" <<endl;
	}
	return 0;
}