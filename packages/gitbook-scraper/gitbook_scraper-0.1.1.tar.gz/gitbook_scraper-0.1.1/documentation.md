# API

API Documentation for the Hyperliquid public API
$
You can also use the API via the Hyperliquid Python SDK: [https://github.com/hyperliquid-dex/hyperliquid-python-sdk](https://github.com/hyperliquid-dex/hyperliquid-python-sdk) There is also a Rust SDK (although it is less maintained): [https://github.com/hyperliquid-dex/hyperliquid-rust-sdk](https://github.com/hyperliquid-dex/hyperliquid-rust-sdk) There are also Typescript SDKs written by members of the community: [https://github.com/nktkas/hyperliquid](https://github.com/nktkas/hyperliquid) [https://github.com/nomeida/hyperliquid](https://github.com/nomeida/hyperliquid) CCXT also maintains integrations in multiple languages that conforms with the standard CCXT API: [https://docs.ccxt.com/#/exchanges/hyperliquid](https://docs.ccxt.com/#/exchanges/hyperliquid) All example API calls use the Mainnet url (https://api.hyperliquid.xyz), but you can make the same requests against Testnet using the corresponding url (https://api.hyperliquid-testnet.xyz)
/$
[PreviousBrand kit](https://hyperliquid.gitbook.io/hyperliquid-docs/brand-kit) [NextNotation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/notation)
Last updated 6 days ago

## EVM

EVM
$
The HyperEVM consists of EVM blocks built as part of L1 execution, inheriting all security from HyperBFT consensus. HYPE is the native gas token on the HyperEVM. To move HYPE from the L1 to HyperEVM, send HYPE to `0x2222222222222222222222222222222222222222` . See the instructions in [Native Transfers](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/native-transfers) for more details on how this works. Note that there are currently no official frontend components of the EVM. Users can build their own frontends or port over existing EVM applications. All interaction with the EVM happens through the JSON-RPC. For example, users can add the chain to their wallets by entering the RPC URL and chain ID. There is currently no websocket JSON-RPC support for the HyperEVM. On both mainnet and testnet, HYPE on HyperEVM has 18 decimals. A few differences between testnet and mainnet HyperEVM are highlighted below: 
### Mainnet
 Chain ID: 999 JSON-RPC endpoint: `https://rpc.hyperliquid.xyz/evm` for mainnet 
### Testnet
 Chain ID: 998 JSON-RPC endpoint: `https://rpc.hyperliquid-testnet.xyz/evm`
/$
[PreviousDeploying HIP-1 and HIP-2 assets](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/deploying-hip-1-and-hip-2-assets) [NextDual-block architecture](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/dual-block-architecture)
Last updated 3 hours ago

### Dual-block architecture

Dual-block architecture
$
The total HyperEVM throughput is split between small blocks that happen at a fast rate and large blocks that happen at a slower rate. The HyperEVM "mempool" is still onchain state with respect to L1 execution, but is split into two independent mempools that source transactions for the two block types. The two block types are interleaved with a unique increasing sequence of EVM block numbers. The primary motivation behind the dual-block architecture is to decouple block speed and block size when allocating throughput improvements. Users want faster blocks for lower time to confirmation. Builders want larger blocks to include larger transactions such as more complex contract deployments. Instead of a forced tradeoff, the dual-block system will allow simultaneous improvement along both axes. The initial configuration is set conservatively, and throughput is expected to increase over successive technical upgrades. Fast block duration is set to 2 seconds with a 2M gas limit. Slow blocks duration is set to 1 minute with a 30M gas limit. Developers can deploy larger contracts as follows: 
1. Submit L1 action {"type": "evmUserModify", "usingBigBlocks": true} to direct EVM transactions to big blocks instead of small blocks. Note that this L1 user state flag is set on the L1 user level, and must be unset again to target small blocks. Like any L1 action, this requires an existing L1 user to send. Like any EOA, the deployer address can be converted to an L1 user by receiving an asset such as USDC on the L1.
2. Optionally use the JSON-RPC method bigBlockGasPrice in place of gasPrice to estimate base gas fee on the next big block.
/$
[PreviousEVM](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm) [NextRaw HyperEVM Block Data](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/raw-hyperevm-block-data)
Last updated 2 hours ago


---

### Raw HyperEVM Block Data

Raw HyperEVM Block Data
$
Builders that wish to index HyperEVM without running a node can use the S3 bucket: `aws s3 ls s3://hl-mainnet-evm-blocks/ --request-payer requester` . There is a similar bucket `s3://hl-testnet-evm-blocks/` for testnet. Some potential applications include a JSON-RPC server with custom rate limits, a HyperEVM block explorer, or other indexed services and tooling for builders. While the data is public for anyone to use, the requester must pay for data transfer costs. The filenames are predictably indexed by EVM block number, e.g. `s3://hl-mainnet-evm-blocks/0/6000/6123.rmp.lz4.` An indexer can copy block data from S3 on new HyperEVM blocks. The files are stored in MessagePack format and then compressed using LZ4. Note that testnet starts with directory `s3://hl-testnet-evm-blocks/18000000` and the earlier testnet RPC blocks were not backfilled. An example can be found in the Python SDK: [https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/examples/evm_block_indexer.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/examples/evm_block_indexer.py)
/$
[PreviousDual-block architecture](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/dual-block-architecture) [NextInteracting with the L1](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/interacting-with-the-l1)
Last updated 2 hours ago


---

### Interacting with the L1

Interacting with the L1
$?
/$
[PreviousRaw HyperEVM Block Data](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/raw-hyperevm-block-data) [NextNative Transfers](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/native-transfers)
Last updated 2 hours ago


---

### Native Transfers

Native Transfers
$
Spot assets can be sent between the L1 and the EVM. Spot assets on the L1 are called `native spot` while ones on the EVM are called `EVM spot` . The spot deployer can link their native spot asset to any ERC20 contract deployed to the EVM. The native spot asset and ERC20 token can be deployed in either order. The only native transfer currently enabled on mainnet is for HYPE. In order for transfers between the two to work the system address ( `0x2222222222222222222222222222222222222222` ) must have the total non-system balance on the other side. For example, to deploy an ERC20 contract for an existing native spot asset, the system contract should have the entirety of the EVM spot supply equal to the max native spot supply.
Once this is done the spot deployer needs to send a spot deploy action to link the token to the EVM: Copy 
```min-w-full
/*** @param token - The token index to link* @param address - The address of the ERC20 contract on the evm.* @param evmExtraWeiDecimals - The difference in Wei decimals between native and EVM spot. E.g. native PURR has 5 weiDecimals but EVM PURR has 18, so this would be 13. evmExtraWeiDecimals should be in the range [-2, 18] inclusive*/interface SetEvmContract {type: “setEvmContract”;token: number;Address: address;evmExtraWeiDecimals: number;}
```
 Once a token is linked, it can be converted between native and EVM spot by sending the token to the system address ( `0x2222222222222222222222222222222222222222` ). This can be done on the L1 using a spotSend action (or via the frontend) and on the EVM by using an ERC transfer.
There are currently no checks that the system address has sufficient supply or that the contract is a valid ERC20, so be careful when sending funds. EVM PURR has been deployed as `0xa9056c15938f9aff34CD497c722Ce33dB0C2fD57` HYPE is a special case as the native gas token on the EVM. HYPE is received on the EVM side of a transfer as the native gas token instead of an ERC20 token. To transfer back to the L1, HYPE can be sent as a transaction value. The EVM transfer address `0x222..2` is a system contract that emits `event Received(address indexed user, uint256 amount)` as its payable `receive()` function. Here `user` is `msg.sender` , so this implementation enables both smart contracts and EOAs to transfer HYPE back to the L1. Note that there is a small gas cost to emitting this log on the EVM side. Attached is a sample script for deploying an ERC20 token to the EVM and linking it to a native spot token. [39KBerc20_example.py](https://2356094849-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyUdp569E6w18GdfqlGvJ%2Fuploads%2F4k3MpHVOdp1EBQ7jaUW2%2Ferc20_example.py?alt=media&token=eb96dabe-3de0-425f-a998-5a78bb1f94b9)
/$
[PreviousInteracting with the L1](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/interacting-with-the-l1) [NextWrapped HYPE](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/wrapped-hype)
Last updated 2 hours ago


---

### Wrapped HYPE

Wrapped HYPE
$
A canonical system contract for wrapped HYPE is deployed at `0x555...5` . The contract is immutable, with the same source code as wrapped ETH on Ethereum, apart from the token name and symbol. The source code for WHYPE is provided below. Note that this is based on the WETH contract on Ethereum mainnet and other EVM chains. Copy 
```min-w-full
pragma solidity >=0.4.22 <0.6;contract WHYPE9 {string public name = "Wrapped HYPE";string public symbol = "WHYPE";uint8 public decimals = 18;event Approval(address indexed src, address indexed guy, uint wad);event Transfer(address indexed src, address indexed dst, uint wad);event Deposit(address indexed dst, uint wad);event Withdrawal(address indexed src, uint wad);mapping(address => uint) public balanceOf;mapping(address => mapping(address => uint)) public allowance;function() external payable {deposit();}function deposit() public payable {balanceOf[msg.sender] += msg.value;emit Deposit(msg.sender, msg.value);}function withdraw(uint wad) public {require(balanceOf[msg.sender] >= wad);balanceOf[msg.sender] -= wad;msg.sender.transfer(wad);emit Withdrawal(msg.sender, wad);}function totalSupply() public view returns (uint) {return address(this).balance;}function approve(address guy, uint wad) public returns (bool) {allowance[msg.sender][guy] = wad;emit Approval(msg.sender, guy, wad);return true;}function transfer(address dst, uint wad) public returns (bool) {return transferFrom(msg.sender, dst, wad);}function transferFrom(address src, address dst, uint wad) public returns (bool) {require(balanceOf[src] >= wad);if (src != msg.sender && allowance[src][msg.sender] != uint(-1)) {require(allowance[src][msg.sender] >= wad);allowance[src][msg.sender] -= wad;}balanceOf[src] -= wad;balanceOf[dst] += wad;emit Transfer(src, dst, wad);return true;}}
```
/$
[PreviousNative Transfers](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/evm/native-transfers)
Last updated 59 minutes ago


---


---


---
