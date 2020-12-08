import random

greeting = input("Hello, do you want to enter a quote ? (Print 'Yes' or 'No') ")

if greeting == 'Yes':
  num_of_quotes = int(input("How many quotes do you want to append: "))
  def enter_quote():
    f = open("quotes.txt", "a")
    for quote in range(num_of_quotes):
      new_quote = input("Enter new quote: ")
      f.write(new_quote + "\n")  
    f.close()
  if __name__ == "__main__":
    enter_quote()
elif greeting == 'No':
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
else:
  print("Please enter only 'Yes' or 'No'")    