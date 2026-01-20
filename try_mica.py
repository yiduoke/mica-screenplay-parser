from screenplayparser import ScreenplayParser
import os

film_name = "american_psycho"
SCRIPT_PATH = f"data/screenplays/screenplays/{film_name}.txt"

# Create rule-based parser
rule_parser = ScreenplayParser(use_rules=True)

# Read script
with open(SCRIPT_PATH) as reader:
    script = reader.read().split("\n")

# Parse it
rule_tags = rule_parser.parse(script)

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)

# Save to a file with tags and lines together
output_path = f"output/{film_name}_parsed.txt"
with open(output_path, "w") as f:
    for tag, line in zip(rule_tags, script):
        f.write(f"{tag}: {line}\n")

print(f"✓ Parsed {len(script)} lines")
print(f"✓ Saved to {output_path}")