# One-shot Bankr deployment prompt

**Ready for mainnet deployment?** Replace `YOUR_PUBLIC_REPOSITORY_URL` with the URL of your own public repository containing the exported `collection/artwork.json` and `collection/config.json`. Post the prompt below on X. The prompt **authorizes deployment and gas spending**, not minting. It intentionally starts with `@bankrbot`.

---

@bankrbot create and deploy a fully on-chain generative NFT collection on Robinhood Chain using my Mintbay Studio artwork and configuration.

Everything you need is here:
YOUR_PUBLIC_REPOSITORY_URL

Use this skill for creating NFT collections:
https://netprotocol.app/skill.md

Follow `collection/config.json` and `collection/artwork.json` exactly. Use the existing Net Protocol base specified by the repository configuration without changing its Net integration.

Generate, compile, deploy, and verify the collection on Robinhood Etherscan (https://robin.etherscan.io).

Return the collection address, deployment transaction hash, and Etherscan verification links. Do not mint NFTs or execute unrelated transactions.

---

**Note:** The creator/admin address, price, supply, royalties and optional features come from the JSON configuration, not the social post. If compilation or deployment fails, report the error; do not deploy a different implementation or change networks/admins to work around it. Some Net registration messages may create auxiliary on-chain data contracts; these are not necessarily separately verifiable Solidity implementations.

For an optional no-transaction test, see [`BANKR_BASE_PROMPT.md`](BANKR_BASE_PROMPT.md). For creator minting *after* deployment, see [`BANKR_CREATOR_MINT_PROMPT.md`](BANKR_CREATOR_MINT_PROMPT.md).
