def calculate_solid_score(transaction_history, total_token_balance, sol_balance, smart_contract_interactions, staking_activities):
    # Adjust weights to ensure the score is on a scale of 1-100
    score = 0
    score += len(transaction_history) * 0.05
    score += total_token_balance * 0.1
    score += sol_balance * 0.2
    score += len(smart_contract_interactions) * 0.3
    score += len(staking_activities) * 0.35

    # Ensure the score is within the 1-100 range
    return min(max(score, 1), 100)
