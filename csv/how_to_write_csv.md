# 대학 데이터 csv 파일로 정리하기

## university
- name: 대학 이름
- logo: 로고 파일명 (대학 영문명, 공유 문서함에 있는 로고 파일명 그대로)
  - ex) 서울대학교: seoul.png
- review url: 대학백과 리뷰 url

## major block
학과 블럭: 일정이 다른 학과가 있다면 묶어서 처리하기 위한 단위 (수시, 정시 따로)

ex) 미술대학/음악대학/인문계열/자연계열 - 이렇게 서로 일정이 다르다면 해당 단위 4개를 만들고 일정을 각각 따로 처리하기

- university: 대학 이름
- susi_jeongsi: 수시 or 정시
- name: 학과 블럭 이름
  - ex: 인문계열, 의학계열, 그 외

### jeongsi major block
- university: 대학 이름
- name: 학과 블럭 이름

## jeonhyeong
전형 정보

- university: 대학 이름
- susi_jeongsi: 수시 or 정시
- year: 학년도
- name: 전형 이름

## schedule
일정 정보

### susi schedule
- university: 대학 이름
- susi_jeongsi: 수시 or 정시
- year: 학년도
- jeonhyeong: 전형 이름
- major block: 학과 블럭 이름
- description: 일정 정보
  - ex) 지원서 접수
- start date: 일정 시작 시점
  - ex) 2020-06-06T18:00:00
- end date: 일정 종료 시점
