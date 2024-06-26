import json

# universal contracts (cross chain)
MULTICALL_3_NETWORK_TO_ADDRESS_MAPPING = {
    "MAINNET": "",
    "LINEA-MAINNET": "0xcA11bde05977b3631167028862bE2a173976CA11",
}

# contracts specific
CONTRACTS_NETWORK_ADDRESS_TO_NAME_AND_ABI_MAPPING = {
    "MAINNET": {},
    "LINEA-MAINNET": {
            "0xAAA75a605C2f245A30Fb4299E5CDfBF6B4FB30B6": {
                "name": "nile_lens",
                "abi": json.loads("""[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"address[]","name":"poolAddresses","type":"address[]"},{"internalType":"uint256","name":"maxReturn","type":"uint256"}],"name":"addressEarned","outputs":[{"components":[{"internalType":"address","name":"poolAddress","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct Lens.Earned[]","name":"earnings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"maxReturn","type":"uint256"}],"name":"addressEarnedCl","outputs":[{"components":[{"internalType":"address","name":"poolAddress","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct Lens.Earned[]","name":"earnings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"uint256","name":"skip","type":"uint256"},{"internalType":"address[]","name":"rewardTokens","type":"address[]"},{"internalType":"uint256","name":"maxReturn","type":"uint256"}],"name":"addressEarnedClPageable","outputs":[{"internalType":"bool","name":"finished","type":"bool"},{"internalType":"uint256","name":"currentNfpIndex","type":"uint256"},{"components":[{"internalType":"address","name":"poolAddress","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct Lens.Earned[]","name":"earnings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"gaugeAddress","type":"address"},{"internalType":"address","name":"rewardToken","type":"address"}],"name":"addressEarnedClSingle","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"},{"internalType":"address","name":"gaugeAddress","type":"address"},{"internalType":"address","name":"rewardToken","type":"address"}],"name":"addressEarnedSingle","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allActivePools","outputs":[{"internalType":"address[]","name":"pools","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allFeeDistributors","outputs":[{"internalType":"address[]","name":"feeDistributors","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allGauges","outputs":[{"internalType":"address[]","name":"gauges","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPools","outputs":[{"internalType":"address[]","name":"pools","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPoolsInfo","outputs":[{"components":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"bool","name":"stable","type":"bool"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"address","name":"gauge","type":"address"},{"internalType":"address","name":"feeDistributor","type":"address"},{"internalType":"address","name":"pairFees","type":"address"},{"internalType":"uint256","name":"pairBps","type":"uint256"}],"internalType":"struct Lens.Pool[]","name":"_poolsInfo","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"allPoolsRewardData","outputs":[{"components":[{"internalType":"address","name":"gauge","type":"address"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"rewardRate","type":"uint256"}],"internalType":"struct Lens.tokenRewardData[]","name":"rewardData","type":"tuple[]"}],"internalType":"struct Lens.gaugeRewardsData[]","name":"rewardsData","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"bribeRewardsForPool","outputs":[{"internalType":"address[]","name":"rewards","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"pool","type":"address"}],"name":"bribesPositionOf","outputs":[{"components":[{"internalType":"address","name":"feeDistributor","type":"address"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"earned","type":"uint256"}],"internalType":"struct Lens.userBribeTokenData[]","name":"bribeData","type":"tuple[]"}],"internalType":"struct Lens.userFeeDistData","name":"rewardsData","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"emissionsTokenAddress","outputs":[{"internalType":"address","name":"emissionsToken","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeDistributorFactory","outputs":[{"internalType":"address","name":"_gaugeFactory","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"feeDistributorForPool","outputs":[{"internalType":"address","name":"feeDistributor","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gaugeFactory","outputs":[{"internalType":"address","name":"_gaugeFactory","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"gaugeForPool","outputs":[{"internalType":"address","name":"gauge","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"gaugeRewardsForPool","outputs":[{"internalType":"address[]","name":"rewards","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IVoter","name":"_voter","type":"address"},{"internalType":"address","name":"_router","type":"address"},{"internalType":"address","name":"_v2Factory","type":"address"},{"internalType":"address","name":"_v2Nfp","type":"address"},{"internalType":"address","name":"_v2Router","type":"address"},{"internalType":"address","name":"_v2QuoterV2","type":"address"},{"internalType":"address","name":"_v2PairFlash","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"minter","outputs":[{"internalType":"contract IMinter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minterAddress","outputs":[{"internalType":"address","name":"_minter","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"pairBps","outputs":[{"internalType":"uint256","name":"bps","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolFactory","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"poolInfo","outputs":[{"components":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"bool","name":"stable","type":"bool"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"address","name":"gauge","type":"address"},{"internalType":"address","name":"feeDistributor","type":"address"},{"internalType":"address","name":"pairFees","type":"address"},{"internalType":"uint256","name":"pairBps","type":"uint256"}],"internalType":"struct Lens.Pool","name":"_poolInfo","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"poolRewardsData","outputs":[{"components":[{"internalType":"address","name":"gauge","type":"address"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"rewardRate","type":"uint256"}],"internalType":"struct Lens.tokenRewardData[]","name":"rewardData","type":"tuple[]"}],"internalType":"struct Lens.gaugeRewardsData","name":"rewardData","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"pools","type":"address[]"}],"name":"poolsRewardsData","outputs":[{"components":[{"internalType":"address","name":"gauge","type":"address"},{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"rewardRate","type":"uint256"}],"internalType":"struct Lens.tokenRewardData[]","name":"rewardData","type":"tuple[]"}],"internalType":"struct Lens.gaugeRewardsData[]","name":"rewardsData","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolMetadata","outputs":[{"components":[{"internalType":"address","name":"veAddress","type":"address"},{"internalType":"address","name":"emissionsTokenAddress","type":"address"},{"internalType":"address","name":"voterAddress","type":"address"},{"internalType":"address","name":"poolsFactoryAddress","type":"address"},{"internalType":"address","name":"gaugesFactoryAddress","type":"address"},{"internalType":"address","name":"minterAddress","type":"address"}],"internalType":"struct Lens.ProtocolMetadata","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsDistributor","outputs":[{"internalType":"address","name":"_rewardsDistributor","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address[]","name":"poolAddresses","type":"address[]"},{"internalType":"address[][]","name":"rewardTokens","type":"address[][]"},{"internalType":"uint256","name":"maxReturn","type":"uint256"}],"name":"tokenIdEarned","outputs":[{"components":[{"internalType":"address","name":"poolAddress","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"internalType":"struct Lens.Earned[]","name":"earnings","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"feeDistributorAddress","type":"address"},{"internalType":"address","name":"rewardToken","type":"address"}],"name":"tokenIdEarnedSingle","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenIdRebase","outputs":[{"internalType":"uint256","name":"rebase","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v2Factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v2Nfp","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v2PairFlash","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v2QuoterV2","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"v2Router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ve","outputs":[{"internalType":"contract IVotingEscrow","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"veNFTsOf","outputs":[{"internalType":"uint256[]","name":"NFTs","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"vePositionsOf","outputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"lockedAmount","type":"uint256"},{"internalType":"uint256","name":"votingPower","type":"uint256"},{"internalType":"uint256","name":"lockEnd","type":"uint256"}],"internalType":"struct Lens.userVeData[]","name":"veData","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"voter","outputs":[{"internalType":"contract IVoter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"voterAddress","outputs":[{"internalType":"address","name":"_voter","type":"address"}],"stateMutability":"view","type":"function"}]""")                
            },
            "0xAAA32926fcE6bE95ea2c51cB4Fcb60836D320C42": {
                "name": "nile-factory",
                "abi": json.loads("""[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":true,"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"FeeAmountEnabled","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldFeeCollector","type":"address"},{"indexed":true,"internalType":"address","name":"newFeeCollector","type":"address"}],"name":"FeeCollectorChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldSetter","type":"address"},{"indexed":true,"internalType":"address","name":"newSetter","type":"address"}],"name":"FeeSetterChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldImplementation","type":"address"},{"indexed":true,"internalType":"address","name":"newImplementation","type":"address"}],"name":"ImplementationChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":true,"internalType":"uint24","name":"fee","type":"uint24"},{"indexed":false,"internalType":"int24","name":"tickSpacing","type":"int24"},{"indexed":false,"internalType":"address","name":"pool","type":"address"}],"name":"PoolCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0New","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],"name":"SetFeeProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"pool","type":"address"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0New","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],"name":"SetPoolFeeProtocol","type":"event"},{"inputs":[],"name":"POOL_INIT_CODE_HASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"createPool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickSpacing","type":"int24"}],"name":"enableFeeAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint24","name":"","type":"uint24"}],"name":"feeAmountTickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeCollector","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeProtocol","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint24","name":"","type":"uint24"}],"name":"getPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_nfpManager","type":"address"},{"internalType":"address","name":"_votingEscrow","type":"address"},{"internalType":"address","name":"_voter","type":"address"},{"internalType":"address","name":"_implementation","type":"address"},{"internalType":"address","name":"_feeSetter","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initializePool","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nfpManager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"}],"name":"poolFeeProtocol","outputs":[{"internalType":"uint8","name":"__poolFeeProtocol","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_pool","type":"address"},{"internalType":"uint24","name":"_fee","type":"uint24"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeCollector","type":"address"}],"name":"setFeeCollector","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint8","name":"_feeProtocol","type":"uint8"}],"name":"setFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newFeeSetter","type":"address"}],"name":"setFeeSetter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_implementation","type":"address"}],"name":"setImplementation","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"uint8","name":"_feeProtocol","type":"uint8"}],"name":"setPoolFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"pool","type":"address"},{"internalType":"uint8","name":"feeProtocol0","type":"uint8"},{"internalType":"uint8","name":"feeProtocol1","type":"uint8"}],"name":"setPoolFeeProtocol","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"voter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"votingEscrow","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]"""),
            },
            "0xC17680F80Acf72C2dc78EC6E2b36161c3206973A": {
                "name": "multi_rewards_staking",
                "abi": json.loads("""[{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_stakingToken","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"isPaused","type":"bool"}],"name":"PauseChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Recovered","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"reward","type":"uint256"}],"name":"RewardAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"rewardsToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"reward","type":"uint256"}],"name":"RewardPaid","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"newDuration","type":"uint256"}],"name":"RewardsDurationUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Staked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawn","type":"event"},{"constant":false,"inputs":[],"name":"acceptOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"address","name":"_rewardsDistributor","type":"address"},{"internalType":"uint256","name":"_rewardsDuration","type":"uint256"}],"name":"addReward","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"_rewardsToken","type":"address"}],"name":"earned","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"exit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"getReward","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"}],"name":"getRewardForDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"lastPauseTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"}],"name":"lastTimeRewardApplicable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"uint256","name":"reward","type":"uint256"}],"name":"notifyRewardAmount","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"}],"name":"recoverERC20","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"rewardData","outputs":[{"internalType":"address","name":"rewardsDistributor","type":"address"},{"internalType":"uint256","name":"rewardsDuration","type":"uint256"},{"internalType":"uint256","name":"periodFinish","type":"uint256"},{"internalType":"uint256","name":"rewardRate","type":"uint256"},{"internalType":"uint256","name":"lastUpdateTime","type":"uint256"},{"internalType":"uint256","name":"rewardPerTokenStored","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"}],"name":"rewardPerToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewardTokens","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"rewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bool","name":"_paused","type":"bool"}],"name":"setPaused","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"address","name":"_rewardsDistributor","type":"address"}],"name":"setRewardsDistributor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"uint256","name":"_rewardsDuration","type":"uint256"}],"name":"setRewardsDuration","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"stakingToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"userRewardPerTokenPaid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""),
            }
    }
}