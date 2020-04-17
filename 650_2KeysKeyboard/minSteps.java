/*
dp[i]表示，通过复制粘贴操作，得到 i 个字符，最少需要几步操作。

如果一个数是素数，那么最少操作就是一开始复制一个，最后一个个粘贴；

如果一个数不是素数，那么最少操作就可以按它的因数分解一下，简化操作。

举个例子，比如12，可以分解为 以下几种情况：

12 = 2*6, 需要操作CPCPPPPP总共8步

12 = 3*4, 需要操作CPPCPPP总共7步

12 = 4*3, 需要操作CPPPCPP总共7步

12 = 6*2, 需要操作CPPPPPCP总共8步

其实可以发现，因子相同的情况下，交换因子相乘的顺序，需要的步骤是一样的。所以我们可以简化一下分解的步骤，只需要找到小于sqrt(n)的因子即可。

假设找到的因子是 j ，那么需要的最小步骤就是 dp[j] + dp[i/j]，其中，dp[j]表示需要多少步生成这个因子，dp[i/j]表示需要多少步基于这个因子得到 i。

将 i / j 个字符看作一个，那么需要的最少的操作步骤则是 i。
*/
class Solution {
    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        int r = (int)Math.sqrt(n);
        for(int i = 2; i <= n; ++i) {
            dp[i] = i;
            for(int j = 2; j <= r; ++j) {
                if(i % j == 0) {
                    dp[i] = dp[j] + dp[i / j];
                    break;
                }
            }
        }

        return dp[n];
    }
}