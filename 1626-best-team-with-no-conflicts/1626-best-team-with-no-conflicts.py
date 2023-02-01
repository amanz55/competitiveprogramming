class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        num_players = len(scores)
        age_score = list(zip(ages, scores))
        
        age_score.sort()
        dp = [0 for i in range(num_players)]
        dp[0] = age_score[0][1]
        
        ans = dp[0]
        for i in range(1, num_players):
            dp[i] = dp[i] + age_score[i][1]
            for j in range(i):
                same_age = (age_score[i][0] == age_score[j][0])
                has_conflict = (age_score[i][1] < age_score[j][1])
                
                if same_age or not has_conflict:
                    dp[i] = max(dp[j] + age_score[i][1], dp[i])
                    
            ans = max(dp[i], ans)
        
        return ans