

'''
71. Simplify Path
Medium
Topics
premium lock iconCompanies

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

Return the simplified canonical path.


'''

class Solution:
    def simplifyPath(self, path: str) -> str:

        stack: list[str] = []

        
        name = ''
        for c in path:
            if c == '/':
                if len(name) > 0:
                    if name == '..':
                        if stack:
                            stack.pop()
                        name = ''

                    elif name == '.':
                        name = ''
                    else:
                        stack.append(name)
                        name = ''
            else:
                name += c


        if len(name) > 0:
            if name == '..':
                if stack:
                    stack.pop()
                name = ''
            elif name == '.':
                    name = ''
            else:
                stack.append(name)
                name = ''

        #print(stack)
        output = ''
        for d in stack:
            if d != '.':
                output += '/' + d
 
        if len(output) == 0:
            return '/'

        return output
    

s = Solution()
out = s.simplifyPath('/a/./b/../../c/')
print(out)


