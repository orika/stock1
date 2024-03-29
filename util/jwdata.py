import tushare as ts
import pandas as pd
import datetime
import util.JWDataFromTushare as jdt
import util.JWDataFromDB as jdd

import warnings
warnings.filterwarnings("ignore")

ts.set_token('d3fdbde82434cd6d7897550852136449f9fcba912e3eacb47b004600')
pro = ts.pro_api()

### 使用DB 数据源
use_db = True

def get_hs300_codes():
    codes = ['000001.SZ', '000002.SZ', '000063.SZ', '000069.SZ', '000100.SZ', '000157.SZ', '000333.SZ', '000338.SZ',
             '000402.SZ', '000408.SZ', '000413.SZ', '000415.SZ', '000423.SZ', '000425.SZ', '000538.SZ', '000553.SZ',
             '000568.SZ', '000596.SZ', '000625.SZ', '000627.SZ', '000629.SZ', '000630.SZ', '000651.SZ', '000656.SZ',
             '000661.SZ', '000671.SZ', '000703.SZ', '000709.SZ', '000725.SZ', '000728.SZ', '000768.SZ', '000776.SZ',
             '000783.SZ', '000786.SZ', '000858.SZ', '000876.SZ', '000895.SZ', '000898.SZ', '000938.SZ', '000961.SZ',
             '000963.SZ', '001979.SZ', '002007.SZ', '002008.SZ', '002010.SZ', '002024.SZ', '002027.SZ', '002032.SZ',
             '002044.SZ', '002050.SZ', '002065.SZ', '002081.SZ', '002120.SZ', '002142.SZ', '002146.SZ', '002153.SZ',
             '002179.SZ', '002202.SZ', '002230.SZ', '002236.SZ', '002241.SZ', '002252.SZ', '002271.SZ', '002294.SZ',
             '002304.SZ', '002310.SZ', '002311.SZ', '002352.SZ', '002410.SZ', '002411.SZ', '002415.SZ', '002422.SZ',
             '002456.SZ', '002460.SZ', '002466.SZ', '002468.SZ', '002475.SZ', '002493.SZ', '002508.SZ', '002555.SZ',
             '002558.SZ', '002594.SZ', '002601.SZ', '002602.SZ', '002624.SZ', '002625.SZ', '002673.SZ', '002714.SZ',
             '002736.SZ', '002739.SZ', '002773.SZ', '002925.SZ', '002938.SZ', '002939.SZ', '002945.SZ', '300003.SZ',
             '300015.SZ', '300017.SZ', '300024.SZ', '300033.SZ', '300059.SZ', '300070.SZ', '300072.SZ', '300122.SZ',
             '300124.SZ', '300136.SZ', '300142.SZ', '300144.SZ', '300251.SZ', '300296.SZ', '300408.SZ', '300413.SZ',
             '300433.SZ', '300498.SZ', '600000.SH', '600004.SH', '600009.SH', '600010.SH', '600011.SH', '600015.SH',
             '600016.SH', '600018.SH', '600019.SH', '600023.SH', '600025.SH', '600027.SH', '600028.SH', '600029.SH',
             '600030.SH', '600031.SH', '600036.SH', '600038.SH', '600048.SH', '600050.SH', '600061.SH', '600066.SH',
             '600068.SH', '600085.SH', '600089.SH', '600100.SH', '600104.SH', '600109.SH', '600111.SH', '600115.SH',
             '600118.SH', '600153.SH', '600170.SH', '600176.SH', '600177.SH', '600188.SH', '600196.SH', '600208.SH',
             '600219.SH', '600221.SH', '600233.SH', '600271.SH', '600276.SH', '600297.SH', '600299.SH', '600309.SH',
             '600332.SH', '600339.SH', '600340.SH', '600346.SH', '600352.SH', '600362.SH', '600369.SH', '600372.SH',
             '600383.SH', '600390.SH', '600398.SH', '600406.SH', '600415.SH', '600436.SH', '600438.SH', '600482.SH',
             '600487.SH', '600489.SH', '600498.SH', '600516.SH', '600519.SH', '600522.SH', '600535.SH', '600547.SH',
             '600566.SH', '600570.SH', '600583.SH', '600585.SH', '600588.SH', '600606.SH', '600637.SH', '600660.SH',
             '600663.SH', '600674.SH', '600688.SH', '600690.SH', '600703.SH', '600704.SH', '600705.SH', '600733.SH',
             '600741.SH', '600760.SH', '600795.SH', '600809.SH', '600816.SH', '600837.SH', '600867.SH', '600886.SH',
             '600887.SH', '600893.SH', '600900.SH', '600919.SH', '600926.SH', '600958.SH', '600977.SH', '600998.SH',
             '600999.SH', '601006.SH', '601009.SH', '601012.SH', '601018.SH', '601021.SH', '601066.SH', '601088.SH',
             '601108.SH', '601111.SH', '601117.SH', '601138.SH', '601155.SH', '601162.SH', '601166.SH', '601169.SH',
             '601186.SH', '601198.SH', '601211.SH', '601212.SH', '601216.SH', '601225.SH', '601228.SH', '601229.SH',
             '601238.SH', '601288.SH', '601298.SH', '601318.SH', '601319.SH', '601328.SH', '601336.SH', '601360.SH',
             '601377.SH', '601390.SH', '601398.SH', '601555.SH', '601577.SH', '601600.SH', '601601.SH', '601607.SH',
             '601618.SH', '601628.SH', '601633.SH', '601668.SH', '601669.SH', '601688.SH', '601727.SH', '601766.SH',
             '601788.SH', '601800.SH', '601808.SH', '601818.SH', '601828.SH', '601838.SH', '601857.SH', '601877.SH',
             '601878.SH', '601881.SH', '601888.SH', '601898.SH', '601899.SH', '601901.SH', '601919.SH', '601933.SH',
             '601939.SH', '601985.SH', '601988.SH', '601989.SH', '601992.SH', '601997.SH', '601998.SH', '603019.SH',
             '603156.SH', '603160.SH', '603259.SH', '603260.SH', '603288.SH', '603799.SH', '603833.SH', '603858.SH',
             '603986.SH', '603993.SH']

    return codes

