import cv2
import mediapipe as mp

# MediaPipe 초기화
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# 입술 위와 아래의 랜드마크 ID
UPPER_LIP_ID = 13
LOWER_LIP_ID = 14

# 웹캠 열기
cap = cv2.VideoCapture(0)

# FaceMesh 초기화
with mp_face_mesh.FaceMesh(
    max_num_faces=1,  # 최대 감지할 얼굴 수
    refine_landmarks=True,  # 정밀 랜드마크 사용
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("카메라에서 영상을 가져올 수 없습니다.")
            break

        # BGR 이미지를 RGB로 변환
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # FaceMesh 처리
        result = face_mesh.process(rgb_frame)

        # 랜드마크 그리기
        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                h, w, _ = frame.shape
                
                # 전체 얼굴 메쉬 그리기
                mp_drawing.draw_landmarks(
                    frame, face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION,  # 전체 메쉬 연결선
                    mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1)
                )

                # 입술 위와 아래의 좌표 가져오기
                upper_lip = face_landmarks.landmark[UPPER_LIP_ID]
                lower_lip = face_landmarks.landmark[LOWER_LIP_ID]

                # 픽셀 좌표로 변환
                upper_lip_point = (int(upper_lip.x * w), int(upper_lip.y * h))
                lower_lip_point = (int(lower_lip.x * w), int(lower_lip.y * h))

                # 입술 위와 아래에 점 찍기
                cv2.circle(frame, upper_lip_point, 5, (0, 255, 0), -1)  # 녹색 점
                cv2.circle(frame, lower_lip_point, 5, (255, 0, 0), -1)  # 파란색 점

        # 결과 출력
        cv2.imshow('MediaPipe FaceMesh', frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
