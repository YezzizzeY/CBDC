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





#### 3.5 Installing chaincodes on the channel

In Fabric, smart contracts are deployed on the network in packages referred to as chaincode. A Chaincode is installed on the peers of an organization and then deployed to a channel, where it can then be used to endorse transactions and interact with the blockchain ledger. Before a chaincode can be deployed to a channel, the members of the channel need to agree on a chaincode definition that establishes chaincode governance. When the required number of organizations agree, the chaincode definition can be committed to the channel, and the chaincode is ready to be used.

```bash
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
```





### 4 Test with CBDC Demo



#### 4.1 Get the CBDC github repo

First, we need to get the CBDC sdk and CBDC smart contract using github:

```bash
git clone https://github.com/YezzizzeY/CBDC.git
```



#### 4.2 Add CBDC_transaction doc folder to fabric-samples



#### 4.3 Setting basic network

This command will deploy the Fabric test network with two peers, an ordering service, and three certificate authorities (Orderer, Org1, Org2). Instead of using the cryptogen tool, we bring up the test network using certificate authorities, hence the `-ca` flag. Additionally, the org admin user registration is bootstrapped when the certificate authority is started.

```bash
./network.sh up createChannel -c mychannel -ca
```



#### 4.4 Compile and deploy the CBDC smart contract

```bash
./network.sh deployCC -ccn testgo -ccp ../CBDC_transaction/CBDC_contract_go/ -ccl go
```



#### 4.5 Integrate SDK into our application

go into application-gateway-go and run 

```bash
go run assetTransfer.go
```

the success output is:

```bash
root@ubuntu:/home/yezzi/Desktop/CBDC/fabric-samples/CBDC_transaction/application-gateway-go# go run assetTransfer.go 
connect to contract succeed:  &{0xc0001eba10 0xc000150ec0 mychannel testgo }

--> Submit Transaction: InitLedger, function creates the initial set of assets on the ledger 
*** Transaction committed successfully

--> Evaluate Transaction: GetAllAssets, function returns all the current assets on the ledger
Raw Evaluate Result: [{"appraisedValue":0,"id":"asset1707417670515","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerA","merchant":"MerchantA","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"asset1707417728055","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerA","merchant":"MerchantA","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"assetExampleID","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerA","merchant":"MerchantA","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"init0","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerA","merchant":"MerchantA","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"init1","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerB","merchant":"MerchantB","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"init2","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerC","merchant":"MerchantC","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false},{"appraisedValue":0,"id":"init3","proposalTimeStamp":1622548800,"deliveryTimeStamp":0,"amount":1000,"buyer":"BuyerD","merchant":"MerchantD","buyerSig":"BuyerASignature","merchantSig":"","platformSig":"","partySig":"","paymentSuccess":false,"deliverSuccess":false,"buyerConfirmDeliverSig":"","tradeSuccess":false}]
*** Result:[
  {
    "appraisedValue": 0,
    "id": "asset1707417670515",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerA",
    "merchant": "MerchantA",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "asset1707417728055",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerA",
    "merchant": "MerchantA",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "assetExampleID",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerA",
    "merchant": "MerchantA",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "init0",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerA",
    "merchant": "MerchantA",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "init1",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerB",
    "merchant": "MerchantB",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "init2",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerC",
    "merchant": "MerchantC",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  },
  {
    "appraisedValue": 0,
    "id": "init3",
    "proposalTimeStamp": 1622548800,
    "deliveryTimeStamp": 0,
    "amount": 1000,
    "buyer": "BuyerD",
    "merchant": "MerchantD",
    "buyerSig": "BuyerASignature",
    "merchantSig": "",
    "platformSig": "",
    "partySig": "",
    "paymentSuccess": false,
    "deliverSuccess": false,
    "buyerConfirmDeliverSig": "",
    "tradeSuccess": false
  }
]

--> Submit Transaction: CreateAsset, creates new asset with ID asset1707417780878, ProposalTimeStamp 1622548800, Amount 1000, Buyer BuyerA, BuyerSig BuyerASignature, and Merchant MerchantA
*** Transaction committed successfully

--> Evaluate Transaction: ReadAsset, function returns asset attributes
*** Result:{
  "appraisedValue": 0,
  "id": "asset1707417780878",
  "proposalTimeStamp": 1622548800,
  "deliveryTimeStamp": 0,
  "amount": 1000,
  "buyer": "BuyerA",
  "merchant": "MerchantA",
  "buyerSig": "BuyerASignature",
  "merchantSig": "",
  "platformSig": "",
  "partySig": "",
  "paymentSuccess": false,
  "deliverSuccess": false,
  "buyerConfirmDeliverSig": "",
  "tradeSuccess": false
}

--> Submit Transaction: UpdateAsset asset70, asset70 does not exist and should return an error
*** Successfully caught the error:
Endorse error for transaction fbf3ccdd3d70a2f7bf18f96078d335671fb2db42b15c7c4e08b3e8563fdbc076 with gRPC status Aborted: rpc error: code = Aborted desc = failed to endorse transaction, see attached details for more info
Error Details:
- address: peer0.org1.example.com:7051, mspId: Org1MSP, message: chaincode response 500, Function UpdateAsset not found in contract SmartContract

```



### 5 SDK and smart contract

To help read the smart contract and CBDC sdk here, I've put the source code here

#### 5.1 smart contract

this is written by go, here is the core document, if you want to see the whole files, please refer to CBDC_transaction folder

```go
package chaincode

import (
	"encoding/json"
	"fmt"

	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract provides functions for managing an Asset
type SmartContract struct {
	contractapi.Contract
}

// Asset describes basic details of what makes up a simple asset
// Insert struct field in alphabetic order => to achieve determinism across languages
// golang keeps the order when marshal to json but doesn't order automatically
type Asset struct {
	AppraisedValue         int    `json:"appraisedValue"`
	ID                     string `json:"id"`
	ProposalTimeStamp      int64  `json:"proposalTimeStamp"`
	DeliveryTimeStamp      int64  `json:"deliveryTimeStamp"`
	Amount                 int    `json:"amount"`
	Buyer                  string `json:"buyer"`
	Merchant               string `json:"merchant"`
	BuyerSig               string `json:"buyerSig"`
	MerchantSig            string `json:"merchantSig"`
	PlatformSig            string `json:"platformSig"`
	PartySig               string `json:"partySig"`
	PaymentSuccess         bool   `json:"paymentSuccess"`
	DeliverSuccess         bool   `json:"deliverSuccess"`
	BuyerConfirmDeliverSig string `json:"buyerConfirmDeliverSig"`
	TradeSuccess           bool   `json:"tradeSuccess"`
}


// InitLedger adds a base set of assets to the ledger
func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	assets := []Asset{
		{
			ID:                "init0",
			ProposalTimeStamp: 1622548800, // 示例时间戳
			Amount:            1000,
			Buyer:             "BuyerA",
			BuyerSig:          "BuyerASignature",
			Merchant:          "MerchantA",
		},
		{
			ID:                "init1",
			ProposalTimeStamp: 1622548800, // 示例时间戳
			Amount:            1000,
			Buyer:             "BuyerB",
			BuyerSig:          "BuyerASignature",
			Merchant:          "MerchantB",
		},
		{
			ID:                "init2",
			ProposalTimeStamp: 1622548800, // 示例时间戳
			Amount:            1000,
			Buyer:             "BuyerC",
			BuyerSig:          "BuyerASignature",
			Merchant:          "MerchantC",
		},
		{
			ID:                "init3",
			ProposalTimeStamp: 1622548800, // 示例时间戳
			Amount:            1000,
			Buyer:             "BuyerD",
			BuyerSig:          "BuyerASignature",
			Merchant:          "MerchantD",
		},
	}

	for _, asset := range assets {
		assetJSON, err := json.Marshal(asset)
		if err != nil {
			return err
		}

		err = ctx.GetStub().PutState(asset.ID, assetJSON)
		if err != nil {
			return fmt.Errorf("failed to put to world state. %v", err)
		}
	}

	return nil
}

// CreateAsset issues a new asset to the world state with given details.
func (s *SmartContract) CreateAsset(ctx contractapi.TransactionContextInterface, id string, proposalTimeStamp int64, amount int, buyer string, buyerSig string, merchant string) error {
	exists, err := s.AssetExists(ctx, id)
	if err != nil {
		return err
	}
	if exists {
		return fmt.Errorf("the asset %s already exists", id)
	}

	// 创建一个新的Asset实例，只包含必需的字段
	asset := Asset{
		ID:                id,
		ProposalTimeStamp: proposalTimeStamp,
		Amount:            amount,
		Buyer:             buyer,
		BuyerSig:          buyerSig,
		Merchant:          merchant,
		// 其他字段保留其零值或默认值
	}
	assetJSON, err := json.Marshal(asset)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(id, assetJSON)
}

// ReadAsset returns the asset stored in the world state with given id.
func (s *SmartContract) ReadAsset(ctx contractapi.TransactionContextInterface, id string) (*Asset, error) {
	assetJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return nil, fmt.Errorf("failed to read from world state: %v", err)
	}
	if assetJSON == nil {
		return nil, fmt.Errorf("the asset %s does not exist", id)
	}

	var asset Asset
	err = json.Unmarshal(assetJSON, &asset)
	if err != nil {
		return nil, err
	}

	return &asset, nil
}

// UpdateAssetDeliveryTimeStamp updates the DeliveryTimeStamp of an asset.
func (s *SmartContract) UpdateAssetDeliveryTimeStamp(ctx contractapi.TransactionContextInterface, id string, newTimeStamp int64) error {
	return s.updateAssetField(ctx, id, func(asset *Asset) {
		asset.DeliveryTimeStamp = newTimeStamp
	})
}

// UpdateAssetPaymentSuccess updates the PaymentSuccess of an asset.
func (s *SmartContract) UpdateAssetPaymentSuccess(ctx contractapi.TransactionContextInterface, id string, newStatus bool) error {
	return s.updateAssetField(ctx, id, func(asset *Asset) {
		asset.PaymentSuccess = newStatus
	})
}

// UpdateAssetMerchantSig updates the MerchantSig of an asset.
func (s *SmartContract) UpdateAssetMerchantSig(ctx contractapi.TransactionContextInterface, id string, newSig string) error {
	return s.updateAssetField(ctx, id, func(asset *Asset) {
		asset.MerchantSig = newSig
	})
}

// updateAssetField is a helper function to update an asset field
func (s *SmartContract) updateAssetField(ctx contractapi.TransactionContextInterface, id string, updateFunc func(*Asset)) error {
	assetJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return fmt.Errorf("failed to read from world state: %v", err)
	}
	if assetJSON == nil {
		return fmt.Errorf("the asset %s does not exist", id)
	}

	var asset Asset
	err = json.Unmarshal(assetJSON, &asset)
	if err != nil {
		return err
	}

	// Call the passed function to update the asset
	updateFunc(&asset)

	// Serialize the updated asset and write it back to the state
	updatedAssetJSON, err := json.Marshal(asset)
	if err != nil {
		return err
	}

	return ctx.GetStub().PutState(id, updatedAssetJSON)
}

// DeleteAsset deletes a given asset from the world state.
func (s *SmartContract) DeleteAsset(ctx contractapi.TransactionContextInterface, id string) error {
	exists, err := s.AssetExists(ctx, id)
	if err != nil {
		return err
	}
	if !exists {
		return fmt.Errorf("the asset %s does not exist", id)
	}

	return ctx.GetStub().DelState(id)
}

// AssetExists returns true when asset with given ID exists in world state
func (s *SmartContract) AssetExists(ctx contractapi.TransactionContextInterface, id string) (bool, error) {
	assetJSON, err := ctx.GetStub().GetState(id)
	if err != nil {
		return false, fmt.Errorf("failed to read from world state: %v", err)
	}

	return assetJSON != nil, nil
}

// GetAllAssets returns all assets found in world state
func (s *SmartContract) GetAllAssets(ctx contractapi.TransactionContextInterface) ([]*Asset, error) {
	// range query with empty string for startKey and endKey does an
	// open-ended query of all assets in the chaincode namespace.
	resultsIterator, err := ctx.GetStub().GetStateByRange("", "")
	if err != nil {
		return nil, err
	}
	defer resultsIterator.Close()

	var assets []*Asset
	for resultsIterator.HasNext() {
		queryResponse, err := resultsIterator.Next()
		if err != nil {
			return nil, err
		}

		var asset Asset
		err = json.Unmarshal(queryResponse.Value, &asset)
		if err != nil {
			return nil, err
		}
		assets = append(assets, &asset)
	}

	return assets, nil
}

```



