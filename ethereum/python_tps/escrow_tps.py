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
contract_address = "0xC998ab057ad6c585D33271E377025cf2474b6E24"  # 替换为你的合约地址
abi_file_path = 'C:/Users/Yezzi/Desktop/cbdc/CBDC/ethereum/python_tps/abi.json'  # 替换为你的ABI文件路径

# 读取ABI
with open(abi_file_path, 'r') as abi_file:
    contract_abi = json.load(abi_file)

# 创建合约对象
escrow_contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# 调用合约方法并测量延迟
def call_contract_methods():
    latencies = []
    num_transactions = 4
    
    # 1. deposit
    tx_start_time = time.time()
    tx_hash = escrow_contract.functions.deposit().transact({'from': accounts[0], 'value': web3.to_wei(1, 'ether')})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    tx_end_time = time.time()
    latencies.append(tx_end_time - tx_start_time)

    # 2. merchantValidate
    tx_start_time = time.time()
    tx_hash = escrow_contract.functions.merchantValidate("merchant_sign").transact({'from': accounts[0]})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    tx_end_time = time.time()
    latencies.append(tx_end_time - tx_start_time)

    # 3. startDelivery
    tx_start_time = time.time()
    tx_hash = escrow_contract.functions.startDelivery().transact({'from': accounts[0]})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    tx_end_time = time.time()
    latencies.append(tx_end_time - tx_start_time)

    # 4. deliveryValidate
    tx_start_time = time.time()
    tx_hash = escrow_contract.functions.deliveryValidate("delivery_sign").transact({'from': accounts[0]})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    tx_end_time = time.time()
    latencies.append(tx_end_time - tx_start_time)

    duration = sum(latencies)
    tps = num_transactions / duration
    avg_latency = sum(latencies) / len(latencies)
    
    return tps, avg_latency

# 主函数
def main():
    tps, avg_latency = call_contract_methods()
    print(f"TPS: {tps:.2f}")
    print(f"Average Latency: {avg_latency:.4f} seconds")

if __name__ == "__main__":
    main()
