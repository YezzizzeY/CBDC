const EcommercePlatform = artifacts.require("EcommercePlatform");

contract("EcommercePlatform", accounts => {
  it("should upload a transaction proposal", async () => {
    const instance = await EcommercePlatform.deployed();
    await instance.uploadTransactionProposal(1, "merchantWallet123", 100, { from: accounts[0] });
    const proposal = await instance.proposals(0);
    assert.equal(proposal.productId, 1);
    assert.equal(proposal.merchantWallet, "merchantWallet123");
    assert.equal(proposal.price, 100);
  });

  it("should allow merchant to sign the proposal", async () => {
    const instance = await EcommercePlatform.deployed();
    const signature = "merchantSignature123";
    await instance.signProposalByMerchant(0, signature, { from: accounts[1] });
    const proposal = await instance.proposals(0);
    assert.equal(proposal.merchantSigned, true);
    assert.equal(proposal.merchantSignature, signature);
  });

  it("should allow platform to sign the proposal", async () => {
    const instance = await EcommercePlatform.deployed();
    const signature = "platformSignature123";
    await instance.signProposalByPlatform(0, signature, { from: accounts[0] });
    const proposal = await instance.proposals(0);
    assert.equal(proposal.platformSigned, true);
    assert.equal(proposal.platformSignature, signature);
  });

  it("should confirm delivery", async () => {
    const instance = await EcommercePlatform.deployed();
    await instance.confirmDelivery(0, { from: accounts[2] });
    const proposal = await instance.proposals(0);
    assert.equal(proposal.deliveryConfirmed, true);
  });

  it("should complete the process", async () => {
    const instance = await EcommercePlatform.deployed();
    await instance.completeProcess(0, { from: accounts[0] });
    const proposal = await instance.proposals(0);
    assert.equal(proposal.processCompleted, true);
  });
});
