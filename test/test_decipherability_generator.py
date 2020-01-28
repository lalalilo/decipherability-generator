import unittest

from src.decipherability import compute_decipherability_percentage, find_decipherable_words_above_threshold


class DecipherabilityGeneratorTest(unittest.TestCase):

    def test_find_decipherable_words_above_threshold(self):
        dico = self._get_dico()
        mastered_relations = ['ch-S', 'au-O', 'ff-f', 'a-a']
        words_with_percentages = find_decipherable_words_above_threshold(dico, mastered_relations)

        self.assertIn('chauffa', words_with_percentages)
        self.assertIn('chevrotement', words_with_percentages)
        self.assertIn('vin', words_with_percentages)
        self.assertEqual(1.0, words_with_percentages['chauffa'])
        self.assertEqual(1/10, words_with_percentages['chevrotement'])
        self.assertEqual(0.0, words_with_percentages['vin'])

    def test_find_decipherable_words_above_threshold_with_threshold(self):
        dico = self._get_dico()
        mastered_relations = ['ch-S', 'au-O', 'ff-f', 'a-a']
        words_with_percentages = find_decipherable_words_above_threshold(dico, mastered_relations, threshold=0.2)

        self.assertIn('chauffa', words_with_percentages)
        self.assertNotIn('chevrotement', words_with_percentages)
        self.assertNotIn('vin', words_with_percentages)
        self.assertEqual(1.0, words_with_percentages['chauffa'])

    def test_find_decipherable_words_above_threshold_100(self):
        dico = self._get_dico()
        mastered_relations = ['ch-S', 'au-O', 'ff-f', 'a-a']
        words_with_percentages = find_decipherable_words_above_threshold(dico, mastered_relations, threshold=1.0)

        self.assertIn('chauffa', words_with_percentages)
        self.assertNotIn('chevrotement', words_with_percentages)
        self.assertNotIn('vin', words_with_percentages)
        self.assertEqual(1.0, words_with_percentages['chauffa'])

    @staticmethod
    def _get_dico():
        return {
            'chauffa': ['ch-S', 'au-O', 'ff-f', 'a-a'],
            'chevrotement': ['ch-S', 'e-*', 'v-v', 'r-R', 'o-O', 't-t', 'e-#', 'm-m', 'en-@', 't-#'],
            'vin': ['v-v', 'in-5'],
        }
