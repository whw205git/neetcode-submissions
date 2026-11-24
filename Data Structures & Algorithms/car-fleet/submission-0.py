class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Take each position/speed pair, then sort by position desc
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if not stack or stack[-1] < time_to_target:
                stack.append(time_to_target)

        return len(stack)
