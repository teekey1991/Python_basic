"""
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値

ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
1つの統計量につき、それ専用の関数を実装すること
実行例
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""
# 合計値
def sum():
    sum_number = 0
    number = 0
    for x in range(0, len(put)):
        number = int(put[x])
        sum_number = sum_number + number
    return sum_number

# 最大値
def max():
    check_number = 0
    #max_number = 0
    for x in range(0, len(put)):
        number = int(put[x])
        if number > check_number:
            max_number = number
                return max_number
# 最小値
#def min():


# 平均値
def ave():
    ave_number = int(sum() / len(put))
    return ave_number


put = input("データを入力してください(スペース区切り) > ").split()
print(f"合計値： {sum()}")
print(f"最大値： {max()}")
#print(f"最低値： {ave()}")
print(f"平均値： {ave()}")
