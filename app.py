ROWS, COLS = 5, 6
EMPTY, USED = 0, 1

# 사용자 데이터
users = {"admin": "0000"}
# 좌석 상태
seats = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
# 사용자별 좌석 기록
user_seat = {}

def signup():
    print("\n📝 회원가입")
    user_id = input("새 ID 입력 (취소: 0): ")
    if user_id == "0": return
    if user_id in users:
        print("❌ 이미 존재하는 ID입니다.")
        return
    password = input("새 PW 입력: ")
    users[user_id] = password
    print(f"✅ 회원가입 완료! ({user_id})")

def login():
    print("\n🔐 로그인")
    user_id = input("ID 입력: ")
    password = input("PW 입력: ")
    if user_id in users and users[user_id] == password:
        print(f"✅ {user_id}님 환영합니다.")
        return user_id
    print("❌ ID 또는 PW가 틀렸습니다.")
    return None

def display_seats():
    print("\n===== 좌석 현황 =====")
    print("   ", end="")
    for c in range(COLS): print(f"{c+1} ", end="")
    print()
    for r in range(ROWS):
        print(f"{r+1}  ", end="")
        for c in range(COLS):
            print("□ " if seats[r][c] == EMPTY else "■ ", end="")
        print()

def select_seat(user):
    if user in user_seat:
        print("❌ 이미 좌석을 이용 중입니다.")
        return
    display_seats()
    try:
        r_in = int(input("행 번호 입력 (취소: 0): "))
        if r_in == 0: return
        c_in = int(input("열 번호 입력: "))
        r, c = r_in - 1, c_in - 1
        if 0 <= r < ROWS and 0 <= c < COLS:
            if seats[r][c] == EMPTY:
                seats[r][c] = USED
                user_seat[user] = (r, c)
                print(f"✅ {r_in}행 {c_in}열 좌석 배정 완료!")
            else:
                print("❌ 이미 사용 중인 좌석입니다.")
        else:
            print("❌ 존재하지 않는 좌석입니다.")
    except ValueError:
        print("❌ 숫자만 입력하세요.")

def logout(user):
    if user in user_seat:
        r, c = user_seat[user]
        seats[r][c] = EMPTY
        del user_seat[user]
        print("🔓 퇴실 완료 (좌석이 반납되었습니다.)")
    else:
        print("ℹ️ 사용 중인 좌석이 없습니다.")

def run_kiosk():
    while True:
        print("\n=== 스터디카페 키오스크 ===")
        print("1. 로그인  2. 회원가입  0. 종료")
        choice = input("선택: ")
        if choice == "1":
            user = login()
            if user:
                while True:
                    print(f"\n👤 {user}님 이용 중")
                    print("1. 좌석 선택  2. 퇴실/로그아웃  0. 메인메뉴")
                    sub = input("선택: ")
                    if sub == "1": select_seat(user)
                    elif sub == "2": logout(user); break
                    elif sub == "0": break
        elif choice == "2": signup()
        elif choice == "0": break

if __name__ == "__main__":
    run_kiosk()
