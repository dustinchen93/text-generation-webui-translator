import requests

def send_payload(prompt, server="127.0.0.1"):
    request = {
        'prompt':f"User:{prompt}\nAssistant:",
        'max_new_tokens': 1024,
        'do_sample': True,
        'temperature': 0.8,
        'top_p': 0.5,
        'typical_p': 1,
        'repetition_penalty': 1.2,
        'encoder_repetition_penalty': 1.0,
        'top_k': 100,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'custom_stopping_strings': "Assistant:" ##for example <-----------
    }
    
    response = requests.post(f"http://{server}:5000/api/v1/generate", json=request)
    return response.json()["results"][0]["text"]
