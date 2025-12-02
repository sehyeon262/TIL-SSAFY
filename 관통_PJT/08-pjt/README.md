# 🧭 Git 협업 규칙 

`08-pjt` 프로젝트를 기준으로,
**각자 자신의 폴더에서만 작업**하고
**브랜치별로 관리 후 master로 합병**

---

## ✅ 1. 최초 세팅

```bash
git clone https://lab.ssafy.com/tjfls295/08-pjt
cd 07-pjt
git switch -c <본인_이름>   # 예: git switch -c seorin
```

* master 브랜치에서는 직접 작업하지 않는다.
* 모든 작업은 **개인 브랜치**에서 진행한다.

---

## ✅ 2. 작업

1. **본인 전용 폴더 생성**

   ```bash
   mkdir <본인_이름>
   ```

   예시:

   ```
   seorin
   sehyeon
   ```

2. **자신의 폴더 안에서만 코드 작성 및 수정**

   * 다른 사람의 폴더는 임의로 수정하지 않는다.
   * 협의가 필요한 경우, 반드시 주석으로 표시한다.

     ```python
     # [수정자: 서린] 텍스트 색상 변경 (2025-11-21)
     ```

    💡 병합 전에 개인 폴더는 삭제해도 상관없음(깔끔)

3. **작업 완료 후 커밋 및 푸시**

   ```bash
   git add .
   git commit -m "11_21_이름 작업 내용"
   git push origin <본인_이름>
   ```

---

## ✅ 3. GitLab에서 Merge Request (PR) 생성

1. GitLab에서 `Merge Request` 생성
2. Reviewer 또는 Assignee 지정
3. 코드 리뷰 후 `master` 브랜치로 merge

> ⚠️ **주의:**
> 충돌(conflict)이 발생하지 않도록
> 서로의 폴더 구조를 변경하지 않는다.

---

## ✅ 4. master 최신화

모든 병합이 완료된 후, 팀원 전원은 아래 명령어를 실행한다.

```bash
git checkout master
git pull origin master
```

> 👉 master 브랜치를 항상 최신 상태로 유지해야 한다.

---

## ✅ 5. 다음 작업 시작 시

새 브랜치를 생성한다.

```bash
git switch -c <새_브랜치명>
```

---

* 각자의 폴더 안에 개별 작업 내용이 정리된다.
* 모든 브랜치는 merge 완료 후 삭제 가능하다.

```bash
git branch -d <브랜치명>
```

---

## ✅ 6. 최종 상태

* master(`M3`)에는 모든 브랜치가 반영된 최종 버전이 남는다.
* 사용 완료된 개인 브랜치는 정리되어 깔끔한 상태 유지.

---
