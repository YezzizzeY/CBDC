# CBDC Experiment



## Technical report of setting up hyperledger fabric testnet, installing chaincodes and using sdk

### 1 Preparing prerequisites

#### 1.1 Golang



#### 1.2 Git



#### 1.3 cURL



#### 1.4 Docker



#### 1.5 Nodejs



#### 1.6 npm



### 2 Installing Fabric and Fabric Samples



#### 2.1 Download Fabric sample, Docker images and binaries

- Download a simple Fabric test network using Docker compose, and a set of sample applications that demonstrate its core capabilities. 
- Download precompiled Fabric CLI tool binaries and Fabric Docker Images which will be downloaded to environment.
- Downloads the latest Hyperledger Fabric Docker images and tags them as latest
- Downloads the following platform-specific Hyperledger Fabric CLI tool binaries and config files into the fabric-samples /bin and /config directories. (network.configtxgen, configtxlator, cryptogen, discover, idemixgen, orderer, osnadmin, peer, fabric-ca-client, fabric-ca-server)

```bash
curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh && chmod +x install-fabric.sh
```



#### 2.2 Choosing components

To specify the components to download add one or more of the following arguments. 

To pull the Docker containers and clone the samples repo, run one of these commands for example.

```bash
./install-fabric.sh docker samples binary
or
./install-fabric.sh d s b
```





### 3 Build up the network

After having downloaded the Hyperledger Fabric Docker images and samples, you can deploy a test network by using scripts that are provided in the fabric-samples repository. The test network is provided for learning about Fabric by running nodes on your local machine. Developers can use the network to test their smart contracts and applications. The network is meant to be used only as a tool for education and testing and not as a model for how to set up a network. 

In general, modifications to the scripts are discouraged and could break the network. It is based on a limited configuration that should not be used as a template for deploying a production network: It includes two peer organizations and an ordering organization. For simplicity, a single node Raft ordering service is configured. To reduce complexity, a TLS Certificate Authority (CA) is not deployed. All certificates are issued by the root CAs. The sample network deploys a Fabric network with Docker Compose. Because the nodes are isolated within a Docker Compose network, the test network is not configured to connect to other running Fabric nodes.



#### 3.1 Bring up the test network

```bash
cd fabric-samples/test-network
```

In this directory, you can find an annotated script, `network.sh`, that stands up a Fabric network using the Docker images on your local machine.

From inside the `test-network` directory, run the following command to remove any containers or artifacts from any previous runs:

```bash
./network.sh down
```

If we have used this before, the output is like:

