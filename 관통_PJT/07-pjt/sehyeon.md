# 🎬 07-pjt : Database 설계를 활용한 REST API 설계(영화)
## 📌 프로젝트 개요

이 프로젝트는 영화 관련 데이터를 관리하고 사용자 리뷰를 처리하는 REST API 서버를 만드는 것을 목표로 합니다. Django + Django REST Framework를 활용하여 배우, 영화, 리뷰 데이터를 조회하거나 생성·수정·삭제할 수 있는 구조를 구축했습니다.

---

## ⚙️ 주요 기능

| 구분         | 기능명                  | 설명                                                |
| ---------- | -------------------- | ------------------------------------------------- |
| Actor API  | 전체 배우 조회             | `/api/v1/actors/` GET                             |
| Actor API  | 단일 배우 조회             | `/api/v1/actors/<actor_id>/` GET                  |
| Movie API  | 전체 영화 조회             | `/api/v1/movies/` GET                             |
| Movie API  | 단일 영화 조회             | `/api/v1/movies/<movie_id>/` GET (출연 배우 & 리뷰 포함)  |
| Review API | 전체 리뷰 조회             | `/api/v1/reviews/` GET                            |
| Review API | 단일 리뷰 조회·수정·삭제       | `/api/v1/reviews/<review_id>/` GET / PUT / DELETE |
| Review API | 리뷰 생성                | `/api/v1/movies/<movie_id>/reviews/` POST         |
| Validation | Serializer 기반 유효성 검증 | 입력 데이터 검증 및 응답 데이터 직렬화                            |
| RESTful 설계 | HTTP Method 규칙 준수    | GET/PUT/POST/DELETE 동작 구현                         |
| 초기 데이터     | fixtures 로드          | actors.json / movies.json / reviews.json          |



---

## 📋 구현 기능 및 기술


### Serializer 구성

요구사항에 맞춰 데이터 검증 및 응답 구조를 설정했습니다.

1. 배우 목록/상세용 Serializer
2. 영화 목록/상세용 Serializer
3. 리뷰 목록/상세/생성 Serializer

리뷰 생성 시 movie 필드는 read_only이며, 뷰에서 값 주입 방식 사용

---

### 전체 리뷰 조회 /api/v1/reviews/ (GET)

![](/images/5.png)

* 리뷰 title, content 조회

---

### 리뷰 상세(/api/v1/reviews/<id>/)

![](/images/6.png)

* **GET**
* 리뷰 자체 데이터
* 대상 영화 제목 포함

---

![](/images/7.png)

* **PUT**
* 유효한 데이터만 수정

![](/images/8.png)

---

* **DELETE**
* 리뷰 삭제
* JSON 메시지 예시:
```JSON
{ "message": "review 1 is deleted." }
```

---

### 리뷰 생성 /api/v1/movies/<movie_id>/reviews/ (POST)

![](/images/9.png)

* 전달된 title, content로 새로운 리뷰 생성
* movie_id는 URL에서 가져와 자동 주입
* 성공 응답 예시:
```JSON
{
  "id": 11,
  "movie": { "title": "The Super Mario Bros. Movie" },
  "title": "new title !",
  "content": "new content !"
}

```

---


## 💡 학습한 내용

1. HTTP Method 기반 RESTful 설계
2. DRF Serializer를 활용한 유효성 검증 및 데이터 구조화
3. URL Parameter와 데이터 주입 방식 이해

---

## 🤔 어려웠던 부분

* movie 필드를 read_only로 두고 뷰에서 데이터를 넣어주는 방식이 초반에는 익숙하지 않아 오류가 자주 발생했다.
* 영화 상세 응답에 배우 목록과 리뷰 목록을 동시에 포함시키는 구조를 만들 때 Serializer 순환 참조 문제와 import 순서 충돌을 해결하는 데 시간이 걸렸다.

---

## 🌱 새로 배운 것

* GET/POST/PUT/DELETE 요청 흐름 전체 사이클
* Serializer를 통한 응답 구조 커스터마이징
* get_object_or_404 활용

---

## ✨ 느낀 점

* 이번 프로젝트를 통해 단순 CRUD를 구현하는 것을 넘어 API를 어떻게 설계하고 응답 구조를 어떻게 설계할 것인가를 스스로 고민하게 되었다.
* 특히 HTTP Method 의미를 정확히 적용하고 Serializer를 상황에 맞게 조합하며 RESTful 규칙에 따라 기능을 나누는 과정을 거치며 실제 서비스 API 개발의 감각을 익혔다.
