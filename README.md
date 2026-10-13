# Mintbay Studio → Bankr → Net Protocol

Create generative pixel art in **[Mintbay Pixel Studio](https://studio.mintbay.xyz)**, export **`artwork.json` and `config.json`**, then use **Bankr + [Net Protocol's official skill](https://netprotocol.app/skill.md)** to generate, compile, and — only with separate explicit approval — deploy a fully on-chain NFT collection.

This repository is a reusable **community template**, not an official Net or Bankr service. It does not deploy anything by itself.

## Quick start for creators

1. Open [Mintbay Studio](https://studio.mintbay.xyz/2d) and design your art. Set its **name** and **supply**.
2. Open the **Onchain** tab and enter the public mint price, per-wallet limit, creator allowance, royalties, and optional features.
3. Click **Export artwork.json** and **Export config.json**.
4. Fork this repository (or use **Use this template**), and replace **`collection/artwork.json`** and **`collection/config.json`** with your exported files.
5. Read **`NET_BASE_GUIDE.md`** and **`ADDONS.md`**. The configuration field **`deployment.baseContract`** selects one of the already committed bases.
6. Copy the **read-only generation test** from **`BANKR_BASE_PROMPT.md`** to Bankr. Ask for complete source, compilation artifacts, and tests before considering deployment.
7. Once the contract has been reviewed, use the separate **`BANKR_PROMPT.md`** for a publicly shareable deployment request. It authorizes only the stated deployment and source verification — not extra mints or other transactions.

### What's in this repository?

| Path | Purpose |
| --- | --- |
| [`collection/artwork.json`](collection/artwork.json) | Fully specified artwork: pixel data, layer order, trait names and weights. Replace with your exported art. |
| [`collection/config.json`](collection/config.json) | Collection name, supply, public mint price, wallet cap, creator reserve, royalties, administration, selected add-ons. Replace with your exported config. |
| [`contracts/net/NetIntegratedERC721A.sol`](contracts/net/NetIntegratedERC721A.sol) | Pinned reference-compatible Net base for normal creator deployments. |
| [`contracts/hoodwallet/NetIntegratedERC721A.sol`](contracts/hoodwallet/NetIntegratedERC721A.sol) | Minimal administrator-address variant for HoodWallet-controlled collections. |
| [`NET_BASE_GUIDE.md`](NET_BASE_GUIDE.md) | How to select the base without rewriting Net's registration and activity messaging. |
| [`ADDONS.md`](ADDONS.md) | Explicit optional features, including Hoodie free mint and burn-to-claim. |
| [`BANKR_BASE_PROMPT.md`](BANKR_BASE_PROMPT.md) | Read-only compilation/test prompt. |
| [`BANKR_PROMPT.md`](BANKR_PROMPT.md) | Public deployment prompt, for use only after review. |
| [`scripts/check_net_alignment.py`](scripts/check_net_alignment.py) | Static consistency check (not a substitute for Solidity compilation/tests). |

## Important: fixed base contracts

**Bankr should not regenerate, replace or rewrite either Net base.** The standard base uses the actual transaction deployer as its immutable administrator. The HoodWallet variant instead accepts the configured administrator address, enabling Hoodie token-bound-wallet administration without deploying from the TBA itself. The Net registration and mint/transfer/burn message logic remain consistent with the Net skill.

For new generic collections, select `contracts/net/NetIntegratedERC721A.sol`. For an intentionally HoodWallet-administered collection, select `contracts/hoodwallet/NetIntegratedERC721A.sol` and provide the correct account address in `collection.deployerAddress`. Do **not** use Hoodie #351's address for unrelated collections.

## Example: 8x8Portait

The included example uses 8×8 pixel artwork, 8 layers, 53 traits and 2,048 maximum supply. It demonstrates 0.001 ETH public mints, a 20-mint public wallet limit, 20 creator mints, 6% ERC-2981 royalties, and permanent administration by **Hoodie #351's HoodWallet**. These settings are for this example only. Other artists should export their own `config.json` from Studio.

The Hoodie-gated one-free-mint feature is **optional**. The free claim and public/creator mints share one supply; with 2,048 total tokens, claims cannot be promised to all 6,000 Hoodies. A creator allowance is a lifetime mint limit, **not** a guaranteed reserved allocation unless additional reservation logic is separately designed.

## Rendering and contract expectations

- The source `artwork.json` is read at code generation time. All selected art and metadata must be stored/rendered on-chain and remain functional without GitHub or a web server.
- Select traits according to their **relative weights** and preserve layer order/transparency and exact colors. Repeated combinations are acceptable.
- If the source contains `incompatibleWith` rules, Bankr must honor them or explicitly report the mismatch rather than silently discarding rules.
- Validate bytecode limits, mint economics, NFT metadata JSON/SVG, and owner/burn authorization by compiling and testing the **actual full source files**.
- ERC-2981 does not enforce royalty payments. Burn-for-claim records do not implement a future claim contract's replay protection.
- Because Net's reference randomness uses `block.prevrandao`, avoid high-value rarity lottery promises.

## Safety

The **test prompt** prohibits all on-chain actions. The separate **deployment prompt** should only be sent when you're ready for mainnet spending, after reviewing the generated code and transaction details. The collection's public mint is generally live as soon as the contract is deployed unless you specifically implement a mint pause. A GitHub commit or Studio export does not deploy anything.

**[Create artwork in Mintbay Studio](https://studio.mintbay.xyz) · [Official Net skill](https://netprotocol.app/skill.md)**
