class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []
        for a in asteroids:
            while st and st[-1]>0 and a<0:
                if st[-1]<-a:
                    st.pop()
                    continue
                elif st[-1]==-a:
                    st.pop()
                break
            else:
                st.append(a)
        return st