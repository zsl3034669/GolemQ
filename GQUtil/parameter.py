#
# The MIT License (MIT)
#
# Copyright (c) 2018-2020 azai/Rgveda/GolemQuant
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
"""
这里定义的是一些常用常量
"""
from GolemQ.GQUtil.const import _const
import sys

class AKA(_const):
    """
    趋势状态常量，专有名称指标，定义成常量可以避免直接打字符串造成的拼写错误。
    """

    # 蜡烛线指标
    CODE = 'code'
    NAME = 'name'
    OPEN = 'open'
    HIGH = 'high'
    LOW = 'low'
    CLOSE = 'close'
    VOLUME = 'volume'
    VOL = 'vol'
    DATETIME = 'datetime'
    LAST_CLOSE = 'last_close'
    PRICE = 'price'

    SYSTEM_NAME = 'GolemQuant'

    # 趋势指标名称
    MACD_CROSS = 'MACD_CROSS'

    MACD_TREND = 'MACD_TREND'
    MACD_CROSS_ZERO = 'MACD_CROSS_ZERO'
    BOLL_CROSS = 'BOLL_CROSS'
    KDJ_CROSS = 'KDJ_CROSS'
    KDJ_TP_CROSS = 'KDJ_TP_CROSS'

    MA_CROSS = 'MA_CROSS'
    MA30_CROSS = 'MA30_CROSS'

    PRE_MA_CROSS = 'PRE_MA_CROSS'
    PRE_CROSS_JX = 'PRE_CROSS_JX'
    PRE_CROSS_SX = 'PRE_CROSS_SX'

    MAX_FACTOR_CROSS = 'MAX_FACTOR_CROSS'
    MAX_FACTOR_CROSS_JX = 'MAX_FACTOR_CROSS_JX'
    MAX_FACTOR_CROSS_SX = 'MAX_FACTOR_CROSS_SX'

    # 趋势
    TREND = 'TREND'
    TREND_STATUS = 'TREND_STATUS'
    STAGE = 'STAGE'
    STATE = 'STATE'
    STATES = 'STATES'
    METADATA = 'METADATA'

    UPRISING = 'UPRISING' # codex066_buy_model_combine_on_uprising_with_macd_high_tide
    BLACKSWAN = 'BLACKSWAN' #
    SHADOW = 'SHADOW'
    COMBINE = 'COMBINE'
    UNKNOWN = 'UNKOWN'
    END_DT = 'END'
    START_DT = 'START'
    HYPER = 'HYPER'
    REQUST_PRICE = 'REQUST_PRICE'
    REQUST_TIMESTAMP = 'REQUST_TIMESTAMP'
    PROFIT = 'profit'
    FINAL_PROFIT = 'FIN_PROF'
    MAX_PROFIT = 'MAX_PROF'
    MAX_LOSS = 'MAX_LOSS'
    MAX_DRAWDOWN = 'MAX_DRDN'
    DUAL_CROSS_JX = 'DUAL_CROSS_JX'
    DUAL_CROSS_SX = 'DUAL_CROSS_SX'
    PEAK_POINT = 'PEAK_POINT'
    PEAK_POINT_MAX_FACTOR = 'PEAK_POINT_MAX_FACTOR'

    REMARK = "REMARK"

    SUB_ROUTE = 'SUB_ROUTE'
    MAIN_ROUTE = 'MAIN_ROUTE'
    FAST_ESCAPE = "FAST_ESCAPE"

    #def __setattr__(self, name, value):
    #    raise Exception(u'Const Class can\'t allow to change property\'
    #    value.')
    #    return super().__setattr__(name, value)
class TREND_STATUS(_const):
    """
    趋势状态常量，专有名称指标，定义成常量可以避免直接打字符串造成的拼写错误。
    """
    T_BAND = 'T_BAND' 
    WAVELET = 'WAVELET' 
    UNKNOWN = 'UNKOWN'

    # 状态
    LOWER_SETTLE_PRICE = 'LO_SETTLE'
    BOOTSTRAP_I = 'BOOTSTRAP' # BOOTSTRAP PHASE I
    BOOTSTRAP_I_PRNT = 'BST1_PRNT'
    BOOTSTRAP_COMBO = 'BST_COMBO' # 混合 BOOTSTRAP形态
    BOOTSTRAP_COMBO_MINOR = 'BST_COMBO_MINOR' # 小时间周期的BOOTSTRAP形态
    BOOTSTRAP_GROUND_ZERO = 'BST_GND_O' # BOOTSTRAP GROUND ZERO 形态
    BOOTSTRAP_GROUND_ZERO_MINOR = 'BST_GND_O_MINOR' # BOOTSTRAP GROUND ZERO 形态
    BOOTSTRAP_GROUND_ZERO_CANDIDATE = 'BST_GND_O_CAN' # BOOTSTRAP GROUND ZERO CANDIDATE
    BOOTSTRAP_I_CANDIDATE = 'BTSTRP_CAN' # BOOTSTRAP PHASE I CANDIDATE
    BOOTSTRAP_II = 'BOOTSTRAP2' # BOOTSTRAP PHASE II
    BOOTSTRAP_II_CANDIDATE = 'BTSTRP2_CAN' # BOOTSTRAP PHASE II CANDIDATE
    INTER_ITERATION = 'UP_ITER' # 符合下一级迭代
    UPRISING = 'UPRISING'
    UPRISING_MAJOR = 'UPRISING_MAJOR'
    MAINFEST_UPRISING = 'UPRISING'
    ATR_RAIL = 'ATR_RAIL'
    UPRISING_RAIL = 'UPRISING_RAIL'
    DOWNRISK_RAIL = 'DOWNRISK_RAIL'
    MAINFEST_UPRISING_COEFFICIENT = 'UPRISING_COEFFICIENT'
    PEAK_POINT = 'PEAK_POINT'
    OUT_OF_FUEL = 'OOM'  # OUT OF MANA
    DEADPOOL = 'DEADPOOL' # UR DEAD!  MAN
    CANDIDATE = 'CANDIDATE'
    CANDIDATE_MINOR = 'CANDIDATE_MINOR'
    HYPER_BOOTSTRAP = 'HYP_BOTSRP'
    VOLUME_FLOW_BOOST = 'VOL_FLOW_BOOST'
    VOLUME_FLOW_BOOST_BONUS = 'VOL_FLOW_BOOST_BONUS'
    HYPER_PUNCH = 'PUNCH'
    CLUSTER_GROUP = 'CLT_GRP'
    CLUSTER_GROUP_TOWARDS = 'CLT_GRP_TOWARDS'
    CLUSTER_GROUP_TOWARDS_MINOR = 'CLT_GRP_MINOR'
    CLUSTER_GROUP_TOWARDS_PRNT = 'CLT_GRP_TOWARDS_PRNT'
    CLUSTER_GROUP_TOWARDS_RS = 'CLT_GRP_TOWARDS_RS'

    MACD_CROSS = 'MACD_CRS'

    COMBINE = 'COMBINE'
    NARROW = "NARROW"
    TOP = "TOP"
    BALANCE = "BALANCE"
    BOTTOM = 'BOTTOM'

    POSITION_ONHOLD = 'POS_ONHOLD'
    POSITION = 'POSITION'
    TRIGGER = 'TRIGGER'
    TRIGGER_FADE = 'TRG_FADE'
    POSITION_R5 = 'POS_R5'
    TRIGGER_R5 = 'TRG_R5'
    TRIGGER_RSRS = 'TRG_RSRS'
    POSITION_RSRS = 'POS_RSRS'
    TRIGGER_RPS = 'TRG_RPS'
    POSITION_RPS = 'POS_RPS'
    TRIGGER_BOOTSTRAP_GROUND_ZERO = 'TRIGGER_BST_GND_O' # 小时间周期的RSRS启动
    POSITION_BOOTSTRAP_GROUND_ZERO = 'POS_BST_GND_O'

    FAKE = 'FAKE'
    MISS = 'MISS'

    # 调试标记
    DEBUG = 'DEBUG'
    VERBOSE = 'verbose'

    def __setattr__(self, name, value):
        raise Exception(u'Const Class can\'t allow to change property\' value.')
        return super().__setattr__(name, value)

