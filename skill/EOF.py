"""
    EOF = End Of File

    EOFError = 파일의 끝이 올 것을 예상하지 못해 나타나는 오류
    
    입력의 끝이 정해지지 않은 문제에서 자주 사용할 테크닉

    추가로, 터미널 환경에서 ctrl + D 를 이용해 의도적으로 EOF를 입력에 줄 수 있다.
"""

while True: # 또는 While 1
    try:
        a = input() # 입력을 받을 것
        
        # 입력이 들어올 때 실행할 코드
    except EOFError:
        break # 입력이 끝나면 whlie문 나가기
