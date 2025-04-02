2

# Step 1: Precompute probability distribution for sums (2-12)
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

# Dictionary to store sum probabilities
probability_dict = {}
for i in range(2, 13):  # Possible sums from 2 to 12
    c = 0
    for j in [(d1, d2) for d1 in dice1 for d2 in dice2]:
        if i == sum(j):
            c += 1
    probability_dict[i] = c / 36  # Since there are 36 possible outcomes

# Step 2: Read input
R = int(input())  # Number of rounds
player1_wins = 0
player2_wins = 0

def get_probability(sum_value):
    return probability_dict[sum_value]

# Step 3: Process each round
for _ in range(R):
    P1_d1, P1_d2, P2_d1, P2_d2 = map(int, input().split())
    
    P1_sum = P1_d1 + P1_d2
    P2_sum = P2_d1 + P2_d2
    
    P1_prob = get_probability(P1_sum)
    P2_prob = get_probability(P2_sum)
    
    # The player with the less probable sum wins the round
    if P1_prob < P2_prob:
        player1_wins += 1
    elif P2_prob < P1_prob:
        player2_wins += 1

# Step 4: Determine the overall winner
if player1_wins > player2_wins:
    print("Player 1 wins")
elif player2_wins > player1_wins:
    print("Player 2 wins")
else:
    print("It's a draw")