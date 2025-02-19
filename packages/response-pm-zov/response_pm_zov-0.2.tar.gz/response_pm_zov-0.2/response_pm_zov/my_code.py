def get_erc():
    return """
    // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract GerdaCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("GerdaCoin", "GERDA") {
        _mint(msg.sender, initialSupply);
    }
}

contract KrendelCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("KrendelCoin", "KRENDEL") {
        _mint(msg.sender, initialSupply);
    }
}

contract RTKCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("RTKCoin", "RTK") {
        _mint(msg.sender, initialSupply);
    }
}

contract Professional is ERC20 {
    constructor(uint256 initialSupply) ERC20("Professional", "PROFI") {
        _mint(msg.sender, initialSupply);
    }
}

    """



def get_factory():
    return """
    // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./Pool.sol";

contract Factory {
    mapping(address => address) public getPool;
    address[] public allPools;

    function createPool(address tokenA, address tokenB) external returns (address pool) {
        require(tokenA != tokenB, "Factory: IDENTICAL_ADDRESSES");
        (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
        require(token0 != address(0), "Factory: ZERO_ADDRESS");
        require(getPool[token0] == address(0), "Factory: POOL_EXISTS");
        bytes memory bytecode = type(Pool).creationCode;
        bytes32 salt = keccak256(abi.encodePacked(token0, token1));
        assembly {
            pool := create2(0, add(bytecode, 32), mload(bytecode), salt)
        }
        Pool(pool).initialize(token0, token1);
        getPool[token0] = pool;
        allPools.push(pool);
    }
}


    """

def get_pool():
    return """
    // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Pool {
    address public token0;
    address public token1;
    uint256 public reserve0;
    uint256 public reserve1;

    function initialize(address _token0, address _token1) external {
        token0 = _token0;
        token1 = _token1;
    }

    function addLiquidity(uint256 amount0, uint256 amount1) external {
        IERC20(token0).transferFrom(msg.sender, address(this), amount0);
        IERC20(token1).transferFrom(msg.sender, address(this), amount1);
        reserve0 += amount0;
        reserve1 += amount1;
    }

    function swap(uint256 amount0Out, uint256 amount1Out, address to) external {
        require(amount0Out > 0 || amount1Out > 0, "Pool: INSUFFICIENT_OUTPUT_AMOUNT");
        (uint256 _reserve0, uint256 _reserve1) = (reserve0, reserve1);
        require(amount0Out < _reserve0 && amount1Out < _reserve1, "Pool: INSUFFICIENT_LIQUIDITY");

        if (amount0Out > 0) IERC20(token0).transfer(to, amount0Out);
        if (amount1Out > 0) IERC20(token1).transfer(to, amount1Out);
        reserve0 = _reserve0 - amount0Out;
        reserve1 = _reserve1 - amount1Out;
    }
}

"""

def get_router():
    return """
    // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./Factory.sol";
import "./Pool.sol";

contract Router {
    Factory public factory;

    constructor(address _factory) {
        factory = Factory(_factory);
    }

    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to
    ) external {
        require(path.length >= 2, "Router: INVALID_PATH");
        
        // Get pool address directly using token addresses
        address poolAddress = factory.getPool(path[0]);
        Pool pool = Pool(poolAddress);
        
        IERC20(path[0]).transferFrom(msg.sender, address(pool), amountIn);
        pool.swap(amountOutMin, 0, to);
    }
}
"""

def get_staking():
    return """
    // SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Staking {
    IERC20 public lpToken;
    uint256 public rewardPerSecond = 13;
    mapping(address => uint256) public staked;
    mapping(address => uint256) public lastRewardTime;

    constructor(address _lpToken) {
        lpToken = IERC20(_lpToken);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        lpToken.transferFrom(msg.sender, address(this), amount);
        staked[msg.sender] += amount;
        lastRewardTime[msg.sender] = block.timestamp;
    }

    function withdraw(uint256 amount) external {
        require(staked[msg.sender] >= amount, "Staking: INSUFFICIENT_STAKED");
        staked[msg.sender] -= amount;
        lpToken.transfer(msg.sender, amount);
    }

    function getReward() external view returns (uint256) {
        uint256 timeDiff = block.timestamp - lastRewardTime[msg.sender];
        return staked[msg.sender] * timeDiff * rewardPerSecond;
    }
}

"""

