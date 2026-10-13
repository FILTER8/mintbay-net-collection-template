# Read-only Bankr prompt (after files are committed to GitHub)

Hey @bankrbot, please use the official Net Protocol skill:
https://netprotocol.app/skill.md

My Mintbay Studio repository is:
https://github.com/FILTER8/mintbay-net-collection-template

Please read `NET_BASE_GUIDE.md`, `collection/config.json`, and `collection/artwork.json`.

For the Hoodie #351 example, use the **existing** `contracts/hoodwallet/NetIntegratedERC721A.sol` exactly as committed. It is a narrowly adapted version of Net's documented ERC721A base, with fixed HoodWallet administration and an inheritable seeded mint helper. Do not regenerate or replace the Net base. Preserve its registration and mint/transfer/burn messaging logic byte for byte.

Generate only the collection-specific Solidity (packed art data, renderer/metadata, royalties, Hoodie free mint, burn-to-claim) and tests, using the config and art as the sources of truth. Pin solc 0.8.24, ERC721A 4.3.0 and Solady. Include complete source files, compile output, decoded sample tokenURI JSON and SVG, and all test results. Flag any inconsistency or dependency mismatch rather than guessing.

**STRICTLY OFF-CHAIN: DO NOT DEPLOY, SIGN, BROADCAST, MINT, BURN, SUBMIT TRANSACTIONS OR SPEND FUNDS.** Wait for separate explicit authorization.
