import google.generativeai as genai

# --- PASTE YOUR API KEY HERE ---
try:
    genai.configure(api_key="YOUR_KEY") 
except Exception as e:
    print(f"Error configuring API key: {e}")
    print("--- \nPlease double-check that your API key is correct and pasted as a string.")
    exit()

print("--- Finding available models for your key ---")
found_models = False
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
            found_models = True
except Exception as e:
    print(f"Error listing models: {e}")
    print("--- \nThis often means the 'Generative Language API' is NOT enabled in your Google Cloud Project.")

if not found_models:
    print("\n--- No models found ---")
    print("This is the main problem. Please check the solution below.")

print("--- Test complete ---")
