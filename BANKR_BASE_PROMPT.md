# Bankr read-only test prompt (no blockchain transactions)

Replace `YOUR_PUBLIC_REPOSITORY_URL` with **your own public fork URL**.

---

Hey @bankrbot, I made a generative pixel-art collection using Mintbay Studio and want to turn it into a fully on-chain NFT collection.

My GitHub repository: **YOUR_PUBLIC_REPOSITORY_URL**

Use the official Net Protocol skill: https://netprotocol.app/skill.md

Please read `NET_BASE_GUIDE.md`, `ADDONS.md`, `collection/config.json` and `collection/artwork.json`. Use the **already committed** Net base indicated by `deployment.baseContract` in the config; do not regenerate, modify or replace it, and preserve its Net registration and mint/transfer/burn messages.

Generate the collection-specific Solidity, packed on-chain artwork, SVG renderer, weighted trait generation and metadata, implementing only the selected features and values from the files. Preserve pixels, colors, weights, layer order and transparency. Repeated combinations are allowed. Respect or explicitly flag incompatible trait rules.

Compile and test the complete Solidity source, check the runtime bytecode limit, verify a sample decoded tokenURI/SVG, and report mint permissions and gas considerations. Provide the **actual complete** source files, artifacts and test output. Report any missing required settings instead of guessing.

**STRICTLY READ-ONLY / OFF-CHAIN. DO NOT DEPLOY, SIGN, BROADCAST, MINT, BURN, SUBMIT TRANSACTIONS OR SPEND FUNDS. Wait for separate explicit authorization.**
