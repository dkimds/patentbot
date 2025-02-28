# patentbot
### AI-Based Patent Evaluation Bot

## Overview
PatentGenius는 특허의 기술적, 법적 가치를 평가하기 위한 AI 기반 특허 평가 봇입니다. Retrieval-Augmented Generation(RAG)과 감성 기반 가치 평가를 조합하여 특허의 질적 가치를 정량화합니다.

## Features
- **Patent Document Parsing**: PDF 및 텍스트 기반 특허 문서 업로드 및 분석
- **RAG-based Prior Art Search**: 유사특허 검색 및 기술분류 기반 필터링
- **Automated Value Estimation**: LLM을 통한 기술적 가치 평가
- **Streamlit Web Interface**: 사용자 친화적인 웹 대시보드 제공

## Tech Stack
- LlamaIndex
- LangChain
- FAISS
- Streamlit

## Installation
```bash
git clone https://github.com/yourname/patentbot.git
cd patentbot
pip install -r requirements.txt
```

## Usage
```bash
streamlit run app.py
```

## Roadmap
- [x] 특허 문서 업로드 및 파싱
- [x] RAG 기반 유사특허 검색
- [ ] 멀티 에이전트 기반 기술분류 매칭
- [ ] 감성 기반 가치 평가 모델 추가
- [ ] vLLM 최적화 배포

## License
MIT License

