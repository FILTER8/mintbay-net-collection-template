#!/usr/bin/env python3
"""Static guard: confirm the HoodWallet variant differs from the Net base only
in its intended constructor-admin change and private -> internal mint helper.
This is not a Solidity compile or security audit.
"""
from pathlib import Path
import difflib
import re

root = Path(__file__).resolve().parents[1]
plain = (root / "contracts/net/NetIntegratedERC721A.sol").read_text()
hood = (root / "contracts/hoodwallet/NetIntegratedERC721A.sol").read_text()

# Strip comments (only) before comparison.
def strip_comments(s: str) -> str:
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    s = re.sub(r"//[^\n]*", "", s)
    return '\n'.join(x.strip() for x in s.splitlines() if x.strip())

expected = plain.replace(
    "        uint256 creatorReserve_\n    ) ERC721A(name_, symbol_) {\n        _deployer = msg.sender;",
    "        uint256 creatorReserve_,\n        address admin_\n    ) ERC721A(name_, symbol_) {\n        require(admin_ != address(0), \"Zero admin\");\n        _deployer = admin_;",
).replace(
    "function _mintSeeded(address to, uint256 amount) private",
    "function _mintSeeded(address to, uint256 amount) internal",
)

a, b = strip_comments(expected), strip_comments(hood)
if a != b:
    print('FAIL: Unexpected functional differences in HoodWallet Net base:')
    print(''.join(difflib.unified_diff(a.splitlines(True), b.splitlines(True), fromfile='expected', tofile='actual')))
    raise SystemExit(1)

for needle in [
    'try NET.sendMessage(name_, TOPIC_COLLECTION, abi.encodePacked(tx.origin)) {} catch {}',
    'try NET.sendMessageViaApp(msgSender, text, topic, "") {} catch {}',
    'string internal constant TOPIC_COLLECTION = "nft-collection";',
]:
    if needle not in hood or needle not in plain:
        raise SystemExit('FAIL: Missing official Net integration pattern: ' + needle)

print('PASS: Net registration and activity messaging match the pinned source.')
print('PASS: HoodWallet variant has only the two intended functional changes.')
print('NOTE: Static comparison only; compile and behavioral tests are still required.')
