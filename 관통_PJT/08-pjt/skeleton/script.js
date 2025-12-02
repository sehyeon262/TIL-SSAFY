/**
 * 제공 코드
 */
// 기본 영화 데이터 (JavaScript Array)
const genres = genreRawData
const movies = movieRawData
// 데이터 확인
console.log(genres.length)
console.log(genres[0])
console.log(movies.length)
console.log(movies[0])

/**
 * 대부분의 작업은 script.js에서 진행해도 무방하나 원한다면 js 파일 추가 가능
 * HTML 요소 추가를 위한 `.innerHTML` 사용 금지, 요소의 내용을 비우는 용도로는 사용 가능 (`.innerHTML = ```)
 */


// 현재 영화
let currentGenre = null

// 즐겨찾기 목록
let favorites = []


// A. 영화 목록 보여주기 함수
function movieList(movieLst) {
  const movieListTag = document.querySelector('#movie-list-section')

  const ulTag = movieListTag.querySelector('ul')
  if (ulTag) {
    ulTag.remove()
  }

  const ul = document.createElement('ul')

  movieLst.forEach((movie) => {
    const li = document.createElement('li')

    const titleTag = document.createElement('span')
    titleTag.textContent = movie.title
    titleTag.style.cursor = 'pointer'
    li.appendChild(titleTag)

    li.style.marginBottom = '5px'


    // 즐겨찾기 버튼 추가하기
    const favoriteBtn = document.createElement('a')
    favoriteBtn.href = '#'
    favoriteBtn.style.marginLeft = '10px'
    favoriteBtn.style.fontSize = '0.9em'


    // 즐겨찾기 여부 확인
    const isFavorite = favorites.includes(movie)
    if (isFavorite) {
      favoriteBtn.textContent = ' 취소'
      favoriteBtn.style.color = 'orange'
    } else {
      favoriteBtn.textContent = ' 즐겨찾기'
      favoriteBtn.style.color = 'blue'
    }

    favoriteBtn.addEventListener('click', (e) => {
      e.preventDefault()
      toggleFavorite(movie)
    })

    li.appendChild(favoriteBtn)


    // E. 삭제 버튼 추가 !!!!
    const deleteBtn = document.createElement('a')
    deleteBtn.textContent = ' 삭제'
    deleteBtn.href = '#'
    deleteBtn.style.marginLeft = '10px'
    deleteBtn.style.color = 'red'
    deleteBtn.style.fontSize = '0.9em'

    deleteBtn.addEventListener('click', (e) => {
      e.preventDefault()
      deleteMovie(movie)
    })

    li.appendChild(deleteBtn)
    ul.appendChild(li)
  })

  movieListTag.appendChild(ul)
}


// B. 선택된 장르만 보여주는 함수
function filterGenre(genre) {
  if (genre === null) {
    // 전체 영화 보여주기
    return movies
  } else if (genre === 'favorites') {
    // 즐겨찾기 영화만 보여주기
    return favorites
  } else {
    // 선택된 장르만 필터해서 보여주기
    return movies.filter(movie => movie.genres.includes(genre))
  }
}


// B. 장르 목록 보여주는 함수
function createGenre() {
  const genreTag = document.querySelector('#movie-genre-filter')

  const select = document.createElement('select')
  select.className = 'form-select mb-3'
  select.id = 'genre-select'

  // 전체 다 보여주기 추가!!
  const allOption = document.createElement('option')
  allOption.value = ''
  allOption.textContent = '전체'
  select.appendChild(allOption)

  // 즐겨찾기 옵션 추가
  const favoriteOption = document.createElement('option')
  favoriteOption.value = 'favorites'
  favoriteOption.textContent = '즐겨찾기'
  select.appendChild(favoriteOption)

  // 각 장르마다 추가해주기
  genres.forEach(genre => {
    const option = document.createElement('option')
    option.value = genre.id
    option.textContent = genre.name
    select.appendChild(option)
  })


  select.addEventListener('change', (e) => {
    const selectGenre = e.target.value

    if (selectGenre === '') {
      currentGenre = null
    } else if (selectGenre === 'favorites') {
      currentGenre = 'favorites'
    } else {
      currentGenre = parseInt(selectGenre)
    }

    const filterMovies = filterGenre(currentGenre)
    movieList(filterMovies)
  })

  genreTag.appendChild(select)
}


