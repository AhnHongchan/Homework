import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL02_PYTHON_JUYEON'

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

    # angle = 0.0
    # power = 0.0

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

    print('balls:', balls)
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]
    targetBall_x = 0
    targetBall_y = 0



    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # 공의 지름 및 반지름
    ball_d = 5.73
    ball_r = 5.73 / 2

    # 벡터 크기 계산하기
    def vector_size(vector):
        size = math.sqrt(vector[0]**2 + vector[1]**2)
        return size

    # 벡터 정규화 -> 단위벡터로 변경
    def normalization(vector):
        norm = [0, 0]
        size = vector_size(vector)
        norm[0] = vector[0] * 1 / size
        norm[1] = vector[1] * 1 / size
        return norm

    # 접점의 좌표를 내 공과 목적공의 좌표만을 가지고 계산
    def contact(target, hole):
        """
        :param target: 목적공 좌표
        :param hole: 들어갈 hole의 좌표
        :return: 접점 좌표
        """
        vec_r = [hole[0] - target[0], hole[1] - target[1]]
        vec_t = [0, 0]
        vec_t[0] = normalization(vec_r)[0] * -2.0 * ball_r
        vec_t[1] = normalization(vec_r)[1] * -2.0 * ball_r
        contact_ball = [0, 0]
        contact_ball[0] = vec_t[0] + target[0]
        contact_ball[1] = vec_t[1] + target[1]
        return contact_ball

    # 벡터 내적 계산
    def dot_product(v1:[], v2:[]):
        """
        :param v1: 벡터1
        :param v2: 벡터2
        :return: 내적 계산값
        """
        v = v1[0] * v2[0] + v1[1] * v2[1]
        return v

    # 각도 및 파워 계산
    def angle_power(v1, v2):
        '''
        :param v1: 벡터 v1 (예) 기준 벡터 [0, 1]my_ball ~ contact_ball 벡터
        :param v2: 벡터 v2
        :return: angle
        '''
        dot = dot_product(v1, v2)
        size_v1 = vector_size(v1)
        size_v2 = vector_size(v2)
        angle = math.degrees(math.acos(dot / (size_v1 * size_v2)))
        return angle

    # 어디로 때려넣을건지
    def where_hole(target):
        """
        :param target: 목적공 좌표 [x, y]
        :return: 들어갈 hole 좌표 [x, y]
        """

        m = 0.5
        holes = [[0+m, 0+m], [127, 0+m], [254-m, 0+m], [0+m, 127-m], [127, 127-m], [254-m, 127-m]]
        prior = [[i] for i in range(6)]
        pri_dis = []
        pri_ang = []
        dis_list = []
        ang_list = []

        # distance & angle을 고려한 홀 우선순위 생성
        for i in range(len(holes)):
            # vec: target -> hole
            vec = [HOLES[i][0] - target[0], HOLES[i][1] - target[1]]

            distance = vector_size(vec)
            dis_list.append(distance)
            pri_dis.append(distance)
            # 1. 내공 -> 접점 벡터
            vec1 = [whiteBall_x - target[0], whiteBall_y - target[1]]
            # 2. 접점 -> hole 벡터
            vec2 = [HOLES[i][0] - target[0], HOLES[i][1] - target[1]]
            # angle 계산
            ang = angle_power(vec1, vec2)
            ang_list.append(ang)
            pri_ang.append(ang)
            '''
            # 가중치를 적용한 우선순위 삽입
            pri = distance * 0.3 + ang * 0.7
            prior[i].append(pri)
            '''
        # for i in range(6):
        pri_dis.sort()
        pri_ang.sort(reverse=True)
        for i in range(6):
            d = pri_dis.index(dis_list[i]) + 1
            a = pri_ang.index(ang_list[i]) + 1
            pri = d * 0.3 + a * 0.7
            prior[i].append(pri)
        # print(prior)
        prior.sort(key=lambda x: x[1])
        # print(prior)
        print('목표 hole:', prior[0][0])
        return HOLES[prior[0][0]], ang_list[prior[0][0]]

    def select_hole_according_target(target):
        # 1. 접점 좌표 계산
        target_ball = target

        # 2. 목적공을 어디로 집어넣을 지 hole 좌표 계산
        hole, hole_ang = where_hole(target_ball)
        contact_ball = contact(target_ball, hole)
        vec_a = [contact_ball[0] - whiteBall_x, contact_ball[1] - whiteBall_y]

        # angle
        st = [0, 1]  # 기준 벡터
        ang = angle_power(st, vec_a)
        if whiteBall_x > contact_ball[0]:
            ang = 360 - ang

        # power 계산값 - 주어짐
        pow = math.sqrt(70**2 + vector_size(vec_a)*0.5 )
        # print(pow)
        return ang, pow, hole_ang

    def different_ball(vector, target, diff_ball):
        """
        :param vector: 내 공 -> target
        :param target: target 좌표
        :param diff_ball: 다른 공
        :return: 0, 1
        """
        c = target[1] - vector[1] / vector[0] * target[0]
        d_upper = vector[0] / vector[1] * diff_ball[0] - diff_ball[1] + c
        d_lower = math.sqrt(math.pow(vector[1]/vector[0], 2) + 1)
        d = d_upper / d_lower
        if d < 3 * ball_r:
            return 0
        else:
            return 1

    # 목적공 정하기
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # print(order)
    ##################################
    # order = 1, order =2 변경하기
    if order == 1:
        target_ball_list = [balls[1], balls[3]]
        diff_ball_list = [balls[2], balls[4]]
    else:
        diff_ball_list = [balls[1], balls[3]]
        target_ball_list = [balls[2], balls[4]]
    target_list = []
    for i in range(len(target_ball_list)):
        # 타겟공 우선순위 정하기기
        # 현재 공이 존재하는 지 확인
        if target_ball_list[i][0] > 0:
            print('공 순서:', i * 2 + 1, target_ball_list[i])
            # 타겟 공
            targetBall_x = float(target_ball_list[i][0])
            targetBall_y = float(target_ball_list[i][1])
            vec = [targetBall_x - whiteBall_x, targetBall_y, whiteBall_y]# 내 공 -> target
            target = [targetBall_x, targetBall_y]
            for diff_ball in diff_ball_list:
                if not different_ball(vec, target, diff_ball):
                    break
            if not different_ball(vec, target, balls[5]):
                break
            # 무사히 나옴 -> angle, power 유지
            target_list.append(select_hole_according_target([targetBall_x, targetBall_y]))

    # 무사히 못나오면 target_list 없어
    if target_list:
        target_list.sort(key=lambda x: -x[2])
        # print(target_list[0])   # 1번 공[angle, power, target_angle], 3번 공[angle, power, target_angle]
        # 다른 공 경로에 있는 지 확인 작업

        angle, power, _ = target_list[0]
        # print(angle, power)
    else:
        # 내꺼 공이 남아있어
        print(target_list)
        for i in range(len(target_ball_list)):
            if target_ball_list[i][0] > 0:
                # 내꺼 공을 쳐
                angle, power, _ = select_hole_according_target([target_ball_list[i][0], target_ball_list[i][1]])
        # 내꺼 공이 다 들어갔어
                break
        else:
            print('5번 칠래')
            angle, power, _ = select_hole_according_target([balls[5][0], balls[5][1]])

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