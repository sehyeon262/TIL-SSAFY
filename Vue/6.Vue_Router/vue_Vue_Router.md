# 📘 목차 (Table of Contents)

### 1. Routing

### 2. Vue Router
- Basic Routing
- Named Routes
- Dynamic Route Matching
- Nested Routes
- Programmatic Navigation

### 3. route와 router
- route
- router

### 4. Navigation Guard
- Globally Guard
- Per-route Guard
- In-component Guard

### 참고
- Lazy Loading Routes


---


# 학습 목표
✓ RouterLink와 RouterView를 사용해 기본 라우팅을 구현한다.

✓ 경로 대신 이름을 사용한 Named Routes로 페이지를 이동한다.

✓ 동적 라우팅을 설정하고 useRoute로 파라미터 값을 얻는다.

✓ useRouter의 push 메서드를 사용해 프로그래밍 방식으로 이동한다.

✓ children 속성을 사용하여 중첩된 라우트를 구성할 수 있다.

✓ 전역 가드 beforeEach를 사용해 라우팅을 제어할 수 있다.

✓ 컴포넌트 가드로 페이지를 떠나거나 업데이트될 때를 제어한다.


---


# ✅ Routing

## 🔵 Routing이란? 
- 네트워크에서 경로를 선택하는 프로세스

```
- 라우팅은 사용자가 접속한 URL 주소에 따라 적절한 페이지(컴포넌트)를 보여주는 기능입니다.
- /home 주소는 Home 컴포넌트로, /about 주소는 About 컴포넌트로 연결하는 등 미리 정의된 경로에 따라 어떤 내용을 보여줄지 결정합니다.
```


## 🔵 SSR에서의 Routing
- SSR에서 routing은 **서버** 측에서 수행
- 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
- 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고 **새 HTML로 전체 페이지를 다시 로드**

> 💡 **SSR** : 서버에서 완성된 html 페이지를 만들어, 브라우저에 보내는 방식

    ![alt text](image.png)


## 🔵 CSR에서의 Routing
- CSR에서의 routing은 **클라이언트** 측(브라우저)에서 수행
- 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드하지 않음

> 💡 **CSR** : 서버는 뼈대만 주고, 브라우저가 직접 페이지를 그리는 방식

    ![alt text](image-1.png)


## 🔵 SPA에서 Routing이 없다면
- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감
    - 링크를 공유할 시 첫 페이지만 공유 가능
- 브라우저의 뒤로 가기 기능을 사용할 수 없음

➤ 페이지는 1개이지만, **주소에 따라 여러 컴포넌트를 새로 렌더링**하여 마치 **여러 페이지를 사용하는 것처럼** 보이도록 해야 함

> 💡 **SPA** : 하나의 페이지 안에서, 내용만 바꿔가며 보여주는 웹 앱


---


# ✅ Vue Router

## 🔵 Vue Router 란?                   
- Vue 공식 라우터 (The official Router for Vue.js)

- Vue.js의 공식 라우팅 라이브러리로, Vue로 만든 SPA에서 페이지 이동 기능을 구현할 때 사용됩니다.
- 페이지를 새로고침하지 않는 링크를 만드는 `<router-link>`와, 현재 URL에 맞는 컴포넌트를 보여주는 `<router-view>`라는 핵심 컴포넌트를 제공합니다.
- 어떤 URL 경로에 어떤 컴포넌트를 보여줄지 정의하기만 하면, Vue Router가 연결해줍니다.


## 🔵 사전 준비 (1/2)
- Vite로 프로젝트 생성 시 Router 추가

    ![alt text](image-3.png)


## 🔵 사전 준비 (2/2)
- 서버 실행 후 Router로 인한 프로젝트 변화 확인

    ➤ Home, About 링크에 따라 변경되는 URL과 새로 렌더링 되는 화면

    ![alt text](image-4.png)

### TIP - Vue 서버 실행하는 방법
1. npm create vue@latest
2. 생성된 프로젝트 폴더로 이동 ($ cd [프로젝트명])
3. 패키지 설치 ($ npm install)
4. 서버 실행 ($ npm run dev)


