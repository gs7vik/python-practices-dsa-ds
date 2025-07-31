from collections import deque

class Solution:
    def findOrder(words):
        letters = set()
        for word in words:
            for c in word:
                letters.add(c)
        
        # Map each letter to an index
        char_index = {c: i for i, c in enumerate(letters)}
        index_char = {i: c for c, i in char_index.items()}  # for final output

        adj_list = [[] for _ in range(len(letters))]
        indeg = [0] * len(letters)

        for i in range(len(words) - 1):
            curr = words[i]
            next = words[i + 1]
            
            # Check prefix edge case: "abc", "ab"
            if curr.startswith(next) and len(curr) > len(next):
                return ""

            for j in range(min(len(curr), len(next))):
                if curr[j] != next[j]:
                    u = char_index[curr[j]]
                    v = char_index[next[j]]
                    if v not in adj_list[u]:  # Avoid duplicate edges
                        adj_list[u].append(v)
                        indeg[v] += 1
                    break

        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        ans_list = []
        while q:
            x = q.popleft()
            ans_list.append(index_char[x])
            for i in adj_list[x]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)

        if len(ans_list) == len(letters):
            return ''.join(ans_list)
        else:
            return ""
