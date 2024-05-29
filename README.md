# SOLID-Scorer

## Overview

The Solana ID On-Chain Scoring Module is a tool to analyze the on-chain footprint of Solana wallet accounts and derive a SOLID score indicating the level of credibility of the given account. The module consists of three main components:

1. **Data Collection**: Collects data from the Solana blockchain.
2. **Scoring**: Calculates the SOLID score based on the collected data.
3. **Flask APP**: Provides an API to access the SOLID score for individual or aggregated wallet accounts.

## Project Structure

- `scoror.py`: Contains the logic for calculating the SOLID score.
- `data_extractor.py`: Contains functions to collect data from the Solana blockchain.
- `app.py`: Contains the Flask API to get the SOLID score.

## Parameters and Weightage

The SOLID score is calculated based on various parameters with specific weightage assigned to each. Here are the details:

### Transaction History

The number of transactions made by the wallet. This indicates the activity level of the wallet.

- **Weightage**: 0.05 per transaction

### Total Token Balance

The total balance of all tokens held by the wallet. This shows the wealth or holding capacity of the wallet.

- **Weightage**: 0.1 per token unit

### SOL Balance

The balance of Solana (SOL) tokens in the wallet. Given a higher weight as it is the native token.

- **Weightage**: 0.2 per SOL unit

### Smart Contract Interactions

The number of interactions with smart contracts. This shows the engagement with dApps and DeFi.

- **Weightage**: 0.3 per interaction

### Staking Activities

The number of staking activities. This indicates the participation in securing the network.

- **Weightage**: 0.35 per staking activity

The final SOLID score is a sum of these weighted parameters.

## Setup

### Prerequisites

- Python 3.7 or higher
- Flask
- Solana Python SDK

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/<yourusername>/solana-id-scoring-module.git
   cd solana-id-scoring-module
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Flask API

1. Start the Flask API:

   ```sh
   python app.py
   ```

2. The API will be available at `http://127.0.0.1:5000`.

### API Endpoints

#### Get SOLID Score for a Single Wallet

- **Endpoint**: `/score/<wallet_address>`
- **Method**: `GET`
- **Description**: Retrieves the SOLID score for the specified wallet address.

Example:

```sh
GET /score/YourWalletAddressHere
```

#### Get Aggregated SOLID Score for Multiple Wallets

- **Endpoint**: `/aggregate_score`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Description**: Retrieves the aggregated SOLID score for multiple wallet addresses.

Example:

```sh
POST /aggregate_score {"wallet_addresses":["WalletAddress1", "WalletAddress2"] }
```
