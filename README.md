# Mintbay Studio → Bankr → Net Protocol

Create generative pixel art in **[Mintbay Pixel Studio](https://studio.mintbay.xyz)**, export **`artwork.json` and `config.json`**, then use **Bankr + [Net Protocol's official skill](https://netprotocol.app/skill.md)** to generate, compile, deploy and verify a fully on-chain NFT collection through an explicit Bankr prompt.

This repository is a reusable **community template**, not an official Net or Bankr service. It does not deploy anything by itself.

## Quick start for creators

1. Open [Mintbay Studio](https://studio.mintbay.xyz/2d) and design your art. Set its **name** and **supply**.
2. Open the **Onchain** tab and enter the public mint price, per-wallet limit, creator allowance, royalties, and optional features.
3. Click **Export artwork.json** and **Export config.json**.
4. Fork this repository (or use **Use this template**), and replace **`collection/artwork.json`** and **`collection/config.json`** with your exported files.
5. Read **`NET_BASE_GUIDE.md`** and **`ADDONS.md`**. The configuration field **`deployment.baseContract`** selects one of the already committed bases.
6. Enter your GitHub repository URL in Studio and click **Copy Bankr Deployment Prompt**, or use [`BANKR_PROMPT.md`](BANKR_PROMPT.md). The prompt starts with `@bankrbot` and requests generation, compilation, mainnet deployment and source verification in one task. **Posting it authorizes real transactions and gas spending.**
7. Find the deployed collection and verification links on [Robinhood Etherscan](https://robin.etherscan.io). Creator minting is a **separate** action; use [`BANKR_CREATOR_MINT_PROMPT.md`](BANKR_CREATOR_MINT_PROMPT.md) only after deployment. An optional, longer **read-only** test is still available in [`BANKR_BASE_PROMPT.md`](BANKR_BASE_PROMPT.md).

### What's in this repository?

| Path | Purpose |
| --- | --- |
| [`collection/artwork.json`](collection/artwork.json) | Fully specified artwork: pixel data, layer order, trait names and weights. Replace with your exported art. |
| [`collection/config.json`](collection/config.json) | Collection name, supply, public mint price, wallet cap, creator reserve, royalties, administration, selected add-ons. Replace with your exported config. |
| [`contracts/net/NetIntegratedERC721A.sol`](contracts/net/NetIntegratedERC721A.sol) | Pinned reference-compatible Net base for normal creator deployments. |
| [`contracts/hoodwallet/NetIntegratedERC721A.sol`](contracts/hoodwallet/NetIntegratedERC721A.sol) | Minimal administrator-address variant for HoodWallet-controlled collections. |
| [`NET_BASE_GUIDE.md`](NET_BASE_GUIDE.md) | How to select the base without rewriting Net's registration and activity messaging. |
| [`ADDONS.md`](ADDONS.md) | Explicit optional features, including Hoodie free mint and burn-to-claim. |
| [`BANKR_PROMPT.md`](BANKR_PROMPT.md) | Short one-shot `@bankrbot` mainnet deployment and verification prompt. |
| [`BANKR_CREATOR_MINT_PROMPT.md`](BANKR_CREATOR_MINT_PROMPT.md) | Separate creator mint prompt, including HoodWallet execution. |
| [`BANKR_BASE_PROMPT.md`](BANKR_BASE_PROMPT.md) | Optional read-only compilation/test prompt. |
| [`scripts/check_net_alignment.py`](scripts/check_net_alignment.py) | Static consistency check (not a substitute for Solidity compilation/tests). |

## Important: fixed base contracts

**Bankr should not regenerate, replace or rewrite either Net base.** The standard base uses the actual transaction deployer as its immutable administrator. The HoodWallet variant instead accepts the configured administrator address, enabling Hoodie token-bound-wallet administration without deploying from the TBA itself. The Net registration and mint/transfer/burn message logic remain consistent with the Net skill.

For new generic collections, select `contracts/net/NetIntegratedERC721A.sol`. For an intentionally HoodWallet-administered collection, select `contracts/hoodwallet/NetIntegratedERC721A.sol` and provide the correct account address in `collection.deployerAddress`. Do **not** use Hoodie #351's address for unrelated collections.

## Example: 8x8Portait

The included example uses 8×8 pixel artwork, 8 layers, 53 traits and 2,048 maximum supply. It demonstrates 0.001 ETH public mints, a 20-mint public wallet limit, 20 creator mints, 6% ERC-2981 royalties, and permanent administration by **Hoodie #351's HoodWallet**. These settings are for this example only. Other artists should export their own `config.json` from Studio.

**Live deployment (14 October 2026):** The 8x8Portait collection was deployed on Robinhood Chain using Bankr and the Net Protocol integration. The collection source is verified on **[Robinhood Etherscan](https://robin.etherscan.io/address/0x2ee6305804dd94f7ff695c5ab1f3ae805f317653#code)**. [Deployment transaction](https://robin.etherscan.io/tx/0x2ffa11688586468529d6774020a63ecb17ecfbc644b47378d97dd143259dc987) · [First creator mint, token #1](https://robin.etherscan.io/tx/0xd0c0e3394b73a58c11e07b979f8d843fca5e595989edc857eade3c27545e6f95). The creation transaction also created a Net-related data contract; do not assume every auxiliary data contract has standard Solidity source to verify. The live deployed contract is **not** redeployed by following this template; users should deploy their own collection with their own artwork/configuration.

The Hoodie-gated one-free-mint feature is **optional**. The free claim and public/creator mints share one supply; with 2,048 total tokens, claims cannot be promised to all 6,000 Hoodies. A creator allowance is a lifetime mint limit, **not** a guaranteed reserved allocation unless additional reservation logic is separately designed.

## Rendering and contract expectations

- The source `artwork.json` is read at code generation time. All selected art and metadata must be stored/rendered on-chain and remain functional without GitHub or a web server.
- Select traits according to their **relative weights** and preserve layer order/transparency and exact colors. Repeated combinations are acceptable.
- If the source contains `incompatibleWith` rules, Bankr must honor them or explicitly report the mismatch rather than silently discarding rules.
- Validate bytecode limits, mint economics, NFT metadata JSON/SVG, and owner/burn authorization by compiling and testing the **actual full source files**.
- ERC-2981 does not enforce royalty payments. Burn-for-claim records do not implement a future claim contract's replay protection.
- Because Net's reference randomness uses `block.prevrandao`, avoid high-value rarity lottery promises.

## Safety

The optional **read-only test prompt** prohibits all on-chain actions. The **one-shot deployment prompt** authorizes mainnet spending and must only be posted when you are ready to deploy; it is not a sandbox or simulation. The separate **creator mint prompt** authorizes additional mint transactions. Review configuration and contract permissions before use. The collection's public mint is generally live as soon as the contract is deployed unless you specifically implement a mint pause. A GitHub commit or Studio export does not deploy anything.

**[Create artwork in Mintbay Studio](https://studio.mintbay.xyz) · [Official Net skill](https://netprotocol.app/skill.md)**
