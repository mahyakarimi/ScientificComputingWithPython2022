def dec2bin(num): return bin(num)

def dec2hex(num): return hex(num)

def bin2dec(binary):
  binary = list(binary[2:])#eliminate 0b from the begining
  SUM = 0
  for (idx, s) in enumerate(binary):
    power = len(binary) - idx - 1
    SUM += int(s) * (2 ** power)
  return SUM

def hex2dec(heximal):
  hex_con = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
  heximal = list(heximal[2:])#eliminate 0x from the begining
  SUM = 0
  for (idx, s) in enumerate(heximal):
    power = len(heximal) - idx - 1
    try:
      s = int(s)
    except:
      s = hex_con[s]
    SUM += s * (16 ** power)
  return SUM

def hex2bin(heximal):
  return dec2bin(hex2dec(heximal))

def bin2hex(binary):
  return dec2hex(bin2dec(binary))


def conversion(inp, inp_type, out_type):

  if   (inp_type, out_type) == ("dec", "bin"): return dec2bin(inp)
  elif (inp_type, out_type) == ("bin", "dec"): return bin2dec(inp)
  elif (inp_type, out_type) == ("dec", "hex"): return dec2hex(inp)
  elif (inp_type, out_type) == ("hex", "dec"): return hex2dec(inp)
  elif (inp_type, out_type) == ("hex", "bin"): return hex2bin(inp)
  elif (inp_type, out_type) == ("bin", "hex"): return bin2hex(inp)

print(conversion(982, "dec","bin"))

print(conversion("0b1111010110", "bin","dec"))

print(conversion(982, "dec","hex"))

print(conversion("0x3d6", "hex","dec"))

print(conversion("0x3d6", "hex","bin"))

print(conversion("0b1111010110", "bin","hex"))