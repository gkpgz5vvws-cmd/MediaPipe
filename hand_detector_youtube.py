import cv2
import mediapipe as mp
import yt_dlp

# 유튜브 주소 입력받기
youtube_url = input("🔗 유튜브 동영상 링크를 입력하세요: ").strip()

# ffmpeg 없이 다운로드 가능한 단일 포맷(mp4)만 지정하여 가져오기
print("⏳ 유튜브 영상 정보를 분석 및 다운로드 중입니다...")
ydl_opts = {
    'format': 'best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': 'downloaded_video.mp4',
    'noplaylist': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_url])
    video_path = 'downloaded_video.mp4'

# MediaPipe 손 감지 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

# 다운로드된 로컬 영상 파일로 OpenCV 열기
cap = cv2.VideoCapture(video_path)

print("📷 유튜브 손 감지 시작! (종료하려면 영상 창을 누르고 ESC를 누르세요)")

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("⚠️ 영상을 모두 재생했거나 프레임을 읽지 못했습니다.")
            break

        # RGB 변환 및 손 감지 수행
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # 화면에 손 랜드마크 그리기
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style())

        # 결과 화면 출력
        cv2.imshow('YouTube Hand Detection', image)
        
        # ESC 누르면 종료
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()