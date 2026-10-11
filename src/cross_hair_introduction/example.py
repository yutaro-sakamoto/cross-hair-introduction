import dataclasses
from enum import Enum
from typing import TypeVar
import re

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

@dataclasses.dataclass
class JpegMetadata:
    num: int
    location: str
    direction: str
    kind: str

def match_old_files(s) -> bool:
    return re.fullmatch(r"(0|[1-9][0-9]+)_[A-Za-z0-9]+_[A-Za-z0-9]+\.jpeg", s) is not None

def match_new_files(s) -> bool:
    return re.fullmatch(r"(0|[1-9][0-9]+)_[A-Za-z0-9]+_[A-Za-z0-9]+_[A-Za-z0-9]+\.jpeg", s) is not None

class UnsupportedFileTypeError(ValueError):
    """Raised when a JPEG file name matches no known naming format."""

def metadata_to_jpeg_file_name(metadata: JpegMetadata) -> str:
    if metadata.direction:
        return f"{metadata.num}_{metadata.location}_{metadata.direction}_{metadata.kind}.jpeg"
    return f"{metadata.num}_{metadata.location}_{metadata.kind}.jpeg"

# pre: match_old_files(jpeg_file_name) or match_new_files(jpeg_file_name)
# post: jpeg_file_name == f"{__return__.num}
def jpeg_file_name_to_metadata(jpeg_file_name: str) -> JpegMetadata:
    r'''
    pre: match_old_files(jpeg_file_name) or match_new_files(jpeg_file_name)
    post: metadata_to_jpeg_file_name(__return__) == jpeg_file_name
    '''
    body = jpeg_file_name.split('.')[0]
    items = body.split('_')
    num = int(items[0])
    location = items[1]
    if len(items) == 4:
        direction = items[2]
        kind = items[3]
    elif len(items) == 3:
        direction = ""
        kind = items[2]
    else:
        raise UnsupportedFileTypeError

    return JpegMetadata(
        num,
        location,
        direction,
        kind,
    )