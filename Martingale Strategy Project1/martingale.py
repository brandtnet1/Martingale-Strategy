# The Martingale Project
# CMS 430 Spring 2017
# Brandt Smith

# Simulate flipping coins and counting the number of heads

# Import matplotlib and set it up --- always do this first
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

from random import random

def run_sim(n_flips):
    
    """Simulate 100 coin flips and report the net outcome of earnings"""

    current_money = 255 # Initialized to Starting money of $255
    current_bet = 1     # Initialized to Minimum Bet
    net_outcome = 0     # Start out even net outcome
    
    for trial in range(n_flips):
        rand = random()             # Generate a random number
        if current_money != 0:      # If you still have money you can still bet
            if current_money - current_bet >= 0:     # Player will still have money win or lose
                current_money -= current_bet         # Player makes their bet and its subtracted from their money
                if rand > .5:       # If the random number is greater than .5
                    net_outcome += current_bet       # Add winnings to net outcome
                    current_money += current_bet * 2 # Add winnings plus previous money back into players money
                    current_bet = 1 # Player won so reset bet to minimum                
                else:               # If the random number is less than or equal to .5
                    net_outcome -= current_bet       # Player lost, subtract current bet from net_outcome
                    current_bet = current_bet * 2   # Double Players current bet
            elif current_money - current_bet < 0:    # Player doesn't have enough money to continue martingale if they lose
                current_bet = current_money         # Current bet is lowered to players total amount of money
                current_money = 0
                if rand > .5:       # If the random number is greater than .5
                    net_outcome += current_bet       # Add winnings to net outcome
                    current_money += current_bet * 2 # Add winnings plus previous money back into players money
                    current_bet = 1 #                 
                else:               # If the random number is less than or equal to .5
                    net_outcome -= current_bet       # Player lost, subtract current bet from net_outcome
    
    return net_outcome              # Return amount of money the player won/lost
    
def main():
    
    """Run 1 millions simulations and plot the historgram of results"""
    
    sim_head_counts = []
    
    for sim in range(1000000):
        sim_head_counts.append(run_sim(100))
        
    figure = plt.figure()
    plt.hist(sim_head_counts, 1000)
    plt.title('Distribution of net outcomes in 100 coin flips')
    plt.xlabel('Amount won')
    plt.ylabel('Number of occurances')
    plt.axis([-300, 400, 0, 150000])
    figure.savefig('net_outcome_in_100_coin_flips.pdf')
    
# If this script is being run directly, call the main function
# This set-up is common in modules that are intended to be loaded by
# another script - running the module directly might trigger tests

if __name__=='__main__':
    main()