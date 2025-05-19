import matplotlib.pyplot as plt

# データ（人数と確率）
people = list(range(19))
probabilities = [
    3.8147E-06, 6.86646E-05, 0.000583649, 0.003112793, 0.011672974,
    0.032684326, 0.07081604, 0.121398926, 0.166923523, 0.185470581,
    0.166923523, 0.121398926, 0.07081604, 0.032684326, 0.011672974,
    0.003112793, 0.000583649, 6.86646E-05, 3.8147E-06
]

# ヒストグラムの作成
plt.figure(figsize=(10, 6))
plt.bar(people, probabilities, color='skyblue', edgecolor='black')
plt.xlabel('右耳が聞き耳の人数')
plt.ylabel('確率')
plt.title('右耳が聞き耳の人数の確率分布')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(people)
plt.tight_layout()
plt.show()