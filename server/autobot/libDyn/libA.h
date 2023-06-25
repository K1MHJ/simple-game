#ifdef __cplusplus
extern "C" {
#endif

typedef struct{
  int coin1_cnt;
  int coin5_cnt;
  int coin10_cnt;
  int coin50_cnt;
  int coin100_cnt;
  int coin500_cnt;
}CoinBag;

int Add(int a, int b);
int Sub(int a, int b);
int Test(unsigned int _size, int map[]);
int Play(int map[], unsigned int row, unsigned int col, CoinBag bag, unsigned int *x, unsigned int *y, int *coin);

#ifdef __cplusplus
}
#endif
