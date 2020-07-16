def CoinTracker(arr): 
  
  max_profit = -1
  buy_price = 0
  sell_price = 0
  
  # this allows our loop to keep iterating the buying
  # price until a cheap coin price is found
  change_buy_index = True
  
  # loop through list of coin prices once
  for i in range(0, len(arr)-1):
    
    # selling price is the next element in list
    sell_price = arr[i+1]
    
    # if we have not found a suitable cheap buying price yet
    # we set the buying price equal to the current element
    if change_buy_index: 
      buy_price = arr[i]
    
    # if the selling price is less than the buying price
    # we know we cannot make a profit so we continue to the 
    # next element in the list which will be the new buying price
    if sell_price < buy_price:
      change_buy_index = True 
      continue
    
    # if the selling price is greater than the buying price
    # we check to see if these two indices give us a better 
    # profit then what we currently have
    else:
      temp_profit = sell_price - buy_price
      if temp_profit > max_profit:
        max_profit = temp_profit
      change_buy_index = False
      
  return max_profit

print CoinTracker([44, 30, 24, 32, 35, 30, 40, 38, 15])