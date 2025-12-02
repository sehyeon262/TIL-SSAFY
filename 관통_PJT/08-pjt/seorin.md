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

### A. 영화 목록 출력 (F01)

![](/images/2.png)

- `div#movie-list-section` 내부에 영화 목록을 `ul` 요소로 구현
- 각 영화 제목을 `li` 요소로 생성하여 추가
- movies 배열 데이터를 순회하며 동적으로 DOM 요소 생성

```javascript
function movieList(movieLst) {
  const movieListTag = document.querySelector('#movie-list-section')

  // 기존 ul 제거
  const ulTag = movieListTag.querySelector('ul')
  if (ulTag) {
    ulTag.remove()
  }

  const ul = document.createElement('ul')

  movieLst.forEach((movie) => {
    const li = document.createElement('li')
    const titleTag = document.createElement('span')
    titleTag.textContent = movie.title
    li.appendChild(titleTag)
    ul.appendChild(li)
  })

  movieListTag.appendChild(ul)
}
```

---

### B. 장르별 필터링 (F02)

![](/images/3.png)
![](/images/8.png)

- `div#movie-genre-filter` 내부에 장르 선택 UI 구현
- Bootstrap의 `select` 요소 활용
- '전체', '즐겨찾기' 옵션 및 각 장르 옵션 동적 생성
- 장르 선택 시 해당 장르의 영화만 필터링하여 출력

```javascript
function filterGenre(genre) {
  if (genre === null) {
    return movies  // 전체 영화
  } else if (genre === 'favorites') {
    return favorites  // 즐겨찾기 영화
  } else {
    return movies.filter(movie => movie.genres.includes(genre))
  }
}

function createGenre() {
  const select = document.createElement('select')
  select.className = 'form-select mb-3'

  // 전체 옵션
  const allOption = document.createElement('option')
  allOption.value = ''
  allOption.textContent = '전체'
  select.appendChild(allOption)

  // 장르 옵션들 추가
  genres.forEach(genre => {
    const option = document.createElement('option')
    option.value = genre.id
    option.textContent = genre.name
    select.appendChild(option)
  })
}
```

---

### C. 영화 생성 UI (F03)

![](/images/4.png)

- `div#movie-form-section` 내부에 영화 추가 폼 구현
- 제목 입력 필드 (text input)
- 장르 선택 체크박스 (복수 선택 가능)

---

## 💡 학습한 내용

1. **JavaScript DOM 조작**: `createElement`, `appendChild`, `querySelector` 등을 활용한 동적 요소 생성
2. **이벤트 핸들링**: `addEventListener`를 통한 사용자 인터랙션 처리
3. **배열 메소드 활용**: `forEach`, `filter`, `map`, `includes` 등
4. **데이터 필터링 및 상태 관리**: 장르별 필터링

---

## 🤔 어려웠던 부분

- `.innerHTML` 사용 금지 규칙으로 인해 모든 요소를 `createElement`로 생성해야 했다. 처음에는 불편했지만, DOM API를 깊이 이해하는 계기가 되었다.
- 배열 메소드를 관리하는 게 아직은 익숙하지 않아 장르 checkbox를 관리하는 데 어려움을 겪었다. 

---

## 🌱 새로 배운 것

- **순수 JavaScript DOM 조작의 중요성**: jQuery나 프레임워크 없이 순수 JavaScript로 DOM을 다루는 경험
- **이벤트 위임 패턴**: 동적으로 생성되는 요소들의 이벤트 처리
- **배열 참조와 복사**: JavaScript에서 객체 배열을 다룰 때 참조 관계 이해

---

## ✨ 느낀 점

- 이번 프로젝트는 React나 Vue 같은 프레임워크 없이 동적 웹 애플리케이션을 구현하는 경험이었습니다.
- `.innerHTML` 사용 금지라는 제약이 오히려 DOM API를 제대로 이해하고 활용하는 좋은 학습 기회가 되었습니다.
- 상태 관리와 UI 업데이트를 수동으로 처리하면서, 프레임워크가 내부적으로 어떤 일들을 자동화해주는지 이해할 수 있었습니다.
