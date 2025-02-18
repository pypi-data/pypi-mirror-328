from ..clients import BlockOpenSearchClient, FundingClient, Web3LabelClient, PGClient, Web3Client
from ..utils.cache import file_cache
from typing import List, Dict, Union, Tuple, Any, Optional, defaultdict
import random
import logging
import asyncio

logger = logging.getLogger(__name__)

class AsyncClientProxy:
    def __init__(self, initialize_func):
        self._initialize_func = initialize_func
        self._client = None

    async def _get_client(self):
        """Initialize and return the actual client"""
        if self._client is None:
            self._client = await self._initialize_func()
        return self._client

    def __getattr__(self, name):
        """Returns a proxy for the method that will be called"""
        async def proxy_method(*args, **kwargs):
            client = await self._get_client()
            method = getattr(client, name)
            return await method(*args, **kwargs)
        return proxy_method


class DataCenter:
    """Central data management and processing hub"""

    def __init__(self, config_path: str = "config.yml"):
        """Initialize DataCenter

        Args:
            config_path: Path to config file
        """
        self.config_path = config_path
        self._initialized = False
        self._clients = {}
        self.cache = {}
    
    def __getattr__(self, name):
        """Lazily initialize and return client instances
        
        This method returns a proxy that handles both direct client access and method calls, e.g.:
        client = await dc.label_client
        or
        result = await dc.label_client.some_method()
        """
        if name not in self._clients:
            if name == 'label_client':
                self._clients[name] = AsyncClientProxy(self._initialize_label_client)
            elif name == 'pg_client':
                self._clients[name] = AsyncClientProxy(self._initialize_pg_client)
            elif name == 'web3_client':
                self._clients[name] = AsyncClientProxy(self._initialize_web3_client)
            elif name == 'blockos_client':
                self._clients[name] = AsyncClientProxy(self._initialize_blockos_client)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
        return self._clients[name]

    async def _initialize_label_client(self):
        """Initialize Web3LabelClient asynchronously"""
        client = Web3LabelClient(config_path=self.config_path)
        await client.setup()
        return client

    async def _initialize_pg_client(self):
        """Initialize PGClient asynchronously"""
        client = PGClient(config_path=self.config_path, db_name="local")
        await client.setup()
        return client

    async def _initialize_web3_client(self):
        """Initialize Web3Client asynchronously"""
        client = Web3Client(config_path=self.config_path)
        await client.setup()
        return client

    async def _initialize_blockos_client(self):
        """Initialize BlockOpenSearchClient asynchronously"""
        client = BlockOpenSearchClient(config_path=self.config_path)
        await client.setup()
        return client

    async def _initialize_blockos_client(self):
        """Initialize BlockOpenSearchClient asynchronously"""
        client = BlockOpenSearchClient(config_path=self.config_path)
        await client.setup()
        return client

    async def is_contract_batch(self, addresses: List[str], chain: str = 'eth') -> List[Optional[bool]]:
        """Check if multiple addresses are contracts in parallel.
        
        Args:
            addresses: List of addresses to check
            chain: Chain identifier (default: 'eth')
            
        Returns:
            List of booleans (True for contract, False for non-contract, None for errors)
            in same order as input addresses
        """
        from web3 import Web3
        try:
            # Create coroutines for each address
            web3_client = await self.web3_client._get_client()
            tasks = []
            for address in addresses:
                try:
                    if address == '':
                        tasks.append(asyncio.sleep(0))  # Dummy task for empty address
                        continue
                    checksum_address = Web3.to_checksum_address(address)
                    task = web3_client.eth.get_code(checksum_address)
                    tasks.append(task)
                except Exception as e:
                    logger.error(f"Invalid address {address}: {str(e)}")
                    tasks.append(None)
            
            # Filter out None tasks and keep track of indices
            valid_tasks = []
            task_indices = []
            for i, task in enumerate(tasks):
                if task is not None:
                    valid_tasks.append(task)
                    task_indices.append(i)
            
            # Execute valid tasks
            if valid_tasks:
                results = await asyncio.gather(*valid_tasks, return_exceptions=True)
            else:
                results = []
            
            # Prepare final results list
            final_results = [None] * len(addresses)
            
            # Fill in results for valid tasks
            for idx, result in zip(task_indices, results):
                if isinstance(result, Exception):
                    logger.error(f"Error checking contract for {addresses[idx]}: {str(result)}")
                else:
                    final_results[idx] = result != b''
            
            return final_results
            
        except Exception as e:
            logger.error(f"Error in batch contract check: {str(e)}")
            return [None] * len(addresses)

    async def sample_transactions(
        self,
        single_block: Optional[Union[int, str]] = None,
        block_range: Optional[Tuple[int, int]] = None,
        sample_size: int = 100,
        to_addr_range: Optional[Tuple[str, str]] = None,
        value_range: Optional[Tuple[int, int]] = None,
        gas_range: Optional[Tuple[int, int]] = None,
        four_bytes_list: Optional[List[str]] = None,
        random_seed: Optional[int] = None,
        full_transactions: int = 0
    ) -> Union[List[str], List[Dict]]:
        """Sample transactions from specified blocks.
        
        Args:
            single_block: Single block to sample from
            block_range: Range of blocks to sample from (inclusive)
            sample_size: Number of transactions to sample
            to_address_range: Range of 'to' addresses to filter
            value_range: Range of transaction values to filter
            gas_range: Range of gas used to filter
            four_bytes_list: List of 4-byte function signatures to filter
            random_seed: Random seed for reproducibility
            full_transactions: Level of transaction detail to return:
                0: Only transaction hashes
                1: Transaction data without logs
                2: Full transaction data with logs
            
        Returns:
            List of transaction hashes if full_transactions=0,
            otherwise list of transaction dictionaries
        """
        if random_seed is not None:
            random.seed(random_seed)
            
        filtered_txs = []
        
        # If single block specified, use that
        if single_block is not None:
            filtered_txs.extend(
                await self._fetch_and_filter_block(
                    block_identifier=single_block,
                    to_addr_range=to_addr_range,
                    value_range=value_range,
                    gas_range=gas_range,
                    four_bytes_list=four_bytes_list,
                    full_transactions=full_transactions
                )
            )
            
        # Otherwise use block range
        elif block_range is not None:
            start_block, end_block = block_range
            
            # Calculate how many blocks we need to sample to get enough transactions
            # Assuming average of 200 transactions per block
            avg_txs_per_block = 200
            num_blocks_needed = max(1, sample_size // avg_txs_per_block * 2)  # Double for safety
            
            # Sample blocks within range
            block_numbers = range(start_block, end_block + 1)
            sampled_blocks = random.sample(block_numbers, min(num_blocks_needed, len(block_numbers)))
            
            # Fetch transactions from sampled blocks
            for blk_num in sampled_blocks:
                filtered_txs.extend(
                    await self._fetch_and_filter_block(
                        block_identifier=blk_num,
                        to_addr_range=to_addr_range,
                        value_range=value_range,
                        gas_range=gas_range,
                        four_bytes_list=four_bytes_list,
                        full_transactions=full_transactions
                    )
                )
                
                # If we have enough transactions, stop sampling blocks
                if len(filtered_txs) >= sample_size:
                    break
            
            # If we still don't have enough transactions, sample more blocks
            while len(filtered_txs) < sample_size:
                # Sample a new block
                remaining_blocks = set(block_numbers) - set(sampled_blocks)
                if not remaining_blocks:
                    break
                    
                new_block = random.choice(list(remaining_blocks))
                sampled_blocks.append(new_block)
                
                filtered_txs.extend(
                    await self._fetch_and_filter_block(
                        block_identifier=new_block,
                        to_addr_range=to_addr_range,
                        value_range=value_range,
                        gas_range=gas_range,
                        four_bytes_list=four_bytes_list,
                        full_transactions=full_transactions
                    )
                )
        
        # If we have more transactions than needed, randomly sample
        if len(filtered_txs) > sample_size:
            filtered_txs = random.sample(filtered_txs, sample_size)
        # If we have fewer transactions than needed, raise an error
        elif len(filtered_txs) < sample_size:
            raise ValueError(f"Could not find {sample_size} transactions matching criteria. Only found {len(filtered_txs)}")
            
        return filtered_txs

    async def _fetch_and_filter_block(
        self,
        block_identifier: Union[int, str],
        to_addr_range: Optional[Tuple[str, str]],
        value_range: Optional[Tuple[int, int]],
        gas_range: Optional[Tuple[int, int]],
        four_bytes_list: Optional[List[str]],
        full_transactions: int = 0
    ) -> Union[List[str], List[Dict]]:
        """
        Fetch and filter transactions from a block based on criteria.
        Returns either transaction hashes or transaction objects based on full_transactions parameter.

        Args:
            block_identifier: Block number or hash
            to_addr_range: Range of 'to' addresses to filter
            value_range: Range of transaction values to filter
            gas_range: Range of gas used to filter
            four_bytes_list: List of 4-byte function signatures to filter
            full_transactions: Level of transaction detail to return:
                0: Only transaction hashes
                1: Transaction data without logs
                2: Full transaction data with logs

        Returns:
            List of transaction hashes if full_transactions=0,
            otherwise list of transaction dictionaries
        """
        web3_client = await self.web3_client._get_client()
        block = await web3_client.eth.get_block(block_identifier, full_transactions=True)
        transactions = block.transactions

        result = []
        for tx in transactions:
            if self._match_filters(
                tx,
                to_addr_range=to_addr_range,
                value_range=value_range,
                gas_range=gas_range,
                four_bytes_list=four_bytes_list
            ):
                if full_transactions == 0:
                    # Return only transaction hash
                    result.append("0x"+tx.hash.hex())
                elif full_transactions == 1:
                    # Return transaction data without logs
                    tx_dict = dict(tx)
                    result.append(tx_dict)
                else:  # full_transactions == 2
                    # Return full transaction data with logs
                    tx_dict = dict(tx)
                    try:
                        tx_receipt = self.w3_client.get_transaction_receipt(tx.hash)
                        tx_dict['receipt'] = dict(tx_receipt)
                    except Exception as e:
                        logger.warning(f"Failed to get receipt for tx {tx.hash.hex()}: {str(e)}")
                    result.append(tx_dict)

        return result

    def _match_filters(
        self,
        tx: Dict,
        to_addr_range: Optional[Tuple[str, str]],
        value_range: Optional[Tuple[int, int]],
        gas_range: Optional[Tuple[int, int]],
        four_bytes_list: Optional[List[str]],
    ) -> bool:
        if to_addr_range and tx["to"] is not None:
            start_to, end_to = to_addr_range
            to_lower = tx["to"].lower()
            if not (start_to.lower() <= to_lower <= end_to.lower()):
                return False

        if value_range:
            min_val, max_val = value_range
            if not (min_val <= tx["value"] <= max_val):
                return False

        if gas_range:
            min_gas, max_gas = gas_range
            if not (min_gas <= tx["gas"] <= max_gas):
                return False

        if four_bytes_list:
            tx_input = tx.get("input", "0x")
            if len(tx_input) < 10:
                return False


            method_id = tx_input[0:10].lower()
            if method_id not in [m.lower() for m in four_bytes_list]:
                return False

        return True

    async def sample_addresses(
        self,
        sample_size: int = 100,
        only_contracts: int = 0,
        single_block: Optional[Union[int, str]] = None,
        block_range: Optional[Tuple[int, int]] = None,
        random_seed: Optional[int] = None,
        address_type: str = 'both',  # 'from', 'to', or 'both'
        max_attempts: int = 3  # Maximum number of sampling attempts
    ) -> List[str]:
        """Sample addresses from transactions, optionally filtering for contracts.
        
        Args:
            sample_size: Number of addresses to sample
            only_contracts: If True, only return contract addresses
            single_block: Single block to sample from
            block_range: Range of blocks to sample from (inclusive)
            random_seed: Random seed for reproducibility
            address_type: Type of addresses to sample ('from', 'to', or 'both')
            max_attempts: Maximum number of attempts to find enough addresses
            
        Returns:
            List of sampled addresses
        """
        if random_seed is not None:
            random.seed(random_seed)
        
        all_addresses = set()
        attempt = 0
        multiplier = 2  # Initial sampling multiplier
        
        while attempt < max_attempts:
            # Sample transactions with increasing multiplier
            current_sample_size = sample_size * multiplier * (attempt + 1)
            transactions = await self.sample_transactions(
                single_block=single_block,
                block_range=block_range,
                sample_size=current_sample_size,
                random_seed=random_seed,
                full_transactions=1
            )
            
            # Extract addresses based on type
            for tx in transactions:
                if address_type in ('from', 'both') and tx.get('from'):
                    all_addresses.add(tx['from'])
                if address_type in ('to', 'both') and tx.get('to'):
                    all_addresses.add(tx['to'])
            
            addresses = list(all_addresses)
            
            # If we need contracts, filter them, only_contract=-1 means no contract, 0 means mix, 1 means only contract
            if only_contracts != 0:
                is_contract_results = await self.is_contract_batch(addresses)
                # Filter out None values and treat them as non-contracts
                contract_addresses = [
                    addr for addr, is_contract in zip(addresses, is_contract_results)
                    if is_contract
                ]
                
                if only_contracts == 1:
                    addresses = contract_addresses
                else:
                    addresses = [addr for addr in addresses if addr not in contract_addresses]
            
            # If we have enough addresses, break
            if len(addresses) >= sample_size:
                break
                
            attempt += 1
            
        # If we still don't have enough addresses after all attempts, raise error
        if len(addresses) < sample_size:
            raise ValueError(
                f"Could not find {sample_size} {'contract ' if only_contracts else ''}"
                f"addresses after {max_attempts} attempts. Only found {len(addresses)}"
            )
        
        # Randomly sample the required number of addresses
        sampled_addresses = random.sample(addresses, sample_size)
        return sampled_addresses

    @file_cache(namespace="all_txs", ttl=3600*24)  # Cache for 24 hours
    async def fetch_all_txs_from(self, address: str) -> List[Dict[str, Any]]:
        """Fetch all transactions from a single address.
        
        Args:
            address: The address to fetch transactions from
            
        Returns:
            List of dictionaries representing the transactions
        """

        tx_hashes = await self.blockos_client.fetch_all_txhashes_from(address)
        return await self.blockos_client.search_transaction_batch(tx_hashes)


    async def tx_entropy_of(self, address: str, tx_details: Dict[str, Any] = None) -> float:
        """Calculate the entropy of transactions based on multiple dimensions.
        
        Dimensions considered:
        - To address type (token/pair/normal contract/none)
        - Method ID
        - Gas price
        - Gas used
        - Value
        
        Returns:
            float: Entropy value representing transaction pattern complexity
        """
        import math
        
        if tx_details is None:
            tx_details = await self.fetch_all_txs_from(address)
        
        if not tx_details:
            return 0.0

        # Prepare address categorization
        counterparties = [tx['ToAddress'] for tx in tx_details.values()]
        is_contract_results = await self.is_contract_batch(counterparties)
        contract_counterparties = [
            addr for addr, is_contract in zip(counterparties, is_contract_results)
            if is_contract
        ]
        is_token_results = await self.is_token_contract_batch(contract_counterparties)
        token_counterparties = [
            addr for addr, is_token in zip(contract_counterparties, is_token_results)
            if is_token
        ]
        is_pair_results = await self.is_pair_contract_batch(contract_counterparties)
        pair_counterparties = [
            addr for addr, is_pair in zip(contract_counterparties, is_pair_results)
            if is_pair
        ]

        # Create address type mapping
        addr_type_map = {}
        for addr in counterparties:
            if addr in pair_counterparties:
                addr_type_map[addr] = 'pair'
            elif addr in token_counterparties:
                addr_type_map[addr] = 'token'
            elif addr in contract_counterparties:
                addr_type_map[addr] = 'normal'
            else:
                addr_type_map[addr] = 'eoa'
        # Prepare transaction feature vectors
        tx_features = []
        for tx in tx_details.values():
            to_addr = tx['ToAddress']
            feature = (
                addr_type_map[to_addr],  # Address type
                tx.get('MethodId', '0x'),  # Method ID
                # tx.get('GasPrice', 0),  # Gas price
                round(math.log10(tx.get('GasUsed', 0)),2),  # Gas used
                1 if int(tx.get('Value', 0)) / 1e18 > 0 else 0  # Whether there's value transfer
            )
            tx_features.append(feature)

        # Calculate frequency of each unique feature combination
        feature_counts = {}
        total_txs = len(tx_features)
        for feature in tx_features:
            feature_counts[feature] = feature_counts.get(feature, 0) + 1

        # Calculate entropy
        entropy = 0.0
        for count in feature_counts.values():
            probability = count / total_txs
            entropy -= probability * math.log2(probability)

        return entropy

    async def is_token_contract_batch(self, addresses: List[str], chain: str = 'Ethereum') -> List[bool]:
        if not addresses:
            return []
        query = """
        SELECT address::text, EXISTS (
            SELECT 1 FROM token_info 
            WHERE address = ANY($1::text[]) AND chain = $2
        ) AS is_token
        FROM unnest($1::text[]) AS address
        """
        results = await self.pg_client.execute(query, (addresses, chain))
        return [result['is_token'] for result in results]

    async def is_pair_contract_batch(self, addresses: List[str], chain_id: int = 1) -> List[bool]:
        if not addresses:
            return []
        query = """
        SELECT address::text, EXISTS (
            SELECT 1 FROM pair_info 
            WHERE pair = ANY($1::text[]) AND chain_id = $2
        ) AS is_pair
        FROM unnest($1::text[]) AS address
        """
        results = await self.pg_client.execute(query, (addresses, chain_id))
        return [result['is_pair'] for result in results]


    async def is_automated_address(self, address: str, chain_id: int = 1) -> bool:
        """Check if an address is automated based on transaction patterns"""
        try:
            address = address.lower()
            first_interactions = await self.blockos_client.first_sent_transaction_batch([address])
            interactions_counts = await self.blockos_client.search_sent_transaction_count_batch([address])

            # Get current block number using web3 client
            web3_client = await self.web3_client._get_client()
            current_block = await web3_client.eth.block_number

            # print(first_interactions)
            # print(interactions_counts)
            # Frequency
            if not first_interactions.get(address) or 'first_tx_block' not in first_interactions[address]:
                return False
            # print("current block is", current_block, type(current_block))
            # print("first tx block is", first_interactions[address]['first_tx_block'], type(first_interactions[address]['first_tx_block']))
            days = (current_block - first_interactions[address]['first_tx_block']) / 300
            years = days / 365
            if years <= 0:
                return False
            avg_txs_per_year = interactions_counts[address]['totalTxCount'] / years
            # If more than 3000 transactions per year on average, consider it automated
            if avg_txs_per_year > 3000:
                return True

            tx_details = await self.fetch_all_txs_from(address)

            # Check for transactions in consecutive blocks
            block_numbers = sorted(int(tx['Block']) for tx in tx_details.values())

            for i in range(len(block_numbers) - 1):
                if block_numbers[i + 1] - block_numbers[i] <= 1:
                    return True

            # Check for high daily transaction count
            daily_tx_counts = defaultdict(int)
            for tx in tx_details.values():
                date = tx['Timestamp'][:10]  # Extract date part
                daily_tx_counts[date] += 1
            
            max_daily_txs = max(daily_tx_counts.values(), default=0)
            if max_daily_txs > 280:
                return True

            # Check trading bot usage
            automated_addresses = {
                '0x3328f7f4a1d1c57c35df56bbf0c9dcafca309c49',  # BANANA
                '0xdb5889e35e379ef0498aae126fc2cce1fbd23216',  # BANANA Old
                '0x80a64c6d7f12c47b7c66c5b4e20e72bc1fcd5d9e',  # Maestro
                '0x50b8f49f4b2e80e09ce8015c4e7a9c277738fd3d',  # AIMBOT
                '0x6a153cdf5cc58f47c17d6a6b0187c25c86d1acfd',  # Prophet
                '0x3999d2c5207c06bbc5cf8a6bea52966cabb76d41'   # Unibot
            }
            if any(tx['ToAddress'].lower() in automated_addresses for tx in tx_details.values()):
                return True
            
            address_entropy = await self.tx_entropy_of(address, tx_details)
            if address_entropy < 3:
                return True
            return False
        except Exception as e:
            logger.error(f"Error checking address automation: {address} {str(e)}")
            return False

    async def close(self) -> None:
        """Close all clients and clean up resources"""
        if self._initialized:
            await asyncio.gather(*(
                client.close() for client in self._clients.values()
            ))
            self._clients.clear()
            self._initialized = False

    # async def get_addresses_labels(self, addresses: List[str]) -> List[Dict[str, Any]]:
    #     """Get labels for a list of addresses"""
    #     try:
    #         label_client = await self.label_client
    #         return await label_client.get_addresses_labels(addresses)
    #     except Exception as e:
    #         logger.error(f"Error getting address labels: {str(e)}")
    #         return []

    # async def get_addresses_by_label(self, label: str, chain_id: int = 1) -> List[Dict[str, Any]]:
    #     """Find addresses by label"""
    #     try:
    #         label_client = await self.label_client
    #         return await label_client.get_addresses_by_label(label, chain_id)
    #     except Exception as e:
    #         logger.error(f"Error getting addresses by label: {str(e)}")
    #         return []
            
    # async def get_addresses_by_type(self, type_category: str, chain_id: int = 1) -> List[Dict[str, Any]]:
    #     """Find addresses by type"""
    #     try:
    #         label_client = await self.label_client
    #         return await label_client.get_addresses_by_type(type_category, chain_id)
    #     except Exception as e:
    #         logger.error(f"Error getting addresses by type: {str(e)}")
    #         return []