## 🔵 Vue 프로젝트 구조 변화
1. App.vue 코드 변화

2. router 폴더 신규 생성

3. views 폴더 신규 생성


## 🔵 1. App.vue 코드 변화: RouterLink
- 페이지를 다시 로드 하지 않고 URL을 변경하여 URL 생성 및 관련 로직을 처리
- HTML의 `<a>` 태그를 렌더링
```vue
<!-- App.vue -->
<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
```


## 🔵 1. App.vue 코드 변화: RouterView
- RouterLink URL에 해당하는 컴포넌트를 표시
- 원하는 곳에 배치하여 컴포넌트를 레이아웃에 표시 할 수 있음
```vue
<!-- App.vue -->
<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
```


## 🔵 RouterLink와 RouterView
![alt text](image-5.png)


## 🔵 2. router/index.js
- 라우팅에 관련된 정보 및 설정이 작성 되는 곳
- 웹 사이트 여러 페이지들의 주소 목록을 작성(‘/’, ‘home’, ...)
- 각 주소로 접속했을 때, 어떤 Vue 컴포넌트(페이지 화면)를 보여줄 지 연결

### TIP
- 프로젝트 규모가 작을 때는 index.js 하나로 관리해도 충분합니다.
- 프로젝트 규모가 커질 때는 기능별로 경로 관리를 하고, index.js에서 합치는 방식으로 운영합니다.


## 🔵 3. views
- RouterView 위치에 렌더링 할 컴포넌트를 배치
- 기존 components 폴더와 기능적으로 다른 것은 없으며 **단순 분류의 의미**로 구성됨

※ 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장


---


# ✅ Basic Routing

## 🔵 라우팅 기본 동작 순서
1. index.js에 라우터 관련 설정 작성

2. RouterLink에 index에 정의한 주소 값 작성

3. RouterLink 클릭 시 경로와 일치하는 컴포넌트가 RouterView에서 렌더링


## 🔵 라우팅 기본 동작 살펴보기 (1/3)
1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
```js
// index.js
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    }, …
  ]
})
```


## 🔵 라우팅 기본 동작 살펴보기 (2/3)
2. RouterLink의 ‘to’ 속성으로 index.js에서 정의한 주소 값(path)을 사용
```js
<!-- App.vue -->
<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
```


## 🔵 라우팅 기본 동작 살펴보기 (3/3)
3. RouterLink 클릭 시 경로와 일치하는 컴포넌트가 RouterView에서 렌더링 됨
```js
<!-- App.vue -->
<template>
  <header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
```


---


# ✅ Named Routes


## 🔵 path 경로를 그대로 사용하기
- 현재는 index.js에서 입력한 path 경로를 그대로 RouterLink에 사용하고 있음
- 이 방식은 URL 경로를 변경할 때, 해당 경로를 사용한 모든 파일을 일일이 찾아다니며 수정해야 하는 단점이 있음 (유지보수 난이도 증가)
```js
// index.js
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ {
      path: '/',
      name: 'home',
      component: HomeView,
    }, {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    }]
})
```
```js
<!-- App.vue -->
<RouterLink to="/">Home</RouterLink>
<RouterLink to="/about">About</RouterLink>
```


## 🔵 Named Routes
- name 속성 값에 경로에 대한 이름을 지정
- 경로에 연결하려면 RouterLink에 v-bind를 사용해 'to' props 객체로 전달 가능
- 하드 코딩된 URL을 사용하지 않아도 되며, 오타를 방지할 수 있음
```js
// index.js
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ {
      path: '/',
      name: 'home',
      component: HomeView,
    }, {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    }]
})
```
```js
<!-- App.vue -->
…
<RouterLink :to="{ name: 'home' }">Home</RouterLink>
<RouterLink :to="{ name: 'about' }">About</RouterLink>
…
```

> 💡 **v-bind** : 콜론(:)을 사용해, HTML 속성을 데이터와 실시간으로 연동

> 💡 **props 객체** : 부모 컴포넌트가 자식 컴포넌트에게 데이터를 전달하는 통로


---


# ✅ Dynamic Route Matching


