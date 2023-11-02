# Travelog [나의 여행 기록물] 🚅
- 나의 행복했던 여행 추억들을 남기는 블로그 서비스입니다



## 목차
1. [기획의도](#1-기획-의도)
2. [프로젝트 목표](#2-프로젝트-목표)
3. [요구사항 분석 및 기능명세서](#3-요구사항-분석-및-기능명세서)
4. [개발 일정](#4-개발-일정)
5. [개발 환경 및 배포](#5-개발-환경-및-배포)
6. [프로젝트 구조](#6-개발-일정-및-프로젝트-구조)
7. [ERD](#7-ERD)
8. [프로토타입](#8-프로토타입)

## 1. 기획의도
이전에 여행 했던 추억들을 언젠가 기억하고 싶을 때 볼 수 있는 블로그를 기획하였습니다  


## 2. 프로젝트 목표
국내여행, 해외여행이라는 큰 카테고리 안에서 내가 기억하고 싶은 여행과 사진들을 기록한다  
다른 사람들의 기록들을 구경하면서 다음 여행에 참고하도록 할 수 있게한다  

## 3. 요구사항 분석 및 기능명세서
### 기본 요구사항
- 함수형 뷰와 클래스형 뷰 중 하나를 선택해서 개발하기
    - 클래스형 뷰 채택
- 모놀리식으로 개발하기
- 데이터베이스 구조를 설계하여 ERD 작성하기

### 단계별 요구사항
0. Django Admin을 이용한 게시글 읽기 및 메인페이지 구현  
    <details>
    <summary>요구사항</summary>

    1. 메인 페이지 구현
        - url : `/`
        - 페이지 제목과 블로그 입장하기 버튼이 있다

    2. Django admin을 이용하여 게시글 작성
        - 게시글은 제목, 내용으로 구성
        - `/admin` 을 이용하여 게시글을 작성

    3. 작성되어 있는 게시글 목록을 볼 수 있다
        - url : `/blog`
        - 게시글들의 제목을 확인할 수 있다

    4. 작성 되어있는 게시글 상세 페이지를 볼 수 있다.
        - `/blog/<int:id>`
        - 게시글의 제목/내용을 보는 기능

    </details>

1. 블로그 CRUD 기능 구현
    <details>
    <summary>요구사항</summary>

    1. 게시글 작성 기능 구현
        - url : `/blog/write`
        - 게시글 제목과 내용을 작성할 수 있는 페이지
        - 작성한 게시글이 저장되어 게시글 목록에 보여야 한다
        - 카테고리가 지정될 수 있어야 한다

    2. 게시글 수정 기능 구현
        - url : `/blog/edit/<int:id>`
        - 게시글의 제목 또는 내용을 수정 하는 기능
        - 게시글 제목과 내용을 수정할 수 있는 페이지
        - 수정된 내용은 게시글 목록보기/상세보기에 반영

    3. 게시글 삭제 기능 구현
        - url : `/blog/delete/<int:id>`
        - 게시글을 삭제하는 기능
        - 삭제를 완료한 이후에 게시글 목록 화면으로 돌아간다
        - 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하며,  
        접근 시도 시 404 에러가 발생

    4. 게시글 검색 기능 구현
        - url : `/blog/search/<str:tag>`
        - 주제와 카테고리에 따라 검색이 가능
        - 검색한 게시물은 시간순에 따라 정렬이 가능해야함

    </details>

2. 로그인/회원가입 기능을 이용하여 블로그 구현
    <details>
    <summary>요구사항</summary>

    1. 메인페이지 구현
        - 회원가입/로그인 버튼 추가
        - 회원가입 버튼 클릭 시, 회원가입 페이지로 이동
        - 로그인 버튼 클릭 시, 로그인 페이지로 이동

    2. 회원가입 기능 구현
        - `/register`
        - 회원가입이 가능한 페이지
        - id, password를 입력받아야 한다

    3. 로그인 기능 구현
        - `/login`
        - 로그인이 가능한 페이지
        - id, password를 입력받아야 한다

    4. 게시글 작성 기능 구현
        - 로그인을 한 유저만 해당 기능을 이용할 수 있게 변경

    5. 게시글 목록 기능 구현
        - 모든 사용자들이 게시된 블로그 게시물들의 제목을 확인할 수 있다

    6. 게시글 수정 기능 구현
        - 로그인을 한 유저만 해당 기능을 사용할 수 있게 변경
        - 본인의 게시글만 수정 가능하도록 변경

    7. 게시글 삭제 기능 구현
        - 로그인을 한 유저만 해당 기능을 사용할 수 있게 변경
        - 본인의 게시글만 삭제 가능하도록 변경
        - 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하게 변경
            - 접근 시도 시, <존재하지 않는 게시글>임을 알리는 페이지를 노출
    
    </details>

3. 블로그 기능 외 추가 기능 작성 및 배포
    <details>
    <summary>요구사항</summary>

    1. 게시글 작성 기능 구현
        - 사진 업로드가 가능하도록 변경
        - 게시글 조회수가 올라가도록 변경

    2. 회원 관련 추가 기능
        - 비밀번호 변경
        - 프로필 수정
        - 닉네임 추가

    3. 댓글 기능
        - 댓글 추가 
        - 댓글 삭제
        - 대댓글

    4. 부가 기능
        - collectstatic 사용하여 정적 파일 모으기

    5. AWS Lightsail로 배포

    </details>

### 기능명세서
  
![기능명세서](https://github.com/Nam-Younghoon/travelog/assets/58909988/9cd2170d-f2f0-40cb-b6d0-ebfe9341d27a)  

<details>
    <summary>테이블로 보기</summary>
    
|구분|기능명|설명|담당자|Routes|HTTP|진행도|
|---|---|---|---|---|---|---|  
|사용자|로그인|아이디, 비밀번호를 입력해 로그인합니다|남영훈|/user/login/|POST|완료|
||로그아웃|사용자를 로그아웃시키고, 시작페이지로 이동합니다|남영훈|/user/logout/|POST|완료|
||회원가입|아아디, 닉네임, 이메일, 비밀번호를 입력받아 회원가입합니다|남영훈|/user/register/|POST|완료|
|프로필|프로필 조회|사용자의 아이디, 닉네임, 이메일 주소를 조회합니다|남영훈|/user/profile/|GET|완료|
||프로필 수정|사용자의 닉네임, 이메일 주소를 수정합니다|남영훈|/user/profile/update/\<int:pk\>/|POST|완료|
||비밀번호 변경|사용자의 기존 비밀번호를 검증하여 새로운 비밀번호로 변경합니다|남영훈|/user/profile/change-password|POST|완료|
||비밀번호 확인|사용자에게 비밀번호가 변경되었음을 확인시켜줍니다|남영훈|/user/profile/password_change_done|GET|완료|
||회원 탈퇴|사용자 정보를 삭제하고, 탈퇴시킵니다|남영훈|/user/delete/\<int:pk\>/|POST|완료|
|홈|블로그 홈|블로그 대문입니다. 시작하기, 회원가입, 로그인, 로그아웃 등이 있습니다|남영훈|/|GET|완료|
|블로그|게시글 전체조회|등록되어 있는 모든 게시글 리스트를 보여줍니다|남영훈|/blog/|GET|완료|
||게시글 상세조회|등록되어 있는 게시글의 상세내용을 보여줍니다|남영훈|/blog/\<int:pk\>/|POST|완료|
||게시글 검색|카테고리, 태그, 게시글 제목으로 필터링한 게시글을 조회합니다|남영훈|/search/?q=&sort=|GET|완료|
||게시글 작성|새로운 게시글을 작성합니다|남영훈|/blog/write|POST|완료|
||게시글 수정|등록했던 게시글의 내용을 수정합니다|남영훈|/blog/edit/\<int:pk\>/|POST|완료|
||게시글 삭제|등록했던 게시글을 삭제합니다|남영훈|/blog/delete/\<int:pk\>/|POST|완료|
||게시글 댓글|등록된 게시글에 댓글을 남깁니다|남영훈|/blog/write/comment/\<int:pk\>/|POST|완료|
||게시글 댓글 삭제|등록된 게시글에 남긴 댓글을 삭제합니다|남영훈|/blog/delete/comment/\<int:pk\>/|POST|완료|
||게시글 대댓글|등록된 게시글의 등록된 댓글에 대해 댓글을 작성합니다|남영훈|/blog/write/comment/reply/\<int:pk\>/|POST|완료|
||게시글 대댓글 삭제|등록된 게시글의 등록된 댓글에 대해 댓글을 작성합니다|남영훈|/blog/delete/recomment/\<int:pk\>/|POST|완료|
    
</details>


## 4. 개발 일정
![wbs](https://github.com/Nam-Younghoon/travelog/assets/58909988/63254087-be51-4893-9b6a-fba445bf38e7)

<details>
<summary>Task로 확인하기</summary>  

![travelog_wbs_notion](https://github.com/Nam-Younghoon/travelog/assets/58909988/aea723ea-bd3e-4711-8036-d60152b5718f)

</details>


## 5. 개발 환경 및 배포
[배포 URL](http://43.200.194.3/)

## 6. 프로젝트 구조
```

📦travelog
 ┣ 📂.config
 ┃ ┣ 📂nginx
 ┃ ┃ ┗ 📜travelog.conf
 ┃ ┗ 📂uwsgi
 ┃ ┃ ┣ 📜travelog.ini
 ┃ ┃ ┗ 📜uwsgi.service
 ┣ 📂blog
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂home
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂media
 ┣ 📂static
 ┣ 📂templates
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┣ 📜post_list.html
 ┃ ┃ ┣ 📜post_search.html
 ┃ ┃ ┗ 📜post_write.html
 ┃ ┣ 📂home
 ┃ ┃ ┗ 📜home.html
 ┃ ┣ 📂user
 ┃ ┃ ┣ 📜login.html
 ┃ ┃ ┣ 📜password_change_done.html
 ┃ ┃ ┣ 📜password_change_form.html
 ┃ ┃ ┣ 📜profile.html
 ┃ ┃ ┣ 📜register.html
 ┃ ┃ ┣ 📜update.html
 ┃ ┃ ┗ 📜user_confirm_delete.html
 ┃ ┣ 📜403.html
 ┃ ┣ 📜404.html
 ┃ ┗ 📜base.html
 ┣ 📂travelog
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂user
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

## 7. ERD

## 8. 프로토타입
URL : [카카오오븐](https://ovenapp.io/view/aPollCI5P7YxKZw4Fau4UaVxruaia9rL/o5XP9)


