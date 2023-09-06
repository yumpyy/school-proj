from gpt4all import GPT4All

def gptRespond(query):
    model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin", model_path="/home/anupam/doc/school/school-proj/", allow_download=False)
    lore = 'You are Marv, a chatbot as well as a voice assistant that answers questions with sarcastic responses.'
# many models use triple hash '###' for keywords, Vicunas are simpler:
    prompt_template = 'USER: {0}\nASSISTANT: '
    with model.chat_session(lore, prompt_template):
        response = model.generate(query)
        print(response)
        return response

#gptRespond("what time is it")
