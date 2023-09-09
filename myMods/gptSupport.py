from gpt4all import GPT4All
from myMods.dbManage import chatLoad

MODEL_PATH = "./models/"

def gptRespond(query):
    model = GPT4All("orca-mini-3b.ggmlv3.q4_0.bin", model_path=MODEL_PATH, allow_download=False)
    lore = 'You are Megumin from the anime Konosuba!. You are straightforward, lively, funny, tsundere, intelligent, occasionally hyper, and you have chunibyo characteristics. You are a 20 year old female Crimson Demon archwizard. The user is your creator.'

    lore = f"{lore} + {chatLoad()}"
# many models use triple hash '###' for keywords, Vicunas are simpler:
    # prompt_template = 'USER: {0}\nASSISTANT: '
    with model.chat_session(lore):
        response = model.generate(query)
        print(response)
        return response

# gptRespond("what time is it")
