# Bankr creator mint prompt — separate from deployment

Use only **after** the collection is deployed and you know its contract address and creator allowance. Replace all placeholders. This prompt **authorizes an on-chain mint transaction**. It starts with `@bankrbot` for X.

---

@bankrbot mint **QUANTITY** NFTs from the creator allowance of my fully on-chain collection on Robinhood Chain:

COLLECTION_CONTRACT_ADDRESS

Execute `mintToCreator(QUANTITY, RECIPIENT_ADDRESS)` from the collection's authorized administrator account. Send the NFTs to:

RECIPIENT_ADDRESS

If the administrator is a HoodWallet, execute the call **through that HoodWallet**, with the connected EOA paying gas where supported. Do not call from the EOA directly unless it is the authorized administrator.

Use the creator allowance, not the paid public mint or Hoodie free-claim function. Submit only one mint transaction and return the transaction hash, token IDs and https://robin.etherscan.io links.

---

**Important:** Check the available creator allowance and current supply before posting. A creator allowance is a limit, not a guaranteed reserved allocation. Some wallets require a specific contract-execution/delegation flow; do not claim this works for every wallet or invent an execution route.
