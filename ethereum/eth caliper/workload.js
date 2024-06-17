const Web3 = require('web3');
const { abi } = require('./compile');
const web3 = new Web3('ws://localhost:8545');
const contractAddress = '0x0c0f559f9fa019d7f8eb8a1274a7db193dda50f7';
const contract = new web3.eth.Contract(abi, contractAddress);
let accounts;

(async () => {
    accounts = await web3.eth.getAccounts();
})();

const uploadProposal = async () => {
    await contract.methods.uploadTransactionProposal(1, 'merchantWallet123', 100).send({ from: accounts[0], gas: 1500000 });
};

const signProposal = async () => {
    await contract.methods.signProposalByMerchant(0, 'merchantSignature').send({ from: accounts[1], gas: 1500000 });
    await contract.methods.signProposalByPlatform(0, 'platformSignature').send({ from: accounts[0], gas: 1500000 });
};

const confirmDelivery = async () => {
    await contract.methods.confirmDelivery(0).send({ from: accounts[2], gas: 1500000 });
};

const completeProcess = async () => {
    await contract.methods.completeProcess(0).send({ from: accounts[0], gas: 1500000 });
};

module.exports = {
    uploadProposal,
    signProposal,
    confirmDelivery,
    completeProcess
};