def get_deploy():
    return """
    const hre = require("hardhat");
const { ethers } = hre;

async function main() {
    const [owner, tom, ben, rick] = await hre.ethers.getSigners();

    // Step 1: Deploy tokens
    const GerdaCoin = await hre.ethers.getContractFactory("GerdaCoin");
    const gerdaCoin = await GerdaCoin.deploy(ethers.parseUnits("1000000", 18));
    await gerdaCoin.waitForDeployment();
    const GERDA_ADDRESS = await gerdaCoin.getAddress();
    console.log("GerdaCoin deployed to:", GERDA_ADDRESS);

    const KrendelCoin = await hre.ethers.getContractFactory("KrendelCoin");
    const krendelCoin = await KrendelCoin.deploy(ethers.parseUnits("1500000", 18));
    await krendelCoin.waitForDeployment();
    const KRENDEL_ADDRESS = await krendelCoin.getAddress();
    console.log("KrendelCoin deployed to:", KRENDEL_ADDRESS);

    const RTKCoin = await hre.ethers.getContractFactory("RTKCoin");
    const rtkCoin = await RTKCoin.deploy(ethers.parseUnits("3000000", 18));
    await rtkCoin.waitForDeployment();
    const RTK_ADDRESS = await rtkCoin.getAddress();
    console.log("RTKCoin deployed to:", RTK_ADDRESS);

    // Step 2: Deploy Factory
    const Factory = await hre.ethers.getContractFactory("Factory");
    const factory = await Factory.deploy();
    await factory.waitForDeployment();
    const FACTORY_ADDRESS = await factory.getAddress();
    console.log("Factory deployed to:", FACTORY_ADDRESS);

    // Step 3: Deploy Router
    const Router = await hre.ethers.getContractFactory("Router");
    const router = await Router.deploy(FACTORY_ADDRESS);
    await router.waitForDeployment();
    const ROUTER_ADDRESS = await router.getAddress();
    console.log("Router deployed to:", ROUTER_ADDRESS);

    // Step 4: Distribute tokens to Tom and Ben
    const transferAmount = ethers.parseUnits("10000", 18);
    await gerdaCoin.transfer(tom.address, transferAmount);
    await krendelCoin.transfer(tom.address, transferAmount);
    await rtkCoin.transfer(tom.address, transferAmount);
    await gerdaCoin.transfer(ben.address, transferAmount);
    await krendelCoin.transfer(ben.address, transferAmount);
    await rtkCoin.transfer(ben.address, transferAmount);
    console.log("Toms address:", tom.address);
    console.log("Bens address:", ben.address);
    console.log("Tokens distributed to Tom and Ben");

    // Step 5: Create GERDA-KRENDEL pool
    const createPoolTx = await factory.createPool(GERDA_ADDRESS, KRENDEL_ADDRESS);
    await createPoolTx.wait();
    const poolAddress = await factory.getPool(GERDA_ADDRESS);
    if (poolAddress === "0x0000000000000000000000000000000000000000") {
        console.error("Pool creation failed!");
        return;
    }
    console.log("GERDA-KRENDEL pool created at:", poolAddress);

    // Step 6: Deploy Staking
    const Staking = await hre.ethers.getContractFactory("Staking");
    const staking = await Staking.deploy(poolAddress);
    await staking.waitForDeployment();
    const STAKING_ADDRESS = await staking.getAddress();
    console.log("Staking deployed to:", STAKING_ADDRESS);

    // Step 7: Add liquidity to GERDA-KRENDEL pool
    const amountGerda = ethers.parseUnits("1000", 18);
    const amountKrendel = ethers.parseUnits("1000", 18);
    await gerdaCoin.connect(tom).approve(poolAddress, amountGerda);
    await krendelCoin.connect(tom).approve(poolAddress, amountKrendel);

    // Проверка одобрения
    const tomGerdaAllowance = await gerdaCoin.allowance(tom.address, poolAddress);
    const tomKrendelAllowance = await krendelCoin.allowance(tom.address, poolAddress);
    console.log("Tom's GERDA allowance:", ethers.formatUnits(tomGerdaAllowance, 18));
    console.log("Tom's KRENDEL allowance:", ethers.formatUnits(tomKrendelAllowance, 18));

    const pool = await hre.ethers.getContractAt("Pool", poolAddress);
    await pool.connect(tom).addLiquidity(amountGerda, amountKrendel);
    console.log("Liquidity added to GERDA-KRENDEL pool");

    // Step 8: Stake LP tokens
    const lpToken = await hre.ethers.getContractAt("IERC20", poolAddress);
    const lpBalance = await lpToken.balanceOf(tom.address);

    // Проверка баланса LP токенов
    console.log("Tom's LP token balance:", ethers.formatUnits(lpBalance, 18));

    if (lpBalance.eq(0)) {
        console.error("Tom has no LP tokens to stake!");
        return;
    }

    // Одобрение передачи LP токенов
    await lpToken.connect(tom).approve(STAKING_ADDRESS, lpBalance);

    // Проверка одобрения
    const allowance = await lpToken.allowance(tom.address, STAKING_ADDRESS);
    console.log("Tom's LP token allowance for Staking:", ethers.formatUnits(allowance, 18));

    if (allowance.lt(lpBalance)) {
        console.error("Insufficient allowance for staking!");
        return;
    }

    // Вызов функции stake
    try {
        const tx = await staking.connect(tom).stake(lpBalance, { gasLimit: 7000000 });
        await tx.wait();
        console.log("LP tokens staked by Tom");
    } catch (error) {
        console.error("Error calling stake function:", error.message);
    }
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
get_checkconst hre = require("hardhat");

async function main() {
  const [owner] = await hre.ethers.getSigners();
  
  // Получаем контракты
  const GerdaCoin = await hre.ethers.getContractAt("GerdaCoin", "0x5FbDB2315678afecb367f032d93F642f64180aa3");
  const KrendelCoin = await hre.ethers.getContractAt("KrendelCoin", "0x5FbDB2315678afecb367f032d93F642f64180aa3");
  const RTKCoin = await hre.ethers.getContractAt("RTKCoin", "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0");

  // Проверяем балансы
  const gerdaBalance = await GerdaCoin.balanceOf(owner.address);
  const krendelBalance = await KrendelCoin.balanceOf(owner.address);
  const rtkBalance = await RTKCoin.balanceOf(owner.address);

  console.log("Балансы:");
  console.log("GerdaCoin:", gerdaBalance.toString());
  console.log("KrendelCoin:", krendelBalance.toString());
  console.log("RTKCoin:", rtkBalance.toString());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });


"""

