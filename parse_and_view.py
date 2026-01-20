from screenplayparser import ScreenplayParser

# Path to a screenplay
SCRIPT_PATH = "data/screenplays/screenplays/44_inch_chest.txt"

# Create rule-based parser (fast)
rule_parser = ScreenplayParser(use_rules=True)

# Read script
with open(SCRIPT_PATH) as reader:
    script = reader.read().split("\n")

# Parse it
tags = rule_parser.parse(script)

# Print first 50 lines with tags
print("=" * 80)
print("PARSED SCREENPLAY (first 50 lines)")
print("=" * 80)
for i, (tag, line) in enumerate(zip(tags[:50], script[:50])):
    print(f"{i+1:4d} | {tag} | {line}")

print("\n" + "=" * 80)
print(f"Total lines: {len(script)}")
print("=" * 80)

# Optionally save to file
save_output = input("\nSave full output to file? (y/n): ")
if save_output.lower() == 'y':
    output_file = "parsed_screenplay.txt"
    with open(output_file, "w") as f:
        for tag, line in zip(tags, script):
            f.write(f"{tag}: {line}\n")
    print(f"Saved to {output_file}")

