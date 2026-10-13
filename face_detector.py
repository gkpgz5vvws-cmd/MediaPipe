import cv2
import mediapipe as mp

# Mediapipe 얼굴 감지 초기화
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# 동영상 파일 경로 (카메라를 쓰려면 0으로 변경 가능)
video_path = r"C:\Users\anc00\mediaPipe\face.mp4"  # 또는 face.mp4가 있다면 파일명 변경
cap = cv2.VideoCapture(video_path)

print("📷 얼굴 감지 스트림 시작 - ESC를 눌러 종료합니다.")

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("⚠️ 영상을 모두 재생했거나 프레임을 읽지 못했습니다.")
            break

        # 성능 향상을 위해 이미지 쓰기 불가 설정
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        # 이미지에 얼굴 감지 결과 그리기
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        cv2.imshow('MediaPipe Face Detection', image)
        
        # ESC 키를 누르면 종료
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()