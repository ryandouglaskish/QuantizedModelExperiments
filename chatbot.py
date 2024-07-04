from llama_cpp import Llama

# Load the model
llm = Llama(model_path="models/deepseek-llm-7b-chat.Q4_K_M.gguf", n_ctx=2048, n_threads=6)

# Function to generate a response
def generate_response(prompt):
    output = llm(prompt, max_tokens=100, stop=["Human:", "\n"], echo=True)
    return output['choices'][0]['text'].split("Assistant:")[-1].strip()

# Interactive chat loop
print("Chat with the AI. Type 'quit' to exit.")
while True:
    user_input = input("Human: ")
    if user_input.lower() == 'quit':
        break
    
    response = generate_response(f"Human: {user_input}\nAssistant:")
    print("Assistant:", response)