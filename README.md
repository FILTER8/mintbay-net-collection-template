# Mintbay Studio × Net Protocol × Bankr

**Draw your generative pixel-art collection in [Mintbay Studio](https://studio.mintbay.xyz), export its JSON, and ask [Bankr](https://bankr.bot) to deploy it as a fully on-chain NFT collection using the official [Net Protocol skill](https://www.netprotocol.app/skill.md).**

This is a **forkable starter repository** for artists and creators. No Solidity experience is required to prepare your art and a prompt. Bankr is expected to generate and compile the Solidity and submit deployment transactions. **Never approve an unreviewed transaction.**

> This repo is a community workflow/template, **not** an official Net Protocol or Bankr deployment service. Whether Bankr can fetch a GitHub URL and complete the requested workflow must be checked with Bankr. Nothing is deployed merely by forking this repository.

## Quick start

1. **Create your art:** Open **[studio.mintbay.xyz](https://studio.mintbay.xyz)**. Build your collection using pixel layers, traits, and rarity weights. Export its JSON.
2. **Fork this repository** using GitHub's **Fork** button. (The repo owner can also enable **Template repository** in Settings to offer **Use this template**.)
3. **Replace `collection/artwork.json`** with your exported JSON. Do not just rename the old art; replace its contents.
4. **Edit `collection/config.json`** with your collection name, supply, price, wallet cap, creator reserve, and royalty/owner addresses. The sample has placeholders (`null`) that must be filled before deployment.
5. **Choose optional features** in `collection/config.json`. Read `ADDONS.md` if you enable them. The supplied example is configured to request Hoodie-gated free minting, burn-to-claim, transferable ownership, and 6% ERC-2981 royalties.
6. **Copy the prompt** from `BANKR_PROMPT.md` to Bankr, replacing `YOUR_PUBLIC_REPOSITORY_URL` with your fork's URL. Bankr should read your public files and the official Net NFT reference, generate and compile your on-chain collection, and ask for approval before deployment.
7. **Review and verify:** Review all settings and bytecode/contract-size concerns, approve only if correct, and ensure source-code verification and real mint/transfer Net messages are checked after deployment.

### What is in this repository?

| File | Purpose |
| --- | --- |
| [`collection/artwork.json`](collection/artwork.json) | Example unmodified 8×8 portrait export from Mintbay Studio: 8 layers, 53 weighted traits, 2,048 supply. **Replace with your art.** |
| [`collection/config.json`](collection/config.json) | Collection settings and optional feature toggles. **Edit before deployment.** |
| [`BANKR_PROMPT.md`](BANKR_PROMPT.md) | Short Bankr prompt based on the existing Net-skill workflow. |
| [`ADDONS.md`](ADDONS.md) | Optional extension requirements; the Net integration itself must stay intact. |

## How the NFT art works

Mintbay's export supplies the **art ingredients**: canvas dimensions, an ordered list of layers, a list of pixel maps and names for each trait, and relative weights.

For each newly minted NFT, use the **official Net base's per-token seed** to choose **one weighted trait per layer**. Render these layers in the original order (transparent pixels let underlying layers show through). Both the artwork and metadata must derive from the **same** selected traits. **Random combinations may repeat**: this is a generative collection, not a promise that every possible combination or minted piece will be unique.

The final NFT must have **fully on-chain SVG artwork and JSON metadata**. The deployed contract should not fetch the JSON from GitHub; the JSON is input to the contract-generation process only. Bytecode/data may need compact packing to respect EVM contract-size and gas limits.

## Keep the original Net integration

**Do not replace or reinvent the official Net messaging logic.** Bankr should use the documented `NetIntegratedERC721A` base and preserve collection registration and the original `mint`, `transfer`, `burn` message behavior, including `sendMessageViaApp` and best-effort `try/catch` handling.

- [Official Net skill](https://www.netprotocol.app/skill.md)
- [Official Net-integrated NFT reference](https://raw.githubusercontent.com/stuckinaboot/net-public/main/skill-references/nft-collections.md)

You can add artist-requested functionality **around** the base, as described in `ADDONS.md`. If adding transferable ownership requires changing Net's fixed deployer admin code, **the Net posting implementation and semantics must remain untouched**. Bankr must disclose any necessary admin change.

## Example project included

This forkable repo currently contains the **8x8Portait** sample exported from Mintbay Studio. It is **not** the older 64 Faces specification; use the source JSON's actual colors and rarity weights, not any unrelated palette or traits.

The example uses **2,048 max supply** and optionally gates one free claim to each token ID in the OnChainHoodies collection on Robinhood Chain. Because more than 2,048 Hoodies exist, **a free mint for every Hoodie cannot be guaranteed** with this shared cap. No reserved supply is defined in the example.

## Notes before deploying

- **Forking does not deploy.** All blockchain writes and payments should happen through Bankr only after review.
- **Royalties:** ERC-2981 royalty information does not force marketplace payments.
- **Randomness:** Net's reference seed uses `block.prevrandao`; suitable for lightweight generative art, **not** high-stakes rare-trait lotteries.
- **Contract size:** 8×8 layered pixel maps should be packed/compressed into deployable bytecode or data contracts. Bankr must check code size and rendering/gas feasibility before deployment.
- **Ownership:** The upstream Net base pins the deployer for creator premints and withdrawals. Two-step ownership on an inheriting contract alone does **not** transfer these permissions. See `ADDONS.md`.
- **Licensing:** Each artist is responsible for the rights to the art they upload. This template does not grant rights to third-party artwork.

---

**Create in [Mintbay Studio](https://studio.mintbay.xyz) · Deploy with Bankr · Integrate with Net Protocol.**
