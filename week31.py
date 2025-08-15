class wordCount:
    def words(self):
        with open("demo_file.txt","r", encoding="utf-8") as self.data:
            self.lines = self.data.read()

            self.word = self.lines.split()
            self.totalWords = len(self.word)

            print ("this is the total word count in this file : ",self.totalWords)
        

def main():
    count=wordCount()
    count.words()

if __name__ == '__main__':
    main()