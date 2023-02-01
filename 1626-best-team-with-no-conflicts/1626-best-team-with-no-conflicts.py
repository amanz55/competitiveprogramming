class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        num_players = len(scores)
        age_score = list(zip(ages, scores))
        age_score.sort()
        
        dp = [0 for i in range(num_players)]
        dp[-1] = age_score[-1][1]
        for i in range(num_players - 2, -1, -1):
            temp_max = 0
            for j in range(i + 1, num_players):
                if age_score[j][1] >= age_score[i][1]:
                    temp_max = max(temp_max, dp[j])
            dp[i] = age_score[i][1] + temp_max
        return max(dp)