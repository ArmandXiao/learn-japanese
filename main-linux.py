import os
from random import randint

TOTAL_NUM = 1000


class Sentence:
    def __init__(self, num, jp, jph, jpa, cn):
        self.num = num.strip()
        self.jp = jp.strip()
        self.jph = jph.strip()
        self.jpa = jpa.strip().strip("。")
        self.cn = cn.strip()

def read_txt(sentences):
    fi = open("sentences.sep.txt", "r", encoding="utf-8")

    while True:
        num = fi.readline()
        if num == "":
            break
        jp = fi.readline()
        jph = fi.readline()
        jpa = fi.readline()
        cn = fi.readline()
        _ = fi.readline()

        new_sentence = Sentence(num, jp, jph, jpa, cn)
        sentences.append(new_sentence)

def get_input(sentences):
    progress_str = ""
    randflag = False
    randnum = 0
    should_start = False

    try:
        fp = open("progress.txt", "r", encoding="utf-8")
        progress_str = fp.read()
    except:
        fp = open("progress.txt", "w", encoding="utf-8")
        fp.write("1")
        progress_str = "1"

    progress_str = progress_str.strip()
    if progress_str.isnumeric() == False:
        progress_str = "1"

    while True:
        os.system("clear")
        print("You have studied " + progress_str + " out of 1000. Your options:")
        print("1: Start from beginning, 2: Start from #" + progress_str + ", 3: Go to custom #, 4: Random Sentence, 5: exit")
        ans = input("Take your pick: ")
        ans = ans.strip()
        if ans == "1":
            progress_str = "1"
            should_start = True
            break
        elif ans == "2":
            should_start = False
            break
        elif ans == "3":
            while True:
                start_num = input("Tell me where do you want to start? (sentence number): ").strip()
                if start_num.isnumeric == False:
                    print("invalid number")
                    continue
                if int(start_num) > 0 and int(start_num) < 1001:
                    if int(start_num) == 1:
                        should_start = True
                    else:
                        should_start = False
                    progress_str = start_num
                break
            break
        elif ans == "4":
            try:
                randnum = int(input("Pls enter how many random sentences you wanna have:\n"))
                randflag = True
                # print(randnum)
                break
            except:
                print("Can you input a valid number?????????")

        elif ans == "5":
            exit()
    return should_start, randflag, randnum, progress_str

def exec_choice(sentences, should_start, randflag, randnum, progress_str):
    if randflag:
        while randnum > 0:
            os.system("clear")
            start_testing(sentences[randint(0,TOTAL_NUM-1)])
            randnum -= 1
    else:
        for sentence in sentences:
            os.system("clear")
            if should_start == False:
                if sentence.num == progress_str:
                    should_start = True
            if should_start:
                fpo = open("progress.txt", "w", encoding="utf-8")
                fpo.write(sentence.num)
                fpo.close()
                start_testing(sentence)
    
    exec_choice(sentences, *get_input(sentences))

def processAns(ans, jpa):
    index = 0
    ans = ans.strip()
    ans = list(ans)
    while index < len(jpa) and index < len(ans):
        if jpa[index] == " ":
            # list has no return value
            ans.insert(index, " ")
        index += 1

    return "".join(ans)

#@para: sentence: a object of sentence
def start_testing(sentence):
    print("#" + sentence.num)
    print(sentence.jp)
    print(sentence.jph)
    while True:
        ans = input("Type the correct romaji (type 'exit' to quit): \n").strip()
        ans = ans.strip().strip("。").replace(" ","")
        # delete space for matching
        if ans == "exit":
            exit()
        if ans == sentence.jpa.replace(" ",""):
            print("Correct!")
            print("Chisese:", sentence.cn)
            _ = input(" --- press enter to continue --- ")
            break
        else:
            yn = input("Incorrect! Input 'y' to reveal answer. Input anything else to try again.")
            ans_toprint = processAns(ans, sentence.jpa)
            if yn == "y":
                print("Your answer:", ans_toprint)
                print("Correct ans:", sentence.jpa)
                print("Hiragana   :", sentence.jph)
                input("Got it? <Enter> to try again!")
                os.system("clear")
                print("#" + sentence.num)
                print(sentence.jp)
                print(sentence.jph)

if __name__=="__main__":
    # declare global variables
    # global TOTAL_NUM
    # global sentences
    # global randflag
    # global randnum
    # global should_start

    # initialize globals 
    sentences = []

    read_txt(sentences)
    exec_choice(sentences, *get_input(sentences))
