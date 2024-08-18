import streamlit as st

# 앱 제목
st.title('독서 진행 상황 기록 앱')

# 책 목록을 저장할 리스트 초기화
if 'book_list' not in st.session_state:
    st.session_state.book_list = []

# 책 추가 함수
def add_book(book_name):
    st.session_state.book_list.append(book_name)

# 책 삭제 함수
def remove_book(book_name):
    st.session_state.book_list.remove(book_name)

# 책 추가 입력창
book_name = st.text_input("책 이름을 입력하세요:")

# 추가 버튼
if st.button("추가"):
    if book_name:
        add_book(book_name)
        st.success(f"'{book_name}'이(가) 추가되었습니다.")
    else:
        st.warning("책 이름을 입력해 주세요.")

# 책 목록 표시
st.subheader("내 책 목록")

# 각각의 책에 대해 처리
for book in st.session_state.book_list:
    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(book)

    with col2:
        # 삭제 버튼 클릭 시 확인을 위한 상태 저장
        delete_key = f"delete_{book}"
        if st.button("삭제", key=delete_key):
            confirm_key = f"confirm_{book}"  # 확인 메시지를 위한 키
            if not st.session_state.get(confirm_key, False):  # 비어있는 상태라면
                st.session_state[confirm_key] = True  # 확인 상태 설정
                st.warning(f"정말 '{book}'을(를) 삭제하시겠습니까?")  # 확인 메시지 표시
            else:
                # '예' 버튼을 클릭했을 때 책 삭제
                remove_book(book)
                st.success(f"'{book}'이(가) 삭제되었습니다.")
                del st.session_state[confirm_key]  # 확인 상태 삭제

# 앱 종료 버튼
if st.button("앱 종료"):
    st.session_state.book_list.clear()
    st.success("책 목록이 초기화되었습니다.")