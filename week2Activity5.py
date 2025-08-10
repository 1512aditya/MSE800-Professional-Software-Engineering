
class Sen:
    def sentence(self):
        return input("Enter a sentence: ")
    
    def countWords(self, sentence):
        return len(sentence.split())

def main():
    analyze = Sen()

    userSentence = analyze.sentence()

    wordCount = analyze.countWords(userSentence)

    print(f"Number of words in the sentence: {wordCount}")

if __name__ == '__main__':
    main()