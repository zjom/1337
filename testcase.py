from dataclasses import dataclass
from typing import TypeVar, Generic

S = TypeVar("S")
T = TypeVar("T")

@dataclass
class TestCase(Generic[S,T]):
    Input: S
    Expected: T
