#include "../libA.h"
#include <iostream>


int Add(int a, int b)
{
  return a+b;
}

int Sub(int a, int b)
{
  return a-b;
}

int Test(unsigned int _size, int map[])
{
  std::cout << _size << "d" << map[0] << std::endl;
  return _size;
}

int Play(int map[], unsigned int row, unsigned int col, CoinBag bag, unsigned int *x, unsigned int *y, int *coin)
{
  std::cout << row << "x" << col << std::endl;
  std::cout << bag.coin1_cnt << std::endl;

  for(int j = 0;j<row;j++){
      std::cout << "{";
    for(int i = 0;i<col;i++){
      if(i != 0){
        std::cout << ",\t";
      }
      std::cout << map[j * col + i];
    }
    std::cout << "}" << std::endl;
  }
  *x = 5;
  *y = 3;
  *coin = 50;
  return 1;
}
