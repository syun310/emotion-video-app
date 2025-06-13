
import streamlit as st

# 감정과 대응되는 영상 파일 매핑 (파일은 같은 폴더에 있어야 함)
emotion_to_video = {
    "기쁨": "joy_video.mp4",
    "슬픔": "sadness_video.mp4",
    "분노": "anger_video.mp4",
    "불안": "anxiety_video.mp4"
}

st.set_page_config(page_title="감정 기반 영상 소멸 시스템", layout="centered")
st.title("🎬 감정 기반 영상 소멸 시스템")
st.markdown("지금 느끼는 감정을 아래에 입력해주세요. 해당 감정에 맞는 영상이 재생됩니다.")

# 사용자 감정 입력 받기
user_input = st.text_input("✍️ 지금 어떤 감정이 드시나요?", placeholder="예: 기쁨, 슬픔, 화남...")

# 감정 매칭 및 영상 재생
if user_input:
    emotion = "기타"
    if "기쁘" in user_input or "행복" in user_input:
        emotion = "기쁨"
    elif "슬프" in user_input:
        emotion = "슬픔"
    elif "화" in user_input or "짜증" in user_input:
        emotion = "분노"
    elif "불안" in user_input or "초조" in user_input:
        emotion = "불안"

    st.success(f"감지된 감정: {emotion}")

    if emotion in emotion_to_video:
        video_path = emotion_to_video[emotion]
        st.video(video_path)
    else:
        st.warning("해당 감정에 맞는 영상이 아직 준비되지 않았습니다.")
