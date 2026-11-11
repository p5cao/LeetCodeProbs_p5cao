class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        from collections import deque
        blocked = set(deadends)
        def neighbors_of(state:str)->list[str]:
            neighbors = []
            str_list = list(state)
            for idx, char in enumerate(str_list):
                nb_list_1, nb_list_2 = str_list.copy(), str_list.copy()
                if char == '0':
                    char_1, char_2 = '9','1'
                elif char == '9':
                    char_1, char_2 = '8','0'
                else:
                    char_1, char_2 = str(int(char)-1), str(int(char) + 1)
                nb_list_1[idx] = char_1
                nb_list_2[idx] = char_2
                neighbor_1, neighbor_2 = ''.join(nb_list_1), ''.join(nb_list_2)
                if neighbor_1 not in blocked:
                    neighbors.append(neighbor_1)
                if neighbor_2 not in blocked:
                    neighbors.append(neighbor_2)
            return neighbors
        
        def bfs(state:str)->int:
            
            if state in blocked:
                return -1
            queue = deque([(state, 0)])
            visited = {state}
            while queue:
                popped_state, count = queue.popleft()
                if popped_state == target:
                    return count
                for neighbor in neighbors_of(popped_state):
                    if neighbor not in visited:
                        queue.append((neighbor, count+1))
                        visited.add(neighbor)
            return -1
        return bfs('0000')
        

