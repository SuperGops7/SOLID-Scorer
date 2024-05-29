from flask import Flask, request, jsonify
from data_extractor import get_transaction_history, get_token_balances, get_sol_balance, get_smart_contract_interactions, get_staking_activities, aggregate_wallets
from scoror import calculate_solid_score

app = Flask(__name__)

@app.route('/score/<wallet_address>', methods=['GET'])
def get_solid_score(wallet_address):
    transaction_history = get_transaction_history(wallet_address)
    total_token_balance = get_token_balances(wallet_address)
    sol_balance = get_sol_balance(wallet_address)
    smart_contract_interactions = get_smart_contract_interactions(wallet_address)
    staking_activities = get_staking_activities(wallet_address)
    solid_score = calculate_solid_score(transaction_history, total_token_balance, sol_balance, smart_contract_interactions, staking_activities)
    return jsonify({'wallet_address': wallet_address, 'solid_score': solid_score})

@app.route('/aggregate_score', methods=['POST'])
def get_aggregated_solid_score():
    wallet_addresses = request.json.get('wallet_addresses', [])
    aggregated_data = aggregate_wallets(wallet_addresses)
    aggregated_score = calculate_solid_score(
        aggregated_data['transaction_history'],
        aggregated_data['total_token_balance'],
        aggregated_data['sol_balance'],
        aggregated_data['smart_contract_interactions'],
        aggregated_data['staking_activities']
    )
    return jsonify({'wallet_addresses': wallet_addresses, 'aggregated_score': aggregated_score})

if __name__ == "__main__":
    app.run(debug=True)
