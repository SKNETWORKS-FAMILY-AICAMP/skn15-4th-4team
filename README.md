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
<img width="791" height="452" alt="image" src="https://github.com/user-attachments/assets/c208c1f9-151a-4699-8d71-41c074fde56e" />

---

지속적인 챗봇 기술의 발전으로 **ChatGPT**의 사용자는 기하급수적으로 증가하고 있다.  
특히 학습에 ChatGPT를 활용하는 사례가 크게 늘고 있으며, 실제로 2025년 7월 OpenAI에서는 학생들을 위해 **학습 전용 ChatGPT**를 공개하기도 했다.  

많은 학습자들은 새로운 개념을 이해하거나, 과제를 해결하거나, 자신만의 학습 플랜을 세울 때 GPT를 적극적으로 활용한다.  
궁금한 점이 있으면 GPT에게 질문하고, 필요한 답을 얻으며 학습 효율을 높일 수 있다.

그러나 기존 GPT만으로 학습을 진행하는 데에는 몇 가지 한계점이 존재한다.  


<img width="688" height="313" alt="image" src="https://github.com/user-attachments/assets/cec7611e-597d-49e6-befc-85859c1fa65d" />

---
* **범용적인 학습만을 지원**하기 때문에 **사용자가 특정한 내용을 학습하고 싶을 때 사용하기엔 부적절**하다는 점이 있다. 이는 RAG를 활용하여 사용자가 원하는 학습 데이터를 사용할 수 있도록 개인화시키고자 한다.

* 또 10일, 20일이 지나면 대화가 누적되어 이전 내역을 찾기 어려워지고, 때문에 **장기적인 반복 학습이나 복습에는 다소 취약**하다.


#### 이러한 점을 개선하기 위해, 팀 사고에서는 학습용 웹 어플리케이션인 Anki와 연동하여 망각 주기에 따른 학습이 가능한 챗봇을 구현하고 배포하고자 한다.

  <img width="600" height="529" alt="image" src="https://github.com/user-attachments/assets/ccf7ad95-49d0-40cc-9e71-2a14028be531" />
  
---
* Anki는 위와 같은 망각 주기를 이용하여 사용자가 효과적으로 반복 학습을 할 수 있는 학습용 웹 어플리케이션이다.

* 챗봇은 Anki의 애드온인 Anki Connection을 연동하여, 사용자가 질문한 내용이나 학습한 내용을 바탕으로 **Anki에 저장**하고자 한다. 또, 사용자와 봇의 대화내역은 AWS를 통해 열어둔 외부 DB 서버에 저장되어 이후에도 대화 내역을 열람할 수 있다.

* 또, 사용자가 질문했을 때 시스템**DB, PDF 문서, 이미지 검색을 동시에 활용**하여 **최적의 답변**을 구현하여 환각 및 오정보를 최소한으로 한 학습 어플리케이션이 되도록 할 예정이다.

* 최종적으로, 이러한 서비스를 Docker를 통해 웹으로 배포하는 것이 목표이다.

## 🔑 핵심 기능 소개

- **다중 소스 RAG**  
    데이터베이스, 문서, 이미지 검색을 동시에 통합하여 더욱 풍부하고 정확한 답변 제공
    
- **양방향 처리**
    
    - 사용자에게는 실시간으로 답변 제공
    - 동시에 해당 답변을 DB에 최적화된 형태로 저장 → 학습용 + 검색용으로 활용
- **지속적 복습 지원**  
    DB에 저장된 질문/답변을 MCP + Anki API를 통해 다시 불러와 **개인화된 복습** 가능
    
- **PostgreSQL 기반 구조화 저장**
- MySQL DB를 통한 회원가입 및 **로그인 / 로그아웃 구현.
- 기존 대화 내역 또한 MySQL에 저장하여 사이드 바를 통해 다시 볼 수 있음.
- 사용자는 자신의 대화 내역 만을 볼 수 있고, 오래된 내용은 직접 삭제할 수 있음.

## 🖐️ 프로젝트 소개

### 시스템 흐름도

![[Pasted image 20250916122906.png]]


**웹 페이지 동작 
![[Pasted image 20250916115055.png]]


**chat bot api 작동 방식** 
![[Pasted image 20250916123538.png]]

**벡터 DB 상호 작용**

![[Pasted image 20250916123557.png]]

### ERD
![[Pasted image 20250916123647.png]]

### **auth_user**

사용자 정보를 저장하는 테이블. Django 기본 User 모델과 매핑됩니다.

- `id` (int, PK): 사용자 고유 ID
    
- `password` (varchar): 비밀번호
    
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

