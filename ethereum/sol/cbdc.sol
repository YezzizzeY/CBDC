// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EcommercePlatform {
    struct TransactionProposal {
        uint256 productId;
        string merchantWallet;
        uint256 price;
        uint256 timestamp;
        bool merchantSigned;
        string merchantSignature;
        bool platformSigned;
        string platformSignature;
        bool deliveryConfirmed;
        bool processCompleted;
    }

    mapping(uint256 => TransactionProposal) public proposals;
    uint256 public proposalCounter;

    // Step 1: User uploads transaction proposal
    function uploadTransactionProposal(uint256 _productId, string memory _merchantWallet, uint256 _price) public {
        proposals[proposalCounter] = TransactionProposal({
            productId: _productId,
            merchantWallet: _merchantWallet,
            price: _price,
            timestamp: block.timestamp,
            merchantSigned: false,
            merchantSignature: "",
            platformSigned: false,
            platformSignature: "",
            deliveryConfirmed: false,
            processCompleted: false
        });
        proposalCounter++;
    }

    // Step 2: Merchant signs the proposal
    function signProposalByMerchant(uint256 _proposalId, string memory _signature) public {
        proposals[_proposalId].merchantSigned = true;
        proposals[_proposalId].merchantSignature = _signature;
    }

    // Step 2: Platform signs the proposal
    function signProposalByPlatform(uint256 _proposalId, string memory _signature) public {
        proposals[_proposalId].platformSigned = true;
        proposals[_proposalId].platformSignature = _signature;
    }

    // Step 3: Delivery company uploads delivery information
    function confirmDelivery(uint256 _proposalId) public {
        proposals[_proposalId].deliveryConfirmed = true;
    }

    // Step 4: Record process completion information
    function completeProcess(uint256 _proposalId) public {
        proposals[_proposalId].processCompleted = true;
    }
}
