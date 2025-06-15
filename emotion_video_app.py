import streamlit as st
import streamlit.components.v1 as components

# 감정과 유튜브 영상 ID 매핑
video_map = {
    "기쁨": "1aY-TS-4mk4",
    "슬픔": "C1EbNnZ4UgI",
    "분노": "RhVVSvBjKJk"
}

st.set_page_config(page_title="감정 기반 영상 소멸 시스템", layout="centered")
st.title("🎞 감정 기반 영상 소멸 시스템")
st.markdown("지금 느끼는 감정을 아래에 입력해주세요. 해당 감정에 맞는 영상이 재생됩니다.")

# 감정 입력
user_input = st.text_input("✍ 지금 어떤 감정이 드시나요?", placeholder="예: 기쁨, 슬픔, 분노...")

# 감정 분석 및 출력
if user_input:
    emotion = "기타"
    if "기쁨" in user_input or "행복" in user_input:
        emotion = "기쁨"
    elif "슬픔" in user_input:
        emotion = "슬픔"
    elif "화" in user_input or "짜증" in user_input:
        emotion = "분노"

    st.success(f"감지된 감정: {emotion}")

    # iframe으로 유튜브 영상 삽입
    if emotion in video_map:
        video_id = video_map[emotion]
        youtube_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&rel=0&modestbranding=1"
        
        components.html(
            f"""
            <iframe width="100%" height="400" src="{y
