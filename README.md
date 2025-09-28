# skn15-4th-4team

# 1. 팀 소개
## 📑 Team 사고(思考)

| 이름              | 직책                    | -                                                                                                                                  |
| --------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 최민석 @Minsuk1014 | 팀장, REST API 제작, 벡터 DB 관리, 워크플로우 기획| <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/0f7ec347-9f05-4747-878b-ae4db82ad4fa" /> |
| 김민규 @kmklifegk  | UI 총괄                 | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/4dac5983-f9d7-4bcf-bf9f-56aca4445042" /> |
| 김주형 @wugud09    | Chat bot API 관리 및 연결  | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/4dac5983-f9d7-4bcf-bf9f-56aca4445042" /> |
| 강민정 @kmj212936  | 깃 허브 관리, django DB 구현 | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/d37f032d-a391-4ee7-a640-a42411291697" /> |
| 이세진 @isjini     | Django 구현 총괄          | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/e6c2a8d2-e5ab-4d14-b74e-220eb5cbb098" /> |
| 최서린 @seorinchoi | DB 서버 연결, 깃 허브 문서 관리  | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/f8f8083b-8b6a-49c6-9488-4e80d3bce37f" /> |




# 2. 프로젝트 기간
2025.09.15, 2025.09.16 (총 2일)
	

# 3. 프로젝트 개요

## 📕 프로젝트명
### Anki 기반 개인화 복습 챗봇(웹 사용 가능)


## ✅ 프로젝트 배경 및 목적

# 프로젝트 고도화 계획

