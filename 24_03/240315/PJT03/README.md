# PJT03

## 1. Bootstrap의 Navbar 예시를 활용하여 Navbar 만들기
 - 모든 sub-components가 들어간 navbar를 사용하였다.
 - 이 중 search 기능을 가진 button과 input을 삭제하였다.
 - large breakpoint에서 button으로 바뀌는 기능은 그대로 사용하였다.
 - large(992px)를 기준으로 너비가 더 커지면 버튼 대신 위에 목록이 그대로 나오도록 설정하였다.

 - Navbar-brand에 해당하는 부분은 Portfolio로 수정하였고, 글자 크기도 40px로 변경하였다.
 - Navbar에 나오는 메뉴에 해당 부분으로 가는 link를 걸어서 Navbar에서 메뉴를 찾아갈 수 있게 하였다. 또한, 글자도 17px로 조정하였다.

 - 전공(생명과학)과 현재 배우는 것(개발자)과 관련된 픽토그램을 추가하였다. 
 - 기존에 검은색으로 되어 있어서 그림판을 통해 하얀색으로 도색하였다.
 - 해당 픽토그램은 <img> 태그를 통해 반영하였다.

 - Navbar를 fixed로 고정시키고 body의 내용이 fixed 아래로 덮히는 것을 방지하려고 body에 padding-top을 navbar의 크기만큼 주었다.
 - 이를 통해 스크롤로 이동하더라도 navbar가 여전히 보이는 형식을 주었다.

## 2. 내용
 - 내용은 크게 Headline / Info / Personality / Project / Skills / Contact 으로 나뉘어있다.
 - 전반적으로 green 계열의 색을 사용하여 눈을 편안하게 해 주었다.
 - 또한 navbar와 대비되게 검은색 글씨를 사용하였다.

 - large(992px)를 기준으로 그것보다 너비가 더 커지면 (navbar)와 같은 기준으로
 Info - Personality / Project - Skills 가 같은 열에 동시에 들어가게 된다.
 - 상대적으로 Info와 Project가 내용이 더 길어서 3:2의 배율로 나누었다.
 - 이를 위해 display: flex;로 설정하였다.

## 3. footer
 - footer 역시 위의 navbar처럼 fixed 기능을 이용하였고, 마찬가지로 contact의 충분한 공간을 확보하려고 body에 padding-bottom을 주었다.

## 4. 마무리
포트폴리오에 정작 채울 수 있는 내용이 많지 않아 처리할 게 많지 않았다. 나중에 실제로 만들 게 된다면 훨씬 많은 내용을 만들 수 있었으면 좋겠다.