# 📘 Parse mock email headers and body from plain unstructured text

raw_email = """
From: alice@example.com
To: bob@example.com
Date: 2025-09-16
Subject: Project update

Hi Bob,

Here's the latest update on the quantum learning experiments. Let’s sync up Thursday.

Best,
Alice
"""

# Basic parsing
lines = raw_email.strip().split('\n')
meta = {k.strip(): v.strip() for k, v in [line.split(':', 1) for line in lines if ':' in line]}
body = '\n'.join(line for line in lines if ':' not in line and line.strip())

print("📌 Parsed Metadata:", meta)
print("\n📝 Body Content:\n", body)

# === 🏠 HOMEWORK ===
# 1. Try parsing multiple emails separated by "---".
# 2. Add regex to extract specific patterns (e.g., date, email, keywords).
