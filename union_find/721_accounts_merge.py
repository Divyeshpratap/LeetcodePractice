'''
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
'''
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find_parent(self, node):

        if self.parent[node] == node:
            return node
        result = node

        while self.parent[result] != result:
            result = self.parent[result]
        return result

    def union(self, node1, node2):

        root1 = self.find_parent(node1)
        root2 = self.find_parent(node2)
        if root1 == root2:
            return False

        if self.rank[root1] >= self.rank[root2]:
            self.rank[root1] += self.rank[root2]
            self.parent[root2] = root1
        else:
            self.rank[root2] += self.rank[root1]
            self.parent[root1] = root2
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        email_unique = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_unique:
                    email_unique[email] = i
                else:
                    uf.union(i, email_unique[email])

        account_email = defaultdict(list)
        for email, index in email_unique.items():
            leader = uf.find_parent(index)
            account_email[leader].append(email)

        res = []
        for i, emails in account_email.items():
            name = accounts[i][0]
            res.append([name] + sorted(account_email[i]))

        return res
'''

