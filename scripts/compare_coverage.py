"""Compare identifiers at one declared unit; no upstream tool is invoked."""
import argparse
import hashlib
import json
from pathlib import Path


def compare(target, retrieved, inventory=None):
    target, retrieved = set(target), set(retrieved)
    if not target:
        raise ValueError("target must not be empty")
    if inventory is not None:
        inventory = set(inventory)
        if not retrieved <= inventory:
            raise ValueError("retrieved contains IDs outside inventory; check units and versions")
    return {
        "target_count": len(target),
        "retrieved_targets": sorted(target & retrieved),
        "unretrieved_targets": sorted(target - retrieved),
        "present_but_not_retrieved": None if inventory is None else sorted((target & inventory) - retrieved),
        "absent_from_inventory": None if inventory is None else sorted(target - inventory),
        "query_coverage": len(target & retrieved) / len(target),
    }


def read_ids(path):
    raw = Path(path).read_bytes()
    ids = {line.strip() for line in raw.decode("utf-8-sig").splitlines() if line.strip()}
    return ids, hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    parser.add_argument("--retrieved", required=True)
    parser.add_argument("--inventory")
    args = parser.parse_args()
    try:
        target, th = read_ids(args.target)
        retrieved, rh = read_ids(args.retrieved)
        inventory, ih = read_ids(args.inventory) if args.inventory else (None, None)
        result = compare(target, retrieved, inventory)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    result["input_sha256"] = {"target": th, "retrieved": rh, "inventory": ih}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
