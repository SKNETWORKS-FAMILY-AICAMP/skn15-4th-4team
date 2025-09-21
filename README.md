# skn15-4th-4team

# 1. 팀 소개
## 📑 Team 사고(思考)

| 이름              | 직책                    | -                                                                                                                                  |
| --------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 최민석 @Minsuk1014 | 팀장, Chat bot API 관리   | <img width="102" height="116" alt="image" src="https://github.com/user-attachments/assets/0f7ec347-9f05-4747-878b-ae4db82ad4fa" /> |
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



# 6. 한 줄 회고

**최서린** 이전에 streamlit으로 만든걸 웹으로 배포하는 과정이 사실 쉽지만은 않았지만, 인터넷 안에서 접속이 되고 db 서버로 연결도 해보고 여러모로 재미있는 경험이었던 것 같습니다. 팀원분들이 함께 노력해주셔서 그런 것 같습니다! 감사합니다!
