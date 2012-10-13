#!/usr/bin/python
# vim: ts=2 sts=2 sw=2 et
import random

operators = [
    #(14, "!{}", lambda x: not x),
    #(14, "~{}", lambda x: ~x),
    #(14, "+{}", lambda x: x),
    #(14, "-{}", lambda x: -x),
    (13, "{} * {}",  lambda x, y: x * y),
    (13, "{} / {}",  lambda x, y: x / y),
    (13, "{} % {}",  lambda x, y: x % y),
    (12, "{} + {}",  lambda x, y: x + y),
    (12, "{} - {}",  lambda x, y: x - y),
    (11, "{} << {}", lambda x, y: x << y),
    (11, "{} >> {}", lambda x, y: x >> y),
    (10, "{} < {}",  lambda x, y: x < y),
    (10, "{} <= {}", lambda x, y: x <= y),
    (10, "{} > {}",  lambda x, y: x > y),
    (10, "{} >= {}", lambda x, y: x >= y),
    ( 9, "{} == {}", lambda x, y: x == y),
    ( 9, "{} != {}", lambda x, y: x != y),
    ( 8, "{} & {}",  lambda x, y: x & y),
    ( 7, "{} ^ {}",  lambda x, y: x ^ y),
    ( 6, "{} | {}",  lambda x, y: x | y),
    ( 5, "{} && {}", lambda x, y: bool(x and y)),
    ( 4, "{} || {}", lambda x, y: bool(x or y)),
    ( 1, "{} , {}",  lambda x, y: y),
    ]

random.seed()

x = [2, 3, 5]

while True:
  random.shuffle(x)
  (p1, s1, f1) = random.choice(operators)
  (p2, s2, f2) = random.choice(operators)

  try:
    if p2 > p1:
      ans = f1(x[0], f2(x[1], x[2]))
    else:
      ans = f2(f1(x[0], x[1]), x[2])
  except ZeroDivisionError, ValueError:
    continue

  s = s1.format(x[0], s2.format(x[1], x[2]))
  print
  print s

  user_ans = float("inf")
  try:
    while user_ans != ans:
      user_ans = raw_input("=> ")
      if user_ans[0] == "?":
        print int(ans)
        break
      try:
        user_ans = int(user_ans)
      except ValueError:
        user_ans = float("inf")
  except EOFError:
    break




