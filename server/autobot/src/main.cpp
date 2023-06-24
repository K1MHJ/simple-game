#include <dlfcn.h>
#include <iostream>
#include "libStat.h"

int callDyn();

int main()
{
  int a;
  try {
    a = callDyn();
    std::cout << "a = " << a << std::endl;
  } catch (...) {
    std::cout << "Exception : callDyn()\n"; 
  }
  return 0;
}

int callDyn()
{
  char dynlib_path[256];
  strcpy(dynlib_path,DYNLIB_DIR);
  strcat(dynlib_path,"/libDyn.so");
  void* handle = dlopen(dynlib_path, RTLD_LAZY);
  typedef int (*add_t)(int, int);
  add_t add = (add_t) dlsym(handle, "Add");
  int rst = add(12,33);
  dlclose(handle);
  return rst;
}
