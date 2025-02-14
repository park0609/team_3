
def youngu():
    text = input("단어를 입력하세요")
    if text[0] == text[2]:
        return (f"{text}는 거꾸로 해도 같은 단어입니다.")
    else:
        return (f"{text}는 거꾸로 해도 같은 단어가 아닙니다.")
youngu()