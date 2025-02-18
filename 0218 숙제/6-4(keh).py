class Memo:
    def __init__(self,text1="",text2=""):
        self.text1 = text1
        self.text2 = text2
    def write(self):
        text1 = input("메모할 사항을 입력하세요 !")
        with open("memo.txt","w",encoding="utf-8") as f:
            f.write(text1)
    def rewrite(self):
        text2 = input("추가 메모를 입력하세요 !")
        with open("memo.txt","a",encoding="utf-8") as f:
            f.write(f" {text2}")
    def read_memo(self):
        f = open("memo.txt","r",encoding="utf-8")
        for line in f:    
            return line 
        f.close()