```bash
root@ubuntu:/home/yezzi/Desktop/CBDC/fabric-samples/test-network# ./network.sh down
/bin/bash: /home/yezzi/anaconda3/lib/libtinfo.so.6: no version information available (required by /bin/bash)
Using docker and docker-compose
Stopping network
Stopping cli                    ... done
Stopping orderer.example.com    ... done
Stopping peer0.org2.example.com ... done
Stopping peer0.org1.example.com ... done
Stopping ca_orderer             ... done
Stopping ca_org2                ... done
Stopping ca_org1                ... done
Removing cli                    ... done
Removing orderer.example.com    ... done
Removing peer0.org2.example.com ... done
Removing peer0.org1.example.com ... done
Removing ca_orderer             ... done
Removing ca_org2                ... done
Removing ca_org1                ... done
Removing network fabric_test
Removing network compose_default
WARNING: Network compose_default not found.
Removing volume compose_orderer.example.com
Removing volume compose_orderer2.example.com
WARNING: Volume compose_orderer2.example.com not found.
Removing volume compose_orderer3.example.com
WARNING: Volume compose_orderer3.example.com not found.
Removing volume compose_orderer4.example.com
WARNING: Volume compose_orderer4.example.com not found.
Removing volume compose_peer0.org1.example.com
Removing volume compose_peer0.org2.example.com
Removing volume compose_peer0.org3.example.com
WARNING: Volume compose_peer0.org3.example.com not found.
Error: No such volume: docker_orderer.example.com
Error: No such volume: docker_peer0.org1.example.com
Error: No such volume: docker_peer0.org2.example.com
Removing remaining containers
Removing generated chaincode docker images
Untagged: dev-peer0.org2.example.com-basic_1.0.1-1a7857a39b9fbcf7b74769cf157985e8b9a9324df3bd21d760a128262b5ebb06-c042e5d3dc64bcd56f8c9da1ddd486670b87d050ad3523f7edb657931fe8662e:latest
Deleted: sha256:02e0a447a68e78fd180d2ca2dffedbf2f985332818578af1abddcfc5eb07811a
Deleted: sha256:eb5ab3a1660ae62f3d263081a9d6df66c1cfa92176b90e02ca2eed7efd9bfd7e
Deleted: sha256:f9d4701b7b27f30af571a9e5c5fb3d40cbf187920df55c61d0c2f4d7561dfa90
Deleted: sha256:a1aea1d35960b724d58f7cf37043bae113760b3d4723c8e89d62cdfaad7d6276
Untagged: dev-peer0.org1.example.com-basic_1.0.1-1a7857a39b9fbcf7b74769cf157985e8b9a9324df3bd21d760a128262b5ebb06-573f5f625647851030ef34249aec52de6d221b87b229325006e6321e0cffe44a:latest
Deleted: sha256:b608bab3f159353ef857d18cc1079afe197c07a436a4c6ad161f74ed1c529ebc
Deleted: sha256:f3924ce9730560fcd1777448a7ffeb3881fcb05e8a71888bd7a965d142b01939
Deleted: sha256:415332051f060762d3f76bdbd72121711c3d31fc8b4d1c1af8502bb71dbbe50f
Deleted: sha256:5aa8750ee8607cf6d10ccf4cd84a5e3a5dd27b8f44c1f0c6bfc15163c7ac54a4

```



You can then bring up the network by issuing the following command. You will experience problems if you try to run the script from another directory:

```go
./network.sh up
```

This command creates a Fabric network that consists of two peer nodes, one ordering node. No channel is created when you run `./network.sh up`:

