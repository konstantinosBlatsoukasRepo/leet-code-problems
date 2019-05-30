class Solution(object):
    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    def uniqueMorseRepresentations(self, words):
        morsed_words = []
        for word in words:
            morsed_word = []
            for character in word:
                morsed_word.append(self.MORSE[ord(character) - 97])
            joined_morsed = "".join(morsed_word)
            morsed_words.append(joined_morsed)

        morse_words_set = set()
        for morsed_word in morsed_words:
            morse_words_set.add(morsed_word)

        return len(morse_words_set)


solution = Solution()

print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

# "gin" -> "--...-."
