class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position,speed)]
        st = []

        for p,s in sorted(cars)[::-1]:
            time_required = (target-p)/s
            if not st or time_required>st[-1]:
                st.append(time_required)
        return len(st)