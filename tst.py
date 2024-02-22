from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
login(token="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")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))