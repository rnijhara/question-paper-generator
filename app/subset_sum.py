from typing import List

from app.question import Question


class SubsetSum:
    def __init__(self):
        self.dp = None
        self.subsets = None

    def _populate_subsets(self, questions: List[Question], i: int, total: int, subset: List[Question]):
        if i == 0 and total != 0 and self.dp[0][total]:
            subset.append(questions[i])
            self.subsets.append(subset.copy())
            subset.clear()
            return

        if i == 0 and total == 0:
            self.subsets.append(subset.copy())
            subset.clear()
            return

        if self.dp[i - 1][total]:
            new_subset = subset.copy()
            self._populate_subsets(questions, i - 1, total, new_subset)

        if total >= questions[i].marks and self.dp[i - 1][total - questions[i].marks]:
            subset.append(questions[i])
            self._populate_subsets(questions, i - 1, total - questions[i].marks, subset)

    def get_all_subsets(self, questions: List[Question], total: int) -> List[List[Question]]:
        n = len(questions)

        if n == 0 or total < 0:
            return []

        self.dp = [[False for _ in range(total + 1)] for _ in range(n)]
        self.subsets = []
        for i in range(n):
            self.dp[i][0] = True
        if questions[0].marks <= total:
            self.dp[0][questions[0].marks] = True

        for i in range(1, n):
            for j in range(total + 1):
                if questions[i].marks <= j:
                    self.dp[i][j] = self.dp[i - 1][j] or self.dp[i - 1][j - questions[i].marks]
                else:
                    self.dp[i][j] = self.dp[i - 1][j]

        if not self.dp[n - 1][total]:
            return []

        self._populate_subsets(questions, n - 1, total, [])
        return self.subsets
