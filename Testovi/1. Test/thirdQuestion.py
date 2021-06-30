import random

random.seed(0)


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Game:
    def __init__(self, game_space):
        self.total_dots = 0
        self.game_space = list(game_space)
        for ii in range(len(self.game_space)):
            for j in range(len(self.game_space)):
                if self.game_space[ii][j] == '.':
                    self.total_dots += 1

    def decrement_total_dots(self):
        self.total_dots -= 1


class Pacman:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.left = -1
        self.up = -1
        self.right = -1
        self.down = -1

    def play_game(self):
        # Base case
        if self.game.total_dots == 0:
            return

        # Check init location
        if self.game.game_space[self.player.x][self.player.y] == '.':
            self.game.decrement_total_dots()
            self.game.game_space[self.player.x][self.player.y] = '#'

        # Check right
        if self.player.y < len(self.game.game_space) - 1 and self.game.game_space[self.player.x][
            self.player.y + 1] == '.':
            self.right = 1
        elif self.player.y < len(self.game.game_space) - 1:
            self.right = 0
        else:
            self.right = -1

        # Check up
        if self.player.x > 0 and self.game.game_space[self.player.x - 1][self.player.y] == '.':
            self.up = 1
        elif self.player.x > 0:
            self.up = 0
        else:
            self.up = -1

        # Check left
        if self.player.y > 0 and self.game.game_space[self.player.x][self.player.y - 1] == '.':
            self.left = 1
        elif self.player.y > 0:
            self.left = 0
        else:
            self.left = -1

        # Check down
        if self.player.x < len(self.game.game_space) - 1 and self.game.game_space[self.player.x + 1][
            self.player.y] == '.':
            self.down = 1
        elif self.player.x < len(self.game.game_space) - 1:
            self.down = 0
        else:
            self.down = -1

        # Move the player
        move_total = 0
        if self.right != -1:
            move_total += self.right
        if self.up != -1:
            move_total += self.up
        if self.left != -1:
            move_total += self.left
        if self.down != -1:
            move_total += self.down

        # If there are no dots around
        rand_x = int
        rand_y = int
        if move_total == 0:
            random_num_db = list()

            if self.right == 0:
                random_num_db.append((self.player.x, self.player.y + 1))
            if self.up == 0:
                random_num_db.append((self.player.x - 1, self.player.y))
            if self.left == 0:
                random_num_db.append((self.player.x, self.player.y - 1))
            if self.down == 0:
                random_num_db.append((self.player.x + 1, self.player.y))

            rand_index = random.randint(0, len(random_num_db) - 1)
            rand_x = random_num_db[rand_index][0]
            rand_y = random_num_db[rand_index][1]

            self.player.move(rand_x, rand_y)
            print(f'[{rand_x}, {rand_y}]')
            self.play_game()

        # If there is only one dot around
        elif move_total == 1:
            if self.right == 1:
                rand_x = self.player.x
                rand_y = self.player.y + 1
            elif self.up == 1:
                rand_x = self.player.x - 1
                rand_y = self.player.y
            elif self.left == 1:
                rand_x = self.player.x
                rand_y = self.player.y - 1
            elif self.down == 1:
                rand_x = self.player.x + 1
                rand_y = self.player.y

            self.player.move(rand_x, rand_y)
            print(f'[{rand_x}, {rand_y}]')
            self.play_game()

        # If there are more than one dots around
        elif move_total > 1:
            random_num_db = list()

            if self.right == 1:
                random_num_db.append((self.player.x, self.player.y + 1))
            if self.up == 1:
                random_num_db.append((self.player.x - 1, self.player.y))
            if self.left == 1:
                random_num_db.append((self.player.x, self.player.y - 1))
            if self.down == 1:
                random_num_db.append((self.player.x + 1, self.player.y))

            rand_index = random.randint(0, len(random_num_db) - 1)
            rand_x = random_num_db[rand_index][0]
            rand_y = random_num_db[rand_index][1]

            self.player.move(rand_x, rand_y)
            print(f'[{rand_x}, {rand_y}]')
            self.play_game()


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    table = []

    for i in range(n):
        table.append([j for j in input()])

    player_init = Player()
    game_init = Game(table)
    pacman = Pacman(player_init, game_init)

    pacman.play_game()
