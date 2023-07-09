name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("公司每日增长系数是%d,经过%d天的增长后,股票达到了%.2f" % (stock_price_daily_growth_factor, growth_days, 19.99 * (1.2 ** 7)))
