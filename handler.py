import json

from src.decipherability import find_decipherable_words_above_threshold, compute_decipherability_for_text, \
    find_words_with_non_mastered_LO
from src.load_dico import load_dico

dico = load_dico('./manulex.json')

def find_mastered_words(event, context):
    mastered_relations = list(
        map(str.strip, (event["queryStringParameters"]["masteredRelations"] or '').split(','))
    )

    threshold = float(event["queryStringParameters"]["threshold"] or 1)

    decipherable_words = find_decipherable_words_above_threshold(dico,
                                                                 mastered_relations,
                                                                 threshold=threshold,
                                                                 include_words_with_muted_letters=False)

    response = {
        "statusCode": 200,
        "body": json.dumps(decipherable_words)
    }

    return response


def decipherability_text(event, context):
    mastered_relations = list(
        map(str.strip, (event["queryStringParameters"]["masteredRelations"] or '').split(','))
    )
    text = event["queryStringParameters"]["text"]

    decipherability = compute_decipherability_for_text(dico, mastered_relations, text)

    response = {
        "statusCode": 200,
        "body": decipherability
    }

    return response


def find_mastered_words_with_LO(event, context):
    mastered_relations = list(
        map(str.strip, (event["queryStringParameters"]["masteredRelations"] or '').split(','))
    )
    LO = event["queryStringParameters"]["LO"]

    decipherable_words = find_words_with_non_mastered_LO(dico, LO, mastered_relations)

    response = {
        "statusCode": 200,
        "body": json.dumps(decipherable_words)
    }

    return response