# 获取交易日
def get_cal(date_seq_start, date_seq_end):

    # 获取交易日
    df = pro.trade_cal(exchange_id='', is_open=1, start_date=date_seq_start, end_date=date_seq_end)
    date_seq = list(df.iloc[:, 1])
    # date_seq = [(datetime.datetime.strptime(x, "%Y%m%d")).strftime('%Y-%m-%d') for x in date_seq]
    return date_seq

# 获取单只股票的日线价格
def get_price(code, start, end):
    return jdd.get_price(code, start, end) if use_db else jdt.get_price(code, start, end)

# 获取价格
def get_price_panel(codes, start, end):
    open_data = {}
    close_data = {}
    low_data = {}
    high_data = {}
    prev_close_data = {}
    # 成交量
    volume_data = {}
    # 成交额
    turnover_data = {}

    for code in codes:
        # df = ts.pro_bar(ts_code=code, adj='qfq', start_date=start, end_date=end)
        # # 设置索引
        # df.set_index('trade_date', inplace=True)
        # # 按照日期顺序排序
        # price = df.sort_values(by='trade_date', ascending=True)

        price = get_price(code, start, end)

        open_data[code] = price['open']
        close_data[code] = price['close']
        low_data[code] = price['low']
        high_data[code] = price['high']
        prev_close_data[code] = price['pre_close']
        volume_data[code] = price['vol']
        turnover_data[code] = price['amount']

    open_df = pd.DataFrame(open_data)
    close_df = pd.DataFrame(close_data)
    low_df = pd.DataFrame(low_data)
    high_df = pd.DataFrame(high_data)
    prev_close_df = pd.DataFrame(prev_close_data)
    volume_df = pd.DataFrame(volume_data)
    turnover_df = pd.DataFrame(turnover_data)

    # 创建panel
    panel_data = {'open': open_df, 'close': close_df, 'low': low_df, 'high':high_df, 'prev_close':prev_close_df, 'volume':volume_df, 'turnover':turnover_df}
    pl = pd.Panel(panel_data)

    return pl

def getHS300(start=None, end=None):
    start = (datetime.datetime.strptime(start, "%Y%m%d")).strftime('%Y-%m-%d')
    end = (datetime.datetime.strptime(end, "%Y%m%d")).strftime('%Y-%m-%d')
    df = ts.get_hist_data(code='hs300', start=start, end=end)

    df.sort_index(inplace=True, ascending=True)

    return df

if __name__ == '__main__':




    start = '20190715'
    end = '20190726'

    d = getHS300(start, end) # 获取沪深300指数k线数据

    # pl = get_price_panel(['000001.SZ', '000002.SZ', '000020.SZ', '000505.SZ'], start, end)


    pl = get_price_panel(['000505.SZ'], start, end)

    print('open')
    print(pl['open', :, :])

    print('close')
    print(pl['close', :, :])

    print('low')
    print(pl['low', :, :])


    print('high')
    print(pl['high', :, :])


    print('volume')
    print(pl['volume', :, :])

    print('prev_close')
    print(pl['prev_close', :, :])


    print('turnover')
    print(pl.loc['turnover',:,:].dropna(axis=1,how='any'))