[SKNETWORKS-FAMILY-AICAMP/skn15-3rd-4team](https://github.com/SKNETWORKS-FAMILY-AICAMP/skn15-3rd-4team)

기존 프로젝트를 기반으로 **Django 프레임워크**, **AWS 클라우드 인프라**, **데이터베이스(DB)** 를 활용하여  
프로젝트를 확장 및 고도화를 목적으로 진행함.

- Django를 통한 웹 애플리케이션 구조 개선  
- AWS 배포 및 서비스 환경 구축 (EC2 기반)  
- 데이터베이스 연동 및 관리 최적화
- 성능 향상 및 확장성 확보

## 🖐️ 프로젝트 소개

### 시스템 흐름도

<img width="1310" height="758" alt="image" src="https://github.com/user-attachments/assets/51f680ab-6570-4a9f-ad6a-f2719a444ce7" />


**웹 페이지 동작** 
<img width="1382" height="532" alt="image" src="https://github.com/user-attachments/assets/9994dca4-2826-476e-8e2a-e1461156153e" />


**chat bot api 작동 방식** 
<img width="1155" height="693" alt="image" src="https://github.com/user-attachments/assets/45b7c6f8-1d20-4f85-9723-213eb0c61cb6" />


**벡터 DB 상호 작용**

<img width="1651" height="782" alt="image" src="https://github.com/user-attachments/assets/3e2dcd10-3b14-4463-9509-d35b674a7d7c" />


### ERD
<img width="975" height="757" alt="image" src="https://github.com/user-attachments/assets/3ff3ed70-5e88-440b-8ea1-d2d5ed315faf" />


### **auth_user**

사용자 정보를 저장하는 테이블. Django 기본 User 모델과 매핑됩니다.

**- `id` (int, PK): 사용자 고유 ID**
    
**- `password` (varchar): 비밀번호**
    
- `last_login` (datetime): 마지막 로그인 시간
    
- `is_superuser` (tinyint): 슈퍼유저 여부
    
- `username` (varchar): 사용자 이름 (로그인 ID)
    
- `first_name` (varchar): 이름
    
- `last_name` (varchar): 성
    
- `email` (varchar): 이메일 주소
    
- `is_staff` (tinyint): 관리자 여부
    
- `is_active` (tinyint): 활성화 여부
    
- `date_joined` (datetime): 가입일
    

---

### **auth_user_user_permissions**

사용자의 권한 정보를 관리

- `id` (bigint, PK): 고유 ID
    
- `user_id` (int, FK → auth_user.id): 권한을 가진 사용자
    
- `permission_id` (int): 권한 ID
    

---

### **core_conversation**

대화(Conversation) 정보를 저장

- `id` (bigint, PK): 대화 고유 ID
    
- `title` (varchar): 대화 제목
    
- `created_at` (datetime): 생성일
    
- `updated_at` (datetime): 수정일
    
- `user_id` (int, FK → auth_user.id): 대화를 생성한 사용자
    

---

### **core_message**

대화 메시지를 저장

- `id` (bigint, PK): 메시지 고유 ID
    
- `role` (varchar): 메시지 작성자 역할 (ex. user, assistant)
    
- `content` (longtext): 메시지 내용
    
- `created_at` (datetime): 생성일
    
- `conversation_id` (bigint, FK → core_conversation.id): 속한 대화 ID
- ---


## ❤️ 기대효과

### 👌 학습용(PostgreSQL, Anki API 연동)

✅ 질문·답변을 4지선다 문제와 해설로 변환하여 **복습 가능**하게 저장

✅ DB에 입력한 학습용 자료 뿐만 아니라 웹에 올라와 있는 다양한 온라인 자료들을 활용하여 사용자에게 **폭 넓은 학습을 지원**


### 👌검색 최적화용(PostgreSQL)

✅ **질문·답변을 요약하고, “내가 했던 질문인지”를 추적할 수 있도록 저장**

이를 통해 **단순 Q/A 챗봇을 넘어, 개인화된 복습이 가능한 지식 관리형 GPT 시스템을 구현**

✅ 기존 ChatGPT 시스템처럼, **이전 대화 목록을 확인할 수 있는 사이드 바를 구현**, 챗봇 기반 학습 웹으로서의 역할을 충실히 이행하고자 함

## 👉 이 프로젝트의 주요 사용자


🏫학습자(학생, 자격증 준비생, 자기계발러)

👩‍🏫교육자(교사, 강사), 직장인(사내 학습자, 지식 관리자)

🥸일반 학습자(언어, 취미 학습자)로 나눌 수 있음

**모두 공통적으로 “질문-답변을 단순 소비로 끝내지 않고, 나중에 복습/재활용”이 필요한 사람들이 주 타겟.**


# 4. 기술 스택

### 🛠 기술 스택

##### 개발
![Development](https://img.shields.io/badge/Development-Active-brightgreen)
##### 프론트엔드
![Frontend](https://img.shields.io/badge/Frontend-Django-blue)
![JS](https://img.shields.io/badge/JavaScript-ES6-yellow)
![CSS](https://img.shields.io/badge/CSS-3-blueviolet)
##### AI / 챗봇 로직
![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)
![LangChain](https://img.shields.io/badge/LangChain-Active-success)
![LangGraph](https://img.shields.io/badge/LangGraph-Active-success)
![RAG](https://img.shields.io/badge/RAG-Implementation-red)
![Anki](https://img.shields.io/badge/Anki-Integration-blue)
##### DB
![MySQL](https://img.shields.io/badge/MySQL-8.0-lightblue)
![Progress](https://img.shields.io/badge/Progress-Active-green)
##### 배포
![Docker](https://img.shields.io/badge/Docker-Container-blue)
#### 버전 관리
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)


# 5. 수행결과

youtube.com/watch?v=jubY0Vu526w&feature=youtu.be 

# 6. 한 줄 회고

| 이름              | 한줄 회고 |
| --------------- | --------- |
| 최민석 |로컬에서 개발할 때는 기본적인 흐름만 이해하면 되기 때문에 환경적인 부분까지 크게 신경 쓰지 않아도 됐습니다. 하지만 이번에 AWS와 운영체제, 네트워크를 공부하면서 방화벽, 포트포워딩, 보안과 같은 개념들을 새롭게 알게 되었습니다.도커와 같은 환경을 직접 설정해 본 경험이 큰 도움이 되었습니다.|
| 김민규 |조장의 리더십과 포용력으로 팀을 이끌었으며, 조원들이 열심히 해주었던 프로젝트였던거 같다.|
| 김주형 |프로젝트 규모가 커지면서 일정·역할·이슈·리스크 등 챙길 항목이 훨씬 많다는 것을 체감했고, 의사소통과 Git 협업, 브랜치 전략, 충돌 해결의 중요성을 명확히 배웠습니다. 또한 AWS·컨테이너·Django를 통해 개발→배포→운영까지 엔드투엔드(End-to-End) 흐름을 정리하면서 좋은 경험을 할 수 있었습니다.|
| 강민정 |수업 시간에 배운 내용을 직접 활용해 Anki MCP 기반 개인화 복습 챗봇을 구현해본 경험이 신기하고 뜻깊었습니다. 단순히 따라하기에 그치지 않고, 더 나은 플로우를 고민하며 의견을 제안했던 과정도 프로젝트를 진행하는 데 의미 있는 시간이었습니다. 또한 이번 챗봇 개발을 바탕으로, 다음 프로젝트 역할에서는 이미지 검색 기능을 심화적으로 다뤄보고싶다는 흥미와 동기부여도 생겼습니다. 프로젝트를 진행하면서 어려운 부분이나 고민되는 지점이 있을 때, 팀원들과 함께 의견을 나누며 협력했던 순간들 역시 소중한 경험으로 남았습니다.|
| 이세진 |사이드바/입력창 토글 등 UX 개선과 배포·연동을 확장 방향을 팀과 함께 고민했습니다.좋은 팀원들과 함께하며 많이 배우고 성장한 프로젝트였습니다.|
| 최서린 |기존에 배웠던 내용들을 합쳐서 새로운 결과물이 나올 수 있다는 게 신기했습니다. 다들 자기 자리에서 열심히 준비해주신 덕분에 난이도 있는 프로젝트인데도 금방 완성할 수 있었던 것 같습니다!|
