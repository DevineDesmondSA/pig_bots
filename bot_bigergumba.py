def choice(round_score, my_score, opponent_score):
    if (my_score >= 71) or (opponent_score >= 71):
        return round_score >= (100 - my_score)
    else:
        return round_score >= (21 + (abs(my_score - opponent_score)/8)

# this bot's playstyle has a 0.9% disadvantage against optimal play (read the Wikipedia article on Pig)
