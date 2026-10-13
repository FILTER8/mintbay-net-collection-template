# Mintbay Studio + Net Protocol: locked base contract

Official skill: https://netprotocol.app/skill.md
Official NFT reference: https://raw.githubusercontent.com/stuckinaboot/net-public/main/skill-references/nft-collections.md

## Why these files exist

Bankr should NOT rewrite the Net ERC721A base on each request. It should choose exactly one of the two checked-in bases, use `collection/config.json` for collection settings, and generate only collection-specific source (`ArtworkData.sol`, `Collection.sol`, tests).

These files are based on the official Net-integrated NFT reference. The `net/` version preserves the official behavior. The `hoodwallet/` version has precisely two FUNCTIONAL deviations: (1) an explicit immutable administrator argument in the constructor, because ERC-6551 HoodWallet #351 cannot execute CREATE/CREATE2; (2) the shared `_mintSeeded` helper is `internal` instead of `private`, so a child contract can implement a gated free mint without duplicating the seed/supply logic. Constructor registry and Net activity messages are unchanged.

## Pick one version

- `contracts/net/NetIntegratedERC721A.sol`: the standard reference behavior, admin = actual deploying `msg.sender`; constructor takes six arguments.
- `contracts/hoodwallet/NetIntegratedERC721A.sol`: use for a collection administered by a token-bound HoodWallet; constructor takes a seventh `address admin_` argument and validates nonzero. Other than making `_mintSeeded` inheritable, mint/withdraw/Net behavior is the same.

**Never include both in the same Solidity build:** both define `NetIntegratedERC721A` and `INet`. Copy/select only the chosen version as `NetIntegratedERC721A.sol` in the target build.

## Hoodie #351 example

- `collection/config.json` is the source of truth for the configuration: `0.001` ETH price, `2048` supply, `20` public mints per wallet, `20` creator mints, `600` royalty bps, and administrator `0xd3d65519d2285f7100eba318eb2ccc4b1763ca43`.
- `collection/artwork.json` is the source of truth for the pixel art and weight data.
- For Hoodie #351, select `contracts/hoodwallet/NetIntegratedERC721A.sol`, and pass `deployerAddress` as the seventh base constructor argument. The Net registration message still records `tx.origin` as the creator, per the official protocol; it does *not* register the TBA as creator. The Net app for activity remains the collection address.
- The HoodWallet becomes the only address authorized by `onlyDeployer` and the sole destination of `withdraw()`. The admin remains fixed even if ownership of the Hoodie NFT changes; who controls the HoodWallet must be validated against the deployed HoodOS contracts.
- Current `mintToCreator(uint256,address)` is a lifetime allowance of 20, *not* a supply reservation.

## Collection-specific extensions (NOT part of the Net base)

1. ERC-2981 royalty metadata (the marketplace must voluntarily honor it).
2. `freeMint(uint256 hoodieId)`: caller must be the current NFT owner, each Hoodie ID usable once, call inherited `_mintSeeded(msg.sender, 1)`, sharing the same total supply cap. This does **not** count against public paid-mint wallet cap unless you deliberately add that rule.
3. `burnForClaim`: require NFT owner or a carefully chosen authorized caller, store permanent burn record with **owner at burn time** as beneficiary, caller, claim contract snapshot, and timestamp. Future claim contract must check the record is targeted to its own address AND implement one-time redemption. A configured address alone does not prove the address supports claiming. For maximum user protection consider requiring owner-only burn, rather than operator burn.
4. Fully on-chain renderer and metadata, with deterministic seed-based weighted traits. Validate JSON metadata, on-chain SVG output, and gas/size limits.

## Net integration must be kept unchanged

- Constructor: `try NET.sendMessage(name_, TOPIC_COLLECTION, abi.encodePacked(tx.origin)) {} catch {}` with `TOPIC_COLLECTION = "nft-collection"`.
- `_afterTokenTransfers`: once per ERC721A batch, mint topic sender=`to`, transfer/burn topic sender=`from`, `sendMessageViaApp(..., "")` wrapped in `try/catch`.
- Do NOT override `_afterTokenTransfers` in the collection contract.
- Do NOT replace registry with `sendMessageViaApp` or `app-register`.
- Do NOT change seeded mint ordering (`_seed` before `_mint`).

## Verification and deployment policy

- Run `python3 scripts/check_net_alignment.py` to statically verify Net-message code and intended differences between the two bases.
- Full compile/test **not performed in this package**; solc 0.8.24, ERC721A 4.3.0, and Solady were not available in the creation environment. Compile both selected-base + collection + packed art with pinned versions before any deployment.
- Test external Net calls via a local/mock EVM. Since Net writes are best effort, verify that failing Net calls do not prevent mints/transfers/burns.
- Check code size (EIP-170), mint/creator limits, one-claim-per-Hoodie, burn claim authorization, source-match to artwork JSON, and HoodWallet/chainID permissions.
- **Never deploy, sign, broadcast, or spend funds based on this template alone.** Require explicit separate permission and source review.
