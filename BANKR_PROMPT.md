# Public Bankr deployment prompt (use only after source review)

Replace `YOUR_PUBLIC_REPOSITORY_URL` with **your own public fork**. Sending this prompt explicitly requests a mainnet deployment if the checks pass. To test without deployment, use **`BANKR_BASE_PROMPT.md`** instead.

---

Hey @bankrbot, let's try something!

I created a generative pixel-art collection in **https://studio.mintbay.xyz**, and I'd like to turn it into a fully on-chain NFT collection.

My GitHub repository is: **YOUR_PUBLIC_REPOSITORY_URL**

Use the official Net Protocol skill: **https://netprotocol.app/skill.md**

Read `collection/artwork.json`, `collection/config.json`, `NET_BASE_GUIDE.md`, and `ADDONS.md`. Use the **existing** Net base specified in `deployment.baseContract` without modifying its registration or mint/transfer/burn messaging. Generate only the collection-specific art renderer, metadata and enabled features using the actual GitHub files — don't invent settings or artwork.

First verify that the Solidity compiles, that SVG/metadata are fully on-chain, that all selected mint limits and administration settings match `config.json`, and that runtime bytecode fits EVM limits. If anything is missing, incompatible or unverifiable, stop and explain before submitting a transaction.

If these checks pass, **deploy one collection** on the network configured in `collection.chainId` and verify the full source code on the chain explorer. Return the collection address, deployment transaction hash, explorer link and verification status. Confirm Net collection registration if it can be verified.

**Do not mint NFTs, transfer tokens, withdraw ETH, configure optional contracts or execute additional transactions. Do not switch networks or administrator addresses to work around a problem.**

Please show the anticipated deployment gas cost and ask for my confirmation before submitting the deployment transaction whenever supported.

Let's see if pixel art can become a fully on-chain collection!
