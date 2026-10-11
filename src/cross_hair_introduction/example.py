import dataclasses
# crosshair: on

def average(numbers: list[float]) -> float:
    '''
    pre: len(numbers) > 0
    post: min(numbers) <= __return__ <= max(numbers)
    '''
    return sum(numbers) / len(numbers)

@dataclasses.dataclass
class ChessPiece:
    x: int
    y: int
    def can_move_to(self, x: int, y: int) -> bool:
        '''
        pre: (0 <= x < 8) and (0 <= y < 8)
        # It7s never valid to "move" to your present location:
        raises: NotImplementedError
        post: implies((x, y) == (self.x, self.y), not __return__)
        '''
        raise NotImplementedError

class Rook(ChessPiece):
    def can_move_to(self, x: int, y: int) -> bool:
        return (x == self.x) or (y == self.y)