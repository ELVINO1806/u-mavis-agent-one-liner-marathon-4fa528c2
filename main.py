import os
LINE = "My smartwatch congratulated me on 10,000 steps, then quietly added: 'all of them to the fridge.'"
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