## 🔵 일정한 패턴의 URL 작성을 반복해야 하는 경우
- 주어진 패턴의 여러 경로를 하나의 컴포넌트에 매핑해야 하는 경우는 어떻게 할까요?
- 예) 모든 사용자의 ID를 활용하여 프로필 페이지 URL을 설계
    - user/1
    - user/2
    - user/3

    ➤ 일정한 패턴의 URL 작성을 반복해야 함

➤ 이럴 때 사용하는 것이 바로 Dynamic Route Matching 


## 🔵 Dynamic Route Matching           
- URL의 일부를 변수로 사용하여 경로를 동적으로 매칭
```
- 동적 라우트 매칭은 /user/1, /user/2 처럼 패턴은 같지만 ID 값만 다른 여러 URL을 하나의 라우트 설정으로 처리하는 기능입니다.
- 이를 통해 수백 개의 상품 상세 페이지나 사용자 프로필 페이지를 각각 만들 필요 없이,
하나의 컴포넌트를 재사용하여 효율적으로 개발할 수 있습니다.
```
https://router.vuejs.org/guide/essentials/dynamic-matching.html


## 🔵 매개변수를 사용한 동적 경로 매칭 활용 (1/5)
- 프로필 페이지로 활용하기 위한 컴포넌트 작성하기
- views 폴더 내 UserView 컴포넌트 작성
```js
<!-- UserView.vue -->
<template>
  <div>
    <h1>UserView</h1>
  </div>
</template>
```


## 🔵 매개변수를 사용한 동적 경로 매칭 활용 (2/5)
- 라우터 관련 설정을 하는 router/index.js 파일에 코드 작성
- 매개변수는 콜론(":")으로 표기하고, UserView 컴포넌트를 라우터로 등록
```js
// index.js
import UserView from '../views/UserView.vue'

const router = createRouter({
  routes: [
    {
      path: '/user/:id',
      name: 'user',
      component: UserView
    },
  ]
})
```


## 🔵 매개변수를 사용한 동적 경로 매칭 활용 (3/5)
- 매개변수는 객체의 params 속성의 객체 타입으로 전달
- 단, 객체의 key 이름과 index.js에서 지정한 매개변수 이름이 같아야 함
- UserView 컴포넌트로 이동하기 위한 RouterLink 작성

![alt text](image-6.png)


## 🔵 매개변수를 사용한 동적 경로 매칭 활용 (4/5)
- 경로가 일치하면 라우트의 매개변수는 컴포넌트에서 $route.params로 참조 가능

➤ 현재 사용자의 id를 출력하기
```js
<!-- UserView.vue -->
<template>
  <div>
    <h1>UserView</h1>
    <h2>{{ $route.params }}번 User 페이지</h2>
    <h2>{{ $route.params.id }}번 User 페이지</h2>
  </div>
</template>
```
결과)
```
UserView
{ "id": "1" }번 User 페이지
1번 User 페이지
```


## 🔵 매개변수를 사용한 동적 경로 매칭 활용 (5/5)
- $route.params 로 template에 바로 작성하는 것보다는
- **`useRoute()`** 함수를 사용해 스크립트 내에서 반응형 변수에 할당 후 템플릿에 출력하는 것을 권장
- 템플릿에서 $route를 사용하는 것과 동일
```js
<!-- UserView.vue -->

import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
```
```html
<!-- UserView.vue -->
<template>
  <div>
    <h2>{{ userId }}번 User 페이지</h2>
  </div>
</template>
```


---


# ✅ Nested Routes

## 🔵 애플리케이션의 UI는 여러 레벨 깊이로 중첩된 컴포넌트로 구성되기도 함
- 이 경우, URL 또한 중첩된 컴포넌트 구조에 맞춰 표현할 수 있음
- **Nested Routes**

    ![alt text](image-7.png)


## 🔵 Nested Routes          
- 중첩된 라우팅

```
- 중첩 라우트는 특정 페이지(부모)의 레이아웃은 유지한 채, 그 안의 일부 영역만 다른 내용으로 교체하는 라우팅 방식입니다.
- '사용자' 페이지의 사이드바는 그대로 두고, 주된 내용 영역만 '프로필', '게시글 목록' 등으로 바꿔 보여주는 대시보드 형태의 UI를 만들 때 매우 유용합니다.
```