```bash
Removing remaining containers
Removing generated chaincode docker images
Untagged: dev-peer0.org2.example.com-basic_1.0.1-1a7857a39b9fbcf7b74769cf157985e8b9a9324df3bd21d760a128262b5ebb06-c042e5d3dc64bcd56f8c9da1ddd486670b87d050ad3523f7edb657931fe8662e:latest
Deleted: sha256:02e0a447a68e78fd180d2ca2dffedbf2f985332818578af1abddcfc5eb07811a
Deleted: sha256:eb5ab3a1660ae62f3d263081a9d6df66c1cfa92176b90e02ca2eed7efd9bfd7e
Deleted: sha256:f9d4701b7b27f30af571a9e5c5fb3d40cbf187920df55c61d0c2f4d7561dfa90
Deleted: sha256:a1aea1d35960b724d58f7cf37043bae113760b3d4723c8e89d62cdfaad7d6276
Untagged: dev-peer0.org1.example.com-basic_1.0.1-1a7857a39b9fbcf7b74769cf157985e8b9a9324df3bd21d760a128262b5ebb06-573f5f625647851030ef34249aec52de6d221b87b229325006e6321e0cffe44a:latest
Deleted: sha256:b608bab3f159353ef857d18cc1079afe197c07a436a4c6ad161f74ed1c529ebc
Deleted: sha256:f3924ce9730560fcd1777448a7ffeb3881fcb05e8a71888bd7a965d142b01939
Deleted: sha256:415332051f060762d3f76bdbd72121711c3d31fc8b4d1c1af8502bb71dbbe50f
Deleted: sha256:5aa8750ee8607cf6d10ccf4cd84a5e3a5dd27b8f44c1f0c6bfc15163c7ac54a4
root@ubuntu:/home/yezzi/Desktop/CBDC/fabric-samples/test-network# ./network.sh up
/bin/bash: /home/yezzi/anaconda3/lib/libtinfo.so.6: no version information available (required by /bin/bash)
Using docker and docker-compose
Starting nodes with CLI timeout of '5' tries and CLI delay of '3' seconds and using database 'leveldb' with crypto from 'cryptogen'
LOCAL_VERSION=v2.5.4
DOCKER_IMAGE_VERSION=v2.5.4
/home/yezzi/Desktop/CBDC/fabric-samples/test-network/../bin/cryptogen
Generating certificates using cryptogen tool
Creating Org1 Identities
+ cryptogen generate --config=./organizations/cryptogen/crypto-config-org1.yaml --output=organizations
org1.example.com
+ res=0
Creating Org2 Identities
+ cryptogen generate --config=./organizations/cryptogen/crypto-config-org2.yaml --output=organizations
org2.example.com
+ res=0
Creating Orderer Org Identities
+ cryptogen generate --config=./organizations/cryptogen/crypto-config-orderer.yaml --output=organizations
+ res=0
Generating CCP files for Org1 and Org2
/bin/bash: /home/yezzi/anaconda3/lib/libtinfo.so.6: no version information available (required by /bin/bash)
Creating network "fabric_test" with the default driver
Creating volume "compose_orderer.example.com" with default driver
Creating volume "compose_peer0.org1.example.com" with default driver
Creating volume "compose_peer0.org2.example.com" with default driver
Creating orderer.example.com    ... done
Creating peer0.org2.example.com ... done
Creating peer0.org1.example.com ... done
Creating cli                    ... done
CONTAINER ID   IMAGE                               COMMAND             CREATED         STATUS                  PORTS                                                                                                                             NAMES
3169ca7e4b27   hyperledger/fabric-tools:latest     "/bin/bash"         1 second ago    Up Less than a second                                                                                                                                     cli
43a15c22b444   hyperledger/fabric-orderer:latest   "orderer"           2 seconds ago   Up Less than a second   0.0.0.0:7050->7050/tcp, :::7050->7050/tcp, 0.0.0.0:7053->7053/tcp, :::7053->7053/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp   orderer.example.com
4f41e88efd9a   hyperledger/fabric-peer:latest      "peer node start"   2 seconds ago   Up 1 second             0.0.0.0:7051->7051/tcp, :::7051->7051/tcp, 0.0.0.0:9444->9444/tcp, :::9444->9444/tcp                                              peer0.org1.example.com
b006a656b0cd   hyperledger/fabric-peer:latest      "peer node start"   2 seconds ago   Up 1 second             0.0.0.0:9051->9051/tcp, :::9051->9051/tcp, 7051/tcp, 0.0.0.0:9445->9445/tcp, :::9445->9445/tcp      
```



#### 3.2 Check the docker components and network design

After your test network is deployed, you can take some time to examine its components. Run the following command to list all of Docker containers that are running on your machine. You should see the three nodes that were created by the `network.sh` script:

```bash
docker ps -a
```

Output:

```bash
CONTAINER ID   IMAGE                               COMMAND             CREATED              STATUS              PORTS                                                                                                                             NAMES
3169ca7e4b27   hyperledger/fabric-tools:latest     "/bin/bash"         About a minute ago   Up About a minute                                                                                                                                     cli
43a15c22b444   hyperledger/fabric-orderer:latest   "orderer"           About a minute ago   Up About a minute   0.0.0.0:7050->7050/tcp, :::7050->7050/tcp, 0.0.0.0:7053->7053/tcp, :::7053->7053/tcp, 0.0.0.0:9443->9443/tcp, :::9443->9443/tcp   orderer.example.com
4f41e88efd9a   hyperledger/fabric-peer:latest      "peer node start"   About a minute ago   Up About a minute   0.0.0.0:7051->7051/tcp, :::7051->7051/tcp, 0.0.0.0:9444->9444/tcp, :::9444->9444/tcp                                              peer0.org1.example.com
b006a656b0cd   hyperledger/fabric-peer:latest      "peer node start"   About a minute ago   Up About a minute   0.0.0.0:9051->9051/tcp, :::9051->9051/tcp, 7051/tcp, 0.0.0.0:9445->9445/tcp, :::9445->9445/tcp     
```



#### 3.3 Creating a channel

Now that we have peer and orderer nodes running on our machine, we can use the script to create a Fabric channel for transactions between Org1 and Org2. Channels are a private layer of communication between specific network members. Channels can be used only by organizations that are invited to the channel, and are invisible to other members of the network. Each channel has a separate blockchain ledger. Organizations that have been invited “join” their peers to the channel to store the channel ledger and validate the transactions on the channel.

