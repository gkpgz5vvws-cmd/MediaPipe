# 🤖 MediaPipe 예제 모음 (Hands & Face Detection)

Google MediaPipe 라이브러리를 활용한 컴퓨터 비전 및 머신러닝 실습 프로젝트입니다[cite: 16].

---

## 📂 프로젝트 구성 (Files)

* **`hand_detector.py`**: MediaPipe Hands를 활용한 실시간 손 감지 및 랜드마크 트래킹 프로그램 (동영상/웹캠 지원)
* **`face_detector.py`**: MediaPipe Face Detection을 활용한 얼굴 영역 및 특징점 감지 프로그램
* **`selfie_segmentation.py`**: 사람과 배경을 분리하여 배경 블러(Blur) 처리를 수행하는 이미지 세그멘테이션 실습 파일[cite: 15]
* **`requirements.txt`**: 프로젝트 실행에 필요한 필수 패키지 목록 (`mediapipe`, `opencv-python`)

---

## ⚙️ 환경 설정 및 실행 방법 (How to Run)

1. **가상환경 생성 및 활성화**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate