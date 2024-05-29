from solana.rpc.api import Client
import solana

# Initialize Solana Client
solana_client = Client("https://api.mainnet-beta.solana.com")

def get_transaction_history(wallet_address):
    public_key = solana.rpc.types.Pubkey.from_string(wallet_address)
    transactions = solana_client.get_confirmed_signature_for_address2(public_key, limit=1000)
    return transactions['result']

def get_token_balances(wallet_address):
    public_key = solana.rpc.types.Pubkey.from_string(wallet_address)
    token_accounts = solana_client.get_token_accounts_by_owner(public_key, {"encoding": "jsonParsed"})
    total_balance = 0
    for account in token_accounts['result']['value']:
        if 'parsed' in account['account']['data']:
            amount = account['account']['data']['parsed']['info']['tokenAmount']['uiAmount']
            total_balance += amount
    return total_balance

def get_sol_balance(wallet_address):
    public_key = solana.rpc.types.Pubkey.from_string(wallet_address)
    balance = solana_client.get_balance(public_key)
    return balance['result']['value'] / 1e9  # Convert lamports to SOL

def get_smart_contract_interactions(wallet_address):
    public_key = solana.rpc.types.Pubkey.from_string(wallet_address)
    transactions = get_transaction_history(wallet_address)
    interactions = []

    # Example criteria for smart contract interaction
    for tx in transactions:
        details = solana_client.get_confirmed_transaction(tx['signature'])
        if details['result'] is not None:
            for instruction in details['result']['transaction']['message']['instructions']:
                if instruction['programIdIndex'] != 1:  # Assuming non-native programs indicate smart contracts
                    interactions.append(instruction)
    
    return interactions

def get_staking_activities(wallet_address):
    public_key = solana.rpc.types.Pubkey.from_string(wallet_address)
    stake_program_id = solana.rpc.types.Pubkey.from_string("Stake11111111111111111111111111111111111111")
    stake_accounts = solana_client.get_token_accounts_by_owner(public_key, {'programId': str(stake_program_id)})
    staking_activities = []

    for account in stake_accounts['result']['value']:
        staking_activities.append(account['account']['data']['parsed']['info'])

    return staking_activities

def aggregate_wallets(wallet_addresses):
    aggregated_data = {
        'transaction_history': [],
        'total_token_balance': 0,
        'sol_balance': 0,
        'smart_contract_interactions': [],
        'staking_activities': []
    }
    for address in wallet_addresses:
        aggregated_data['transaction_history'].extend(get_transaction_history(address))
        aggregated_data['total_token_balance'] += get_token_balances(address)
        aggregated_data['sol_balance'] += get_sol_balance(address)
        aggregated_data['smart_contract_interactions'].extend(get_smart_contract_interactions(address))
        aggregated_data['staking_activities'].extend(get_staking_activities(address))
    
    return aggregated_data
