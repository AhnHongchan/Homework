document.addEventListener('DOMContentLoaded', function () {
    const player1Img = document.getElementById('player1-img');
    const player2Img = document.getElementById('player2-img');
    const countA = document.querySelector('.countA');
    const countB = document.querySelector('.countB');
    const scissorsButton = document.getElementById('scissors-button');
    const rockButton = document.getElementById('rock-button');
    const paperButton = document.getElementById('paper-button');
    const modal = document.querySelector('.modal');
    const modalContent = document.querySelector('.modal-content');
  
    let player1Score = 0;
    let player2Score = 0;
  
    // 가위바위보 게임 실행 함수
    function playGame(player1, player2) {
      if (player1 === player2) {
        return 0; // 무승부
      } else if (
        (player1 === 'scissors' && player2 === 'rock') ||
        (player1 === 'rock' && player2 === 'paper') ||
        (player1 === 'paper' && player2 === 'scissors')
      ) {
        return 2; // 플레이어 2 승리
      } else {
        return 1; // 플레이어 1 승리
      }
    }
  
    // 모달 표시 함수
    function showModal(message) {
      modalContent.textContent = message;
      modal.style.display = 'block';
      setTimeout(() => {
        modal.style.display = 'none';
      }, 3000);
    }
  
    // 플레이어 1이 버튼을 클릭했을 때
    scissorsButton.addEventListener('click', function () {
      player1Img.src = './img/scissors.png';
      const player1Choice = 'scissors'; // 플레이어 1의 선택
      let player2Choice; // 플레이어 2의 선택 변수 선언
      let timerId = setInterval(() => {
        // 매 초마다 새로운 플레이어 2의 선택 생성
        const choices = ['scissors', 'rock', 'paper'];
        player2Choice = choices[Math.floor(Math.random() * choices.length)];
        player2Img.src = `./img/${player2Choice}.png`;
      }, 100); // 매 0.1초마다 새로운 선택 생성
  
      // 3초 후에 결과 표시 및 모달 숨기기
      setTimeout(() => {
        clearInterval(timerId); // setInterval 중지
        const result = playGame(player1Choice, player2Choice);
        if (result === 0) {
          showModal("It's a tie!");
        } else if (result === 1) {
          player1Score++;
          countA.textContent = player1Score;
          showModal('Player 1 wins!');
        } else {
          player2Score++;
          countB.textContent = player2Score;
          showModal('Player 2 wins!');
        }
      }, 3000);
    });
  
    // 나머지 버튼 클릭 이벤트 핸들러 등록
    rockButton.addEventListener('click', function () {
      player1Img.src = './img/rock.png';
      const player1Choice = 'rock'; // 플레이어 1의 선택
      let player2Choice; // 플레이어 2의 선택 변수 선언
      let timerId = setInterval(() => {
        // 매 초마다 새로운 플레이어 2의 선택 생성
        const choices = ['scissors', 'rock', 'paper'];
        player2Choice = choices[Math.floor(Math.random() * choices.length)];
        player2Img.src = `./img/${player2Choice}.png`;
      }, 100); // 매 0.1초마다 새로운 선택 생성
  
      // 3초 후에 결과 표시 및 모달 숨기기
      setTimeout(() => {
        clearInterval(timerId); // setInterval 중지
        const result = playGame(player1Choice, player2Choice);
        if (result === 0) {
          showModal("It's a tie!");
        } else if (result === 1) {
          player1Score++;
          countA.textContent = player1Score;
          showModal('Player 1 wins!');
        } else {
          player2Score++;
          countB.textContent = player2Score;
          showModal('Player 2 wins!');
        }
      }, 3000);
    });
  
    paperButton.addEventListener('click', function () {
      player1Img.src = './img/paper.png';
      const player1Choice = 'paper'; // 플레이어 1의 선택
      let player2Choice; // 플레이어 2의 선택 변수 선언
      let timerId = setInterval(() => {
        // 매 초마다 새로운 플레이어 2의 선택 생성
        const choices = ['scissors', 'rock', 'paper'];
        player2Choice = choices[Math.floor(Math.random() * choices.length)];
        player2Img.src = `./img/${player2Choice}.png`;
      }, 100); // 매 0.1초마다 새로운 선택 생성
  
      // 3초 후에 결과 표시 및 모달 숨기기
      setTimeout(() => {
        clearInterval(timerId); // setInterval 중지
        const result = playGame(player1Choice, player2Choice);
        if (result === 0) {
          showModal("It's a tie!");
        } else if (result === 1) {
          player1Score++;
          countA.textContent = player1Score;
          showModal('Player 1 wins!');
        } else {
          player2Score++;
          countB.textContent = player2Score;
          showModal('Player 2 wins!');
        }
      }, 3000);
    })
})