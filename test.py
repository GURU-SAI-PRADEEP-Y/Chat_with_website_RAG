import openai

# Set your API key
openai.api_key = open_api

# Generate a response using GPT-4oaa
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # Correct model name
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])
