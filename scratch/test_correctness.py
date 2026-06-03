import itertools
from collections import deque

def minOperations_brute(nums):
    n = len(nums)
    target = tuple(range(n))
    start = tuple(nums)
    if start == target:
        return 0
        
    visited = {start: 0}
    q = deque([start])
    
    while q:
        curr = q.popleft()
        d = visited[curr]
        
        # Op 1: Reverse
        next_state1 = curr[::-1]
        if next_state1 == target:
            return d + 1
        if next_state1 not in visited:
            visited[next_state1] = d + 1
            q.append(next_state1)
            
        # Op 2: Rotate Left
        next_state2 = curr[1:] + (curr[0],)
        if next_state2 == target:
            return d + 1
        if next_state2 not in visited:
            visited[next_state2] = d + 1
            q.append(next_state2)
            
    return -1

def minOperations_state_space(nums):
    n = len(nums)
    if n <= 1:
        return 0
        
    dist_I = [-1] * n
    dist_D = [-1] * n
    
    dist_I[0] = 0
    q = deque([('I', 0)])
    
    while q:
        t, k = q.popleft()
        d = dist_I[k] if t == 'I' else dist_D[k]
        
        if t == 'I':
            # Backward L: I_{(k-1) % n} -> I_k
            nk = (k - 1) % n
            if dist_I[nk] == -1:
                dist_I[nk] = d + 1
                q.append(('I', nk))
            # Backward R: D_{(k-1) % n} -> I_k
            nk = (k - 1) % n
            if dist_D[nk] == -1:
                dist_D[nk] = d + 1
                q.append(('D', nk))
        else:  # t == 'D'
            # Backward L: D_{(k+1) % n} -> D_k
            nk = (k + 1) % n
            if dist_D[nk] == -1:
                dist_D[nk] = d + 1
                q.append(('D', nk))
            # Backward R: I_{(k+1) % n} -> D_k
            nk = (k + 1) % n
            if dist_I[nk] == -1:
                dist_I[nk] = d + 1
                q.append(('I', nk))
                
    first = nums[0]
    
    is_I = True
    for i in range(n):
        if nums[i] != (first + i) % n:
            is_I = False
            break
            
    if is_I:
        return dist_I[first]
        
    is_D = True
    for i in range(n):
        if nums[i] != (first - i + n) % n:
            is_D = False
            break
            
    if is_D:
        return dist_D[first]
        
    return -1

def test_all():
    for n in range(1, 9):
        print(f"Testing n={n}...")
        for p in itertools.permutations(range(n)):
            ans_brute = minOperations_brute(list(p))
            ans_state = minOperations_state_space(list(p))
            if ans_brute != ans_state:
                print(f"FAILED for permutation {p}: brute={ans_brute}, state={ans_state}")
                return
    print("ALL TESTS PASSED!")

if __name__ == "__main__":
    test_all()
