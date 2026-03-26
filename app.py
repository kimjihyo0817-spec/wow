import streamlit as st

# 1. 저장소 설정 (스트림릿이 재실행되어도 데이터를 기억하게 함)
if 'users' not in st.session_state:
    st.session_state.users = {"admin": "0000"}
if 'seats' not in st.session_state:
    st.session_state.seats = [[0 for _ in range(6)] for _ in range(5)]
if 'user_seat' not in st.session_state:
    st.session_state.user_seat = {}
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

st.title("🏨 스터디카페 키오스크")

# ---------- 로그인 상태가 아닐 때 (메인 화면) ----------
if st.session_state.current_user is None:
    menu = st.sidebar.selectbox("메뉴 선택", ["로그인", "회원가입"])

    if menu == "회원가입":
        st.subheader("📝 회원가입")
        new_id = st.text_input("새 ID 입력")
        new_pw = st.text_input("새 PW 입력", type="password")
        if st.button("가입하기"):
            if new_id in st.session_state.users:
                st.error("이미 존재하는 ID입니다.")
            else:
                st.session_state.users[new_id] = new_pw
                st.success(f"{new_id}님 가입 완료!")

    elif menu == "로그인":
        st.subheader("🔐 로그인")
        user_id = st.text_input("ID 입력")
        user_pw = st.text_input("PW 입력", type="password")
        if st.button("로그인"):
            if user_id in st.session_state.users and st.session_state.users[user_id] == user_pw:
                st.session_state.current_user = user_id
                st.rerun() # 화면 새로고침
            else:
                st.error("ID 또는 PW가 틀렸습니다.")

# ---------- 로그인 완료 상태 (사용자 메뉴) ----------
else:
    st.success(f"👤 {st.session_state.current_user}님 환영합니다!")
    
    if st.button("로그아웃"):
        st.session_state.current_user = None
        st.rerun()

    st.divider()
    
    # 좌석 현황판 그리기
    st.subheader("🪑 좌석 현황")
    cols = st.columns(6)
    for r in range(5):
        cols = st.columns(6)
        for c in range(6):
            seat_label = f"{r+1}-{c+1}"
            is_used = st.session_state.seats[r][c] == 1
            
            # 좌석 버튼
            if cols[c].button(f"{'■' if is_used else '□'}\n{seat_label}", key=f"s{r}{c}"):
                if is_used:
                    # 내가 앉은 자리면 퇴실 가능
                    if st.session_state.user_seat.get(st.session_state.current_user) == (r, c):
                        st.session_state.seats[r][c] = 0
                        del st.session_state.user_seat[st.session_state.current_user]
                        st.info("퇴실 처리되었습니다.")
                        st.rerun()
                    else:
                        st.warning("이미 다른 분이 사용 중입니다.")
                else:
                    # 빈 자리면 입실
                    if st.session_state.current_user in st.session_state.user_seat:
                        st.warning("이미 좌석을 이용 중입니다.")
                    else:
                        st.session_state.seats[r][c] = 1
                        st.session_state.user_seat[st.session_state.current_user] = (r, c)
                        st.success(f"{seat_label} 좌석이 배정되었습니다.")
                        st.rerun()
