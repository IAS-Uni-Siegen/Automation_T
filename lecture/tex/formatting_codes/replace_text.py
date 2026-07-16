import os
import re
import shutil

from sources import sources
from images import images

file_path = r"D:\Master_Mechatronics\WHB\Automation Technologies\Automation_T\lecture\tex\Lecture03.tex"

# ----------------------------
# Backup
# ----------------------------
shutil.copy(file_path, file_path + ".bak")

# ----------------------------
# Helpers
# ----------------------------
def build_caption(img_key):
    img = images.get(img_key)
    if not img:
        return None

    caption = img["caption"]
    src = sources.get(img["source_id"])

    if src:
        caption += f" (adapted from \\href{{{src['link']}}}{{{src['source']}}})"

    return caption


def extract_img_key(path):
    base = os.path.basename(path)
    return os.path.splitext(base)[0]


def is_complete_caption(line):
    """
    A caption is complete if it contains:
    \href{link}{source}
    """
    return re.search(r'\\href\{[^}]+\}\{[^}]+\}', line) is not None


# ----------------------------
# Patterns
# ----------------------------
include_pattern = re.compile(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}')
caption_pattern = re.compile(r'\\caption\*?\{.*?\}')

# ----------------------------
# Load file
# ----------------------------
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ----------------------------
# Process
# ----------------------------
i = 0

while i < len(lines):
    line = lines[i]
    match = include_pattern.search(line)

    if match:
        img_path = match.group(1)
        img_key = extract_img_key(img_path)
        caption_text = build_caption(img_key)

        # skip if no mapping found
        if not caption_text:
            i += 1
            continue

        replaced = False

        # -----------------------------------
        # CASE 1: caption exists nearby
        # -----------------------------------
        for j in range(1, 4):
            if i + j < len(lines):
                m = caption_pattern.search(lines[i + j])

                if m:
                    existing_line = lines[i + j]

                    # only replace if caption is NOT complete
                    if not is_complete_caption(existing_line):
                        lines[i + j] = f"    \\caption*{{{caption_text}}}\n"

                    replaced = True
                    break

        # -----------------------------------
        # CASE 2: no caption → wrap in figure
        # -----------------------------------
        if not replaced:
            figure_block = [
                "\\begin{figure}\n",
                f"    {line.strip()}\n",
                f"    \\caption*{{{caption_text}}}\n",
                "\\end{figure}\n"
            ]

            # replace includegraphics line with full figure block
            lines = lines[:i] + figure_block + lines[i + 1:]
            i += len(figure_block)
            continue

    i += 1

# ----------------------------
# Write back
# ----------------------------
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Done: captions updated (only incomplete ones replaced) ✅")