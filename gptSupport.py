from gpt4all import GPT4All

def gptRespond(query):
    model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin", model_path="/home/anupam/doc/school/school-proj/", allow_download=False)
    output = model.generate(query, max_tokens=50)
    print("output : ",output)
    response = str(output).split("\n")[-1]
    return response