https://router.vuejs.org/guide/essentials/nested-routes.html#Nested-Routes


## 🔵 중첩된 라우팅 활용 (1/4)
- 유저 프로필 내부에 중첩으로 사용할 컴포넌트 생성
- components 폴더에 UserProfile, UserPosts 컴포넌트 작성 후 라우터 등록
```html
<!-- UserProfile.vue -->

<template>
  <div>
    <h1>UserProfile</h1>
  </div>
</template>
```
```html
<!-- UserPosts.vue -->

<template>
  <div>
    <h1>UserPosts</h1>
  </div>
</template>
```
```js
// index.js

import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
```


## 🔵 중첩된 라우팅 활용 (2/4)
- “children” 옵션을 사용해 중첩된 라우터에 컴포넌트를 등록
- children 옵션은 배열 형태로 필요한 만큼 중첩 관계를 표현할 수 있음
```js
// index.js
{
  path: '/user/:id',
  component: UserView,
  name: 'user'
  children: [
    // UserProfile은 UserView의 <RouterView> 내부에 렌더링
    { path: 'profile', name: 'userProfile', component: UserProfile},

    // UserPosts는 UserView의 <RouterView> 내부에 렌더링
    { path: 'posts', name: 'userPosts', component: UserPosts}
  ],
},
```


## 🔵 중첩된 라우팅 활용 (3/4)
- 두 컴포넌트(userProfile, userPosts)에 대한 RouterLink 및 RouterView 작성
- Profile과 Posts 링크를 클릭해서 렌더링 결과 확인
```js
// UserView.vue

import { useRoute, RouterLink, RouterView } from 'vue-router'
```
```html
<template>
  <div>
    <RouterLink :to="{ name: 'userProfile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'userPosts' }">Posts</RouterLink>
    <h1>UserView</h1>
    <h2>{{ userId }}번 User 페이지</h2>
    <hr>
    <RouterView />
  </div>
</template>
```
![alt text](image-8.png)


## 🔵 중첩된 라우팅 활용 (4/4)
- 중첩된 Named Routes를 다룰 때는 일반적으로 “하위 경로에만 이름을 지정”
- 이렇게 하면 /user/:id로 이동했을 때 항상 중첩된 경로를 바로 렌더링 가능
    - /user/:id 접속 시 바로 중첩된 경로가 표시 (UserProfile) 
    
    ※ 단, 이전처럼 상위 경로의 이름을 유지하는 구조로 작성해도 무관

```js
// index.js
{
  path: '/user/:id',
  // name: 'user',
  component: UserView,
  children: [
    { path: '', name: 'user', component: UserProfile},
    { path: 'profile', name: 'userProfile', component: UserProfile},
    { path: 'posts', name: 'userPosts', component: UserPosts}
  ],
},
```
![alt text](image-9.png)


## 🔵 중첩된 라우팅 주의사항
- 컴포넌트 간 부모-자식 관계 관점이 아닌 **“URL에서의 중첩된 관계를 표현”** 하는 관점으로 바라보기
- 자식 라우트의 path는 / 없이 작성해야, 부모 경로 뒤에 자동으로 연결 됨
- 부모 라우트의 파라미터(:id)는 자식 컴포넌트에서도 바로 접근해서 사용할 수 있음


---


# ✅ Programmatic Navigation


## 🔵 Programmatic Navigation 란?
- `<RouterLink>`를 사용하는 대신, **JavaScript 코드를 사용**해 페이지를 이동시키는 것

```
- Programmatic Navigation은 사용자가 <router-link>를 클릭하는 대신, JavaScript 코드(로직)를 통해 특정 URL로 이동시키는 기능입니다.
- 뒤에서 배울 router.push()와 같은 메서드를 호출하여, 원하는 경로로 강제 이동시킬 수 있습니다.
```
https://router.vuejs.org/guide/essentials/navigation.html#Programmatic-Navigation


## 