#### 5.2 SDK

```go
/*
Copyright 2021 IBM All Rights Reserved.

SPDX-License-Identifier: Apache-2.0
*/

package main

import (
	"bytes"
	"context"
	"crypto/x509"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path"
	"time"

	"github.com/hyperledger/fabric-gateway/pkg/client"
	"github.com/hyperledger/fabric-gateway/pkg/identity"
	"github.com/hyperledger/fabric-protos-go-apiv2/gateway"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/status"
)

const (
	mspID        = "Org1MSP"
	cryptoPath   = "../../test-network/organizations/peerOrganizations/org1.example.com"
	certPath     = cryptoPath + "/users/User1@org1.example.com/msp/signcerts/cert.pem"
	keyPath      = cryptoPath + "/users/User1@org1.example.com/msp/keystore/"
	tlsCertPath  = cryptoPath + "/peers/peer0.org1.example.com/tls/ca.crt"
	peerEndpoint = "localhost:7051"
	gatewayPeer  = "peer0.org1.example.com"
)

var now = time.Now()
var assetId = fmt.Sprintf("asset%d", now.Unix()*1e3+int64(now.Nanosecond())/1e6)

func main() {
	// The gRPC client connection should be shared by all Gateway connections to this endpoint
	clientConnection := newGrpcConnection()
	defer clientConnection.Close()

	id := newIdentity()
	sign := newSign()

	// Create a Gateway connection for a specific client identity
	gw, err := client.Connect(
		id,
		client.WithSign(sign),
		client.WithClientConnection(clientConnection),
		// Default timeouts for different gRPC calls
		client.WithEvaluateTimeout(5*time.Second),
		client.WithEndorseTimeout(15*time.Second),
		client.WithSubmitTimeout(5*time.Second),
		client.WithCommitStatusTimeout(1*time.Minute),
	)
	if err != nil {
		panic(err)
	}
	defer gw.Close()

	// Override default values for chaincode and channel name as they may differ in testing contexts.
	chaincodeName := "testgo"
	//if ccname := os.Getenv("CHAINCODE_NAME"); ccname != "" {
	//	chaincodeName = ccname
	//}

	channelName := "mychannel"
	if cname := os.Getenv("CHANNEL_NAME"); cname != "" {
		channelName = cname
	}

	network := gw.GetNetwork(channelName)
	contract := network.GetContract(chaincodeName)
	fmt.Println("connect to contract succeed: ", contract)

	initLedger(contract)
	getAllAssets(contract)
	createAsset(contract)
	readAssetByID(contract)
	exampleErrorHandling(contract)
}

// newGrpcConnection creates a gRPC connection to the Gateway server.
func newGrpcConnection() *grpc.ClientConn {
	certificate, err := loadCertificate(tlsCertPath)
	if err != nil {
		panic(err)
	}

	certPool := x509.NewCertPool()
	certPool.AddCert(certificate)
	transportCredentials := credentials.NewClientTLSFromCert(certPool, gatewayPeer)

	connection, err := grpc.Dial(peerEndpoint, grpc.WithTransportCredentials(transportCredentials))
	if err != nil {
		panic(fmt.Errorf("failed to create gRPC connection: %w", err))
	}

	return connection
}

// newIdentity creates a client identity for this Gateway connection using an X.509 certificate.
func newIdentity() *identity.X509Identity {
	certificate, err := loadCertificate(certPath)
	if err != nil {
		panic(err)
	}

	id, err := identity.NewX509Identity(mspID, certificate)
	if err != nil {
		panic(err)
	}

	return id
}

func loadCertificate(filename string) (*x509.Certificate, error) {
	certificatePEM, err := os.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("failed to read certificate file: %w", err)
	}
	return identity.CertificateFromPEM(certificatePEM)
}

// newSign creates a function that generates a digital signature from a message digest using a private key.
func newSign() identity.Sign {
	files, err := os.ReadDir(keyPath)
	if err != nil {
		panic(fmt.Errorf("failed to read private key directory: %w", err))
	}
	privateKeyPEM, err := os.ReadFile(path.Join(keyPath, files[0].Name()))

	if err != nil {
		panic(fmt.Errorf("failed to read private key file: %w", err))
	}

	privateKey, err := identity.PrivateKeyFromPEM(privateKeyPEM)
	if err != nil {
		panic(err)
	}

	sign, err := identity.NewPrivateKeySign(privateKey)
	if err != nil {
		panic(err)
	}

	return sign
}

// This type of transaction would typically only be run once by an application the first time it was started after its
// initial deployment. A new version of the chaincode deployed later would likely not need to run an "init" function.
func initLedger(contract *client.Contract) {
	fmt.Printf("\n--> Submit Transaction: InitLedger, function creates the initial set of assets on the ledger \n")
	_, err := contract.SubmitTransaction("InitLedger")
	if err != nil {
		panic(fmt.Errorf("failed to submit transaction: %w", err))
	}

	fmt.Printf("*** Transaction committed successfully\n")
}

// Evaluate a transaction to query ledger state.
func getAllAssets(contract *client.Contract) {
	fmt.Println("\n--> Evaluate Transaction: GetAllAssets, function returns all the current assets on the ledger")

	evaluateResult, err := contract.EvaluateTransaction("GetAllAssets")

	// 打印原始返回的数据
	fmt.Printf("Raw Evaluate Result: %s\n", string(evaluateResult))
	if err != nil {
		panic(fmt.Errorf("failed to evaluate transaction: %w", err))
	}



	// 继续您原有的处理逻辑
	result := formatJSON(evaluateResult)
	fmt.Printf("*** Result:%s\n", result)
}


func createAsset(contract *client.Contract) {
	// 定义创建资产所需的参数
	assetId := assetId// 示例资产ID，实际应用中可能需要动态生成或从用户输入获取
	proposalTimeStamp := "1622548800"
	amount := "1000" // 示例金额
	buyer := "BuyerA" // 买家示例
	buyerSig := "BuyerASignature" // 买家签名示例
	merchant := "MerchantA" // 商家示例

	fmt.Printf("\n--> Submit Transaction: CreateAsset, creates new asset with ID %s, ProposalTimeStamp %s, Amount %s, Buyer %s, BuyerSig %s, and Merchant %s\n",
		assetId, proposalTimeStamp, amount, buyer, buyerSig, merchant)

	// 调用智能合约的CreateAsset函数
	_, err := contract.SubmitTransaction("CreateAsset", assetId, proposalTimeStamp, amount, buyer, buyerSig, merchant)
	if err != nil {
		panic(fmt.Errorf("failed to submit transaction: %w", err))
	}

	fmt.Printf("*** Transaction committed successfully\n")
}


// Evaluate a transaction by assetID to query ledger state.
func readAssetByID(contract *client.Contract) {
	fmt.Printf("\n--> Evaluate Transaction: ReadAsset, function returns asset attributes\n")

	evaluateResult, err := contract.EvaluateTransaction("ReadAsset", assetId)
	if err != nil {
		panic(fmt.Errorf("failed to evaluate transaction: %w", err))
	}
	result := formatJSON(evaluateResult)

	fmt.Printf("*** Result:%s\n", result)
}



// Submit transaction, passing in the wrong number of arguments ,expected to throw an error containing details of any error responses from the smart contract.
func exampleErrorHandling(contract *client.Contract) {
	fmt.Println("\n--> Submit Transaction: UpdateAsset asset70, asset70 does not exist and should return an error")

	_, err := contract.SubmitTransaction("UpdateAsset", "asset70", "blue", "5", "Tomoko", "300")
	if err == nil {
		panic("******** FAILED to return an error")
	}

	fmt.Println("*** Successfully caught the error:")

	switch err := err.(type) {
	case *client.EndorseError:
		fmt.Printf("Endorse error for transaction %s with gRPC status %v: %s\n", err.TransactionID, status.Code(err), err)
	case *client.SubmitError:
		fmt.Printf("Submit error for transaction %s with gRPC status %v: %s\n", err.TransactionID, status.Code(err), err)
	case *client.CommitStatusError:
		if errors.Is(err, context.DeadlineExceeded) {
			fmt.Printf("Timeout waiting for transaction %s commit status: %s", err.TransactionID, err)
		} else {
			fmt.Printf("Error obtaining commit status for transaction %s with gRPC status %v: %s\n", err.TransactionID, status.Code(err), err)
		}
	case *client.CommitError:
		fmt.Printf("Transaction %s failed to commit with status %d: %s\n", err.TransactionID, int32(err.Code), err)
	default:
		panic(fmt.Errorf("unexpected error type %T: %w", err, err))
	}

	// Any error that originates from a peer or orderer node external to the gateway will have its details
	// embedded within the gRPC status error. The following code shows how to extract that.
	statusErr := status.Convert(err)

	details := statusErr.Details()
	if len(details) > 0 {
		fmt.Println("Error Details:")

		for _, detail := range details {
			switch detail := detail.(type) {
			case *gateway.ErrorDetail:
				fmt.Printf("- address: %s, mspId: %s, message: %s\n", detail.Address, detail.MspId, detail.Message)
			}
		}
	}
}

// Format JSON data
func formatJSON(data []byte) string {
	var prettyJSON bytes.Buffer
	if err := json.Indent(&prettyJSON, data, "", "  "); err != nil {
		panic(fmt.Errorf("failed to parse JSON: %w", err))
	}
	return prettyJSON.String()
}

```

