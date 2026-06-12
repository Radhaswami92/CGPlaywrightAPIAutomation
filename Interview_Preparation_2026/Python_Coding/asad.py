from pathlib import Path

current_script = Path(__file__).resolve()

# 2. Go up 2 levels: Python_Coding -> Interview_Preparation_2026 -> CGPlaywrightAPIAutomation
project_root = current_script.parents[2]

print(project_root)
actual_path =str(project_root) + r"\Learn_Playwright_BDD_Framework\features\OrderTransaction.feature"
print(actual_path)