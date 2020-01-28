import json

def load_dico(json_name):
    with open(json_name) as json_file:
        data = json.load(json_file)
    dico = {line['word']: line['relations'] for line in data}
    return dico