class FEATURES(_const):
    STRATEGY_TYPE = 'STRATEGY_TYPE'
    STRATEGY_TYPE_PRNT = 'STRATEGY_PRN'

    BOOTSTRAP_ANCHOR = 'BST_ANCHOR'
    BOOTSTRAP_ANCHOR_MINOR = 'BST_ANCHOR_MINOR'
    BOOTSTRAP_ANCHOR_MAJOR = 'BST_ANCHOR_MAJOR'
    BOOTSTRAP_ANCHOR_TIMING_LAG = 'BST_ANCHOR_LAG'

    ZEN_RSRS_TIMING_LAG = 'ZW_RSRS_LAG'
    ZEN_RSRS_TIMING_LAG_MINOR = 'ZW_RSRS_LAG_MINOR'
    ZEN_RSRS_RETURNS = 'ZW_RSRS_RET'
    ZEN_RSRS_SORTINO = 'ZW_RSRS_SORTINO'
    ZEN_RSRS_SORTINO_TIMING_LAG = 'ZW_RSRS_SORTINO_LAG'
    ZEN_RSRS_ANNUAL_RETURNS = 'ZW_RSRS_ANN_RET'
    ZEN_RSRS_MAJOR_TIMING_LAG = 'ZW_RSRS_MAJOR_LAG'
    ZEN_RSRS_SORTINO_R8_MEAN = 'ZW_RSRS_SORTINO_rl_8_mean'
    ZEN_RSRS_SORTINO_R8_MEAN_TIMING_LAG = 'ZW_RSRS_SORTINO_rl_8_mean_LAG'

    BOLL_RAISED_SORTINO = 'BOLL_RAISED_SORTINO'
    BOLL_RAISED_ANNUAL_RETURNS = 'BOLL_RAISED_ANN_RET'
    BOLL_RAISED_SORTINO_R8_MEAN = 'BOLL_RAISED_SORTINO_rl_8_mean'
    BOLL_DRAWDOWN_PEAK_OPEN = 'BOLL_DRWDN_PEAK_OPEN'

    ATR_U_RAIL_TIMING_LAG = 'ATR_U_RAIL_LAG'
    ATR_U_RAIL_TIMING_LAG_MINOR = 'ATR_U_RAIL_LAG_MINOR'
    ATR_L_RAIL_TIMING_LAG = 'ATR_L_RAIL_LAG'
    ATR_L_RAIL_TIMING_LAG_MINOR = 'ATR_L_RAIL_LAG_MINOR'

    ATR_L_BOLL = 'ATR_L_BOLL'
    ATR_L_BOLL_TIMING_LAG = 'ATR_L_BOLL_LAG'

    UPRISING_CHECKPOINT_TIMING_LAG = 'UPRISING_CHKPOINT_LAG'
    UPRISING_RAIL_TIMING_LAG = 'UPRISING_RAIL_LAG'
    UPRISING_RAIL_TIMING_LAG_MINOR = 'UPRISING_RAIL_LAG_MINOR'
    UPRISING_RAIL_SORTINO = 'UPRISING_RAIL_SORTINO'

    DOWNRISK_RAIL_TIMING_LAG = 'DOWNRISK_RAIL_LAG'

    STDAVG_TIMING_LAG = 'STDAVG_LAG'

    PCT_CHANGE_TIMING_LAG = 'PCT_CHG2_LAG'
    PCT_CHANGE_TIMING_LAG_MINOR = 'PCT_CHG2_TIMING_LAG_MINOR'

    ATR_UB_BOLL_TIMING_LAG = 'ATR_U_BOLL_LAG'
    ATR_UB_BOLL_TIMING_LAG_MINOR = 'ATR_U_BOLL_LAG_MINOR'
    ATR_LB_BOLL_TIMING_LAG = 'ATR_L_BOLL_LAG'
    ATR_LB_BOLL_TIMING_LAG_MINOR = 'ATR_L_BOLL_LAG_MINOR'

    ZEN_WAVELET_TIMING_LAG_MINOR = 'ZW_LAG_MINOR'
    ZEN_BOOST_TIMING_LAG_MINOR = 'ZB_LAG_MINOR'

    BEST_IMF1 = 'BEST_IMF1'
    BEST_IMF1_NORM = 'BEST_IMF1_NORM'
    BEST_IMF1_TIMING_LAG = 'BEST_IMF1_LAG'
    BEST_IMF2 = 'BEST_IMF2'
    BEST_IMF2_NORM = 'BEST_IMF2_NORM'
    BEST_IMF2_TIMING_LAG = 'BEST_IMF2_LAG'
    BEST_IMF3 = 'BEST_IMF3'
    BEST_IMF3_NORM = 'BEST_IMF3_NORM'
    BEST_IMF3_TIMING_LAG = 'BEST_IMF3_LAG'
    BEST_IMF4 = 'BEST_IMF4'
    BEST_IMF4_NORM = 'BEST_IMF4_NORM'
    BEST_IMF4_TIMING_LAG = 'BEST_IMF4_LAG'
    BOOST_IMF_TIMING_LAG = 'BOOST_IMF_LAG'

    def __setattr__(self, name, value):
        raise Exception(u'Const Class can\'t allow to change property\' value.')
        return super().__setattr__(name, value)


