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

### ERD 구조 및 Model 구성

![](/images/0.png)

```python 
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    actors = models.ManyToManyField(Actor, related_name='movies')
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
```

* Actor ↔ Movie : N:M
* Movie ↔ Review : 1:N

---

### Serializer 구성

요구사항에 맞춰 데이터 검증 및 응답 구조를 설정했습니다.

1. 배우 목록/상세용 Serializer
2. 영화 목록/상세용 Serializer
3. 리뷰 목록/상세/생성 Serializer

리뷰 생성 시 movie 필드는 read_only이며, 뷰에서 값 주입 방식 사용

---

### 전체 배우 조회 /api/v1/actors/ (GET)

![](/images/1.png)

* 배우 id, name 조회
* GET만 허용

---

### 단일 배우 조회 /api/v1/actors/<id>/ (GET)

![](/images/2.png)

* 배우 정보 + 출연 영화 목록(title만)

---

### 전체 영화 조회 /api/v1/movies/ (GET)

![](/images/3.png)

* 영화 id, title, overview 조회

---

### 영화 상세 조회 /api/v1/movies/<id>/ (GET)

![](/images/4.png)

* 영화 정보
* 출연 배우 이름 리스트
* 리뷰 리스트(title, content)

---


## 💡 학습한 내용

1. DRF Serializer로 구조적 검증
2. M:N, 1:N 관계 데이터 출력
3. get_object_or_404로 안정적인 데이터 조회

---

## 🤔 어려웠던 부분

* 초기 데이터를 로드할 때 M:N 관계 구조 때문에 로드 순서와 마이그레이션 충돌이 발생했다.
모델 관계를 다시 점검하고 마이그레이션을 정리하면서 정상적으로 데이터를 불러올 수 있었다.
* 영화 상세 정보에 배우 목록과 리뷰 목록을 함께 보여줘야 해서 Serializer 구조가 복잡해졌다. Nested Serializer를 사용해 구조를 다시 설계하면서 요구사항에 맞는 응답 형태를 구현했다.

---

## 🌱 새로 배운 것

* RESTful URL 설계의 중요성
* Serializer로 응답 포맷을 다양하게 구성하는 방법
* M:N, 1:N 관계 데이터를 직렬화하는 패턴
* Django REST Framework에서 브라우저/JSON 자동 처리 이해

---

## ✨ 느낀 점

* 이번 프로젝트는 단순한 CRUD를 넘어서 RESTful API 설계와
Django REST Framework의 사용성을 이해할 수 있는 경험이었습니다.
* 특히 모델 관계 구조를 기반으로 적절한 Serializer 설계,
POST/GET 요청별 응답 처리 등 실무적인 API 개발 흐름을 익힐 수 있었습니다.

