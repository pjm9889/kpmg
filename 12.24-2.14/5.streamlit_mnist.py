import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import tempfile

# GitHub에 저장된 TFLite 모델 URL
TFLITE_MODEL_URL = "https://github.com/pjm9889/kpmg/raw/main/data/my_mnist_model.tflite"

# TFLite 모델 다운로드 및 로드
def load_tflite_model_from_url(url):
    try:
        # 모델 다운로드
        response = requests.get(url)
        response.raise_for_status()
        
        # 임시 파일에 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix=".tflite") as temp_file:
            temp_file.write(response.content)
            tflite_model_path = temp_file.name
        
        # TFLite 인터프리터 로드
        interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
        interpreter.allocate_tensors()
        return interpreter
    except Exception as e:
        st.error(f"모델 로드 실패: {e}")
        return None

# TFLite 모델 로드
st.sidebar.title("TFLite 모델 로드")
interpreter = load_tflite_model_from_url(TFLITE_MODEL_URL)

if interpreter:
    st.sidebar.success("모델이 성공적으로 로드되었습니다!")

    # 입력/출력 세부 정보
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    st.sidebar.write("입력 세부 정보:", input_details)
    st.sidebar.write("출력 세부 정보:", output_details)

    # 캔버스 설정
    st.title("딥러닝 손글씨 예측 앱")
    st.write("캔버스에 손글씨를 직접 입력하세요!")

    canvas_result = st_canvas(
        fill_color="#000000",  # 검은색으로 채우기
        stroke_width=10,      # 선 두께
        stroke_color="#FFFFFF",  # 흰색으로 그리기
        background_color="#000000",  # 검은 배경
        height=200,
        width=200,
        drawing_mode="freedraw",  # 자유롭게 그리기
        key="canvas",
    )

    # 캔버스 결과 처리
    if canvas_result.image_data is not None:
        try:
            # 캔버스 데이터를 numpy 배열로 변환
            img_array = canvas_result.image_data.astype("uint8")

            # PIL 이미지로 변환 후 28x28 크기로 리사이즈
            img = Image.fromarray(img_array).convert("L")  # 흑백 변환
            img_resized = img.resize((28, 28))  # 28x28 크기로 축소
            img_normalized = np.array(img_resized) / 255.0  # 정규화
            img_normalized = img_normalized.reshape((1, 28, 28, 1)).astype(np.float32)  # 모델 입력 형식으로 변환

            # TFLite 모델에 입력 데이터 설정
            interpreter.set_tensor(input_details[0]['index'], img_normalized)

            # 추론 실행
            interpreter.invoke()

            # 출력 데이터 가져오기
            predictions = interpreter.get_tensor(output_details[0]['index'])
            predicted_label = np.argmax(predictions)

            # 결과 출력
            st.subheader("예측 결과")
            st.write(f"예측값: {predicted_label}")
            st.bar_chart(predictions[0])  # 확률 분포 시각화
        except Exception as e:
            st.error(f"이미지 처리 또는 예측 실패: {e}")
else:
    st.error("모델 로드에 실패했습니다. GitHub URL을 확인하세요.")
