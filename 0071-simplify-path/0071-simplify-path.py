class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        
        for directory in path:
            if not directory or directory == ".":
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
                
        return "/" + "/".join(stack)