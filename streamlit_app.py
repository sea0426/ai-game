import random

import streamlit as st

st.set_page_config(page_title="영단어 게임", page_icon="📚", layout="centered")

WORDS = [
    {"word": "friend", "meaning": "친구"},
    {"word": "school", "meaning": "학교"},
    {"word": "happy", "meaning": "행복한"},
    {"word": "beautiful", "meaning": "예쁜"},
    {"word": "travel", "meaning": "여행하다"},
    {"word": "important", "meaning": "중요한"},
    {"word": "library", "meaning": "도서관"},
    {"word": "winter", "meaning": "겨울"},
    {"word": "practice", "meaning": "연습하다"},
    {"word": "question", "meaning": "질문"},
]


def reset_game():
    st.session_state.questions = random.sample(WORDS, 8)
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.feedback = ""
    st.session_state.answer_input = ""
    st.session_state.game_over = False


if "questions" not in st.session_state:
    reset_game()

st.title("📚 중학생 영단어 게임")
st.write("뜻을 보고 영어 단어를 맞혀 보세요! 쉬운 단어로 만들어봤어요.")

if st.button("게임 시작 / 다시 시작"):
    reset_game()

st.write("")

if st.session_state.game_over:
    st.success(f"게임이 끝났어요! 총 {len(st.session_state.questions)}문제 중 {st.session_state.score}개 맞혔습니다.")
    st.write("다시 시작하려면 버튼을 눌러 주세요.")
else:
    current = st.session_state.questions[st.session_state.index]
    st.caption(f"문제 {st.session_state.index + 1} / {len(st.session_state.questions)}")
    st.metric("점수", f"{st.session_state.score}점")
    st.subheader(f"뜻: {current['meaning']}")

    answer = st.text_input("영어로 써 보세요", key="answer_input")

    if st.button("정답 확인"):
        user_answer = answer.strip().lower()
        if user_answer == current["word"].lower():
            st.session_state.score += 1
            st.session_state.feedback = f"정답입니다! '{current['word']}'예요."
        else:
            st.session_state.feedback = f"아쉽습니다. 정답은 '{current['word']}'입니다."
        st.session_state.show_result = True

    if st.session_state.show_result:
        if "정답입니다" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.session_state.index + 1 >= len(st.session_state.questions):
            if st.button("게임 끝내기"):
                st.session_state.game_over = True
        else:
            if st.button("다음 문제"):
                st.session_state.index += 1
                st.session_state.show_result = False
                st.session_state.feedback = ""
                st.session_state.answer_input = ""