```bash
./network.sh createChannel
```

output:

```bash
+ configtxlator proto_encode --input config_update_in_envelope.json --type common.Envelope --output Org2MSPanchors.tx
2024-01-13 05:11:30.811 UTC 0001 INFO [channelCmd] InitCmdFactory -> Endorser and orderer connections initialized
2024-01-13 05:11:30.822 UTC 0002 INFO [channelCmd] update -> Successfully submitted channel update
Anchor peer set for org 'Org2MSP' on channel 'mychannel'
Channel 'mychannel' joined
root@ubuntu:/home/yezzi/Desktop/
```



#### 3.4 Writing chaincodes

A simplified smart contract to achieve the functions of CDBC

```javascript
/*
 * SPDX-License-Identifier: Apache-2.0
 */
// Deterministic JSON.stringify()
import {Context, Contract, Info, Returns, Transaction} from 'fabric-contract-api';
import stringify from 'json-stringify-deterministic';
import sortKeysRecursive from 'sort-keys-recursive';
import {Asset} from './asset';
import { Context, Contract, Info, Returns, Transaction } from 'fabric-contract-api';

interface LogisticsInfo {
    ID: string;
    Status: string; // 如 "Delivered", "In Transit"
    // 其他相关字段
}

interface CBDC_Transaction {
    ID: string;
    Amount: number;
    SellerCBDCAddress: string;
    // 其他相关字段
}

@Info({title: 'AssetTransfer', description: 'Smart contract for trading assets'})
export class AssetTransferContract extends Contract {

    @Transaction()
    public async InitLedger(ctx: Context): Promise<void> {

        const logistics: LogisticsInfo[] = [
        ];
        const cbdcTransactions: CBDC_Transaction[] = [
        ];

        for (const log of logistics) {
            await ctx.stub.putState(log.ID, Buffer.from(JSON.stringify(log)));
        }

        for (const cbdc of cbdcTransactions) {
            await ctx.stub.putState(cbdc.ID, Buffer.from(JSON.stringify(cbdc)));
        }
    }

    // 注册CBDCAccount
    @Transaction()
    public async RegisterCBDCAccount(ctx: Context, accountId: string, accountDetails: string): Promise<void> {
        // 实现账户注册逻辑
    }

    // 处理担保交易
    @Transaction()
    public async HandleEscrowTransaction(ctx: Context, transactionId: string, transactionDetails: string): Promise<void> {
        // 处理担保交易逻辑
    }

    // 分账结算
    @Transaction()
    public async SettleAccounts(ctx: Context, logisticsId: string, settlementRules: string): Promise<void> {
        // 实现分账结算逻辑
    }

    // 更新物流信息
    @Transaction()
    public async UpdateLogisticsInfo(ctx: Context, logisticsId: string, newInfo: string): Promise<void> {
        // 实现更新物流信息逻辑
    }

    // 获取物流信息
    @Transaction(false)
    @Returns('string')
    public async GetLogisticsInfo(ctx: Context, logisticsId: string): Promise<string> {
        // 实现获取物流信息逻辑
    }

    // 检查资产是否存在
    @Transaction(false)
    @Returns('boolean')
    public async AssetExists(ctx: Context, id: string): Promise<boolean> {
        const assetJSON = await ctx.stub.getState(id);
        return assetJSON && assetJSON.length > 0;
    }

}

```





#### 3.5 Installing chaincodes on the channel

In Fabric, smart contracts are deployed on the network in packages referred to as chaincode. A Chaincode is installed on the peers of an organization and then deployed to a channel, where it can then be used to endorse transactions and interact with the blockchain ledger. Before a chaincode can be deployed to a channel, the members of the channel need to agree on a chaincode definition that establishes chaincode governance. When the required number of organizations agree, the chaincode definition can be committed to the channel, and the chaincode is ready to be used.

```bash
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
```





### 4 Interacting with hyperledger fabric testnet



#### 4.1 Set up network again and create the channel

This command will deploy the Fabric test network with two peers, an ordering service, and three certificate authorities (Orderer, Org1, Org2). Instead of using the cryptogen tool, we bring up the test network using certificate authorities, hence the `-ca` flag. Additionally, the org admin user registration is bootstrapped when the certificate authority is started.

