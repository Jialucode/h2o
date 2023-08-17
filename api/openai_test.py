
import openai
openai.api_key = "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"

def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=260,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    print(message)
    return message

# Example usage:
# while True:
#     # prompt = "What is the meaning of life?"
#     user_input = input("请输入一些内容：")
# # 打印用户输入
#     print("您输入的内容是:", user_input)
#     message = generate_text(user_input)
#     print(message)
