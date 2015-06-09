__author__ = 'zehavitc'

def ngrams(input, n):
  input = input.split()
  output = []
  for i in range(len(input)-n+1):
    output.append(''.join(c for c in input[i:i+n]))
  return output


# n = ngrams("a b cd ef",1)
# print(n)