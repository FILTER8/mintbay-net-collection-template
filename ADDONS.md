# Optional collection features

These add-ons are generated in the **collection-specific** contract only when enabled in `collection/config.json`. The Net base contract selected by `deployment.baseContract` must remain untouched. Reference: https://netprotocol.app/skill.md.

## `standardRoyalties`

Implement ERC-2981, advertise `0x2a5520c9` in `supportsInterface`, use `collection.royaltyBps` and the explicitly configured `collection.royaltyReceiver`. Bankr should report missing receiver addresses rather than invent one. No forced royalties / transfer filtering are requested.

## `oneFreeMintPerHoodie`

**Optional OnChainHoodies example** — not enabled for unrelated collections by default.

- Check `IERC721(eligibility.hoodieContract).ownerOf(hoodieId) == msg.sender` when `freeMint(uint256 hoodieId)` is called.
- Allow exactly one lifetime free mint per Hoodie **token ID**, including after transfers; record claims on-chain.
- Mint the new NFT to the caller, using the existing inherited seeded mint helper (available in the HoodWallet variant) or the official base's existing internal seed/supply/mint helpers (standard base). **Never rewrite the base to implement this.**
- Paid, free, and creator mints share `collection.maxSupply`; no supply is reserved for free claims unless explicitly redesigned.
- Direct owner check does not automatically support nested HoodWallet ownership; supporting that is outside this example's scope.

## `burnForClaim`

- Expose `setClaimContract(address)` to the collection's immutable administrator. A null initial address is allowed: burns stay disabled until a nonzero target is set.
- `burnForClaim(tokenId)` must check NFT ownership/authorization. Record the **owner at burn time as the claim beneficiary**, never simply `msg.sender`, since an approved operator might submit the burn.
- Record the beneficiary, triggering caller, configured target claim contract, token ID, timestamp and an `exists` flag permanently; expose readable `getBurnRecord(tokenId)` and an event.
- Use the normal ERC721A `_burn(tokenId, true)` flow, preserving Net's original burn message.
- Subsequent changes to `claimContract` must **not** rewrite historical burn targets.
- The future claim contract must verify eligibility (`targetClaimContract == address(this)`, historical owner as beneficiary) and enforce **per-token one-time redemption**. A record is not itself a redemption mechanism.
- For added safety, project authors may choose owner-only burns instead of approved-operator burns. Make this explicit before launch.

## Administration modes

- `deployment.adminMode = standard`: use `contracts/net/NetIntegratedERC721A.sol`. Its immutable `_deployer` is `msg.sender` during deployment; changing `collection.deployerAddress` cannot change that behavior.
- `deployment.adminMode = hoodwallet`: use `contracts/hoodwallet/NetIntegratedERC721A.sol` and set `collection.deployerAddress` to the correct **canonical HoodWallet**. Only the TBA can call `onlyDeployer` admin functions. The deployed contract can be created by an EOA or sponsor while retaining permanent HoodWallet administration.
- Do **not** add `Ownable2Step` or transferable contract ownership: `features.transferableOwnership` remains false.
- Net's registration and mint/transfer/burn activity semantics must remain aligned with the official reference for both modes.

## Mandatory checks before deployment

Confirm all required addresses and prices, deployer privilege behavior, actual tokenURI JSON/SVG, artwork weight/pixel fidelity, eligible free-mint behavior, burn beneficiary and claim history, bytecode size and gas costs. Compile and test the **actual sources** with the documented dependencies; a summary of artwork data is not a substitute for the full file.
