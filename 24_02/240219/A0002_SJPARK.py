import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL02_박성재'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # 기준점을 중심으로 목표가 몇 사분면 또는 축에 있는 확인하는 함수
    def where(me, target):  # 기준점(me)의 좌표와 목표점(target)의 좌표를 입력받아
        if me[0] < target[0] and me[1] < target[1]:
            return 1    # 1사 분면
        elif me[0] > target[0] and me[1] < target[1]:
            return 2    # 2사 분면
        elif me[0] > target[0] and me[1] > target[1]:
            return 3    # 3사 분면
        elif me[0] < target[0] and me[1] > target[1]:
            return 4    # 4사 분면

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # target_stack에 목표 공들의 좌표 값들을 삽입
    target_stack = []
    if order == 1:   # 내가 선공이면
        for i in [1, 3]:   # LIFO 구조이므로 5번을 가장 먼저 넣어주고 타겟공인 1번과 3번의 좌표값을 target_stack에 삽입
            # 초기 [-1.000000, -1.000000]인 좌표는 테이블 위에 없다는 뜻이므로 stack에 안넣겠다
            if balls[i][0] != -1 and balls[i][1] != -1:
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                target_stack.append([targetBall_x, targetBall_y])
    elif order == 2:   # 내가 후공이면
        for i in [2, 4]:   # 타겟공인 2번과 4번의 좌표값을 target_q에 삽입
            # 초기 [-1.000000, -1.000000]인 좌표는 테이블 위에 없다는 뜻이므로 stack에 안넣겠다
            if balls[i][0] != -1 and balls[i][1] != -1:
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                target_stack.append([targetBall_x, targetBall_y])

    if order == 1:
        if (balls[1][0] == -1 and balls[1][1] == -1) and (balls[3][0] == -1 and balls[3][1] == -1):
            target_stack.append(balls[5])

    elif order == 2:
        if (balls[2][0] == -1 and balls[2][1] == -1) and (balls[4][0] == -1 and balls[4][1] == -1):
            target_stack.append(balls[5])
    print(target_stack)

    while target_stack: # target_stack이 빌때까지
        target_now = target_stack.pop() # 현재 내가 넣고자 하는 목표 공의 [x,y] 좌표
        # 테이블을 1구획당 1개의 홀을 갖는 6구획으로 나누고 타겟공이 각 구획에 들어있다면 그 구획에 있는 홀로 들어가게 하자
        if target_now[0] <= 85 and target_now[1] <= 63.5:
            Hole = HOLES[0]
        elif (85 < target_now[0] <= 169) and target_now[1] <= 63.5:
            Hole = HOLES[1]
        elif 169 < target_now[0] and target_now[1] <= 63.5:
            Hole = HOLES[2]
        elif target_now[0] <= 85 and target_now[1] > 63.5:
            Hole = HOLES[3]
        elif (85 < target_now[0] <= 169) and target_now[1] > 63.5:
            Hole = HOLES[4]
        elif 169 < target_now[0] and target_now[1] > 63.5:
            Hole = HOLES[5]

        # 내가 칠 공 기준으로 Hole이 몇 사분면에 있는지 파악하여 내 공이 실제로 가야할 위치를 구한다.
        real_target = []
        power_width = abs(Hole[0] - target_now[0])
        power_height = abs(Hole[1] - target_now[1])
        seta = math.atan((abs(Hole[1] - target_now[1])) / (abs(Hole[0] - target_now[0])))
        if where(target_now, Hole) == 1:
            real_target = [target_now[0] - 5.73 * math.cos(seta), target_now[1] - 5.73 * math.sin(seta)]
        elif where(target_now, Hole) == 2:
            real_target = [target_now[0] + 5.73 * math.cos(seta), target_now[1] - 5.73 * math.sin(seta)]
        elif where(target_now, Hole) == 3:
            real_target = [target_now[0] + 5.73 * math.cos(seta), target_now[1] + 5.73 * math.sin(seta)]
        elif where(target_now, Hole) == 4:
            real_target = [target_now[0] - 5.73 * math.cos(seta), target_now[1] + 5.73 * math.sin(seta)]

        # width, height: 목적 지점과 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
        width = abs(real_target[0] - whiteBall_x)
        height = abs(real_target[1] - whiteBall_y)

        # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
        #   - 1radian = 180 / PI (도)
        #   - 1도 = PI / 180 (radian)
        # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
        radian = math.atan(width / height) if height > 0 else 0
        angle = 180 / math.pi * radian
    
        # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
        if whiteBall_x == real_target[0]:
            if whiteBall_y < real_target[1]:
                angle = 0
            else:
                angle = 180
        elif whiteBall_y == real_target[1]:
            if whiteBall_x < real_target[0]:
                angle = 90
            else:
                angle = 270

        # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
        if whiteBall_x < real_target[0] and whiteBall_y < real_target[1]:
            radian = math.atan(width / height)
            angle = (180 / math.pi * radian)

        # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
        elif whiteBall_x > real_target[0] and whiteBall_y < real_target[1]:
            radian = math.atan(height / width)
            angle = (180 / math.pi * radian) + 270

        # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
        elif whiteBall_x > real_target[0] and whiteBall_y > real_target[1]:
            radian = math.atan(width / height)
            angle = (180 / math.pi * radian) + 180
    
        # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
        elif whiteBall_x < real_target[0] and whiteBall_y > real_target[1]:
            radian = math.atan(height / width)
            angle = (180 / math.pi * radian) + 90
        
        # distance: 두 점(좌표) 사이의 거리를 계산
        distance1 = math.sqrt(width**2 + height**2)
        distance2 = math.sqrt(power_width ** 2 + power_height ** 2)
        distance = max(distance1, distance2)
        # power: 거리 distance에 따른 힘의 세기를 계산
        power = distance * 0.5


    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')