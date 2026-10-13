# Copy this prompt to Bankr

Replace `YOUR_PUBLIC_REPOSITORY_URL` with your **public GitHub fork** URL.

---

Hey @bankrbot, can you create a new **fully on-chain generative NFT collection on Robinhood Chain** using the official Net Protocol skill?

Official skill: https://www.netprotocol.app/skill.md

Here is my artwork and settings from Mintbay Studio: **YOUR_PUBLIC_REPOSITORY_URL**

Please read `collection/artwork.json`, `collection/config.json`, and `ADDONS.md` in my repository. The JSON defines the artwork, ordered layers, trait names, colors, and relative rarity weights. Generate SVG artwork and JSON metadata **entirely on-chain** using Net's original per-token seed. Choose one weighted trait per layer for each mint; random combinations may repeat. Do **not** enumerate all combinations or load JSON from GitHub at runtime.

Use the **original Net `NetIntegratedERC721A` reference implementation and integration** for collection registration and automatic mint/transfer/burn posting. Keep its Net messages and best-effort `try/catch` behavior unchanged. Use the collection-specific additions selected in `collection/config.json`, following `ADDONS.md`; don't add extras not selected.

Please show me the complete configuration and any missing required values first. Compile and test the generated Solidity, ensure EVM bytecode/deployment size is feasible, explain any minimal administrative adjustments required for transferable ownership, and ask me to approve the deployment transaction **before** submitting it through Bankr. After deployment, verify the Solidity source and confirm Net mint/transfer messages are readable on Robinhood Chain.

---

This prompt is a template, **not** proof that Bankr can automatically load every GitHub repo or that any custom Solidity is deployable without review.
