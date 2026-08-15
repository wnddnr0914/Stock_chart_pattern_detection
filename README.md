

## 📌 Introduce
복잡한 주식 시장의 시계열 데이터를 컴퓨터 비전(CNN) 기술로 판독하여 추세의 변곡점을 짚어내고, LLM(거대 언어 모델)을 활용하여 지금 당장 주목해야 할 실시간 투자 정보를 알기 쉽게 브리핑하는 종합 금융 AI 플랫폼입니다.

<br/>

## ✨ Core Features

### 👁️‍🗨️ CNN 기반 차트 형상 판독 
단순한 보조지표 계산을 넘어, 인간의 눈으로 차트를 분석하는 방식을 AI로 구현했습니다.
* **이미지 변환 파이프라인:** OHLCV 시계열 데이터를 노이즈가 제거된 캔들스틱 차트 이미지로 정밀하게 변환(도해)합니다.
* **패턴 자동 분류:** 변환된 이미지를 CNN 모델에 입력하여 '헤드앤숄더', '이중 천장', '박스권' 등 강력한 하락/상승 징후를 자동 분류합니다.
* **일일 스캐닝 시스템:** 매일 장 마감 후 코스피 주요 종목의 데이터를 스크래핑하여 즉각적인 분석 결과를 도출합니다.


## 🛠️ Tech Stack

* **AI / ML:** PyTorch, Transformers, OpenCV, mplfinance
* **Data Pipeline:** Pandas, FinanceDataReader, pykrx
* **Backend:** FastAPI, Celery
* **Frontend:** React.js, Tailwind CSS
* **Infra:** AWS EC2, Docker

<br/>

## 📈 Architecture Flow

1. **Data Collection:** 매일 특정 시간, 타겟 주식 리스트의 정형 데이터를 수집합니다.
2. **Preprocessing:** 수집된 수치 데이터를 CNN 모델 입력에 적합한 2D 이미지 형태로 변환 및 정규화합니다.
3. **Inference (Vision):** 학습된 딥러닝 모델이 차트 패턴을 분류하고 확률(Confidence Score)을 계산합니다.
4. **Real-time Processing:** 실시간 뉴스 및 호가 데이터를 가져와 LLM이 투자 브리핑을 생성합니다.
5. **Serving:** REST API를 통해 웹 프론트엔드로 분석 결과와 브리핑을 송출합니다.

<br/>

<div align="center">
  <i>© 2026 Project Gaemi-Dohae. All rights reserved.</i>
</div>
