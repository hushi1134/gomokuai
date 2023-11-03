

def is_empty(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != " ":
                return False
    return True



def is_bounded(board, y_end, x_end, length, d_y, d_x):
    a = 0
    edge_open = 0
    if (y_end+d_y < len(board)) and (x_end+d_x < len(board[0])) and (x_end+d_x >=0) and board[y_end+d_y][x_end+d_x] != "b" and board[y_end+d_y][x_end+d_x] != "w":
        edge_open+=1
        a = 1

    y = y_end - (d_y*length)
    x = x_end - (d_x*length)
    if d_x != -1 and y>=0 and x>=0 and board[y][x] != "b" and board[y][x]!="w":
        edge_open +=1
        a = 2
    elif d_x == -1 and x<(len(board[0])) and y>=0 and board[y][x] != "b" and board[y][x]!="w":
        edge_open +=1
        a= 2
    elif d_x == -1 and ((y<0) or (x>=(len(board[0])))):
        a = 3


    for z in range(length):
        y1 = y_end - (d_y*z)
        x1 = x_end - (d_x*z)
        if board[y1][x1] != board[y_end][x_end]:
            return "not full sequence"

    if edge_open == 2:
        return "OPEN"
    if edge_open == 1:
        if a ==1:
            if y>=0 and x>=0 and board[y][x]== board[y_end][x_end]:
                return "not the full sequence"
        elif a == 2:
            if (y_end+d_y < len(board)) and (x_end+d_x < len(board[0])) and (x_end+d_x >=0) and board[y_end+d_y][x_end+d_x] == board[y_end][x_end]:
                return "not the full sequence"
        return "SEMIOPEN"
    if edge_open == 0:
        if a!=3 and (y>=0 and x>=0 and board[y][x]== board[y_end][x_end]) or ((y_end+d_y < len(board)) and (x_end+d_x < len(board[0])) and (x_end+d_x >=0) and board[y_end+d_y][x_end+d_x] == board[y_end][x_end]):
            return "not full sequence"

        return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_count = 0
    semi_opencount = 0
    counter = 0
    test = 0
    if d_y == 0 and d_x == 1:
        for x in range(x_start, (len(board[0])-length+1)):
            if board[y_start][x] == col:
                for a in range(length):
                    if board[y_start][x+a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, y_start, (x+length-1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, y_start, (x+length-1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                test = 0
                counter = 0


    if d_y == 1 and d_x == 0:
        for y in range(y_start, (len(board)-length+1)):
            if board[y][x_start] == col:
                for a in range(length):
                    if board[y+a][x_start] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), x_start, length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), x_start, length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                test = 0
                counter = 0


    if d_y == 1 and d_x == 1:
        for y in range(y_start, (len(board)-length+1)):
            x1 = y-y_start+x_start
            if x1<(len(board[0])-length+1) and board[y][x1] == col:
                for a in range(length):
                    if board[y+a][x1+a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), (x1+length-1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), (x1+length-1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                test = 0
                counter = 0

    if d_y == 1 and d_x == -1:
        for y in range(y_start, (len(board)-length+1)):
            x1 = x_start-y+y_start
            if x1<(len(board[0])) and (x1>= (length-1)) and board[y][x1] == col:
                for a in range(length):
                    if board[y+a][x1-a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), (x1-length+1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), (x1-length+1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                test = 0
                counter =0

    counter = 0
    return open_count, semi_opencount

def detect_row2(board, col, y_start, x_start, length, d_y, d_x):
    open_count = 0
    semi_opencount = 0
    closed_count  = 0
    counter = 0
    test = 0
    if d_y == 0 and d_x == 1:
        for x in range(x_start, (len(board[0])-length+1)):
            if board[y_start][x] == col:
                for a in range(length):
                    if board[y_start][x+a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, y_start, (x+length-1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, y_start, (x+length-1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                    if is_bounded(board, y_start, (x+length-1), length, d_y, d_x) == "CLOSED":
                        closed_count+=1
                test = 0
                counter = 0


    if d_y == 1 and d_x == 0:
        for y in range(y_start, (len(board)-length+1)):
            if board[y][x_start] == col:
                for a in range(length):
                    if board[y+a][x_start] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), x_start, length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), x_start, length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                    if is_bounded(board, (y+length-1), x_start, length, d_y, d_x) == "CLOSED":
                        closed_count+=1
                test = 0
                counter = 0


    if d_y == 1 and d_x == 1:
        for y in range(y_start, (len(board)-length+1)):
            x1 = y-y_start+x_start
            if x1<(len(board[0])-length+1) and board[y][x1] == col:
                for a in range(length):
                    if board[y+a][x1+a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), (x1+length-1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), (x1+length-1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                    if is_bounded(board, (y+length-1), (x1+length-1), length, d_y, d_x) == "CLOSED":
                        closed_count+=1
                test = 0
                counter = 0

    if d_y == 1 and d_x == -1:
        for y in range(y_start, (len(board)-length+1)):
            x1 = x_start-y+y_start
            if x1<(len(board[0])) and (x1>= (length-1)) and board[y][x1] == col:
                for a in range(length):
                    if board[y+a][x1-a] == col:
                        counter += 1
                    else:
                        test = 1
                if counter == length and test == 0:
                    if is_bounded(board, (y+length-1), (x1-length+1), length, d_y, d_x) == "OPEN":
                        open_count +=1
                    if is_bounded(board, (y+length-1), (x1-length+1), length, d_y, d_x) == "SEMIOPEN":
                        semi_opencount+=1
                    if is_bounded(board, (y+length-1), (x1-length+1), length, d_y, d_x) == "CLOSED":
                        closed_count+=1
                test = 0
                counter =0

    counter = 0
    return open_count, semi_opencount, closed_count




def detect_rows(board, col, length):
    total_open_count, total_semiopen_count = 0, 0
    for y in range(len(board)):
        oc, soc = detect_row(board, col, y, 0, length, 0, 1)
        total_open_count += oc
        total_semiopen_count += soc
        oc, soc = detect_row(board, col, y, 0, length, 1, 1)
        total_open_count += oc
        total_semiopen_count += soc
        oc, soc = detect_row(board, col, y, len(board[0])-1, length, 1, -1)
        total_open_count += oc
        total_semiopen_count += soc



    for x in range(len(board[0])):
        oc, soc = detect_row(board, col, 0, x, length, 1, 0)
        total_open_count+= oc
        total_semiopen_count += soc

        if x+1 <len(board[0]):
            oc, soc = detect_row(board, col, 0, x+1, length, 1, 1)
            total_open_count += oc
            total_semiopen_count += soc
            oc, soc = detect_row(board, col, 0, x, length, 1, -1)
            total_open_count += oc
            total_semiopen_count += soc


    return total_open_count, total_semiopen_count

def detect_rows2(board, col, length):
    total_open_count, total_semiopen_count, total_closed_count = 0, 0, 0
    for y in range(len(board)):
        oc, soc, cc = detect_row2(board, col, y, 0, length, 0, 1)
        total_open_count += oc
        total_semiopen_count += soc
        total_closed_count += cc
        oc, soc, cc = detect_row2(board, col, y, 0, length, 1, 1)
        total_open_count += oc
        total_semiopen_count += soc
        total_closed_count += cc
        oc, soc, cc = detect_row2(board, col, y, len(board[0])-1, length, 1, -1)
        total_open_count += oc
        total_semiopen_count += soc
        total_closed_count += cc


    for x in range(len(board[0])):
        oc, soc, cc = detect_row2(board, col, 0, x, length, 1, 0)
        total_open_count+= oc
        total_semiopen_count += soc
        total_closed_count += cc
        if x+1 <len(board[0]):
            oc, soc, cc = detect_row2(board, col, 0, x+1, length, 1, 1)
            total_open_count += oc
            total_semiopen_count += soc
            total_closed_count += cc
            oc, soc, cc = detect_row2(board, col, 0, x, length, 1, -1)
            total_open_count += oc
            total_semiopen_count += soc
            total_closed_count += cc



    return total_open_count, total_semiopen_count, total_closed_count


def search_max(board):
    maxscore = -10000000
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == " ":
                board[y][x] = "b"
                score1 = score(board)
                if score1 > maxscore:
                    maxscore = score1
                    move_y = y
                    move_x = x
                board[y][x] = " "

    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])






def is_win(board):

    open_black, semiblack, closedblack = detect_rows2(board, "b", 5)
    open_white, semiwhite, closedwhite = detect_rows2(board, "w", 5)
    if open_black > 0 or semiblack>0 or closedblack>0:
        return "Black won"
    elif open_white > 0 or semiwhite>0 or closedwhite>0:
        return "White won"

    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == " ":
                return "Continue playing"

    return "Draw"


def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    print(detect_row(board, "w", 0,x,length,d_y,d_x))

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0




if __name__ == '__main__':
    play_gomoku(8)