class INDICATOR_FIELD(_const):

    # 标记处金叉点
    IDX_DATETIME = 0
    IDX_DIF = 1
    IDX_DEA = 2
    IDX_MACD = 3
    IDX_CROSS_JC = 4
    IDX_CROSS_SC = 5
    IDX_DELTA = 6
    IDX_PERCENT = 7
    IDX_MA5 = 8
    IDX_MA10 = 9
    IDX_MA30 = 10
    IDX_RSI = 11
    IDX_RSI_DELTA = 12
    IDX_PEAK_LOW = 13
    IDX_PEAK_HIGH = 14
    
    DATETIME = 'datetime'
    TIMESTAMP = 'timestamp'
    POSITION_BEFORE = 'ORD_BF'
    MASSIVE_TREND = 'MASSIVE_TREND'
    DEADPOOL_BEFORE = 'DEADPOOL_BF'
    COMBO_DENSITY_DEA_RELATIVE = 'COMBO_DEA_RLT'
    BOLL_RAISED_MA30_RELATIVE = 'BOL_RIS_MA30_RLT'
    BOLL_RAISED_MA60_RELATIVE = 'BOL_RIS_MA60_RLT'

    DIF = 'DIF'
    DIF_MAX = 'DIF_MAX'
    DIF_NORM = 'DIF_NORM'
    DEA = 'DEA'
    DEA_MINOR = 'DEA_MINOR'
    DEA_UB = 'DEA_UB'
    DEA_ZERO_TIMING_LAG = 'DEA_O_LAG'
    DEA_ZERO_PRNT = 'DEA_O_PRNT'
    DEA_ZERO_TIMING_LAG_MINOR = 'DEA_O_LAG_MINOR'
    DEA_ZERO_MAJOR_TIMING_LAG = 'DEA_O_MAJOR_LAG'
    DIF_ZERO_TIMING_LAG = 'DIF_O_LAG'
    DIF_ZERO_TIMING_LAG_MINOR = 'DIF_O_LAG_MINOR'
    DIF_ZERO_MAJOR_TIMING_LAG = 'DIF_O_MAJOR_LAG'
    DEA_CROSS_JX_BEFORE = 'DEA_JX_BF'
    DIF_CROSS_JX_BEFORE = 'DIF_JX_BF'
    DEA_CROSS_SX_BEFORE = 'DEA_SX_BF'
    DIF_CROSS_SX_BEFORE = 'DIF_SX_BF'
    DEA_SLOPE = 'DEA_SLOPE'
    DEA_SLOPE_UB = 'DEA_SLOPE_UB'
    DEA_SLOPE_CHANGE = 'DEA_SLOPE_CHG'
    DEA_INTERCEPT = 'DEA_INTCEPT'
    DEA_NORM = 'DEA_NORM'
    MACD = 'MACD'
    MACD_MAX = 'MACD_MAX'
    MACD_CROSS = 'MACD_CRS'
    MACD_TREND_TIMING_LAG = 'MACD_TRD_LAG'
    MACD_ZERO_TIMING_LAG = 'MACD_O_LAG'
    MACD_ZERO_TIMING_LAG_MINOR = 'MACD_O_LAG_MINOR'
    MACD_ZERO_MAJOR_TIMING_LAG = 'MACD_O_MAJOR_LAG'
    DEA_INTERCEPT_TIMING_LAG = 'DEA_INTER_LAG'
    MACD_NORM = 'MACD_NORM'
    MACD_INTERCEPT = 'MACD_INTCEPT'
    MACD_TREND = 'MACD_TRD'
    MACD_DELTA = 'MACD_diff_1T'
    #MACD_DELTA = 'MACD_DELTA'
    MACD_DELTA_NORM = 'MACD_diff_1T_NORM'
    #MACD_DELTA_NORM = 'MACD_DELTA_NORM'
    MACD_CROSS_JX_BEFORE = 'MACD_JX_BF'
    MACD_CROSS_SX_BEFORE = 'MACD_SX_BF'
    NEGATIVE_LOWER_PRICE = 'NEG_LOW_PRC'
    NEGATIVE_LOWER_PRICE_BEFORE = 'NEG_LOW_PRC_BF'
    LOWER_SETTLE_PRICE = 'LO_SET_PRC'
    LOWER_SETTLE_PRICE_BEFORE = 'LO_SET_PRC_BF'
    HIGHER_SETTLE_PRICE = 'HI_SET_PRC'
    HIGHER_SETTLE_PRICE_BEFORE = 'HI_SET_PRC_BF'

    PCT_CHANGE = 'PCT_CHG'
    PCT_CHANGE2 = 'PCT_CHG2'
    MA5 = 'MA5'
    MA5_CROSS = 'MA5_CRS'
    MA5_CROSS_JX_BEFORE = 'MA5_JX_BF'
    MA5_CROSS_SX_BEFORE = 'MA5_SX_BF'

    MA10 = 'MA10'
    MA20 = 'MA20'
    MA30 = 'MA30'
    MA30_CROSS = 'MA30_CRS'
    MA30_SLOPE = 'MA30_SLOPE'
    MA30_SLOPE_CHANGE = 'MA30_SLOPE_CHG'
    MA60 = 'MA60'
    MA60_SLOPE = 'MA60_SLOPE'
    MA90 = 'MA90'
    MA90_CROSS = 'MA90_CRS'
    MA90_SLOPE = 'MA90_SLOPE'
    MA90_RETURNS = 'MA90_RET'
    MA90_RETURNS_P19 = 'MA90_RET_P19'
    MA90_RETURNS_P38 = 'MA90_RET_P38'
    MA90_RETURNS_P50 = 'MA90_RET_P50'
    MA120 = 'MA120'
    MA120_SLOPE = 'MA120_SLOPE'
    MA120_RETURNS = 'MA120_RET'
    MA120_RETURNS_P19 = 'MA120_RET_P19'
    MA120_RETURNS_P38 = 'MA120_RET_P38'
    MA120_RETURNS_P50 = 'MA120_RET_P50'
    TRI_MA_CROSS_JX_BEFORE = 'TRI_MA_JX_BF'
    TRI_MA_CROSS_SX_BEFORE = 'TRI_MA_SX_BF'
    MA_MAX = 'MA_MAX'
    VOL_MA5 = 'VOL_MA5'
    VOL_MA10 = 'VOL_MA10'
    VOL_CROSS = 'VOL_CRS'
    VOL_TREND_TIMING_LAG = 'VOL_TRD_LAG'
    RSI = 'RSI'
    RSI_PRNT = 'RSI_PRN'
    RSI_DELTA = 'RSI_diff_1T'
    #RSI_DELTA = 'RSI_DELTA'
    RSI_CROSS = 'RSI_CRS'
    RSI_TREND_TIMING_LAG = 'RSI_TRD_LAG'
    #RSI_CROSS_JX = 'RSI_JX'
    #RSI_CROSS_SX = 'RSI_SX'
    PEAK_OPEN = 'PEAK_OPEN'
    PEAK_OPEN_MINOR = 'PEAK_OPEN_MINOR'
    PEAK_OPEN_ZSCORE = 'PEAK_OPEN_ZSCORE'
    PEAK_OPEN_TIMING_LAG = 'PEAK_OPEN_LAG'
    PEAK_CLOSE = 'PEAK_CLOSE'
    PEAK_LOW = 'PEAK_LOW'
    PRE_PEAK_LOW = 'PRE_PEAK_LOW'
    PEAK_LOW_BEFORE = 'PEAK_LOW_BF'
    PEAK_LOW_RATIO = 'PEAK_LOW_RATIO'
    PEAK_HIGH = 'PEAK_HIGH'
    PRE_PEAK_HIGH = 'PRE_PEAK_HIGH'
    PEAK_HIGH_BEFORE = 'PEAK_HIGH_BF'
    PEAK_HIGH_RATIO = 'PEAK_HIGH_RATIO'

    KDJ_CROSS = 'KDJ_CRS'
    KDJ_K = 'KDJ_K'
    KDJ_D = 'KDJ_D'
    KDJ_J = 'KDJ_J'
    KDJ_J_DELTA = "KDJ_J_diff_1T"
    #KDJ_J_DELTA = "KDJ_J_DELTA"
    KDJ_TREND_TIMING_LAG = 'KDJ_TRD_LAG'
    #KDJ_CROSS_JX = 'KDJ_JX'
    #KDJ_CROSS_SX = 'KDJ_SX'
    ATR = 'ATR'
    ADX = 'ADX'
    ADXR = "ADXR"
    CCI = "CCI"
    CCI_DELTA = "CCI_diff_1T"
    #CCI_DELTA = "CCI_DELTA"
    BOLL = 'BOLL_MA'
    BOLL_CROSS_JX_BEFORE = 'BOLL_JX_BF'
    BOLL_CROSS_SX_BEFORE = 'BOLL_SX_BF'
    BOLL_CROSS = 'BOLL_CRS'
    BOLL_TREND_TIMING_LAG = 'BOLL_TRD_LAG'
    BOLL_RAISED_TIMING_LAG = 'BOLL_RAISED_LAG'
    BOLL_RAISED_TIMING_LAG_MINOR = 'BOLL_RAISED_LAG_MINOR'
    BOLL_RAISED_PRNT = 'BOLL_RAISED_PRNT'
    BOLL_RAISED_IMPULSE = 'BOLL_RAISED_IMP'
    BOLL_RAISED_MAJOR_TIMING_LAG = 'BOLL_RAISED_MAJOR_LAG'
    BOLL_UB = 'BOLL_UB'
    BOLL_LB = 'BOLL_LB'
    BOLL_CHANNEL = 'BOLL_WIDTH'
    BOLL_MAJOR_CHANNEL = 'BOLL_MAJOR_WIDTH'
    BOLL_CHANNEL_RANK = 'BBW_RANK'
    BOLL_CHANNEL_MA30 = "BBW_MA"
    BOLL_DELTA = "BBW_diff_1T"
    BOLL_DELTA2 = "BBW_diff_2T"
    BOLL_DELTA3 = "BBW_diff_3T"
    BOLL_MAJOR_DELTA = "BBW_MAJOR_diff_1T"
    #BOLL_DELTA = "BBW_DELTA"
    BOLL_CLEARANCE = "BBC"

    BIAS3 = 'BIAS3'
    BIAS3_UB = 'BIAS3_UB'
    BIAS3_ZSCORE = 'BIAS3_ZSCORE'
    BIAS3_CROSS = 'BIAS3_CRS'
    BIAS3_CROSS_MEDIAN = 'BIAS3_CRS_MEDIAN'
    BIAS_TREND_TIMING_LAG = 'BIAS_TRD_LAG'
    BIAS3_TREND_TIMING_LAG = 'BIAS3_TRD_LAG'
    BIAS3_TREND_IMPULSE = 'BIAS3_TRD_IMP'
    BIAS3_CROSS_JX_BEFORE = 'BIAS3_CRS_JX_BF'
    BIAS3_CROSS_SX_BEFORE = 'BIAS3_CRS_SX_BF'
    BIAS3_CROSS_DENSITY = 'BIAS3_CRS_DENSITY'

    ZERO = "ZERO"
    Volume_HMA5 = 'VHMA5'
    Volume_HMA10 = 'VHMA10'
    Volume_HMA5_TIMING_LAG = 'VHMA5_LAG'
    Volume_HMA10_TIMING_LAG = 'VHMA10_LAG'

    MAXFACTOR = "MAXFACTOR"
    MAXFACTOR_CROSS = 'MFT_CRS'
    MAXFACTOR_TREND_TIMING_LAG = 'MFT_TRD_LAG'
    MAXFACTOR_DELTA = "MFT_diff_1T"
    MAXFACTOR_ZSCORE = 'MFT_ZSCORE'
    MAXFACTOR_CROSS_JX = 'MFT_JX_BF'
    MAXFACTOR_CROSS_SX = 'MFT_SX_BF'
    MAXFACTOR_BASELINE = 'MFT_REG_BASE'

    REGRESSION_PRICE = 'LRC_PRICE'
    REGRESSION_SLOPE = 'LRC_SLOPE'
    REGRESSION_INTERCEPT = 'LRC_INTCEPT'
    REGRESSION_SLOPE_UB = 'LRC_SLOPE_UB'
    REGRESSION_DIRECTION = 'LRC_DIR'
    REGRESSION_DIRECTION_NEG = 'REG_DIR_NEG'
    LRC_MA30_TIMING_LAG = 'LRC_MA30_LAG'
    LRC_MA30_IMPULSE = 'LRC_MA30_IMP'
    LRC_MA60_TIMING_LAG = 'LRC_MA60_LAG'
    LRC_MA60_IMPULSE = 'LRC_MA60_IMP'
    LRC_MA30_INTERCEPT = 'LRC_MA30_INTCEPT'
    LRC_MA60_INTERCEPT = 'LRC_MA60_INTCEPT'
    LRC_CLEARANCE = 'LRC_CLR'
    LRC_CLEARANCE_CROSS = 'LRC_CLR_CRS'
    LRC_CLEARANCE_PRNT = 'LRC_CLR_PRNT'
    LRC_CLEARANCE_TIMING_LAG = 'LRC_CLR_LAG'
    LRC_CLEARANCE_SORTINO = 'LRC_CLR_SORTINO'
    LRC_CLEARANCE_IMPULSE = 'LRC_CLR_IMP'

    MA_VOL = 'MA_VOL'
    MA_CHANNEL = 'MA_WIDTH'
    MAPOWER = 'MAPOWER'
    MA5_CLEARANCE = 'MA5_CLR'
    MA10_CLEARANCE = 'MA10_CLR'
    MA20_CLEARANCE = 'MA20_CLR'
    MA30_CLEARANCE = 'MA30_CLR'
    MA90_CLEARANCE = 'MA90_CLR'
    MA90_CLEARANCE_PRNT = 'MA90_CLR_PRN'
    MA90_CLEARANCE_TIMING_LAG = 'MA90_CLR_LAG'
    MA90_CLEARANCE_RETURNS = 'MA90_CLR_RET'
    MA90_CLEARANCE_CROSS = 'MA90_CLR_CROSS'
    MA90_CLEARANCE_CROSS_JX = 'MA90_CLR_CROSS_JX'
    MA90_CLEARANCE_CROSS_SX = 'MA90_CLR_CROSS_SX'
    MA120_CLEARANCE = 'MA120_CLR'
    MA120_CLEARANCE_TIMING_LAG = 'MA120_CLR_LAG'

    CONFIDENCE = 'CONFIDENCE'
    ZEN_WAVELET_CROSS = 'ZW_CROSS'
    ZEN_WAVELET_CROSS_JX_BEFORE = 'ZW_JX_BF'
    ZEN_WAVELET_CROSS_SX_BEFORE = 'ZW_SX_BF'
    ZEN_WAVELET_RATIO = 'ZW_RATIO'
    ZEN_WAVELET_TIMING_LAG = 'ZW_LAG'
    ZEN_BOOST_TIMING_LAG = 'ZB_LAG'
    ZEN_WAVELET_TIMING_LAG_MINOR = 'ZW_LAG_MINOR'
    ZEN_BOOST_TIMING_LAG_MINOR = 'ZB_LAG_MINOR'
    ZEN_WAVELE_RETURNS = 'ZW_RET'
    ZEN_WAVELE_MAJOR_RETURNS = 'ZW_MAJOR_RET'
    ZEN_WAVELET_MINOR_TIMING_LAG = 'ZW_MINOR_LAG'
    ZEN_WAVELET_MAJOR_TIMING_LAG = 'ZW_MAJOR_LAG'
    ZEN_TIDE_MEDIAN = 'ZT_MEDIAN'
    ZEN_TIDE_DENSITY = 'ZT_DENSITY'
    ZEN_TIDE_DENSITY_SMA = 'ZT_DENSITY_SMA'
    ZEN_TIDE_DENSITY_SLOPE = 'ZT_DENSITY_SLP'
    ZEN_TIDE_DENSITY_RETURNS = 'ZT_DENSITY_RET'
    ZEN_TIDE_DENSITY_REGRESSION = 'ZT_DENSITY_REG'
    ZEN_TIDE_FLOW = 'ZT_FLOW'
    ZEN_TIDE_FLOW_JX_BEFORE = 'ZT_FLOW_JX_BF'
    ZEN_TIDE_FLOW_SX_BEFORE = 'ZT_FLOW_SX_BF'
    ZEN_TIDE_CROSS_JX = 'ZT_JX'
    ZEN_TIDE_CROSS_SX = 'ZT_SX'
    ZEN_TIDE_MEDIAN_CROSS_JX = 'ZT_MEDIAN_JX'
    ZEN_TIDE_MEDIAN_CROSS_SX = 'ZT_MEDIAN_SX'
    
    MA30_CROSS_JX_BEFORE = 'MA30_JX_BF'
    MA30_CROSS_SX_BEFORE = 'MA30_SX_BF'

    MA90_TP_CROSS = 'MA90_TP_CROSS'
    MA90_TP_CROSS_JX_BEFORE = 'MA90_TP_JX_BF'
    MA90_TP_CROSS_SX_BEFORE = 'MA90_TP_SX_BF'
    MA90_CROSS_JX_BEFORE = 'MA90_JX_BF'
    MA90_CROSS_SX_BEFORE = 'MA90_SX_BF'
    MA30_TREND_TIMING_LAG = 'MA30_TRD_LAG'
    MA30_CROSS_JX = 'MA30_CROSS_JX'
    MA30_CROSS_SX = 'MA30_CROSS_SX'
    MA30_CROSS_TIDE_JX = 'MA30_CRS_TIDE_JX'
    MA30_CROSS_TIDE_SX = 'MA30_CRS_TIDE_SX'
    MA30_TIDE_MEDIAN_CROSS_JX = 'MA30_CRS_MEDIAN_JX'
    MA30_TIDE_MEDIAN_CROSS_SX = 'MA30_CRS_MEDIAN_SX'
    MA30_CROSS_DENSITY = 'MA30_CRS_DENSITY'

    ADXm_Trend = 'ADXm_TRD'
    ADXm_Trend_TIMING_LAG = 'ADXm_TRD_LAG'
    ADXm_Trend_RETURNS = 'ADXm_TRD_RET'
    ADXm_Trend_CROSS_JX = 'ADXm_TRD_JX'
    ADXm_Trend_CROSS_SX = 'ADXm_TRD_SX'
    ADXm_Trend_TIDE_CROSS_JX = 'ADXm_TRD_TIDE_JX'
    ADXm_Trend_TIDE_CROSS_SX = 'ADXm_TRD_TIDE_SX'

    ATR_SuperTrend = 'ATR_SUPTRD'
    ATR_SuperTrend_TIMING_LAG = 'ATR_SUPTRD_LAG'
    ATR_SuperTrend_CROSS_JX = 'ATR_SUPTRD_JX'
    ATR_SuperTrend_CROSS_SX = 'ATR_SUPTRD_SX'
    ATR_SuperTrend_MEDIAN = 'ATR_SUPTRD_MEDIAN'
    ATR_SuperTrend_TIDE_CROSS_JX = 'ATR_SUPTRD_TIDE_JX'
    ATR_SuperTrend_TIDE_CROSS_SX = 'ATR_SUPTRD_TIDE_SX'
    ATR_SuperTrend_MEDIAN_CROSS_JX = 'ATR_SUPTRD_MEDIAN_JX'
    ATR_SuperTrend_MEDIAN_CROSS_SX = 'ATR_SUPTRD_MEDIAN_SX'
    ATR_SuperTrend_DENSITY = 'ATR_SUPTRD_DENSITY'

    ATR_Stopline = 'ATR_Stopline'
    ATR_Stopline_TIMING_LAG = 'ATR_Stopline_LAG'
    ATR_Stopline_RETURNS = 'ATR_Stopline_RET'
    ATR_Stopline_CROSS_JX = 'ATR_Stopline_JX'
    ATR_Stopline_CROSS_SX = 'ATR_Stopline_SX'
    ATR_Stopline_MEDIAN = 'ATR_Stopline_MEDIAN'
    ATR_Stopline_TIDE_CROSS_JX = 'ATR_Stopline_TIDE_JX'
    ATR_Stopline_TIDE_CROSS_SX = 'ATR_Stopline_TIDE_SX'
    ATR_Stopline_MEDIAN_CROSS_JX = 'ATR_Stopline_MEDIAN_JX'
    ATR_Stopline_MEDIAN_CROSS_SX = 'ATR_Stopline_MEDIAN_SX'
    ATR_Stopline_DENSITY = 'ATR_Stopline_DENSITY'

    DRAWDOWN = 'drawdown'
    DRAWDOWN_R3 = 'DRDN_R3'
    DRAWDOWN_R4 = 'DRDN_R4'
    DRAWDOWN_RSI = 'DRDN_RSI'
    DRAWDOWN_HIGH = 'DRDN_HIGH'
    BOLL_CROSS_SX_DEA = 'BOLL_SX_DEA'
    BOLL_SX_DIF = 'BOLL_SX_DIF'
    BOLL_SX_MACD = 'BOLL_SX_MACD'
    BOLL_CROSS_SX_ATR_UB = 'BOLL_SX_ATR_UB'
    BOLL_CROSS_SX_ATR_LB = 'BOLL_SX_ATR_LB'
    BOLL_CROSS_SX_BIAS3 = 'BOLL_SX_BIAS3'
    BOLL_CROSS_SX_WIDTH = 'BOLL_SX_WIDTH'
    BOLL_SX_COMBO_DENSITY = 'BOLL_SX_COMBO_DENSITY'
    BOLL_SX_DRAWDOWN = 'BOLL_SX_DRWDN'
    BOLL_SX_DRAWDOWN_PRNT = 'BOLL_SX_DRWDN_PRN'
    BOLL_SX_MINOR_DRAWDOWN = 'BOLL_SX_MINOR_DRWDN'
    BOLL_SX_MAJOR_DRAWDOWN = 'BOLL_SX_MAJOR_DRWDN'
    BOLL_SX_TRI_MA_CORR = 'BOLL_SX_TRI_MA_CORR'
    BOLL_JX_DRAWDOWN_RATIO = 'BOLL_JX_DRWDN_RATIO'
    ATR_SX_DRAWDOWN = 'ATR_SX_DRWDN'
    ATR_CROSS_SX_HIGH = 'ATR_SX_HI'
    PEAK_HIGH_BACKWARD = 'PEAK_HI_BKWRD'
    DRAWDOWN_RATIO = 'DRDN_RATIO'
    COMBO_MAX_BACKWARD = 'COMBO_MAX_BKWRD'
    MACD_CROSS_SX_DEA = 'MACD_SX_DEA'
    BOLL_CROSS_JX_WIDTH = 'BOLL_JX_WIDTH'
    LAST_LRC_SX_DRAWDOWN = 'LRC_SX_DRD'
    BOLL_CROSS_SX_RSI = 'BOLL_SX_RSI'
    BOLL_CROSS_SX_HIGH = 'BOLL_SX_HI'
    BOLL_CROSS_JX_RSI = 'BOLL_JX_RSI'
    BOLL_CROSS_JX_DEA = 'BOLL_JX_DEA'
    BOLL_JX_CLOSE = 'BOLL_JX_CLOSE'
    BOLL_JX_RAISED = 'BOLL_JX_RAISED'
    BOLL_CROSS_JX_MAXFACTOR = 'BOLL_JX_MFT'
    BOLL_CROSS_JX_ATR_UB = 'BOLL_JX_ATR_UB'
    BOLL_CROSS_JX_ATR_LB = 'BOLL_JX_ATR_LB'

    BOOTSTRAP_GROUND_ZERO_TIMING_LAG = 'BST_GND_O_LAG'
    BOOTSTRAP_GROUND_ZERO_RETURNS = 'BST_GND_O_RET'
    BOOTSTRAP_GROUND_ZERO_BEFORE = 'BST_GND_O_BF'
    BOOTSTRAP_GROUND_ZERO_MINOR_TIMING_LAG = 'BST_GND_O_MINOR_LAG'
    BOOTSTRAP_GROUND_ZERO_MAJOR_TIMING_LAG = 'BST_GND_O_MAJOR_LAG'
    BOOTSTRAP_GROUND_ZERO_MINOR_RETURNS = 'BST_GND_O_MINOR_RET'
    BOOTSTRAP_COMBO_TIMING_LAG = 'BST_COMBO_LAG'
    BOOTSTRAP_COMBO_RETURNS = 'BST_COMBO_RET'
    BOOTSTRAP_COMBO_REMARK = 'BST_COMBO_RMK'
    BOOTSTRAP_COMBO_MINOR_TIMING_LAG = 'BST_COMBO_MINOR_LAG'
    BOOTSTRAP_COMBO_MINOR_RETURNS = 'BST_COMBO_MINOR_RET'
    BOOTSTRAP_COMBO_MINOR_REMARK = 'BST_COMBO_MINOR_RMK'
    BOOTSTRAP_TREND_TIMING_LAG = 'BST_TRD_LAG'
    BOOTSTRAP_TREND_RETURNS = 'BST_TRD_RET'
    BOOTSTRAP_II_TIMING_LAG = 'BST_II_LAG'
    BOOTSTRAP_II_RETURNS = 'BST_II_RET'
    BOOTSTRAP_I_BEFORE = 'BOOTS_I_BF'
    BOOTSTRAP_II_BEFORE = 'BOOTS_II_BF'
    BOOTSTRAP_III_BEFORE = 'BOOTS_III_BF'
    BOOTSTRAP_I_FADE = 'BOOTS_I_FADE'
    BOOTSTRAP_II_FADE = 'BOOTS_II_FADE'

    ATR_CROSS_SX_HIGH = 'ATR_SX_HIGH'
    ATR_JX_DRAWDOWN_RATIO = 'ATR_JX_DRWDN_RATIO'

    DUAL_CROSS = 'DUAL_CRS'
    DUAL_CROSS_JX = 'DUAL_CROSS_JX'
    DUAL_CROSS_SX = 'DUAL_CROSS_SX'
    DUAL_TREND_TIMING_LAG = 'DUAL_TRD_LAG'
    RSRS_TREND_TIMING_LAG = 'RSRS_TRD_LAG'
    RSRS_TREND_TIMING_LAG_MINOR = 'RSRS_TRD_LAG_MINOR'
    RSRS_TREND_TIMING_LAG_MAJOR = 'RSRS_TRD_LAG_MAJOR'

    ATR_Stopline_DUAL_TIDE = 'ATR_SL_DualT'
    ATR_Stopline_DUAL_TIDE_CROSS_JX = 'ATR_SL_DualT_JX'
    ATR_Stopline_DUAL_TIDE_CROSS_SX = 'ATR_SL_DualT_SX'
    ATR_SuperTrend_DUAL_TIDE = 'ATR_ST_DualT'
    ATR_SuperTrend_DUAL_TIDE_CROSS_JX = 'ATR_ST_DualT_JX'
    ATR_SuperTrend_DUAL_TIDE_CROSS_SX = 'ATR_ST_DualT_SX'
    ZEN_DUAL_TIDE = 'ZEN_DualT'
    ZEN_DUAL_TIDE_CROSS_JX = 'ZEN_DualT_JX'
    ZEN_DUAL_TIDE_CROSS_SX = 'ZEN_DualT_SX'
    MA30_CROSS_MEDIAN = 'MA30_CRS_MEDIAN'
    MA30_CROSS_DUAL_TIDE = 'MA30_DualT'
    MA30_CROSS_DUAL_TIDE_JX = 'MA30_DualT_JX'
    MA30_CROSS_DUAL_TIDE_SX = 'MA30_DualT_SX'
    COMBINE_DUAL_TIDE = 'COMB_DualT'
    COMBINE_DUAL_TIDE_JX = 'COMB_DualT_JX'
    COMBINE_DUAL_TIDE_SX = 'COMB_DualT_SX'
    COMBINE_DENSITY = 'COMB_DENSITY'
    COMBINE_MAJOR_DENSITY = 'COMB_MAJOR_DENSITY'
    COMBO_DENSITY_RANK = 'COMB_RANK'
    COMBINE_DENSITY_SMA = 'COMB_SMA'
    COMBINE_DENSITY_SLOPE = 'COMB_SLP'
    COMBINE_DENSITY_REGRESSION = 'COMB_REGR'
    COMBINE_TIDE_CROSS_JX = 'COMBT_JX'
    COMBINE_TIDE_CROSS_SX = 'COMBT_SX'
    COMBO_FLOW = 'COMB_FLOW'
    COMBO_FLOW_JX_BEFORE = 'COMB_FLOW_JX_BF'
    COMBO_FLOW_SX_BEFORE = 'COMB_FLOW_SX_BF'
    COMBO_FLOW_TIMING_LAG = 'COMB_FLOW_LAG'
    COMBO_FLOW_MAJOR_TIMING_LAG = 'COMB_FLOW_MAJOR_LAG'
    COMBO_MAX = 'COMB_MAX'
    COMBO_MIN = 'COMB_MIN'
    COMBO_MAX_BEFORE = 'COMB_MAX_BF'
    COMBO_MIN_BEFORE = 'COMB_MIN_BF'
    COMBO_PHASE = 'COMB_PHASE'
    COMBO_PHASE_JX = 'COMB_PHS_JX'
    COMBO_PHASE_SX = 'COMB_PHS_SX'
    MA120_PHASE = 'MA120_PHASE'
    MA120_PHASE_JX = 'MA120_PHS_JX'
    MA120_PHASE_SX = 'MA120_PHS_SX'

    ATR_CHANNEL = 'ATR_WIDTH'
    ATR_MAJOR_CHANNEL = 'ATR_MAJOR_WIDTH'
    ATR_RATIO = 'ATR_RATIO'
    ATR_UB = 'ATR_UB'
    ATR_LB = 'ATR_LB'
    
    ATR_CROSS_BOLL_LB = 'ATR_CRS_BOLL_LB'
    ATR_CROSS_BOLL_UB = 'ATR_CRS_BOLL_UB'
    ATR_LB_CROSS_BOLL_JX_BEFORE = 'ATR_CRS_BOLL_LB_BF'
    ATR_LB_CLEARANCE = 'ATR_LB_CLR'
    ATR_UB_CLEARANCE = 'ATR_UB_CLR'
    ATR_LB_PADDING = 'ATR_LB_PAD'
    ATR_LB_CLEARANCE_DELTA = 'ATR_LB_CLR_DLT'
    ATR_UB_CLEARANCE_DELTA = 'ATR_UB_CLR_DLT'
    ATR_LB_CLEARANCE_MONOTONIC = 'ATR_LB_CLR_MON'
    ATR_UB_CLEARANCE_MONOTONIC = 'ATR_UB_CLR_MON'
    ATR_LB_CLEARANCE_LIS = 'ATR_LB_CLR_LIS'
    ATR_UB_CLEARANCE_LIS = 'ATR_UB_CLR_LIS'
    
    ATR_CROSS = 'ATR_CRS'
    ATR_CROSS_JX_BEFORE = 'ATR_JX_BF'
    ATR_CROSS_SX_BEFORE = 'ATR_SX_BF'
    LINEAREG_CROSS = 'LRG_CRS'
    LINEAREG_CROSS_JX_BEFORE = 'LRG_JX_BF'
    LINEAREG_CROSS_SX_BEFORE = 'LRG_SX_BF'
    LINEAREG_TREND_TIMING_LAG = 'LRG_TRD_LAG'

    LINEAREG_BAND_CROSS = LINEAREG_BAND = 'LRG_BAND'
    LINEAREG_BAND_TIMING_LAG = 'LRG_BAND_LAG'
    LINEAREG_BAND_TIMING_LAG_MINOR = 'LRG_BAND_LAG_MINOR'
    LINEAREG_BAND_JX_BEFORE = LINEAREG_BAND_CROSS_JX = 'LRG_BAND_JX_BF'
    LINEAREG_BAND_SX_BEFORE = LINEAREG_BAND_CROSS_SX = 'LRG_BAND_SX_BF'
    LINEAREG_BAND_MEDIAN = 'LRG_BAND_MEDIAN'
    LINEAREG_BAND_TIDE_CROSS_JX = 'LRG_BAND_TIDE_JX'
    LINEAREG_BAND_TIDE_CROSS_SX = 'LRG_BAND_TIDE_SX'
    LINEAREG_BAND_MEDIAN_CROSS_JX = 'LRG_BAND_MEDIAN_JX'
    LINEAREG_BAND_MEDIAN_CROSS_SX = 'LRG_BAND_MEDIAN_SX'
    LINEAREG_BAND_DENSITY = 'LRG_BAND_DENSITY'

    LINEAREG_TREND = 'LRG_TRD'
    LINEAREG_TREND_R4 = 'LRG_TRD_RS'
    LINEAREG_CROSS_FADE = 'LRG_CRS_FADE'
    LINEAREG_TREND_CROSS_JX = 'LRG_TRD_JX'
    LINEAREG_TREND_CROSS_SX = 'LRG_TRD_SX'
    LINEAREG_TREND_CROSS_JX_BEFORE = 'LRG_TRD_JX_BF'
    LINEAREG_TREND_CROSS_SX_BEFORE = 'LRG_TRD_SX_BF'
    LINEAREG_TREND_MEDIAN = 'LRG_TRD_MEDIAN'
    LINEAREG_TREND_TIDE_CROSS_JX = 'LRG_TRD_TIDE_JX'
    LINEAREG_TREND_TIDE_CROSS_SX = 'LRG_TRD_TIDE_SX'
    LINEAREG_TREND_MEDIAN_CROSS_JX = 'LRG_TRD_MEDIAN_JX'
    LINEAREG_TREND_MEDIAN_CROSS_SX = 'LRG_TRD_MEDIAN_SX'
    LINEAREG_TREND_DENSITY = 'LRG_TRD_DENSITY'

    MEGAFACTOR_CROSS_JX = 'MEGAFACTOR_JX'
    MEGAFACTOR_CROSS_SX = 'MEGAFACTOR_SX'
    MEGAFACTOR_CROSS_JX_BEFORE = 'MEGAFACTOR_JX_BF'
    MEGAFACTOR_CROSS_SX_BEFORE = 'MEGAFACTOR_SX_BF'
    MEGAFACTOR_COMBINE_CROSS_JX = 'MEGAFACTOR_COMBINE_JX'
    MEGAFACTOR_COMBINE_CROSS_SX = 'MEGAFACTOR_COMBINE_SX'

    ML_FLU_TREND = 'ML_FLU_TREND'
    FLU_POSITIVE = 'FLU_POSITIVE'
    FLU_POSITIVE_MASTER = 'HTRI_MA_JX'
    FLU_NEGATIVE = 'FLU_NEGATIVE'
    FLU_NEGATIVE_MASTER = 'HTRI_MA_SX'
    HYBIRD_TRI_MA = 'HTRI_MA'
    HYBIRD_TRI_MA_JX = 'HTRI_MA_JX'
    HYBIRD_TRI_MA_JX_RS = 'HTRI_MA_JX_RS'
    HYBIRD_TRI_MA_JX_BEFORE = 'HTRI_MA_JX_BF'
    HYBIRD_TRI_MA_SX = 'HTRI_MA_SX'
    HYBIRD_TRI_MA_SX_BEFORE = 'HTRI_MA_SX_BF'
    LAST_HYBIRD_TRI_MA_CORR = 'LS_HTRI_MA_CORR'

    # 量能指标
    AD = 'AD'
    ADOSC = 'ADOSC'
    VOLUME_FLOW = 'VOL_FLOW'
    VOLUME_AD = 'VOL_AD'
    VOLUME_AD_MA = 'VOL_AD_MA'
    VOLUME_AD_PRNT = 'VOL_AD_PRNT'
    VOLUME_ZS21 = 'VOL_ZS21'
    VOLUME_ZS84 = 'VOL_ZS84'
    VOLUME_FLOW_TIMING_LAG = 'VOL_FLOW_LAG'
    VOLUME_AD_ZS21 = 'VOL_AD_ZS21'
    VOLUME_AD_ZS84 = 'VOL_AD_ZS84'
    VOLUME_AD_FLOW = 'VOL_AD_FLOW'
    VOLUME_ADOSC = 'VOL_ADOSC'
    VOLUME_ADOSC_MA = 'VOL_ADOSC_MA'
    VOLUME_ADOSC_FLOW = 'VOL_ADOSC_FLOW'
    VOLUME_FLOW_RATIO = 'VOL_FLOW_RATIO'
    VOLUME_FLOW_BOOST_JX = 'VOL_FLOW_BOOST_JX'
    VOLUME_FLOW_BOOST_SX = 'VOL_FLOW_BOOST_SX'
    VOLUME_FLOW_TRI_CROSS = 'VOL_FLOW_TRI_CRS'
    VOLUME_FLOW_TRI_CROSS_JX = 'VOL_FLOW_TRI_JX'
    VOLUME_FLOW_TRI_CROSS_SX = 'VOL_FLOW_TRI_SX'
    VOLUME_FLOW_BOOST_JX_BEFORE = 'VOL_FLOW_BOOST_JX_BF'
    VOLUME_FLOW_BOOST_SX_BEFORE = 'VOL_FLOW_BOOST_SX_BF'

    # 组合趋势判断
    CLUSTER_GROUP_GAP = 'CLT_GRP_GAP'
    CLUSTER_GROUP_TO = 'CLT_GRP_TO'
    CLUSTER_GROUP_FROM = 'CLT_GRP_FROM'
    CLUSTER_GROUP_BEFORE = 'CLT_GRP_BF'
    TALIB_PATTERNS = 'talib_patterns'
    HDCPERIOD = 'dcperiod'
    HDCPERIOD_NORM = 'DCPERIOD_NORM'
    DOWS_BREAK = 'DOWS_BREAK'
    DOWS_BREAK_UB = 'DOWS_BREAK_UB'
    DOWS_BREAK_LB = 'DOWS_BREAK_LB'
    DOWS_BREAK_JX_BEFORE = 'DOWS_BREAK_JX_BF'
    DOWS_BREAK_SX_BEFORE = 'DOWS_BREAK_SX_BF'

    # 砖块图
    RENKO_TREND = 'RENKO_BAR'
    RENKO_TREND_L = 'RENKO_lBAR'
    RENKO_TREND_L_BRICK_SIZE = 'RENKO_lBAR_BS'
    RENKO_TREND_L_UB = 'RENKO_lBAR_UB'
    RENKO_TREND_L_LB = 'RENKO_lBAR_LB'
    RENKO_TREND_L_PRICE = 'RENKO_lBAR_PRICE'
    RENKO_TREND_L_BEFORE = 'RENKO_lBAR_BF'
    RENKO_TREND_L_JX_BEFORE = 'RENKO_lBAR_JX_BF'
    RENKO_TREND_L_SX_BEFORE = 'RENKO_lBAR_SX_BF'
    RENKO_TREND_L_TIMING_LAG = 'RENKO_lBAR_LAG'
    RENKO_TREND_L_TIMING_LAG_MINOR = 'RENKO_lBAR_LAG_MINOR'
    RENKO_BOOST_L_TIMING_LAG = 'RENKO_lBOOST_LAG'
    RENKO_BOOST_L_TIMING_LAG_MINOR = 'RENKO_lBOOST_LAG_MINOR'
    RENKO_TREND_S = 'RENKO_sBAR'
    RENKO_TREND_S_BRICK_SIZE = 'RENKO_sBAR_BS'
    RENKO_TREND_S_UB = 'RENKO_sBAR_UB'
    RENKO_TREND_S_PRICE = 'RENKO_sBAR_PRICE'
    RENKO_TREND_S_LB = 'RENKO_sBAR_LB'
    RENKO_TREND_S_BEFORE = 'RENKO_sBAR_BF'
    RENKO_TREND_S_TIMING_LAG = 'RENKO_sBAR_LAG'
    RENKO_TREND_S_TIMING_LAG_MINOR = 'RENKO_sBAR_LAG_MINOR'
    RENKO_BOOST_S_TIMING_LAG = 'RENKO_sBOOST_LAG'
    RENKO_BOOST_S_TIMING_LAG_MINOR = 'RENKO_sBOOST_LAG_MINOR'
    RENKO_S_JX_BEFORE = 'RENKO_sBAR_JX_BF'
    RENKO_S_SX_BEFORE = 'RENKO_sBAR_SX_BF'
    RENKO_BOOTSTRAP = 'RENKO_BOOTSTRAP'
    RENKO_OPTIMAL = 'RENKO_OPT'
    RENKO_BRICKS = 'RENKO_BRICKS'
    BOLL_RENKO_TIMING_LAG = 'BOLL_RENKO_LAG'
    BOLL_RENKO_MINOR_TIMING_LAG = 'BOLL_RENKO_MINOR_LAG'

    BASELINE = 'BASELINE'
    BASELINE_ROC = 'BASLIN_ROC'
    BASELINE_SLOPE = 'BASLIN_SLP'
    LEVERAGE = 'LEVERAGE'
    LEVERAGE_DELTA = 'LEVER_D'
    LEVERAGE_NORM = 'LEVER_NORM'
    LEVERAGE_PRE = 'LEVER_PRE'
    LEVERAGE_ONHOLD = 'LEVER_ONHOLD'

    ONHOLD_BEFORE = 'ONHOLD_BEFORE'
    OFFHOLD_BEFORE = 'OFFHOLD_BEFORE'

    RSRS_BETA = 'RSRS_BETA'
    RSRS_BETA_R2 = 'RSRS_BETA_R2'
    RSRS_ZSCORE = 'RSRS_ZSCORE'
    RSRS_ZSCORE_R2 = 'RSRS_ZS_R2'
    RSRS_RIGHT = 'RSRS_RIGHT'

    ZSCORE_21 = 'ZSCORE_21'
    ZSCORE_84 = 'ZSCORE_84'
    RPS_RETURNS = 'RPS_RET'
    RPS_RANK = 'RPS_RANK'
    RPS_PCT = 'RPS_PCT'
    RPS_PUNCH_TIMING_LAG = 'RPS_TRD_LAG'

    LEAST_SQUARE_CIRCLE_X = 'LEAST_SQUR_CIRCLE_X'
    LEAST_SQUARE_CIRCLE_SLOPE = 'LEAST_SQUR_CIRCLE_SLOPE'
    LEAST_SQUARE_CIRCLE_Y = 'LEAST_SQUR_CIRCLE_Y'
    LEAST_SQUARE_CIRCLE_R = 'LEAST_SQUR_CIRCLE_R'
    LEAST_SQUARE_CIRCLE_Residu = 'LEAST_SQUR_CIRCLE_Residu'

    ECHO_TIMING_LAG = 'ECHO_of_LAGs'
    ECHO_TIMING_LAG_DELTA = 'ECHO_of_LAGs_dif_1T'

    SHARPE_RATIO = 'SHARPE_RATIO'
    SORTINO_RATIO = 'SORTINO_RATIO'
    SORTINO_RATIO_RSRS = 'SORTINO_RATIO_RSRS'
    TRANSACTION_RETURN_MEAN = 'TRANS_RET_MEAN'
    ANNUAL_RETURN = 'ANNUAL_RET'
    ANNUAL_RETURN_MEAN = 'ANNUAL_RET_MEAN'
    ANNUAL_RETURN_RSRS = 'ANNUAL_RET_RSRS'
    BENCHMARK_RETURN = 'BENCHMARK_RET'
    ANNUAL_VOLATILITY = 'ANNUAL_VOL'
    ANNUAL_VOLATILITY_PRNT = 'ANNUAL_VOL_PRN'
    DOWNRISK_VOLATILITY = 'DOWNRISK_VOL'
    ANNUAL_VOLATILITY_RSRS = 'ANNUAL_VOL_RSRS'
    TURNOVER_RATIO_MEAN = 'TURNOVER_RATIO_MEAN'

    ALPHA = 'ALPHA'
    BETA = 'BETA'
    ALPHA_ = 'alpha_{}'

    DEADPOOL_FALL_TIMING_LAG = 'DEADPOOL_FALL_LAG'

    MAINFEST_UPRISING_COEFFICIENT = 'UPRISING_COEF'
    MAINFEST_UPRISING_TIMING_LAG = 'UPRISING_LAG'
    MAINFEST_UPRISING_MAJOR_COEFFICIENT = 'UPRISING_MAJOR_COEF'

    def __setattr__(self, name, value):
        raise Exception(u'Const Class can\'t allow to change property\' value.')
        return super().__setattr__(name, value)



class BAR_LABEL():
    BOOTSTRAP_I = 'BOOSTRAP_I_BKWRD'
    BOOTSTRAP_II = 'BOOSTRAP_II_BKWRD'
    TRIGGER_RSRS = 'TRIGGER_RSRS_BKWRD'
    TRIGGER_RPS = 'TRIGGER_RPS_BKWRD'

    def __setattr__(self, name, value):
        raise Exception(u'Const Class can\'t allow to change property\' value.')
        return super().__setattr__(name, value)


#sys.modules[__name__] = _const()