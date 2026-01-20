from screenplayparser import ScreenplayParser
import os

# Prompt user for film name
film_name = input("Enter film name (e.g., 'american_psycho'): ").strip()
if not film_name:
    print("Error: Film name cannot be empty")
    exit(1)

SCRIPT_PATH = f"data/screenplays/screenplays/{film_name}.txt"

# Check if file exists
if not os.path.exists(SCRIPT_PATH):
    print(f"Error: File not found at {SCRIPT_PATH}")
    exit(1)

# Prompt for which parsers to run
use_rules = input("Run rule-based parser? (y/n): ").strip().lower() == 'y'
use_trx = input("Run transformer parser? (y/n): ").strip().lower() == 'y'

if not use_rules and not use_trx:
    print("Error: Must select at least one parser")
    exit(1)

# Read script
with open(SCRIPT_PATH) as reader:
    script = reader.read().split("\n")

# Create output directory if it doesn't exist
os.makedirs("yiduo_output", exist_ok=True)

output_files = []

# Run rule-based parser if requested
if use_rules:
    print("\nRunning rule-based parser...")
    rule_parser = ScreenplayParser(use_rules=True)
    rule_tags = rule_parser.parse(script)

    rules_output_path = f"yiduo_output/rules_{film_name}_parsed.txt"
    with open(rules_output_path, "w") as f:
        for tag, line in zip(rule_tags, script):
            f.write(f"{tag}: {line}\n")
    output_files.append(rules_output_path)
    print(f"✓ Rule-based parsing complete")

# Run transformer parser if requested
if use_trx:
    print("\nRunning transformer parser...")
    trx_parser = ScreenplayParser(use_rules=False, device_id=1)
    trx_tags = trx_parser.parse(script)

    trx_output_path = f"yiduo_output/trx_{film_name}_parsed.txt"
    with open(trx_output_path, "w") as f:
        for tag, line in zip(trx_tags, script):
            f.write(f"{tag}: {line}\n")
    output_files.append(trx_output_path)
    print(f"✓ Transformer parsing complete")

print(f"\n✓ Parsed {len(script)} lines")
print(f"✓ Saved to: {', '.join(output_files)}")