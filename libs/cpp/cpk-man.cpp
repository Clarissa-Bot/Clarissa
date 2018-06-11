#include<iostream>
#include<unistd.h>
#include<cstdlib>
using namespace std;

void exec(char **argv, std::string sys, std::string second, int argc)
{
		std::string result = "";
		for(int i = 3; i < argc; i++)
		{
			result = result + " " + argv[i];
		}
		sys = sys + " " + result;
		system(sys.c_str());
}
void run(int argc, char** argv)
{
	std::string curdir = getcwd(NULL,0);
	std::string main = argv[1];
	if(main == "install")
	{
		std::string second = argv[2];
		std::string sys = "python3 "+curdir+"/bot.py --install-app ";
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
		std::string sys = "python3 "+curdir+"/bot.py --run-app ";
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
		std::string sys = "python3 "+curdir+"/bot.py --make-app ";
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
		std::string sys = "python3 "+curdir+"/bot.py --build-app ";
		sys = sys + second;
		sys = sys + " "+second;
		exec(argv, sys, second, argc);
	}else if(main == "update")
	{
		std::string second = argv[2];
		std::string sys = "python3 "+curdir+"/bot.py --build-app ";
		sys = sys + second;
		sys = sys + " "+second;
		exec(argv, sys, second, argc);
		second = argv[2];
		sys = "py -3 bot.py --install-app ";
		sys = sys + second;
		sys = sys + " "+second;
		exec(argv, sys, second, argc);
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
		cout << "\tupdate: Updates installed cpk" << endl;
		cout << "\t\tEx: cpk update [APP_NAME] [optional: --from-external]" <<endl;
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
		cout << "\tcompile: [FOR DEVELOPERS] Compiles Clarissa Application to .cpk" <<endl;
		cout << "\t\tEx: cpk compile [APP_NAME]" <<endl;
		cout << "\tinstall: Installs a Clarissa Package (.cpk) from a directory" <<endl;
		cout << "\t\tEx: cpk install [CPK_DIR]" << endl;
		cout << "\tmake: [FOR DEVELOPERS] builds a sample application" <<endl;
		cout << "\t\tEx: cpk make [APP_NAME]" << endl;
		cout << "\trun: Runs installed app" << endl;
		cout << "\t\tEx: cpk run [APP_NAME] [optional: --python]" <<endl;
		cout << "\tupdate: Updates installed cpk" << endl;
		cout << "\t\tEx: cpk update [APP_NAME] [optional: --from-external]" <<endl;
	}
	return 0;
}
