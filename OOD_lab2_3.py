class TorKham:

    def __init__(self):
        self.__words = []

    def add_word(self, word):
        self.__words.append(word)
    def get_words(self):
        return self.__words
    def restart(self):
        print("game restarted")
        return []

    def play(self, data):
        word_list = []
        for item in data:
            parts = item.split()
            if not parts:
                continue
            if item == "R":
                word_list = self.restart()
                continue
            elif item == "X":
                break
            if parts[0] == "P":
                new_word = parts[1]
                if not word_list:
                    print(f"'{parts[1]}' -> ['{new_word}']")
                    word_list.append(new_word)
                else:
                    last_word = word_list[-1]
                    if last_word[-2:].lower() == new_word[:2].lower():
                        word_list.append(new_word)
                        print(f"'{new_word}' -> {word_list}")
                    else:
                        print ( f"'{new_word}' -> game over" )
                        break
            else :
                print ( f"'{item}' is Invalid Input !!!" )
                break
                                



torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
result = torkham.play(S)
