import random

def get_quote():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = quotes[random.randint(0, last)]
  rnd2 = quotes[random.randint(0, last)]
  rnd_items = [rnd, rnd2]

  for item in rnd_items:
    print(item, end='')

if __name__== "__main__":
  get_quote()
