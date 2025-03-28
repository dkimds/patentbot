# patentbot
### LLM-Based Patent Evaluation Agent

## Overview
특허의 기술적 가치를 평가하기 위한 AI 기반 특허 평가 에이전트입니다. Retrieval-Augmented Generation(RAG)과 인터뷰 스타일 멀티에이전트 시스템을을 조합하여 특허의 질적 가치를 평가합니다.

## Features
- **Patent Document Parsing**: PDF 및 텍스트 기반 특허 문서 업로드 및 분석
- **Automated Value Estimation**: LLM 에이전트를를 통한 기술적 가치 평가
- **Streamlit Web Interface**: 사용자 친화적인 웹 대시보드 제공

## Tech Stack
- LangGraph
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
streamlit run research_assistant.py
```

## Roadmap
- [x] 특허 문서 업로드 및 파싱
- [x] 멀티 에이전트 기반 기술 분석
- [ ] vLLM 최적화 배포

## License
MIT License

