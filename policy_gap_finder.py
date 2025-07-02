import json
import requests

# LM Studio API settings
API_URL = "http://127.0.0.1:1234/v1/chat/completions"  # Ensure this matches your LM Studio config
MODEL_NAME = "meta-llama-3-8b-instruct"  # Adjust to your actual model name

# Load internal policy file
with open("data/internal_policy.txt", "r", encoding="utf-8") as f:
    internal_policy = f.read()

# Load ISO controls JSON
with open("data/iso-controls.json", "r", encoding="utf-8") as f:
    iso_data = json.load(f)

# Prepare output file
output_path = "data/audit_results.txt"
with open(output_path, "w", encoding="utf-8") as output_file:

    # Iterate through each control
    for domain in iso_data["domains"]:
        for control in domain["controls"]:
            prompt = f"""
Act as a cybersecurity auditor.

This is the internal policy:
\"\"\"{internal_policy}\"\"\"

This is the ISO control ({control['ref']} - {control['title']}):
\"\"\"{control['summary']}\"\"\"

Does the policy meet this control? Reply YES, NO, or PARTIALLY. Explain briefly.
"""

            try:
                # Send request to LM Studio
                response = requests.post(API_URL, json={
                    "model": MODEL_NAME,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.3
                })

                # Parse response
                res_json = response.json()
                if "choices" not in res_json:
                    error_message = f"⚠️ Unexpected response format:\n{res_json}\n"
                    print(error_message)
                    output_file.write(error_message)
                    continue

                reply = res_json["choices"][0]["message"]["content"]

                # Print and write output
                result = f"✅ {control['ref']} - {control['title']}\n💬 {reply}\n{'=' * 60}\n"
                print(result)
                output_file.write(result)

            except Exception as e:
                error_text = f"❌ Error communicating with LM Studio: {e}\n"
                print(error_text)
                output_file.write(error_text)
