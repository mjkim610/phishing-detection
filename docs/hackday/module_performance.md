*Last Update: 2017-05-26-13:45:00*

---

## is_masquerading
#### 설명
URL에 특정 keyword가 있을 경우, 이 키워드가 도메인에 있는지, 아니면 도메인이 아닌 다른 곳에 있는지 확인

#### 판단
- S: keyword가 도메인에 있을 경우
- P: keyword가 도메인이 아닌 곳에 있을 경우
- U: keyword가 없을 경우

#### 결과
- Type: Normal
- Score: 152
    - phishing 26/0
    - phishing like 0/0
    - safe 50/0
    - safe like 0/0
    - unknown 294
- End Time :  2017년 5월 26일 1:25 오후


## can_access
### 특이사항
아래 모듈의 에러를 방지하기 위해 공통적으로 사용되는 모듈
- html_has_same_domain
- has_password_field
- uses_stylesheet_naver
- check_title
- favicon

#### 설명
URL로 페이지에 접속이 가능한지 확인

#### 판단
- U: 접속 불가능

#### 결과
- Score: 227
    - phishing 0/0
    - phishing like 0/0
    - safe 0/0
    - safe like 295/68
    - unknown 7
- End Time:  2017년 5월 26일 12:12 오전


## html_has_same_domain
#### 설명
html에 포함되어 있는 `a`태그의 `href`에 적힌 url들과 현재 도메인의 url을 비교합니다.

#### 판단
- S: 루트도메인과 일치하는 a 태그의 url이 있으면
- U: 일치하는 태그가 없으면

#### 결과
- Type: Normal
- Score: 450
    - phishing 0/0
    - phishing like 0/0
    - safe 294/69
    - safe like 0/0
    - unknown 7
- End Time :  2017년 5월 26일 1:39 오후


## has_password_field
#### 설명
input tag중 password field가 있는지 확인함

#### 판단
- S: password field가 없으면
- U: password field가 있으면

#### 결과
- Type: Normal
- Score: 454
    - phishing 0/0
    - phishing like 0/0
    - safe 295/68
    - safe like 0/0
    - unknown 7
- End Time :  2017년 5월 26일 1:33 오후


## uses_stylesheet_naver
#### 설명
네이버가 아닌 도메인에서 네이버 CSS를 사용하고 있는지 평가

#### 판단
- P: 네이버가 아닌 도메인에서 네이버 CSS를 사용할 경우
- U: 네이버 CSS를 사용하지 않는 경우

#### 결과
- Type: Normal
- Score: 644
    - phishing 51/3
    - phishing like 0/0
    - safe 292/18
    - safe like 0/0
    - unknown 6
- End Time :  2017년 5월 26일 1:57 오후

## check_title
#### 설명
html에 포함된 title이 naver의 title과 같지만, 루트 도메인이 naver.com이 아닌 항목을 점검

#### 판단
- S: 루트 도메인이 같으면
- P: 루트 도메인이 다르면
- U: 타이틀이 다르면

#### 결과
- Type: Normal
- Score: 626
    - phishing 44/0
    - phishing like 0/0
    - safe 293/24
    - safe like 0/0
    - unknown 9
- End Time :  2017년 5월 26일 2:01 오후

## favicon
#### 설명
head태그중 link에 favicon이 메인 도메인과 일치한지 확인함

#### 판단
- S: favicon 위치가 동일한 도메인에 있을 경우
- P: favicon 위치가 현재 페이지의 도메인과 다를 경우

#### 결과
- Type: Normal
- Score: 225
    - phishing 0/0
    - phishing like 0/0
    - safe 0/0
    - safe like 294/69
    - unknown 7
- End Time :  2017년 5월 26일 1:44 오후