const EcommercePlatform = artifacts.require("EcommercePlatform");

module.exports = function(deployer) {
    deployer.deploy(EcommercePlatform);
};
