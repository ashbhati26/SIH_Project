import openai

openai.api_key = "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"  # Replace with your OpenAI API key

messages = []

# System message to start a career counseling chat
messages.append({"role": "system", "content": "You are now chatting with Career Counselor ChatGPT. Please ask any career-related questions."})

print("Your Career Counselor AI is ready!")
while True:
    user_input = input("User: ")
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("AI: " + reply + "\n")
