#include <iostream>
#include <fstream>
#include <cstdlib>

int main(){

    std::string driver_name = "drivers/edgedriver_linux64/msedgedriver";
    std::ifstream driver(driver_name);
    
    
    if(driver.is_open()){
        std::cout << "Found driver\n";
        system(driver_name.c_str());
    }else{
        std::cout << "Could not find Edge driver, please place on in `./drivers/edgedriver...`\n";
        return 1;
    }
    return 0;
} 
