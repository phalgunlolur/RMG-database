#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XYSJ"], ownReverse=False)

reverse = "1,2_S_radical_shift"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XSYJ",
    group = 
"""
1 *1 C   u0 {2,S}
2 *2 S   u0 {1,S} {3,S}
3 *3 R!H u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "YJ-S2s",
    group = 
"""
1 *3 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "X-S2s",
    group = "OR{C-S2s}",
    kinetics = None,
)

entry(
    index = 4,
    label = "CJ-S2s",
    group = 
"""
1 *3 C u1
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CdsJ-S2s",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CsJ-S2s",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    R  u0 {1,S}
3    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CsJ-S2sHH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CsJ-S2sCsH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "CsJ-S2sCsCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "CsJ-S2sS2sH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "CsJ-S2sS2sS2s",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "CsJ-S2sCsS2s",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "CsJ-S2sOneDe",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    R                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "CsJ-S2sOneDeH",
    group = 
"""
1 *3 Cs               u1 {2,S} {3,S}
2    H                u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "CsJ-S2sCdH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "CsJ-S2sOneDeCs",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "CsJ-S2sCdCs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "CsJ-S2sOneDeS2s",
    group = 
"""
1 *3 Cs            u1 {2,S} {3,S}
2    S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "CsJ-S2sCdS2s",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S}
2    S2s u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "SJ-S2s",
    group = 
"""
1 *3 S2s u1
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "C-S2s",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Cb-S2s",
    group = 
"""
1 *1 Cb u0
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Ct-S2s",
    group = 
"""
1 *1 Ct u0 {2,T}
2    C  u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Cds-S2s",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2    C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Cds-S2sH",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2    C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Cds-S2sCs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Cds-S2sCt",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Cds-S2sCb",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Cds-S2sCO",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Cds-S2sOs",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Cds-S2sS2s",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Cds-S2sCd",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Cds-S2sC=S",
    group = 
"""
1 *1 C  u0 {2,D} {3,S}
2    C  u0 {1,D}
3    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "C=S-S2s",
    group = 
"""
1 *1 CS u0 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "C=S-S2sH",
    group = 
"""
1 *1 CS u0 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "C=S-S2sCs",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "C=S-S2sCt",
    group = 
"""
1 *1 CS u0 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "C=S-S2sCb",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cb u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "C=S-S2sCO",
    group = 
"""
1 *1 CS u0 {2,S}
2    CO u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "C=S-S2sOs",
    group = 
"""
1 *1 CS u0 {2,S}
2    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "C=S-S2sS2s",
    group = 
"""
1 *1 CS u0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "C=S-S2sCd",
    group = 
"""
1 *1 CS u0 {2,S}
2    Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "C=S-S2sC=S",
    group = 
"""
1 *1 CS u0 {2,S}
2    CS u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Cs-S2s",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Cs-S2sHHH",
    group = 
"""
1 *1 C u0 {2,S} {3,S} {4,S}
2    H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Cs-S2sCsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Cs-S2sCsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Cs-S2sCsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Cs-S2sOsHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Cs-S2sOsCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Cs-S2sOsCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Cs-S2sOsOsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Cs-S2sOsOsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Cs-S2sOsOsOs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Os u0 {1,S}
3    Os u0 {1,S}
4    Os u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Cs-S2sS2sHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Cs-S2sS2sCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Cs-S2sS2sCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Cs-S2sS2sS2sH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Cs-S2sS2sS2sCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Cs-S2sS2sS2sS2s",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Cs-S2sOneDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [H,Cs,Os,S2s]     u0 {1,S}
4    [H,Cs,Os,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Cs-S2sOneDeHH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    H                u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Cs-S2sCtHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Cs-S2sCbHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Cs-S2sCOHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Cs-S2sCdHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Cs-S2sC=SHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Cs-S2sOneDeCsH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Cs-S2sCtCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Cs-S2sCbCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Cs-S2sCOCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Cs-S2sCdCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Cs-S2sC=SCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Cs-S2sOneDeOsH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Cs-S2sOneDeS2sH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Cs-S2sOneDeCsCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Cs               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Cs-S2sCtCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Cs-S2sCbCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Cs-S2sCOCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Cs-S2sCdCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Cs-S2sC=SCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Cs-S2sOneDeOsCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Cs-S2sOneDeS2sCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Cs-S2sOneDeOsOs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    Os               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Cs-S2sOneDeOsS2s",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    Os               u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Cs-S2sOneDeS2sS2s",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    S2s               u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Cs-S2sTwoDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [H,Cs,Os,S2s]     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Cs-S2sTwoDeH",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Cs-S2sCtCtH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Cs-S2sCtCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Cs-S2sCtCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Cs-S2sCbCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Cs-S2sCbCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Cs-S2sCOCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Cs-S2sCdCtH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Cs-S2sCdCbH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Cs-S2sCdCOH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Cs-S2sCtC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Cs-S2sCbC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Cs-S2sCOC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Cs-S2sCdCdH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    H  u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Cs-S2sCdC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    H  u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Cs-S2sC=SC=SH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Cs-S2sTwoDeCs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Cs               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Cs-S2sCtCtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Cs-S2sCtCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Cs-S2sCtCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Cs-S2sCbCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Cs-S2sCbCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Cs-S2sCOCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CO u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Cs-S2sCdCtCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Ct u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Cs-S2sCdCbCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cb u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Cs-S2sCdCOCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CO u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Cs-S2sCtC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Cs-S2sCbC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Cs-S2sCOC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CO u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Cs-S2sCdCdCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    Cd u0 {1,S} {6,D}
4    Cs u0 {1,S}
5    C  u0 {2,D}
6    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Cs-S2sCdC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S} {5,D}
3    CS u0 {1,S}
4    Cs u0 {1,S}
5    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Cs-S2sC=SC=SCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    CS u0 {1,S}
3    CS u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Cs-S2sTwoDeOs",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    Os               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Cs-S2sTwoDeS2s",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    S2s               u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Cs-S2sThreeDe",
    group = 
"""
1 *1 C                u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO,CS] u0 {1,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
L1: YJ-S2s
    L2: CJ-S2s
        L3: CdsJ-S2s
        L3: CsJ-S2s
            L4: CsJ-S2sHH
            L4: CsJ-S2sCsH
            L4: CsJ-S2sCsCs
            L4: CsJ-S2sS2sH
            L4: CsJ-S2sS2sS2s
            L4: CsJ-S2sCsS2s
            L4: CsJ-S2sOneDe
                L5: CsJ-S2sOneDeH
                    L6: CsJ-S2sCdH
                L5: CsJ-S2sOneDeCs
                    L6: CsJ-S2sCdCs
                L5: CsJ-S2sOneDeS2s
                    L6: CsJ-S2sCdS2s
    L2: SJ-S2s
L1: X-S2s
    L2: C-S2s
        L3: Cb-S2s
        L3: Ct-S2s
        L3: Cds-S2s
            L4: Cds-S2sH
            L4: Cds-S2sCs
            L4: Cds-S2sCt
            L4: Cds-S2sCb
            L4: Cds-S2sCO
            L4: Cds-S2sOs
            L4: Cds-S2sS2s
            L4: Cds-S2sCd
            L4: Cds-S2sC=S
        L3: C=S-S2s
            L4: C=S-S2sH
            L4: C=S-S2sCs
            L4: C=S-S2sCt
            L4: C=S-S2sCb
            L4: C=S-S2sCO
            L4: C=S-S2sOs
            L4: C=S-S2sS2s
            L4: C=S-S2sCd
            L4: C=S-S2sC=S
        L3: Cs-S2s
            L4: Cs-S2sHHH
            L4: Cs-S2sCsHH
            L4: Cs-S2sCsCsH
            L4: Cs-S2sCsCsCs
            L4: Cs-S2sOsHH
            L4: Cs-S2sOsCsH
            L4: Cs-S2sOsCsCs
            L4: Cs-S2sOsOsH
            L4: Cs-S2sOsOsCs
            L4: Cs-S2sOsOsOs
            L4: Cs-S2sS2sHH
            L4: Cs-S2sS2sCsH
            L4: Cs-S2sS2sCsCs
            L4: Cs-S2sS2sS2sH
            L4: Cs-S2sS2sS2sCs
            L4: Cs-S2sS2sS2sS2s
            L4: Cs-S2sOneDe
                L5: Cs-S2sOneDeHH
                    L6: Cs-S2sCtHH
                    L6: Cs-S2sCbHH
                    L6: Cs-S2sCOHH
                    L6: Cs-S2sCdHH
                    L6: Cs-S2sC=SHH
                L5: Cs-S2sOneDeCsH
                    L6: Cs-S2sCtCsH
                    L6: Cs-S2sCbCsH
                    L6: Cs-S2sCOCsH
                    L6: Cs-S2sCdCsH
                    L6: Cs-S2sC=SCsH
                L5: Cs-S2sOneDeOsH
                L5: Cs-S2sOneDeS2sH
                L5: Cs-S2sOneDeCsCs
                    L6: Cs-S2sCtCsCs
                    L6: Cs-S2sCbCsCs
                    L6: Cs-S2sCOCsCs
                    L6: Cs-S2sCdCsCs
                    L6: Cs-S2sC=SCsCs
                L5: Cs-S2sOneDeOsCs
                L5: Cs-S2sOneDeS2sCs
                L5: Cs-S2sOneDeOsOs
                L5: Cs-S2sOneDeOsS2s
                L5: Cs-S2sOneDeS2sS2s
            L4: Cs-S2sTwoDe
                L5: Cs-S2sTwoDeH
                    L6: Cs-S2sCtCtH
                    L6: Cs-S2sCtCbH
                    L6: Cs-S2sCtCOH
                    L6: Cs-S2sCbCbH
                    L6: Cs-S2sCbCOH
                    L6: Cs-S2sCOCOH
                    L6: Cs-S2sCdCtH
                    L6: Cs-S2sCdCbH
                    L6: Cs-S2sCdCOH
                    L6: Cs-S2sCtC=SH
                    L6: Cs-S2sCbC=SH
                    L6: Cs-S2sCOC=SH
                    L6: Cs-S2sCdCdH
                    L6: Cs-S2sCdC=SH
                    L6: Cs-S2sC=SC=SH
                L5: Cs-S2sTwoDeCs
                    L6: Cs-S2sCtCtCs
                    L6: Cs-S2sCtCbCs
                    L6: Cs-S2sCtCOCs
                    L6: Cs-S2sCbCbCs
                    L6: Cs-S2sCbCOCs
                    L6: Cs-S2sCOCOCs
                    L6: Cs-S2sCdCtCs
                    L6: Cs-S2sCdCbCs
                    L6: Cs-S2sCdCOCs
                    L6: Cs-S2sCtC=SCs
                    L6: Cs-S2sCbC=SCs
                    L6: Cs-S2sCOC=SCs
                    L6: Cs-S2sCdCdCs
                    L6: Cs-S2sCdC=SCs
                    L6: Cs-S2sC=SC=SCs
                L5: Cs-S2sTwoDeOs
                L5: Cs-S2sTwoDeS2s
            L4: Cs-S2sThreeDe
"""
)
