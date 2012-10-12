#!/usr/bin/python
import random

operators = [
		#(14, "!{}", lambda x: not x),
		#(14, "~{}", lambda x: ~x),
		#(14, "+{}", lambda x: x),
		#(14, "-{}", lambda x: -x),
		(13, "{} * {}", lambda x, y: x * y),
		(13, "{} / {}", lambda x, y: x / y),
		(13, "{} % {}", lambda x, y: x % y),
		(12, "{} + {}", lambda x, y: x + y),
		(12, "{} - {}", lambda x, y: x - y)
		]

random.seed()

x = [2, 3, 5]
random.shuffle(x)

(p1, s1, f1) = random.choice(operators)
(p2, s2, f2) = random.choice(operators)

s = s1.format(x[0], s2.format(x[1], x[2]))
print s

ans1 = f2(f1(x[0], x[1]), x[2])
ans2 = f1(x[0], f2(x[1], x[2]))

print ans1
print ans2



