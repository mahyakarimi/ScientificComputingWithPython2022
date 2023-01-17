def single_pre_float(bin_str, bias=127):
  sign = int(bin_str[0])
  exponent = list(map(lambda x: int(x), bin_str[1:9]))
  mantissa = list(map(lambda x:int(x), bin_str[9:]))

  EX_SUM = 0
  for idx in range(len(exponent)):
    ex = exponent[idx]
    power = len(exponent) - idx - 1
    EX_SUM += ex * (2 ** power)

  MAN_SUM = 0
  for idx in range(len(mantissa)):
    man = mantissa[idx]
    power = -idx - 1
    MAN_SUM += man * (2 ** power)
  
  return ((-1) ** sign) * (1 + MAN_SUM) * (2 ** (EX_SUM-bias))

print(single_pre_float("00000011111000000000000000000000"))#image1 in the lecture
print(single_pre_float("11000000101100000000000000000000"))#image2 in the lecture