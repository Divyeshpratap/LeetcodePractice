'''
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash '/'.
Directories within the path should be separated by only one slash '/'.
It should not end with a slash '/', unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        curr = ""
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != '.':
                    stack.append(curr)
                curr = ""
            else:
                curr += c

        return "/" + "/".join(stack)
'''
Time Complexity: O(N)
Space Complexity: O(N)
**********************
Summary Statistics:
Runtime: 30 ms, faster than 92.18% of Python3 online submissions for Simplify Path.
Memory Usage: 16.4 MB, less than 94.96% of Python3 online submissions for Simplify Path
'''
