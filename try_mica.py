from screenplayparser import ScreenplayParser
import os

film_name = "american_psycho"
SCRIPT_PATH = f"data/screenplays/screenplays/{film_name}.txt"

# Create rule-based parser
rule_parser = ScreenplayParser(use_rules=True)

# instantiate a transformer-based parser by setting use_rules=False
# device_id is the GPU id the parser will use
trx_parser = ScreenplayParser(use_rules=False, device_id=1)


# Read script
with open(SCRIPT_PATH) as reader:
    script = reader.read().split("\n")

# Parse it
rule_tags = rule_parser.parse(script)
trx_tags = trx_parser.parse(script)

# Create output directory if it doesn't exist
os.makedirs("yiduo_output", exist_ok=True)

# Save to a file with tags and lines together
rules_output_path = f"yiduo_output/rules_{film_name}_parsed.txt"
with open(rules_output_path, "w") as f:
    for tag, line in zip(rule_tags, script):
        f.write(f"{tag}: {line}\n")

trx_output_path = f"yiduo_output/trx_{film_name}_parsed.txt"
with open(trx_output_path, "w") as f:
    for tag, line in zip(trx_tags, script):
        f.write(f"{tag}: {line}\n")

print(f"✓ Parsed {len(script)} lines")
print(f"✓ Saved to {rules_output_path} and {trx_output_path}")