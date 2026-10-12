import os
import json

folder_path = r"D:\Master_Mechatronics\WHB\Automation Technologies\Automation_T\lecture\fig\lec03"

sources = {}

for file in os.listdir(folder_path):
    if file.endswith(".pdf") or file.endswith(".png") or file.endswith(".jpg"):
        name = os.path.splitext(file)[0] 
        
        sources[name] = {
            "caption": "CAPTION",
            "source_id": "Newby"
        }
        
# Save as JSON file
with open("image_sources.json", "w", encoding="utf-8") as f:
    json.dump(sources, f, indent=4)

print("Dictionary created !!!")