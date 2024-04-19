def MassVote(N, Votes):
    total_votes = sum(Votes)
    max_votes = max(Votes)
    max_idx = Votes.index(max_votes) + 1

    if max_votes / total_votes > 0.5:
        return f"majority winner {max_idx}"
    elif Votes.count(max_votes) == 1:
        return f"minority winner {max_idx}"
    else:
        return "no winner"