def get_check_balance():
    return """
    async function checkBalances(gerdaCoin, krendelCoin, rtkCoin, tom, ben) {
    try {
        // Получаем балансы Tom
        const tomGerdaBalance = await gerdaCoin.balanceOf(tom.address);
        const tomKrendelBalance = await krendelCoin.balanceOf(tom.address);
        const tomRTKBalance = await rtkCoin.balanceOf(tom.address);

        // Получаем балансы Ben
        const benGerdaBalance = await gerdaCoin.balanceOf(ben.address);
        const benKrendelBalance = await krendelCoin.balanceOf(ben.address);
        const benRTKBalance = await rtkCoin.balanceOf(ben.address);

        // Выводим балансы Tom
        console.log("Tom's Balances:");
        console.log(`  GERDA: ${ethers.formatUnits(tomGerdaBalance, 18)} GERDA`);
        console.log(`  KRENDEL: ${ethers.formatUnits(tomKrendelBalance, 18)} KRENDEL`);
        console.log(`  RTK: ${ethers.formatUnits(tomRTKBalance, 18)} RTK`);

        // Выводим балансы Ben
        console.log("Ben's Balances:");
        console.log(`  GERDA: ${ethers.formatUnits(benGerdaBalance, 18)} GERDA`);
        console.log(`  KRENDEL: ${ethers.formatUnits(benKrendelBalance, 18)} KRENDEL`);
        console.log(`  RTK: ${ethers.formatUnits(benRTKBalance, 18)} RTK`);
    } catch (error) {
        console.error("Error checking balances:", error);
    }
}
"""

def get_create_pool():
    return """
    const hre = require("hardhat");

async function main() {
    const [signer] = await hre.ethers.getSigners();

    // Deploy Factory
    const Factory = await hre.ethers.getContractFactory("Factory");
    const factory = await Factory.deploy();
    const factoryAddress = await factory.getAddress();
    console.log("Factory deployed to:", factoryAddress);

    // Wait for deployment
    await factory.waitForDeployment();
    
    const GERDA_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
    const KRENDEL_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";

    // Create pool
    const createPoolTx = await factory.createPool(GERDA_ADDRESS, KRENDEL_ADDRESS);
    await createPoolTx.wait();

    // Get pool address
    const poolAddress = await factory.getPool(GERDA_ADDRESS);
    console.log("New pool created at:", poolAddress);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });

"""

def get_swap():
    return """
    const hre = require("hardhat");

async function main() {
    const [signer] = await hre.ethers.getSigners();
    
    // Get token contracts
    const GERDA_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
    const KRENDEL_ADDRESS = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";
    const POOL_ADDRESS = "0x0e0f80E81c209Ee880b33dD96BAE96538bCE30D1";
    
    const gerdaCoin = await hre.ethers.getContractAt("GerdaCoin", GERDA_ADDRESS);
    const pool = await hre.ethers.getContractAt("Pool", POOL_ADDRESS);
    
    // Approve tokens for swap
    const amountIn = "1000";
    await gerdaCoin.approve(POOL_ADDRESS, amountIn);
    
    // Perform swap directly through pool
    await pool.swap(amountIn, "0", signer.address);
    
    console.log("Swap completed successfully!");
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });


get hardhat 
/** @type import('hardhat/config').HardhatUserConfig */
require("@nomicfoundation/hardhat-toolbox");
module.exports = {
  solidity: "0.8.20",
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545"
    },
    """
