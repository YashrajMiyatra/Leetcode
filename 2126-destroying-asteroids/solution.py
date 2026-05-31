class Solution:
    """
    Greedy Algorithm for Asteroid Destruction.
    
    Architecture:
    - **Theoretical Foundation**: To maximize the planet's mass and survive as long as possible, 
      the absolute optimal strategy is to always consume the smallest available asteroid.
      Every consumed asteroid monotonically increases our mass, unlocking the ability to 
      consume strictly larger asteroids.
    - **Execution**: We sort the asteroids in ascending order in O(N log N) time and greedily 
      sweep through them. If at any point the planet's mass is smaller than the current asteroid, 
      it means it's mathematically impossible to proceed (since all remaining asteroids are even larger), 
      and we return False.
    - Time Complexity: O(N log N) dominated by Timsort.
    - Space Complexity: O(1) auxiliary space (O(N) for Timsort internally).
    """
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False
        return True
