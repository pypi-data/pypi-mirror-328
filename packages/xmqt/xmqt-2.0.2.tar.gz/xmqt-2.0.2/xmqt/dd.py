def INTPART(nums):
    """
    通达信向0取整数
    :param nums:
    :return:
    """
    return nums.astype(int)


def MOS(qt, OPEN, CLOSE, HIGH, LOW):
    DIFF = 100 * (qt.EMA(CLOSE, 12) - qt.EMA(CLOSE, 26))
    DEA = qt.EMA(DIFF, 9)
    MACD = (DIFF - DEA) * 2
    死叉 = qt.CROSS(DEA, DIFF)
    N1 = qt.BARSLAST(死叉)
    N2 = qt.REF(qt.BARSLAST(死叉), N1 + 1)
    N3 = qt.REF(qt.BARSLAST(死叉), N2 + N1 + 2)
    CL1 = qt.LLV(LOW, N1 + 1)
    DIFL1 = qt.LLV(DIFF, N1 + 1)
    CL2 = qt.REF(CL1, N1 + 1)
    DIFL2 = qt.REF(DIFL1, N1 + 1)
    CL3 = qt.REF(CL2, N1 + 1)
    DIFL3 = qt.REF(DIFL2, N1 + 1)
    PDIFL2 = qt.IF(DIFL2 > 0, INTPART(qt.LOG(DIFL2)) - 1, INTPART(qt.LOG(-DIFL2)) - 1);
    MDIFL2 = INTPART(DIFL2 / qt.POW(10, PDIFL2));
    PDIFL3 = qt.IF(DIFL3 > 0, INTPART(qt.LOG(DIFL3)) - 1, INTPART(qt.LOG(-DIFL3)) - 1)
    MDIFL3 = INTPART(DIFL3 / qt.POW(10, PDIFL3))
    MDIFB2 = INTPART(DIFF / qt.POW(10, PDIFL2))
    MDIFB3 = INTPART(DIFF / qt.POW(10, PDIFL3))
    直接底部结构 = (CL1 < CL2) & (MDIFB2 > MDIFL2) & DIFF < 0 & (MACD < 0 & qt.REF(MACD, 1) < 0) & MDIFB2 <= qt.REF(
        MDIFB2, 0)
    隔峰底部结构 = (CL1 < CL3 & CL3 < CL2) & (MDIFB3 > MDIFL3) & (MACD < 0 & qt.REF(MACD, 1) < 0) & MDIFB3 <= qt.REF(
        MDIFB3, 0)
    BG = ((MDIFB2 > qt.REF(MDIFB2, 1)) * qt.REF(直接底部结构, 2)) | (
            (MDIFB3 > qt.REF(MDIFB3, 2)) * qt.REF(隔峰底部结构, 2))
    P = qt.CROSS(DIFF, DEA)
    底部结构 = qt.FILTER(BG & P, MACD > 0)
    金叉 = qt.CROSS(DIFF, DEA)
    M1 = qt.BARSLAST(金叉)
    M2 = qt.REF(qt.BARSLAST(金叉), M1 + 1)
    M3 = qt.REF(qt.BARSLAST(金叉), M2 + M1 + 2)
    CH1 = qt.HHV(HIGH, M1 + 1)
    DIFH1 = qt.HHV(DIFF, M1 + 1)
    CH2 = qt.REF(CH1, M1 + 1)
    DIFH2 = qt.REF(DIFH1, M1 + 1)
    CH3 = qt.REF(CH2, M1 + 1)
    DIFH3 = qt.REF(DIFH2, M1 + 1)
    PDIFH2 = qt.IF(DIFH2 > 0, INTPART(qt.LOG(DIFH2)) - 1, INTPART(qt.LOG(-DIFH2)) - 1)
    MDIFH2 = INTPART(DIFH2 / qt.POW(10, PDIFH2))
    PDIFH3 = qt.IF(DIFH3 > 0, INTPART(qt.LOG(DIFH3)) - 1, INTPART(qt.LOG(-DIFH3)) - 1)
    MDIFH3 = INTPART(DIFH3 / qt.POW(10, PDIFH3))
    MDIFT2 = INTPART(DIFF / qt.POW(10, PDIFH2))
    MDIFT3 = INTPART(DIFF / qt.POW(10, PDIFH3))
    直接顶部结构 = (CH1 > CH2) & (MDIFT2 < MDIFH2) & DIFF > 0 & (MACD > 0 & qt.REF(MACD, 1) > 0) & MDIFT2 >= qt.REF(
        MDIFT2, 0)
    隔峰顶部结构 = (CH1 > CH3 & CH3 > CH2) & (MDIFT3 < MDIFH3) & (MACD > 0 & qt.REF(MACD, 1) > 0) & MDIFT3 >= qt.REF(
        MDIFT3, 0)
    TG = ((MDIFT2 < qt.REF(MDIFT2, 1)) * qt.REF(直接顶部结构, 2)) | (
            (MDIFT3 < qt.REF(MDIFT3, 2)) * qt.REF(隔峰顶部结构, 2))
    Q = qt.CROSS(DEA, DIFF)
    顶部结构 = qt.FILTER(TG & Q, MACD < 0)
    return 底部结构, 顶部结构
