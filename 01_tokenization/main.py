import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there i am azaz shaikh"
token = enc.encode(text)

print("token converted ", token)

detoeknizatino = enc.decode(token)

print("decoded token", detoeknizatino)
