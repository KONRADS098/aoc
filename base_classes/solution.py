from abc import ABC, abstractmethod


class Solution(ABC):
    @abstractmethod
    def part1(self, data):
        pass

    @abstractmethod
    def part2(self, data):
        pass
