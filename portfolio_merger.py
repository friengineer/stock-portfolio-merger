import ast

# Takes input and converts it into a list of integers
portfolios = input()
portfolios = ast.literal_eval(portfolios)
# Current highest merged portfolio value
portfolioValue = 0
# Number of portfolio values given
length = len(portfolios)

# If one portfolio value has been given, assign it as the highest merged portfolio
# value
if length == 1:
    portfolioValue = portfolios[0]
else:
    # Iterates over every portfolio value and compares its bitwise XOR with all other
    # portfolio values with the current highest merged portfolio value
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            temporaryPortfolioValue = portfolios[i] ^ portfolios[j]

            if temporaryPortfolioValue > portfolioValue:
                portfolioValue = temporaryPortfolioValue

print(portfolioValue)
