import argparse

from src.decipherability import find_decipherable_words_above_threshold
from src.load_dico import load_dico

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('mastered_relations', nargs='+')
    parser.add_argument('--decipherability-threshold', default=1.0, type=float, help="")
    args = parser.parse_args()

    dico = load_dico('../manulex.json')
    decipherable_words = find_decipherable_words_above_threshold(dico,
                                                                 args.mastered_relations,
                                                                 threshold=args.decipherability_threshold)

    print(decipherable_words)
