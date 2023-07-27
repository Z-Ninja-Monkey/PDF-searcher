#include <string>

extern "C" __declspec(dllexport) void searchFolder(char* folderLocation, char* searchKeywords){
    // do stuff
}

extern "C" __declspec(dllexport) int getProgress(){
    return 5;
}
