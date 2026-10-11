import dataclasses
from enum import Enum
from typing import TypeVar

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

#class Rook(ChessPiece):
#    def can_move_to(self, x: int, y: int) -> bool:
#        return (x == self.x) or (y == self.y)

T = TypeVar('T')

#def consecutive_pairs(x: List[T]) -> List[Tuple[T, T]]:
#    '''
#    post: True
#    '''
#    return [(x[i], x[i + 1]) for i in range(len(x))]

class VehicleType(Enum):
    CAR = 0
    BICYCLE = 1

#@dataclasses.dataclass(init=False)
class Vehicle:
    '''
    inv: (self.fuel_level is None) == (self.kind == VehicleType.BICYCLE)
    '''
    kind: VehicleType
    fuel_level: float | None

def can_use(vehicle: Vehicle) -> bool:
    '''
    post:True
    '''
    if vehicle.kind is VehicleType.BICYCLE:
        return True
    assert vehicle.fuel_level is not None
    return vehicle.fuel_level > 0.0

def csv_first_column(lines: list[str]) -> list[str]:
    '''
        pre: all(',' in line for line in lines)
        post: __return__ == [line.split(',')[0] for line in lines]
    '''
    return [line[:line.index(',')] for line in lines]