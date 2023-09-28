# %%
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("Xenova/gpt-3.5-turbo-16k")
result = tokenizer.encode("hello world")

print(result)

