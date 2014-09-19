from prime_generator import get_primes

with open('wordlist.txt', 'r', encoding="iso-8859-1") as file:
    wordlist = [line.rstrip() for line in file]

lower_alphabet = "abcdefghijklmnopqrstuvwxyz'èóüäçéáåöñëíâôûøêîïàùú"
full_alphabet = lower_alphabet + lower_alphabet.upper()
char_to_prime_map = dict(zip(full_alphabet, get_primes(2)))

def hash(word):
    total = 1 
    for char in word:
        total = total * char_to_prime_map[char]
    return total

def build_hash_map():
    hash_map = {}
    for word in wordlist:
        try:
            hash_map[hash(word)].append(word)
        except KeyError:
            hash_map[hash(word)] = [word]
    return hash_map

def create_anagram_list():
    anagrams = []
    hash_map = build_hash_map()
    for key in hash_map.keys():
        if len(hash_map[key]) > 1:
            anagrams.append(hash_map[key])
    return anagrams
