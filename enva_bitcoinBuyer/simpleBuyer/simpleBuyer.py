#v1
  def get_max_profit(coin_prices):
    max_profit = 0

    # Go through every time
    for outer_time in range(len(coin_prices)):

        # For every time, go through every other time
        for inner_time in range(len(coin_prices)):
            # For each pair, find the earlier and later times
            earlier_time = min(outer_time, inner_time)
            later_time   = max(outer_time, inner_time)

            # And use those to find the earlier and later prices
            earlier_price = coin_prices[earlier_time]
            later_price   = coin_prices[later_time]

            # See what  profit would be if bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

#2
  def get_max_profit(coin_prices):
    max_profit = 0

    # Go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(coin_prices):

        # And go through all the LATER prices
        for later_time in range(earlier_time + 1, len(coin_prices)):
            later_price = coin_prices[later_time]

            # See what  profit would be if bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

#v3
  def get_max_profit(coin_prices):
    min_price  = coin_prices[0]
    max_profit = 0

    for current_price in coin_prices:
        # Ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # See what  profit would be if bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit

#v4 --best to reflect negative profits!
def get_max_profit(coin_prices):
    if len(coin_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # Greedily update min_price and max_profit, so initialize
    # them to the first price and the first possible profit
    min_price  = coin_prices[0]
    max_profit = coin_prices[1] - coin_prices[0]

    # Start at the second (index 1) time
    #  can't sell at the first time, since must buy first,
    # and can't buy and sell at the same time!
    # If started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(coin_prices)):
        current_price = coin_prices[current_time]

        # See what  profit would be if bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit