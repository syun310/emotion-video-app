import streamlit as st
import os

st.title("🎭 감정 기반 영상 전시")
st.write("당신의 감정을 입력하면, 그 감정에 어울리는 영상이 재생됩니다.")

emotion = st.text_input("당신의 감정은 무엇인가요? (예: 기쁨, 슬픔, 분노, 평온)")

video_map = {
    "기쁨": "happy.mp4",
    "슬픔": "sad.mp4",
    "분노": "angry.mp4",
    "평온": "calm.mp4"
}

if emotion:
    video = video_map.get(emotion)
    if video and os.path.exists(video):
        st.success(f"'{emotion}' 감정에 어울리는 영상을 재생합니다.")
        st.video(video)
    else:
        st.warning("⚠️ 해당 감정에 맞는 영상이 없어요. 다른 감정을 입력해보세요.")
