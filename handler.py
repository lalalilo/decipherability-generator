import json

from src.decipherability import find_decipherable_words_above_threshold
from src.load_dico import load_dico

dico = load_dico('./manulex.json')

def main(event, context):
    mastered_relations = list(
        map(str.strip, (event["queryStringParameters"]["masteredRelations"] or '').split(','))
    )

    threshold = float(event["queryStringParameters"]["threshold"] or 1)

    decipherable_words = find_decipherable_words_above_threshold(dico,
                                                                 mastered_relations,
                                                                 threshold=threshold)

    response = {
        "statusCode": 200,
        "body": json.dumps(decipherable_words)
    }

    return response
