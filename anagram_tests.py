import unittest
import anagrams
import timeit

class AnagramTests(unittest.TestCase):

    def test_wordlist(self):
        self.assertIn("cat", anagrams.wordlist)

    def test_hash_produces_same_score_for_anagrams(self):
        anagram_examples = [
            ("cat", "act"),
            ("actors", "castor"),
            ("obverse", "verbose")
            ]
        for word_1, word_2 in anagram_examples:
            self.assertEqual(anagrams.hash(word_1), anagrams.hash(word_2))

    def test_hash_produces_different_scores_for_non_anagrams(self):
        non_examples = [
            ("cat", "hact"),
            ("actors", "dastor"),
            ("obverse", "vxrbose")
            ]
        for word_1, word_2 in non_examples:
            self.assertNotEqual(anagrams.hash(word_1), anagrams.hash(word_2))

    def test_create_anagram_list_finds_all_anagrams(self):
        expected_anagrams = 20683 
        produced_anagrams = len(anagrams.create_anagram_list())
        self.assertEqual(expected_anagrams, produced_anagrams)

    def test_faster_than_andy_thomas(self):
        """
        This test compares the speed of create_anagram_list()
        to the solution of the original kata author, Andy Thomas.
        On my machine (2.5Ghz, i5), it takes roughly 1.4 seconds
        """
        andy_thomas_speed = 1.8 # in seconds
        produced_speed = timeit.timeit(
                "create_anagram_list()", 
                "from anagrams import create_anagram_list",
                number=1)
        self.assertTrue(produced_speed <= andy_thomas_speed)

if __name__ == "__main__":
    unittest.main()