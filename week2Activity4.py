"""
init comes very handy it helps to pass the data one time only so we don't have to pass it
repeatedly
"""
class StringManipulator:
    def find_character(self, text, char):
        return text.find(char)

    def find_length(self, text):
        return len(text)
    
    def convert_to_uppercase(self, text):
        return text.upper()

def main():
    name = "eamplex"
    manipulator = StringManipulator()

    result = manipulator.find_character(name, 'x')
    print(result)

    length = manipulator.find_length(name)
    print(length)

    uppercase_text = manipulator.convert_to_uppercase(name)
    print(uppercase_text)

if __name__=='__main__':
    main()