from llama_cpp import Llama
import json


llm = Llama.from_pretrained(
    repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
    filename="*q8_0.gguf",
    verbose=False
)

prompt = "Q: Name the planets in the solar system? A: "

output = llm(
    prompt, # Prompt
    max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
    stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
    echo=False # Echo the prompt back in the output
) # Generate a completion, can also call create_completion

# print(prompt)
print(json.dumps(output, indent=4))
# print(output['choices'][0]['text'])