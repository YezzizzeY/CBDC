from web3 import Web3
import json
import time

# 连接到 Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("Could not connect to Ganache")

# 获取账户
accounts = web3.eth.accounts

# 合约地址和ABI文件路径
contract_address = "0x21Ff1A0DF0eAF7Dfc5181DD2939EF6191427AB5b"  # 替换为你的合约地址
abi_file_path = 'C:/Users/Yezzi/Desktop/cbdc/CBDC/ethereum/python_tps/e-commerce.json'  # 替换为你的ABI文件路径

# 读取ABI
with open(abi_file_path, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# 创建合约对象
ecommerce_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# 调用合约方法并测量延迟
def call_contract_methods(num_transactions):
    latencies = []

    for i in range(num_transactions):
        # Step 1: User uploads transaction proposal
        tx_start_time = time.time()
        tx_hash = ecommerce_contract.functions.uploadTransactionProposal(
            i, "merchant_wallet", web3.to_wei(1, 'ether')
        ).transact({'from': accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_end_time = time.time()
        latencies.append(tx_end_time - tx_start_time)

        # Step 2: Merchant signs the proposal
        tx_start_time = time.time()
        tx_hash = ecommerce_contract.functions.signProposalByMerchant(
            i, "merchant_signature"
        ).transact({'from': accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_end_time = time.time()
        latencies.append(tx_end_time - tx_start_time)

        # Step 2: Platform signs the proposal
        tx_start_time = time.time()
        tx_hash = ecommerce_contract.functions.signProposalByPlatform(
            i, "platform_signature"
        ).transact({'from': accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_end_time = time.time()
        latencies.append(tx_end_time - tx_start_time)

        # Step 3: Delivery company uploads delivery information
        tx_start_time = time.time()
        tx_hash = ecommerce_contract.functions.confirmDelivery(i).transact({'from': accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_end_time = time.time()
        latencies.append(tx_end_time - tx_start_time)

        # Step 4: Record process completion information
        tx_start_time = time.time()
        tx_hash = ecommerce_contract.functions.completeProcess(i).transact({'from': accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_end_time = time.time()
        latencies.append(tx_end_time - tx_start_time)

    duration = sum(latencies)
    tps = num_transactions * 5 / duration  # 每个交易包括5个合约方法调用
    avg_latency = sum(latencies) / len(latencies)
    
    return tps, avg_latency

# 主函数
def main():
    num_transactions = 100
    
    # 调用合约方法并测量TPS和平均延迟
    tps, avg_latency = call_contract_methods(num_transactions)
    print(f"TPS: {tps:.2f}")
    print(f"Average Latency: {avg_latency:.4f} seconds")

if __name__ == "__main__":
    main()
