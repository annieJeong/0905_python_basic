"""
저녁 식대 계산 모듈
"""

dinner_fee = 150.32
tax_rate = 0.0675
tip_rate = 0.15

total_fee = (dinner_fee * tax_rate) + dinner_fee + (dinner_fee * tip_rate)

print(total_fee)