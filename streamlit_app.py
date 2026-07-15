import random

import streamlit as st

st.set_page_config(page_title="영단어 + BTS 앱", page_icon="🎵", layout="centered")

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

st.title("📚 영어 공부 + BTS 소개")
st.write("원하는 메뉴를 선택해 보세요!")

word_tab, bts_tab = st.tabs(["📖 영단어 게임", "🎤 BTS 소개"])

with word_tab:
    st.header("영단어 게임")
    st.write("뜻을 보고 영어 단어를 맞혀 보세요. 쉬운 단어로 만들었습니다.")

    if st.button("게임 시작 / 다시 시작"):
        reset_game()

    st.write("")

    if st.session_state.game_over:
        st.success(
            f"게임이 끝났어요! 총 {len(st.session_state.questions)}문제 중 {st.session_state.score}개 맞혔습니다."
        )
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

with bts_tab:
    st.header("BTS 소개")
    st.write("BTS는 대한민국의 인기 그룹입니다. 멤버들은 노래와 춤을 잘합니다.")

    st.subheader("BTS의 특징")
    st.markdown(
        "- 멤버가 7명입니다.\n"
        "- 한국에서 시작해 전 세계에서 사랑받고 있습니다.\n"
        "- 노래, 춤, 특별한 퍼포먼스가 인상적입니다."
    )

    st.subheader("멤버")
    st.markdown(
        "- RM: 리더\n"
        "- Jin: 예쁘고 밝은 분위기\n"
        "- Suga: 멋진 랩\n"
        "- j-hope: 활기찬 에너지\n"
        "- Jimin: 섬세한 춤\n"
        "- V: 독특한 매력\n"
        "- Jungkook: 강한 보컬"
    )

    st.info("BTS는 ‘방탄소년단’이라는 이름을 가지고 있어요. ‘방탄’은 방탄총알처럼 막아낸다는 뜻이랍니다.")
