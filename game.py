from game_logger import MyLogger

class Room:
    """
    Base class for Room
    """
    def __init__(self, x, y, name, description, exits):
        """
        :param x: room x
        :param y: room y
        :param name: room name
        :param description: room description
        """
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.exits = exits
        self.log = MyLogger('Room')

    def __str__(self):
        self.log.debug("it returns name and description of the room")
        return f'{self.name}\n{self.description}'


    def _check_exit(self, direction):
        self.log.debug('it returns the right direction to exit the room')
        return direction in self.exits


class Game:
    Directions = {
        "north": (0, -1),
        "south": (0, 1),
        "west": (-1, 0),
        "east": (1, 0)
    }

    def __init__(self, map):
        self.player_x = 0
        self.player_y = 0
        self.map = map
        self.current_room = self._get_room(0, 0)
        self.log = MyLogger('Game')
        self._look_at(self.current_room)

    def _move(self, x, y):
        self.log.debug('Player moves to {x}/{y}')
        new_room = self._get_room(x, y)
        if new_room:
            self.current_room = new_room
            self.player_x += x
            self.player_y += y
            self._look_at(self.current_room)
        else:
            print('Error: missing room')

    def _get_room(self, x, y):
        self.log.debug('we drive values {x}/{y} into the map')
        coords = (x, y)
        room = self.map.get(coords)
        return room

    @staticmethod
    def _look_at(obj):
        print(obj)

    def _parse(self, in_str):
        self.log.debug('we analyze in which direction the player is moving')
        if in_str.startswith('go '):
            direction = in_str[3:]
            if self.current_room._check_exit(direction):
                new_coords = self.Directions[direction]
                self._move(*new_coords)

    def run(self):
        self.log.debug("here is the player's turn")
        while True:
            action = input('>>> ')
            self._parse(action)


if __name__ == '__main__':
    room1 = Room(0, 0, "Main room", "", ["north"])
    room2 = Room(0, -1, "Second room", "", ["south"])
    map = {(room1.x, room1.y): room1,
           (room2.x, room2.y): room2
        }
    game = Game(map)
    game.run()
