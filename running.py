def best_profit(mylist):
  b=max(mylist)
  return b


print ("Give your input")
a = [int(x) for x in input().split(',')]
print ("The maximum Profit =",best_profit(a))