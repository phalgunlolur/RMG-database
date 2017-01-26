#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["XYSJ"], ownReverse=False)

reverse = "Ring_Opening_bySradical"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XSYJ",
    group = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    kinetics = None,
)

entry(
    index = 2,
    label = "YJ",
    group = 
"""
1 *3 R!H u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "XSR3J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *2 S2s  u0 {1,[S,D]} {3,S}
3 *1 C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "XSR3J_S",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *2 S2s  u0 {1,S} {3,S}
3 *1 C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "XSR4J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *2 S2s  u0 {2,[S,D]} {4,S}
4 *1 C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "XSR4J_SS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 S2s  u0 {2,S} {4,S}
4 *1 C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "XSR4J_SD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *2 S2s  u0 {2,S} {4,S}
4 *1 C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "XSR5J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *2 S2s  u0 {3,[S,D]} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 S2s  u0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 S2s  u0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 S2s  u0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,D}
3 *5 R!H u0 {2,D} {4,S}
4 *2 S2s  u0 {3,S} {5,S}
5 *1 C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "XSR6J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *6 R!H u0 {3,[S,D]} {5,[S,D]}
5 *2 S2s  u0 {4,[S,D]} {6,S}
6 *1 C   u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "XSR7J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,[S,D]}
3 *5 R!H u0 {2,[S,D]} {4,[S,D]}
4 *6 R!H u0 {3,[S,D]} {5,[S,D]}
5 *7 R!H u0 {4,[S,D]} {6,[S,D]}
6 *2 S2s  u0 {5,[S,D]} {7,S}
7 *1 C   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "CJ",
    group = "OR{CsJ, CdsJ, CdsJ-2}",
    kinetics = None,
)

entry(
    index = 17,
    label = "CdsJ",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "CdsJ-H",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "CdsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "CdsJ-S2s",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "CdsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "CdsJ-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    R u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "CdsJ_C-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CdsJ_C-Cs2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *4 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "CdsJ_C-S2s2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *4 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CdsJ_S-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CdsJ_C-Cd2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *4 Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CsJ",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2 *4 R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "CsJ-CsS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "CsJ-CsS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CsJ-CsCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CsJ-CsOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CsJ-CsOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CsJ-CsCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CsJ-CsOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "CsJ-CsCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "CsJ-CsOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "CsJ-CsCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cs u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "CsJ-CsTwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "CsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "CsJ-CdS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "CsJ-CdS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "CsJ-CdCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "CsJ-CdOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "CsJ-CdOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "CsJ-CdCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "CsJ-CdOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "CsJ-CdCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "CsJ-CdOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "CsJ-CdCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 Cd u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "CsJ-CdTwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "CsJ-S2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "CsJ-S2sHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "CsJ-S2sCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "CsJ-S2sCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "CsJ-S2sS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "CsJ-S2sS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "CsJ-S2sCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "CsJ-S2sOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "CsJ-S2sOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "CsJ-S2sCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "CsJ-S2sOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "CsJ-S2sCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "CsJ-S2sOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *4 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "CsJ-S2sCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *4 S2s u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "SJ",
    group = 
"""
1 *3 S u1 {2,S}
2 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "S2sJ",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "S2sJ-Cs",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "S2sJ-S2s",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "S2sJ-OneDe",
    group = 
"""
1 *3 S2s            u1 {2,S}
2 *4 [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "S2sJ-Cd",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "CJ-3",
    group = "OR{CsJ-3, CdsJ-3}",
    kinetics = None,
)

entry(
    index = 80,
    label = "CdsJ-3",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    R  u0 {1,D}
3 *2 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "CsJ-3",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "CsJ-3-S2sHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "CsJ-3-S2sCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "CsJ-3-S2sCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "CsJ-3-S2sS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "CsJ-3-S2sS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "CsJ-3-S2sCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "CsJ-3-S2sOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *2 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "CsJ-3-S2sOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *2 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "CsJ-3-S2sCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "CsJ-3-S2sOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *2 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "CsJ-3-S2sCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "CsJ-3-S2sOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *2 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "CsJ-3-S2sCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *2 S2s u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "CsJ-3-S2sTwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *2 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "SJ-3",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *2 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Ct",
    group = 
"""
1 *1 Ct u0
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Cds",
    group = 
"""
1 *1 Cd u0
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "C-RRR",
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
    index = 100,
    label = "C-NonDe",
    group = 
"""
1 *1 C            u0 {2,S} {3,S} {4,S}
2    [H,Cs,Os,S2s] u0 {1,S}
3    [H,Cs,Os,S2s] u0 {1,S}
4    [H,Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "C-HHH",
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
    index = 102,
    label = "C-CsHH",
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
    index = 103,
    label = "C-CsCsH",
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
    index = 104,
    label = "C-CsCsCs",
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
    index = 105,
    label = "C-OneS",
    group = 
"""
1 *1 C         u0 {2,S} {3,S} {4,S}
2    S2s        u0 {1,S}
3    [H,Cs,Os] u0 {1,S}
4    [H,Cs,Os] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "C-S2sHH",
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
    index = 107,
    label = "C-S2sCsH",
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
    index = 108,
    label = "C-S2sCsCs",
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
    index = 109,
    label = "C-OneDe",
    group = 
"""
1 *1 C             u0 {2,S} {3,S} {4,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    R             u0 {1,S}
4    R             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "C-CdHH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "C-CdCsH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "C-CdCsCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "C-CdS2sH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "C-CdS2sCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    S2s u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "C-CdS2sS2s",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Cd u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "C-CtHH",
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
    index = 117,
    label = "C-CtCsH",
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
    index = 118,
    label = "C-CtCsCs",
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
    index = 119,
    label = "C-CtS2sH",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "C-CtS2sCs",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    S2s u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "C-CtS2sS2s",
    group = 
"""
1 *1 C  u0 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
    L2: XSR4J
        L3: XSR4J_SS
        L3: XSR4J_SD
    L2: XSR5J
        L3: XSR5J_SSS
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_SDD
    L2: XSR6J
    L2: XSR7J
L1: C
    L2: Ct
    L2: Cds
    L2: C-RRR
        L3: C-NonDe
            L4: C-HHH
            L4: C-CsHH
            L4: C-CsCsH
            L4: C-CsCsCs
            L4: C-OneS
                L5: C-S2sHH
                L5: C-S2sCsH
                L5: C-S2sCsCs
        L3: C-OneDe
            L4: C-CdHH
            L4: C-CdCsH
            L4: C-CdCsCs
            L4: C-CdS2sH
            L4: C-CdS2sCs
            L4: C-CdS2sS2s
            L4: C-CtHH
            L4: C-CtCsH
            L4: C-CtCsCs
            L4: C-CtS2sH
            L4: C-CtS2sCs
            L4: C-CtS2sS2s
L1: YJ
    L2: CJ
        L3: CdsJ
            L4: CdsJ-H
            L4: CdsJ-Cs
            L4: CdsJ-S2s
            L4: CdsJ-Cd
        L3: CdsJ-2
            L4: CdsJ_C-2
                L5: CdsJ_C-Cs2
                L5: CdsJ_C-S2s2
                L5: CdsJ_C-Cd2
            L4: CdsJ_S-2
        L3: CsJ
            L4: CsJ-Cs
                L5: CsJ-CsHH
                L5: CsJ-CsCsH
                L5: CsJ-CsCsCs
                L5: CsJ-CsS2sH
                L5: CsJ-CsS2sS2s
                L5: CsJ-CsCsS2s
                L5: CsJ-CsOneDe
                    L6: CsJ-CsOneDeH
                        L7: CsJ-CsCdH
                    L6: CsJ-CsOneDeCs
                        L7: CsJ-CsCdCs
                    L6: CsJ-CsOneDeS2s
                        L7: CsJ-CsCdS2s
                L5: CsJ-CsTwoDe
            L4: CsJ-Cd
                L5: CsJ-CdHH
                L5: CsJ-CdCsH
                L5: CsJ-CdCsCs
                L5: CsJ-CdS2sH
                L5: CsJ-CdS2sS2s
                L5: CsJ-CdCsS2s
                L5: CsJ-CdOneDe
                    L6: CsJ-CdOneDeH
                        L7: CsJ-CdCdH
                    L6: CsJ-CdOneDeCs
                        L7: CsJ-CdCdCs
                    L6: CsJ-CdOneDeS2s
                        L7: CsJ-CdCdS2s
                L5: CsJ-CdTwoDe
            L4: CsJ-S2s
                L5: CsJ-S2sHH
                L5: CsJ-S2sCsH
                L5: CsJ-S2sCsCs
                L5: CsJ-S2sS2sH
                L5: CsJ-S2sS2sS2s
                L5: CsJ-S2sCsS2s
                L5: CsJ-S2sOneDe
                    L6: CsJ-S2sOneDeH
                        L7: CsJ-S2sCdH
                    L6: CsJ-S2sOneDeCs
                        L7: CsJ-S2sCdCs
                    L6: CsJ-S2sOneDeS2s
                        L7: CsJ-S2sCdS2s
    L2: SJ
        L3: S2sJ
            L4: S2sJ-Cs
            L4: S2sJ-S2s
            L4: S2sJ-OneDe
                L5: S2sJ-Cd
    L2: CJ-3
        L3: CdsJ-3
        L3: CsJ-3
            L4: CsJ-3-S2sHH
            L4: CsJ-3-S2sCsH
            L4: CsJ-3-S2sCsCs
            L4: CsJ-3-S2sS2sH
            L4: CsJ-3-S2sS2sS2s
            L4: CsJ-3-S2sCsS2s
            L4: CsJ-3-S2sOneDe
                L5: CsJ-3-S2sOneDeH
                    L6: CsJ-3-S2sCdH
                L5: CsJ-3-S2sOneDeCs
                    L6: CsJ-3-S2sCdCs
                L5: CsJ-3-S2sOneDeS2s
                    L6: CsJ-3-S2sCdS2s
            L4: CsJ-3-S2sTwoDe
    L2: SJ-3
"""
)

forbidden(
    label = "RR_13",
    group = 
"""
1 *1 R u0 {2,[S,D]}
2 *3 R u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "RR_birad",
    group = 
"""
1 *3 R u1 {2,[S,D]}
2    R u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

