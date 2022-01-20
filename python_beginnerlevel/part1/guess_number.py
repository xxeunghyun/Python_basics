print("숫자게임을 시작합니다.")

number = 62

exact_num = input("1에서 100 사이의 숫자를 추측해보세요.\n")
guess = int(exact_num)

if(guess == number):
    print("정답입니다!")

else:
    print("오답입니다!")