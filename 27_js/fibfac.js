// Team ApesTogetherStrong :: Joshua Kloepfer, Yaying Liang Li
// SoftDev pd1
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------

function fact(n) { //1, 1, 2, 6, 24, 120
  if (n <= 1) {
    return 1;
  }
  else {
    return n * fact(n-1);
  }
}

function fib(n) { //0, 1, 1, 2, 3, 5, 8
  if (n==0) {
    return 0;
  }
  else if (n <= 2) {
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
}
