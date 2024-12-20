def nba_extrap(ppg, mpg):
    return round(ppg / mpg * 48, 1) if mpg > 0 else 0



print(nba_extrap(12, 20))       # 28.8
print(nba_extrap(10, 10))       # 48.0
print(nba_extrap(5, 17))        # 14.1
print(nba_extrap(0, 0))         # 0
print(nba_extrap(30.8, 34.7))   # 42.6)  # Russell Westbrook 1/15/17
print(nba_extrap(22.9, 33.8))   # 32.5)  # Kemba Walker 1/15/17