```bash
./network.sh up createChannel -c mychannel -ca
```



#### 4.2 Deploy the smart contract

Deploy the chaincode package containing the smart contract by calling the `./network.sh` script with the chaincode name and language options.

```bash
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-typescript/ -ccl typescript
```



#### 4.3 Setting SDK and invocation

A sample application developed using the Fabric Gateway client API for Node.

Run the following command to install the dependencies and build the application. It may take some time to complete:



```bash
npm install
```



#### 4.4 Run the application using npm

When we started the Fabric test network earlier in this tutorial, several identities were created using the Certificate Authorities. These include a user identity for each of the organizations. The application will use the credentials of one of these user identities to transact with the blockchain network.

```bash
npm start
```



#### 4.5 Integrate SDK into our application

First we use the typescript sdk and then we use typescript functions to achieve the application of several users.

```typescript
import * as grpc from '@grpc/grpc-js';
import { connect, Contract, Identity, Signer, signers } from '@hyperledger/fabric-gateway';
import * as crypto from 'crypto';
import { promises as fs } from 'fs';
import * as path from 'path';
import { TextDecoder } from 'util';

const channelName = envOrDefault('CHANNEL_NAME', 'mychannel');
const chaincodeName = envOrDefault('CHAINCODE_NAME', 'basic');
const mspId = envOrDefault('MSP_ID', 'Org1MSP');

// Path to crypto materials.
const cryptoPath = envOrDefault('CRYPTO_PATH', path.resolve(__dirname, '..', '..', '..', 'test-network', 'organizations', 'peerOrganizations', 'org1.example.com'));
const keyDirectoryPath = envOrDefault('KEY_DIRECTORY_PATH', path.resolve(cryptoPath, 'users', 'User1@org1.example.com', 'msp', 'keystore'));
const certPath = envOrDefault('CERT_PATH', path.resolve(cryptoPath, 'users', 'User1@org1.example.com', 'msp', 'signcerts', 'cert.pem'));
const tlsCertPath = envOrDefault('TLS_CERT_PATH', path.resolve(cryptoPath, 'peers', 'peer0.org1.example.com', 'tls', 'ca.crt'));
const peerEndpoint = envOrDefault('PEER_ENDPOINT', 'localhost:7051');
const peerHostAlias = envOrDefault('PEER_HOST_ALIAS', 'peer0.org1.example.com');

const utf8Decoder = new TextDecoder();

async function main(): Promise<void> {
    // Display input parameters
    displayInputParameters();

    // Set up the gRPC client connection
    const client = await newGrpcConnection();

    // Connect to the gateway
    const gateway = connect({
        client,
        identity: await newIdentity(),
        signer: await newSigner(),
        evaluateOptions: () => ({ deadline: Date.now() + 5000 }), // 5 seconds
        endorseOptions: () => ({ deadline: Date.now() + 15000 }), // 15 seconds
        submitOptions: () => ({ deadline: Date.now() + 5000 }), // 5 seconds
        commitStatusOptions: () => ({ deadline: Date.now() + 60000 }), // 1 minute
    });

    try {
        // Interact with the smart contract
        const network = gateway.getNetwork(channelName);
        const contract = network.getContract(chaincodeName);

        // Example functions
        await initLedger(contract);
        await getAllAssets(contract);
        await createAsset(contract, 'asset1', 'yellow', 5, 'Tom', 1300);
        await transferAssetAsync(contract, 'asset1', 'Saptha');
        await readAssetByID(contract, 'asset1');
        await updateNonExistentAsset(contract, 'asset70');
    } finally {
        gateway.close();
        client.close();
    }
}

async function createLogisticsInfo(contract: Contract, logisticsId: string, logisticsDetails: string): Promise<void> {
    console.log('\n--> Submit Transaction: CreateLogisticsInfo');

    await contract.submitTransaction('CreateLogisticsInfo', logisticsId, logisticsDetails);

    console.log('*** Transaction committed successfully');
}

async function createCBDC_Transaction(contract: Contract, transactionId: string, transactionDetails: string): Promise<void> {
    console.log('\n--> Submit Transaction: CreateCBDC_Transaction');

    await contract.submitTransaction('CreateCBDC_Transaction', transactionId, transactionDetails);

    console.log('*** Transaction committed successfully');
}

async function getLogisticsInfo(contract: Contract, logisticsId: string): Promise<void> {
    console.log(`\n--> Evaluate Transaction: GetLogisticsInfo, function returns the logistics info`);

    const resultBytes = await contract.evaluateTransaction('GetLogisticsInfo', logisticsId);

    console.log('*** Result:', utf8Decoder.decode(resultBytes));
}

async function getCBDC_TransactionInfo(contract: Contract, transactionId: string): Promise<void> {
    console.log(`\n--> Evaluate Transaction: GetCBDC_TransactionInfo, function returns the CBDC transaction info`);

    const resultBytes = await contract.evaluateTransaction('GetCBDC_TransactionInfo', transactionId);

    console.log('*** Result:', utf8Decoder.decode(resultBytes));
}


async function createLogisticsInfo(contract: Contract, logisticsId: string, logisticsDetails: string): Promise<void> {
    console.log('\n--> Submit Transaction: CreateLogisticsInfo');

    await contract.submitTransaction('CreateLogisticsInfo', logisticsId, logisticsDetails);

    console.log('*** Transaction committed successfully');
}

async function createCBDC_Transaction(contract: Contract, transactionId: string, transactionDetails: string): Promise<void> {
    console.log('\n--> Submit Transaction: CreateCBDC_Transaction');

    await contract.submitTransaction('CreateCBDC_Transaction', transactionId, transactionDetails);

    console.log('*** Transaction committed successfully');
}

async function getLogisticsInfo(contract: Contract, logisticsId: string): Promise<void> {
    console.log(`\n--> Evaluate Transaction: GetLogisticsInfo, function returns the logistics info`);

    const resultBytes = await contract.evaluateTransaction('GetLogisticsInfo', logisticsId);

    console.log('*** Result:', utf8Decoder.decode(resultBytes));
}

async function getCBDC_TransactionInfo(contract: Contract, transactionId: string): Promise<void> {
    console.log(`\n--> Evaluate Transaction: GetCBDC_TransactionInfo, function returns the CBDC transaction info`);

    const resultBytes = await contract.evaluateTransaction('GetCBDC_TransactionInfo', transactionId);

    console.log('*** Result:', utf8Decoder.decode(resultBytes));
}


async function newGrpcConnection(): Promise<grpc.Client> {
    const tlsRootCert = await fs.readFile(tlsCertPath);
    const tlsCredentials = grpc.credentials.createSsl(tlsRootCert);
    return new grpc.Client(peerEndpoint, tlsCredentials, {
        'grpc.ssl_target_name_override': peerHostAlias,
    });
}

async function newIdentity(): Promise<Identity> {
    const credentials = await fs.readFile(certPath);
    return { mspId, credentials };
}

async function newSigner(): Promise<Signer> {
    const files = await fs.readdir(keyDirectoryPath);
    const keyPath = path.resolve(keyDirectoryPath, files[0]);
    const privateKeyPem = await fs.readFile(keyPath);
    const privateKey = crypto.createPrivateKey(privateKeyPem);
    return signers.newPrivateKeySigner(privateKey);
}

function envOrDefault(key: string, defaultValue: string): string {
    return process.env[key] || defaultValue;
}

async function displayInputParameters(): Promise<void> {
    console.log(`channelName:       ${channelName}`);
    console.log(`chaincodeName:     ${chaincodeName}`);
    console.log(`mspId:             ${mspId}`);
    console.log(`cryptoPath:        ${cryptoPath}`);
    console.log(`keyDirectoryPath:  ${keyDirectoryPath}`);
    console.log(`certPath:          ${certPath}`);
    console.log(`tlsCertPath:       ${tlsCertPath}`);
    console.log(`peerEndpoint:      ${peerEndpoint}`);
    console.log(`peerHostAlias:     ${peerHostAlias}`);
}


main().catch(error => {
    console.error('******** FAILED to run the application:', error);
    process.exitCode = 1;
});


```

