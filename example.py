import okex.Account_api as Account
import okex.Funding_api as Funding
import okex.Market_api as Market
import okex.Public_api as Public
import okex.Trade_api as Trade
import okex.subAccount_api as SubAccount
import okex.status_api as Status
from time import *
import mailNotification as mail

# 开始时间
startTime = time()

if __name__ == '__main__':
    api_key = "f7cc3592-a88a-4549-a42d-bcfee3129da6"
    secret_key = "33B7EF8B48B82CEEB569CF0EDC92B0C3"
    passphrase = "F11010f1"
    # flag是实盘与模拟盘的切换参数 flag is the key parameter which can help you to change between demo and real trading.
    # flag = '1'  # 模拟盘 demo trading
    flag = '0'  # 实盘 real trading

    # account api
    accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag)
    # 查看账户持仓风险 GET Position_risk
    # result = accountAPI.get_position_risk('SWAP')
    # 查看账户余额  Get Balance
    # result = accountAPI.get_account()
    # 查看持仓信息  Get Positions
    # result = accountAPI.get_positions('SWAP', 'BTC-USDT-SWAP')
    # 账单流水查询（近七天） Get Bills Details (recent 7 days)
    # result = accountAPI.get_bills_detail('FUTURES', 'BTC','cross')
    # 账单流水查询（近三个月） Get Bills Details (recent 3 months)
    # result = accountAPI.get_bills_details('FUTURES', 'BTC','cross')
    # 查看账户配置  Get Account Configuration
    # result = accountAPI.get_account_config()
    # 设置持仓模式  Set Position mode
    # result = accountAPI.get_position_mode('long_short_mode')
    # 设置杠杆倍数  Set Leverage
    # result = accountAPI.set_leverage(instId='BTC-USD-210402', lever='10', mgnMode='cross')
    # 获取最大可交易数量  Get Maximum Tradable Size For Instrument
    # result = accountAPI.get_maximum_trade_size('BTC-USDT-210402', 'cross', 'USDT')
    # 获取最大可用数量  Get Maximum Available Tradable Amount
    # result = accountAPI.get_max_avail_size('BTC-USDT-210402', 'isolated', 'BTC')
    # 调整保证金  Increase/Decrease margint
    # result = accountAPI.Adjustment_margin('BTC-USDT-210409', 'long', 'add', '100')
    # 获取杠杆倍数 Get Leverage
    # result = accountAPI.get_leverage('BTC-USDT-210409', 'isolated')
    # 获取币币逐仓杠杆最大可借  Get the maximum loan of isolated MARGIN
    # result = accountAPI.get_max_load('BTC-USDT', 'cross', 'BTC')
    # 获取当前账户交易手续费费率  Get Fee Rates
    # result = accountAPI.get_fee_rates('FUTURES', '', category='1')
    # 获取计息记录  Get interest-accrued
    # result = accountAPI.get_interest_accrued('BTC-USDT', 'BTC', 'isolated', '', '', '10')
    # 获取用户当前杠杆借币利率 Get Interest-accrued
    # result = accountAPI.get_interest_rate()
    # 期权希腊字母PA / BS切换  Set Greeks (PA/BS)
    # result = accountAPI.set_greeks('BS')
    # 查看账户最大可转余额  Get Maximum Withdrawals
    # result = accountAPI.get_max_withdrawal('')

    # funding api
    fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag)
    # 获取充值地址信息  Get Deposit Address
    # result = fundingAPI.get_deposit_address('')
    # 获取资金账户余额信息  Get Balance
    # result = fundingAPI.get_balances('BTC')
    # 资金划转  Funds Transfer
    # result = fundingAPI.funds_transfer(ccy='', amt='', type='1', froms="", to="",subAcct='')
    # 提币  Withdrawal
    # result = fundingAPI.coin_withdraw('usdt', '2', '3', '', '', '0')
    # 充值记录  Get Deposit History
    # result = fundingAPI.get_deposit_history()
    # 提币记录  Get Withdrawal History
    # result = fundingAPI.get_withdrawal_history()
    # 获取币种列表  Get Currencies
    # result = fundingAPI.get_currency()
    # 余币宝申购/赎回  PiggyBank Purchase/Redemption
    # result = fundingAPI.purchase_redempt('BTC', '1', 'purchase')
    # 资金流水查询  Asset Bills Details
    # result = fundingAPI.get_bills()

    # market api
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # 获取所有产品行情信息  Get Tickers
    # result = marketAPI.get_tickers('SPOT')
    # 获取单个产品行情信息  Get Ticker
    # result = marketAPI.get_ticker('BTC-USDT-SWAP')
    # 获取指数行情  Get Index Tickers
    # result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # 获取产品深度  Get Order Book
    # result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # 获取所有交易产品K线数据  Get Candlesticks
    # result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # 获取交易产品历史K线数据（仅主流币实盘数据）  Get Candlesticks History（top currencies in real-trading only）
    # result = marketAPI.get_history_candlesticks('BTC-USDT')
    # 获取指数K线数据  Get Index Candlesticks
    # result = marketAPI.get_index_candlesticks('BTC-USDT')
    # 获取标记价格K线数据  Get Mark Price Candlesticks
    # result = marketAPI.get_markprice_candlesticks('BTC-USDT')
    # 获取交易产品公共成交数据  Get Trades
    # result = marketAPI.get_trades('BTC-USDT', '400')
    # 获取平台24小时成交总量  Get Platform 24 Volume
    # result = marketAPI.get_volume()
    # Oracle 上链交易数据 GET Oracle
    # result = marketAPI.get_oracle()

    # public api
    publicAPI = Public.PublicAPI(api_key, secret_key, passphrase, False, flag)
    # 获取交易产品基础信息  Get instrument
    # result = publicAPI.get_instruments('FUTURES', 'BTC-USDT')
    # 获取交割和行权记录  Get Delivery/Exercise History
    # result = publicAPI.get_deliver_history('FUTURES', 'BTC-USD')
    # 获取持仓总量  Get Open Interest
    # result = publicAPI.get_open_interest('SWAP')
    # 获取永续合约当前资金费率  Get Funding Rate
    # result = publicAPI.get_funding_rate('BTC-USD-SWAP')
    # 获取永续合约历史资金费率  Get Funding Rate History
    # result = publicAPI.funding_rate_history('BTC-USD-SWAP')
    # 获取限价  Get Limit Price
    # result = publicAPI.get_price_limit('BTC-USD-210402')
    # 获取期权定价  Get Option Market Data
    # result = publicAPI.get_opt_summary('BTC-USD')
    # 获取预估交割/行权价格  Get Estimated Delivery/Excercise Price
    # result = publicAPI.get_estimated_price('ETH-USD-210326')
    # 获取免息额度和币种折算率  Get Discount Rate And Interest-Free Quota
    # result = publicAPI.discount_interest_free_quota('')
    # 获取系统时间  Get System Time
    # result = publicAPI.get_system_time()
    # 获取平台公共爆仓单信息  Get Liquidation Orders
    # result = publicAPI.get_liquidation_orders('FUTURES', uly='BTC-USDT', alias='next_quarter', state='filled')
    # 获取标记价格  Get Mark Price
    # result = publicAPI.get_mark_price('FUTURES')
    # 获取合约衍生品仓位档位 Get Tier
    # result = publicAPI.get_tier(instType='MARGIN', instId='BTC-USDT', tdMode='cross')

    # trade api
    tradeAPI = Trade.TradeAPI(api_key, secret_key, passphrase, False, flag)
    # 下单  Place Order
    # result = tradeAPI.place_order(instId='BTC-USDT-210326', tdMode='cross', side='sell', posSide='short',
    #                               ordType='market', sz='100')
    # 批量下单  Place Multiple Orders
    # result = tradeAPI.place_multiple_orders([
    #     {'instId': 'BTC-USD-210402', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17400',
    #      'posSide': 'long',
    #      'clOrdId': 'a12344', 'tag': 'test1210'},
    #     {'instId': 'BTC-USD-210409', 'tdMode': 'isolated', 'side': 'buy', 'ordType': 'limit', 'sz': '1', 'px': '17359',
    #      'posSide': 'long',
    #      'clOrdId': 'a12344444', 'tag': 'test1211'}
    # ])

    # 撤单  Cancel Order
    # result = tradeAPI.cancel_order('BTC-USD-201225', '257164323454332928')
    # 批量撤单  Cancel Multiple Orders
    # result = tradeAPI.cancel_multiple_orders([
    #     {"instId": "BTC-USD-210402", "ordId": "297389358169071616"},
    #     {"instId": "BTC-USD-210409", "ordId": "297389358169071617"}
    # ])

    # 修改订单  Amend Order
    # result = tradeAPI.amend_order()
    # 批量修改订单  Amend Multiple Orders
    # result = tradeAPI.amend_multiple_orders(
    #     [{'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616434384896', 'newPx': '17880'},
    #      {'instId': 'BTC-USD-201225', 'cxlOnFail': 'false', 'ordId': '257551616652488704', 'newPx': '17882'}
    #      ])

    # 市价仓位全平  Close Positions
    # result = tradeAPI.close_positions('BTC-USDT-210409', 'isolated', 'long', '')
    # 获取订单信息  Get Order Details
    # result = tradeAPI.get_orders('BTC-USD-201225', '257173039968825345')
    # 获取未成交订单列表  Get Order List
    # result = tradeAPI.get_order_list()
    # 获取历史订单记录（近七天） Get Order History (last 7 days）
    # result = tradeAPI.get_orders_history('FUTURES')
    # 获取历史订单记录（近三个月） Get Order History (last 3 months)
    # result = tradeAPI.orders_history_archive('FUTURES')
    # 获取成交明细  Get Transaction Details
    # result = tradeAPI.get_fills()
    # 策略委托下单  Place Algo Order
    # result = tradeAPI.place_algo_order('BTC-USDT-210409', 'isolated', 'buy', ordType='conditional', sz='100',posSide='long', tpTriggerPx='60000', tpOrdPx='59999')
    # 撤销策略委托订单  Cancel Algo Order
    # result = tradeAPI.cancel_algo_order([{'algoId': '297394002194735104', 'instId': 'BTC-USDT-210409'}])
    # 获取未完成策略委托单列表  Get Algo Order List
    # result = tradeAPI.order_algos_list('conditional', instType='FUTURES')
    # 获取历史策略委托单列表  Get Algo Order History
    # result = tradeAPI.order_algos_history('conditional', 'canceled', instType='FUTURES')

    # 子账户API subAccount
    subAccountAPI = SubAccount.SubAccountAPI(api_key, secret_key, passphrase, False, flag)
    # 查询子账户的交易账户余额(适用于母账户) Query detailed balance info of Trading Account of a sub-account via the master account
    # result = subAccountAPI.balances(subAcct='')
    # 查询子账户转账记录(仅适用于母账户) History of sub-account transfer(applies to master accounts only)
    # result = subAccountAPI.bills()
    # 删除子账户APIKey(仅适用于母账户) Delete the APIkey of sub-accounts (applies to master accounts only)
    # result = subAccountAPI.delete(pwd='', subAcct='', apiKey='')
    # 重置子账户的APIKey(仅适用于母账户) Reset the APIkey of a sub-account(applies to master accounts only)
    # result = subAccountAPI.reset(pwd='', subAcct='', label='', apiKey='', perm='')
    # 创建子账户的APIKey(仅适用于母账户) Create an APIkey for a sub-account(applies to master accounts only)
    # result = subAccountAPI.create(pwd='123456', subAcct='', label='', Passphrase='')
    # 查看子账户列表(仅适用于母账户) View sub-account list(applies to master accounts only)
    # result = subAccountAPI.view_list()
    # 母账户控制子账户与子账户之间划转（仅适用于母账户）manage the transfers between sub-accounts(applies to master accounts only)
    # result = subAccountAPI.control_transfer(ccy='', amt='', froms='', to='', fromSubAccount='', toSubAccount='')

    # 系统状态API(仅适用于实盘) system status
    Status = Status.StatusAPI(api_key, secret_key, passphrase, False, flag)
    # 查看系统的升级状态
    # result = Status.status()

    # print(json.dumps(result))





    # 设置品种
    currencyType = 'BTC-USDT-SWAP'
    print('交易对: %s ' % currencyType)

    # 设置取几位小数
    setDecimal = 3

    #设置目前杠杆倍数
    lever = 75

    # 设置阶段止盈最少收益比例
    leastProportion = 0.1

    #获取市场信息
    marketInfo = marketAPI.get_ticker(currencyType)

    # 最新价
    lastPrice = round(float(marketInfo["data"][0]['last']),setDecimal)
    print('最新价: %s' % str(lastPrice))

    # 获取持仓信息
    posInfo = accountAPI.get_positions('SWAP', currencyType)
    print(posInfo['data'])


    # #检查是否有持仓
    # if len(posInfo['data']) == 0:
    # # if posInfo['data'][0]['pos'] == '0'
    #     # 无仓位
    #     print('无仓位')
    # else:
    #     # 有仓位
    #     # 持仓方向
    #     posSide = posInfo['data'][0]['posSide']
    #     if posSide == 'long':
    #         print('持仓方向: 多')
    #     else:
    #         print('持仓方向: 空')
    #
    #     # 持仓均价
    #     averagePrice = round(float(posInfo['data'][0]['avgPx']), setDecimal)
    #     print('持仓均价: %s ' % str(averagePrice))
    #
    #     # 价差
    #     differenceValue = round(lastPrice - averagePrice,setDecimal)
    #     print('价差: %s ' % str(differenceValue))
    #
    #     # 持仓量
    #     openInterest = int(posInfo['data'][0]['pos'])
    #     print('持仓量: %s ' % str(openInterest))
    #
    #     # 收益
    #     profit = round(differenceValue * openInterest,setDecimal)
    #     if posSide == 'long':
    #         print('收益: %s ' % str(profit))
    #     else:
    #         profit = - profit
    #         print('收益: %s ' % str(profit))
    #
    #     # 价距
    #     priceDistance = abs(round(differenceValue / openInterest,setDecimal))
    #     print('价距: %s ' % str(priceDistance))
    #
    #     # 判断多空盈利情况并设置阶梯止盈
    #     if posSide == 'long':
    #         if profit > 0:
    #             print('做多且盈利')
    #             #阶梯设置止盈
    #             for i in range(openInterest):
    #                 price = lastPrice - priceDistance * (i + 1)
    #                 tradeAPI.place_algo_order(currencyType, 'cross', 'sell', ordType='trigger', sz='1', posSide='long', triggerPx=price, orderPx='-1')
    #         elif profit == 0:
    #             print('持平')
    #         else:
    #             print('做多但亏损')
    #     else:
    #         if profit > 0:
    #             print('做空且盈利')
    #             # 阶梯设置止盈
    #             for i in range(openInterest):
    #                  price = lastPrice + priceDistance * (i + 1)
    #                  tradeResult = tradeAPI.place_algo_order(currencyType, 'cross', 'buy', ordType='trigger', sz='1', posSide='short', triggerPx=price, orderPx='-1')
    #                  print(tradeResult)
    #         elif profit == 0:
    #             print('持平')
    #         else:
    #             print('做空但亏损')

    # 计时器每n秒执行一次
    # def timer(n):
    #     while True:
    #         param = accountAPI.get_positions('SWAP', currencyType)
    #         lastPrice = round(float(param["data"][0]['last']), 3)
    #         print('最新价: %s ' % str(lastPrice))
    #         time.sleep(n)

    # 计时器
    # timer(3)
    # 邮件通知
    # mail.mailNotification(3)

    # 结束时间
    endTime = time()
    # 执行时长
    exeDuration = round(endTime - startTime,setDecimal)
    print('执行时长: %s s' % exeDuration)