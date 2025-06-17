## 01背包问题  leetcode 494 目标和问题

### **常见形式**：

> $capacity$: 背包容量 \
$w[i]$: 第 $i$ 个物品的体积 \
$c[i]$: 第 $i$ 个物品的价值 \
每种物品只能选择一次

- 至多装capacity，求方案数/最大价值和
- 恰好装capacity，求方案数/最大价值和/最小价值和
- 至少装capacity，求方案数/最小价值和

**至多装capacity，求最大价值和**

最大价值和：`dfs[i, c]=max(dfs[i-1, c], dfs[i-1, c-w[i]] + v[i])`

边界条件：`dfs[i<0, c]=0`

**恰好装capacity，求方案数**

最大价值和：`dfs[i, c]=dfs[i-1, c] + dfs[i-1, c-w[i]]`

边界条件：`dfs[i<0, c！=0]=0，dfs[i<0, c==0]=1`

## 完全背包问题  leetcode 322 零钱兑换

### **常见形式**：

> $capacity$: 背包容量 \
$w[i]$: 第 $i$ 个物品的体积 \
$c[i]$: 第 $i$ 个物品的价值 \
每种物品可以选择无数次

- 至多装capacity，求方案数/最大价值和
- 恰好装capacity，求方案数/最大价值和/最小价值和
- 至少装capacity，求方案数/最小价值和

**至多装capacity，求最大价值和**

最大价值和：`dfs[i, c]=max(dfs[i-1, c], dfs[i, c-w[i]] + v[i])`

边界条件：`dfs[i<0, c]=0`

**恰好装capacity，求方案数**

最大价值和：`dfs[i, c]=dfs[i-1, c] + dfs[i, c-w[i]]`

边界条件：`dfs[i<0, c！=0]=0，dfs[i<0, c==0]=1`