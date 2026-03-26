# =====================================
# Study Cafe Kiosk System (Pro Version)
# SignUp + Login + Seat + Logout
# Google Colab Compatible
# =====================================

ROWS, COLS = 5, 6
EMPTY, USED = 0, 1

# 사용자 데이터
users = {
    "admin": "0000"
}

# 좌석 상태
seats = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# 사용자별 좌석 기록
user_seat = {}   # { user_id : (r, c) }

# ---------- 회원가입 ----------
def signup():
    print("\n📝 회원가입")
    while True:
        user_id = input("새 ID 입력 (취소: 0): ")
        if user_id == "0":
            return
        if user_id in users:
            print("❌ 이미 존재하는 ID입니다.")
            continue

        password = input("새 PW 입력: ")
        users[user_id] = password
        print(f"✅ 회원가입 완료! ({user_id})")
        return

# ---------- 로그인 ----------
def login():
    print("\n🔐 로그인")
    for _ in range(3):
        user_id = input("ID 입력: ")
        password = input("PW 입력: ")

        if user_id in users and users[user_id] == password:
            print(f"✅ {user_id}님 환영합니다.")
            return user_id
        else:
            print("❌ ID 또는 PW가 틀렸습니다.")

    print("🚫 로그인 실패")
    return None

# ---------- 좌석 출력 ----------
def display_seats():
    print("\n===== 좌석 현황 =====")
    print("□ : 빈 좌석   ■ : 사용 중")
    print("    ", end="")
    for c in range(COLS):
        print(f"{c+1} ", end="")
    print()

    for r in range(ROWS):
        print(f"{r+1}   ", end="")
        for c in range(COLS):
            print("□ " if seats[r][c] == EMPTY else "■ ", end="")
        print()
    print("=====================")

# ---------- 좌석 선택 ----------
def select_seat(user):
    if user in user_seat:
        print("❌ 이미 좌석을 이용 중입니다.")
        return

    while True:
        try:
            r = int(input("행 번호 입력 (취소: 0): "))
            if r == 0:
                return

            c = int(input("열 번호 입력: "))
            r -= 1
            c -= 1

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                print("❌ 존재하지 않는 좌석입니다.")
                continue

            if seats[r][c] == USED:
                print("❌ 이미 사용 중인 좌석입니다.")
                continue

            seats[r][c] = USED
            user_seat[user] = (r, c)
            print(f"✅ 좌석 배정 완료 ({user})")
            return

        except ValueError:
            print("❌ 숫자만 입력하세요.")

# ---------- 로그아웃 ----------
def logout(user):
    if user in user_seat:
        r, c = user_seat[user]
        seats[r][c] = EMPTY
        del user_seat[user]
        print("🔓 로그아웃 완료 (좌석 해제됨)")
    else:
        print("ℹ️ 사용 중인 좌석이 없습니다.")

# ---------- 사용자 메뉴 ----------
def user_menu(user):
    while True:
        print(f"\n👤 {user}님 메뉴")
        print("1. 좌석 선택")
        print("2. 로그아웃 (자리 반납)")
        print("0. 메인 화면")

        choice = input("선택: ")

        if choice == "1":
            display_seats()
            select_seat(user)

        elif choice == "2":
            logout(user)
            return

        elif choice == "0":
            return

        else:
            print("❌ 올바른 메뉴를 선택하세요.")

# ---------- 메인 키오스크 ----------
def run_kiosk():
    print("📌 스터디카페 키오스크 시작")

    while True:
        print("\n=== 메인 화면 ===")
        print("1. 로그인")
        print("2. 회원가입")
        print("0. 종료")

        choice = input("선택: ")

        if choice == "1":
            user = login()
            if user:
                user_menu(user)

        elif choice == "2":
            signup()

        elif choice == "0":
            print("이용해주셔서 감사합니다.")
            break

        else:
            print("❌ 올바른 메뉴를 선택하세요.")

# 실행
run_kiosk()