// C. 영화 생성하기 함수
function createMovie() {
  const formTag = document.querySelector('#movie-form-section')

  // 영화 제목 정보 입력
  const titleLabel = document.createElement('label')
  titleLabel.textContent = '제목'
  titleLabel.className = 'form-label'
  titleLabel.setAttribute('for', 'movie-title-input')

  const titleInput = document.createElement('input')
  titleInput.type = 'text'
  titleInput.className = 'form-control mb-3'
  titleInput.id = 'movie-title-input'
  titleInput.placeholder = '영화 제목을 입력하세요'

  formTag.appendChild(titleLabel)
  formTag.appendChild(titleInput)

  // 영화 장르 정보 입력
  const genreLabel = document.createElement('label')
  genreLabel.textContent = '장르 (복수 선택 가능)'
  genreLabel.className = 'form-label'

  formTag.appendChild(genreLabel)

  // 장르 체크박스 만들어주기
  const genreGroup = document.createElement('div')
  genreGroup.className = 'mb-3'
  genreGroup.id = 'genre-checkbox-group'

  genres.forEach(genre => {
    const checkboxDiv = document.createElement('div')
    checkboxDiv.className = 'form-check'

    const checkbox = document.createElement('input')
    checkbox.type = 'checkbox'
    checkbox.className = 'form-check-input genre-checkbox'
    checkbox.value = genre.id
    checkbox.id = `genre-${genre.id}`

    const label = document.createElement('label')
    label.className = 'form-check-label'
    label.setAttribute('for', `genre-${genre.id}`)
    label.textContent = genre.name

    checkboxDiv.appendChild(checkbox)
    checkboxDiv.appendChild(label)
    genreGroup.appendChild(checkboxDiv)
  })

  formTag.appendChild(genreGroup)

  const addBtn = document.createElement('button')
  addBtn.textContent = '추가'
  addBtn.className = 'btn btn-primary'
  addBtn.id = 'add-movie-btn'

  addBtn.addEventListener('click', () => {
    addMovie()
  })

  formTag.appendChild(addBtn)
}

// D. 영화 추가해주는 함수 생성
function addMovie() {
  const titleInput = document.querySelector('#movie-title-input')
  const genreCheckboxes = document.querySelectorAll('.genre-checkbox:checked')

  const title = titleInput.value.trim()
  const selectGenres = Array.from(genreCheckboxes).map(cb => parseInt(cb.value))

  // 유효성 검사 후 alert창 띄워주기
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

  // 최상단에 추가해주기
  movies.unshift(newMovie)

  currentGenre = null
  const genreSelect = document.querySelector('#genre-select')
  genreSelect.value = ''

  // 영화 목록 다시 보여주기
  movieList(movies)

  titleInput.value = ''
  genreCheckboxes.forEach(cb => cb.checked = false)
}

// E. 영화 삭제 함수
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

  // 해당 영화 내에서 다시 보여주기
  const filterMovies = filterGenre(currentGenre)
  movieList(filterMovies)
}

// 즐겨찾기 추가 및 제거 
function toggleFavorite(movie) {
  const index = favorites.indexOf(movie)

  if (index > -1) {
    // 이미 즐겨찾기에 있으면 제거
    favorites.splice(index, 1)
  } else {
    // 즐겨찾기에 없으면 추가
    favorites.push(movie)
  }

  // 현재 장르에 따라 목록 다시 보여주기
  const filterMovies = filterGenre(currentGenre)
  movieList(filterMovies)
}

// 초기화 함수
function init() {
  createGenre()
  movieList(movies)
  createMovie()
}

init()
