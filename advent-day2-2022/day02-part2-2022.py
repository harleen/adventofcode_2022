

rock = "rock"
paper = "paper"
scissors = "scissors"
lose = "lose"
draw = "draw"
win = "win"
RPS_map = {"A" : rock, "B" : paper, "C" : scissors}
key_to_my_strategy_map = {"X": lose, "Y" : draw, "Z": win}
points_map = {rock : 1, paper : 2, scissors : 3, lose: 0, draw : 3, win : 6}

def main():

    game_play = parse_file()
    if (len(game_play) > 1):
        game_play_opponent = game_play[0]
        game_play_me = game_play[1]
        print(f"Number of moves in file: {len(game_play_me)}")
    
        my_points = 0
        for opponent_move_key, my_move in zip(game_play_opponent, game_play_me):
            opponent_move = RPS_map[opponent_move_key]
            points = play_round(opponent_move, dycrpt_my_move(opponent_move, my_move))
            my_points += points[1] if len(points) > 1 else 0
        print(f"My points: {my_points}")


def dycrpt_my_move(opponent_move: str, my_encrypted_move: str) -> str:

    winning_moves = {rock : paper, paper: scissors, scissors : rock}
    losing_moves = {rock : scissors, paper: rock, scissors : paper}

    if key_to_my_strategy_map[my_encrypted_move] == draw:
        return opponent_move
    elif (key_to_my_strategy_map[my_encrypted_move] == win):
        return winning_moves[opponent_move]
    else:
        return losing_moves[opponent_move]
        
def play_round(player_1_move: str, player_2_move: str) -> [int]:
    
    player_1_points = 0
    player_2_points = 0

    print(f"Player 1 play {player_1_move}, Player 2 plays {player_2_move}")
    
    if player_1_move == player_2_move:
        print("Its a tie")
        player_1_points = points_map[draw] 
        player_2_points = points_map[draw]
    elif (
        (player_1_move == 'rock' and player_2_move == 'scissors') or
        (player_1_move == 'paper' and player_2_move == 'rock') or
        (player_1_move == 'scissors' and player_2_move == 'paper')
    ):
        print("Player 1 wins")
        player_1_points = points_map["win"] 
    else:
        print("Player 2 wins")
        player_2_points = points_map["win"] 
    
    player_1_points += points_map[player_1_move] 
    player_2_points += points_map[player_2_move]
    return [player_1_points, player_2_points];

def parse_file():
    game_play_opponent = []
    game_play_me = []
    file_path = 'advent-day2-2022/2022-puzzle2-input.txt'
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            try:
                tokens = line.strip().split();
                game_play_opponent.append(tokens[0])
                game_play_me.append(tokens[1])
            except ValueError as e:
                print (e)
    return (game_play_opponent, game_play_me)

if __name__ == "__main__":
    main()