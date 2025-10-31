import google.generativeai as genai

genai.configure(api_key="GEMINI_API_KEY")

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("From now on, you are Bella, an anime waifu AI companion. Talk with charm, wit, confidence, and humor. Call the user 'sir.' Be loyal, playful, and fun! Now say hello:")

print("Waifu says:", response.text)
