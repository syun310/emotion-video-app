import streamlit as st

emotion_to_video = {
    "기쁨": "joy_video.mp4",
    "슬픔": "sadness_video.mp4",
    "분노": "anger_video.mp4"
}

st.set_page_config(page_title="감정 영상", layout="centered")
st.title("🎬 감정 기반 영상 시스템")
st.markdown("감정을 입력하면 해당 영상이 재생됩니다.")

user_input = st.text_input("감정을 입력하세요 (기쁨/슬픔/분노)")

if user_input:
    if "기쁨" in user_input:
        emotion = "기쁨"
    elif "슬픔" in user_input:
        emotion = "슬픔"
    elif "분노" in user_input or "화" in user_input:
        emotion = "분노"
    else:
        emotion = None

    if emotion:
        st.success(f"감지된 감정: {emotion}")
        st.video(emotion_to_video[emotion])
    else:
        st.warning("기쁨 · 슬픔 · 분노 중 하나만 정확히 입력하세요.")
import streamlit as st

emotion_to_video = {
    "기쁨": "joy_video.mp4",
    "슬픔": "sadness_video.mp4",
    "분노": "anger_video.mp4"
}

st.set_page_config(page_title="감정 영상", layout="centered")
st.title("🎬 감정 기반 영상 시스템")
st.markdown("감정을 입력하면 해당 영상이 재생됩니다.")

user_input = st.text_input("감정을 입력하세요 (기쁨/슬픔/분노)")

if user_input:
    if "기쁨" in user_input:   emotion="기쁨"
    elif "슬픔" in user_input: emotion="슬픔"
    elif "분노" in user_input or "화" in user_input: emotion="분노"
    else: emotion=None

    if emotion:
        st.success(f"감지된 감정: {emotion}")
        st.video(emotion_to_video[emotion])
    else:
        st.warning("기쁨 · 슬픔 · 분노 중 하나만 입력하세요.")

cd ~/Downloads
streamlit run emotion_video_app.py


