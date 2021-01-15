euler1 limit factor1 factor2 = sum[x | x <- [1..limit - 1], x `mod` factor1 == 0 || x `mod` factor2 == 0]

answer1 = euler1 1000 3 5

main = print answer1
