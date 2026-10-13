# Optional contract add-ons (artist-selected)

Bankr: **start with the official Net NFT collection reference**:
https://raw.githubusercontent.com/stuckinaboot/net-public/main/skill-references/nft-collections.md

**Do not replace Net Protocol's messaging integration.** Preserve the Net registration, `sendMessageViaApp` calls from the ERC721A transfer hook, message topics, sender conventions, and best-effort `try/catch` logic. The contract-specific additions below should be added **only when their corresponding `features` flag is true** in `collection/config.json`.

## `standardRoyalties`: ERC-2981

- Expose ERC-2981 royalty info and advertise it through ERC-165 `supportsInterface`.
- Use `royaltyBps` (the sample uses **600 = 6%**) and `royaltyReceiver` from `collection/config.json`.
- No ERC-721C, operator filtering, or transfer-restricting royalty enforcement. ERC-2981 cannot force payment on every marketplace.

## `oneFreeMintPerHoodie`: optional OnChainHoodies example

- Sample Robinhood Chain Hoodie NFT contract: `0x9Ec6C5b9f572A9B02138E553BC5F5882Da735F45` (see config).
- Function shape: `freeMint(uint256 hoodieId)`.
- Verify `IERC721(hoodieContract).ownerOf(hoodieId) == msg.sender` at claim time.
- Each Hoodie token ID can be claimed **once for the life of the collection**, even if the Hoodie later transfers. Mint the new NFT to the caller.
- Supply cap includes **paid, creator, and free mints**. Free mints must use the normal Net ERC721A seed and mint paths so Net emits a standard `mint` message.
- No signatures, Merkle proofs, token-bound-wallet activation, or additional token requirement. This direct owner check does not support nested ownership or claiming directly from a TBA without additional work.
- The sample supply is 2,048 but 6,000 Hoodies exist; a free claim is **not guaranteed to every Hoodie** if the common supply sells out. No free-claim reserve is specified.
- For other projects, set `oneFreeMintPerHoodie` to `false` unless you explicitly intend to use this collection's token gate.

## `burnForClaim`: future redemption address

- Add an owner-settable target, e.g. `setClaimContract(address)`.
- An NFT owner or approved operator can `burnForClaim(uint256 tokenId)` only after a nonzero claim target has been set; it should call ERC721A's normal authorized burn path so Net emits a standard `burn` message.
- Emit a separate local event holding the burner, burned NFT token ID, and claim target.
- This **records** a burn for a future claim; it does **not** automatically award the replacement NFT. Any future redemption contract needs secure eligibility checking and replay protection.

## `transferableOwnership`: two-step ownership transfer

- Add simple two-step owner transfer for collection administrative controls.
- **Caveat from the official Net reference:** its immutable `_deployer` authorizes `mintToCreator()` and receives withdrawals, and the reference methods are not virtual. Simply inheriting `Ownable2Step` does **not** transfer those permissions.
- If complete control transfer is required, Bankr may minimally adapt the deployer-only premint/withdrawal authority in the base **without changing the Net integration code or message behavior**. Report the exact changes for approval, or explicitly disclose that the original deployer retains those privileges if upstream code stays byte-for-byte intact. Never falsely promise full ownership transfer.

## Common validation

Before deployment, confirm all non-null collection parameters, compile against the documented ERC721A/solady versions, check contract code size, test paid/free/creator mint limits and Net hooks, test admin transitions and burn auth, decode a representative on-chain tokenURI/SVG, request explicit transaction approval, and verify the deployed contract source.
