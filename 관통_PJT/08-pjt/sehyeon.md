# 🎬 08-pjt : JavaScript를 활용한 DOM 조작 프로젝트

## 📌 프로젝트 개요

이 프로젝트는 JavaScript를 이용하여 HTML의 내용을 조작하고, 사용자 동작에 따라 동적으로 웹 페이지를 변경하는 영화 목록 관리 애플리케이션을 구현하는 것을 목표로 합니다. 장르별 필터링, 영화 추가/삭제, 즐겨찾기 등의 기능을 화면 새로고침 없이 제공합니다.

---

## ⚙️ 주요 기능

| 구분         | 기능명                  | 설명                                                |
| ---------- | -------------------- | ------------------------------------------------- |
| 영화 목록 | 전체 영화 출력             | 주어진 영화 데이터를 화면에 목록으로 출력                             |
| 장르 필터링  | 장르별 필터링             | 장르 선택 시 해당 장르의 영화만 출력                  |
| 영화 추가 | 영화 생성 UI             | 제목과 장르를 입력받아 새로운 영화를 목록에 추가 |
| 영화 삭제 | 영화 데이터 삭제       | 목록에서 특정 영화를 삭제  |
| 즐겨찾기 | 즐겨찾기 추가/제거 (도전 과제)                | 영화를 즐겨찾기에 추가하고 별도 목록으로 관리                         |
| 유효성 검증 | 입력 데이터 검증 | 제목과 장르 필수 입력 검증 및 alert 처리                         |
| DOM 조작 | JavaScript 활용    | .innerHTML 사용 금지, DOM API를 통한 요소 생성 및 추가                         |

---

## 📋 구현 기능 및 기술

### 프로젝트 구조

- **skeleton/index.html**: UI 구조를 담당하는 HTML 파일
- **skeleton/genres.js**: 장르 데이터를 제공하는 JavaScript 파일
- **skeleton/movies.js**: 영화 데이터를 제공하는 JavaScript 파일
- **skeleton/script.js**: 모든 기능 구현을 담당하는 JavaScript 파일

---

## 전체 페이지 

![](/images/1.png)

---

### D. 영화 데이터 추가 (F04)

![](/images/5.png)
![](/images/6.png)
![](/images/7.png)


- 입력된 데이터로 새로운 영화 객체 생성
- 유효성 검증:
  - 제목이 비어있는 경우 → alert 표시
  - 장르가 선택되지 않은 경우 → alert 표시
- 추가된 영화는 전체 목록 최상단에 표시
- 추가 후 장르 필터가 '전체'로 자동 변경

```javascript
function addMovie() {
  const titleInput = document.querySelector('#movie-title-input')
  const genreCheckboxes = document.querySelectorAll('.genre-checkbox:checked')

  const title = titleInput.value.trim()
  const selectGenres = Array.from(genreCheckboxes).map(cb => parseInt(cb.value))

  // 유효성 검사
  if (title === '') {
    alert('영화 제목을 입력해주세요.')
    return
  }

  if (selectGenres.length === 0) {
    alert('장르를 최소 1개 이상 선택해주세요.')
    return
  }

  const newMovie = {
    title: title,
    genres: selectGenres
  }

  movies.unshift(newMovie)  // 최상단에 추가
  movieList(movies)
}
```

---

### E. 영화 데이터 삭제 (F05)

![](/images/10.png)

- 각 영화 항목에 '삭제' 링크 추가
- 삭제 클릭 시 movies 배열과 favorites 배열에서 제거
- 현재 선택된 장르에 맞게 목록 다시 렌더링

```javascript
function deleteMovie(movie) {
  const index = movies.indexOf(movie)
  if (index > -1) {
    movies.splice(index, 1)
  }

  // 즐겨찾기에서도 제거
  const favoriteIdx = favorites.indexOf(movie)
  if (favoriteIdx > -1) {
    favorites.splice(favoriteIdx, 1)
  }

  const filterMovies = filterGenre(currentGenre)
  movieList(filterMovies)
}
```

---

### F. 즐겨찾기 기능 (F06 - 도전 과제)

![](/images/11.png)
![](/images/12.png)

- 각 영화 항목에 '즐겨찾기' 버튼 추가
- 즐겨찾기 추가 여부에 따라 버튼 텍스트 및 색상 변경
- 장르 선택에 '즐겨찾기' 옵션 추가
- 즐겨찾기 목록 별도 관리

```javascript
function toggleFavorite(movie) {
  const index = favorites.indexOf(movie)

  if (index > -1) {
    favorites.splice(index, 1)  // 제거
  } else {
    favorites.push(movie)  // 추가
  }

  const filterMovies = filterGenre(currentGenre)
  movieList(filterMovies)
}
```

---

## 💡 학습한 내용

1. DOM 조작 기본기: createElement, appendChild, querySelectorAll 등을 사용해 동적으로 요소를 생성하는 법을 익힘
2. 이벤트 처리 흐름 이해: 버튼 클릭, select 변경 등 다양한 이벤트를 addEventListener로 처리
3. 배열 메소드 활용: forEach, filter, map, includes, splice, unshift로 데이터 조작
4. 상태 관리 개념 학습: currentGenre, favorites, movies 등 데이터를 기반으로 화면을 다시 렌더링하는 구조 경험

---

## 🤔 어려웠던 부분

- .innerHTML을 쓰지 않다 보니, 모든 UI를 직접 DOM API로 조립하는 과정이 처음엔 어렵게 느껴짐
- 삭제·즐겨찾기 버튼처럼 동적으로 생성된 요소의 이벤트 관리가 헷갈렸음
- 즐겨찾기 기능처럼 여러 배열의 상태를 동시에 유지·동기화하는 부분이 부담스러웠음

---

## 🌱 새로 배운 것

- 순수 JavaScript만으로도 완전한 동적 UI 구현이 가능하다는 점
- 동적으로 생성되는 요소 처리 시 이벤트 등록 방식과 구조화의 중요성
- 객체 배열에서 동일한 객체를 찾고 조작하기 위한 참조 기반 데이터 처리
- 유효성 검사, 선택 초기화 등 UX를 고려한 기능 구현 경험

---

## ✨ 느낀 점

- 기본 DOM 조작이 생각보다 손이 많이 가지만, 그만큼 작동 원리를 정확히 이해하게 됐습니다.
- 프레임워크(React, Vue)가 왜 필요한지, 어떤 점을 편하게 만들어주는지 체감한 프로젝트였습니다.
- 상태 관리를 직접 구현하며 UI 렌더링 로직과 데이터 흐름에 대한 감각이 생겼습니다.
- 실제 서비스를 만든 느낌이라 재밌었고, 다음엔 코드 구조도 더 깔끔하게 개선해보고 싶다는 생각이 들었습니다.