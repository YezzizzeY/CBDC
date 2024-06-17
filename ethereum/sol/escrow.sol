// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Escrow {
    address public buyer;
    address public seller;
    address public merchant_validator;
    address public delivery_validator;
    string public merchant_sign;
    string public delivery_sign;
    uint public amount;

    enum State { AWAITING_PAYMENT, AWAITING_MERCHANT_VALIDATION, START_DELIVERY, AWAITING_DELIVERY_VALIDATION, COMPLETE }
    State public currentState;

    // Setups
    constructor() {
        currentState = State.AWAITING_PAYMENT;
    }

    function setBuyer(address _buyer) external {
        buyer = _buyer;
    }

    function setSeller(address _seller) external {
        seller = _seller;
    }

    function set_merchant_validator(address _validator) external {
        merchant_validator = _validator;
    }

    function set_delivery_validator(address _validator) external {
        delivery_validator = _validator;
    }

    // 1 pay to contract address as escrow
    function deposit() external payable {
        require(currentState == State.AWAITING_PAYMENT, "Not awaiting payment");
        amount = msg.value;
        currentState = State.AWAITING_MERCHANT_VALIDATION;
    }
    
    // 2 merchant sign for validation
    function merchantValidate(string calldata sign) external {
        require(currentState == State.AWAITING_MERCHANT_VALIDATION, "Not awaiting merchant validation");
        merchant_sign = sign;
        // possible signature verification scheme, but we could also just storage the signature content and verify offchain
        currentState = State.START_DELIVERY;
    }

    // after merchant signs, start delivery
    function startDelivery() external {
        require(currentState == State.START_DELIVERY, "Not ready to start delivery");
        currentState = State.AWAITING_DELIVERY_VALIDATION;
    }

    // 3 delivery sign
    function deliveryValidate(string calldata sign)  external {
        require(currentState == State.AWAITING_DELIVERY_VALIDATION, "Not awaiting delivery validation");
        delivery_sign = sign;
        currentState = State.COMPLETE;
        payable(seller).transfer(amount);
    }


}
