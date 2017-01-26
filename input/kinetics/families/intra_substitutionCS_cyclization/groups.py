#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_cyclization/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["XSYJ"], products=["SY", "XJ"], ownReverse=False)

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
    index = 2,
    label = "C",
    group = 
"""
1 *1 C u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cs",
    group = 
"""
1 *1 Cs u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Cds",
    group = 
"""
1 *1 Cd u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Ct",
    group = 
"""
1 *1 Ct u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C-RRR",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 R  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "S",
    group = 
"""
1 *2 S u0
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "XSR3J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *4 R!H u0 {1,[S,D]} {3,S}
3 *1 Cs  u0 {2,S} {4,S}
4 *2 S2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "XSR3J_S",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *1 Cs  u0 {2,S} {4,S}
4 *2 S2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "XSR3J_D",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *1 Cs  u0 {2,S} {4,S}
4 *2 S2s  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "XSR4J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *4 R!H u0 {2,[S,D]} {4,S}
4 *1 Cs  u0 {3,S} {5,S}
5 *2 S2s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "XSR4J_SS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 Cs  u0 {3,S} {5,S}
5 *2 S2s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "XSR4J_SD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *4 R!H u0 {2,S} {4,S}
4 *1 Cs  u0 {3,S} {5,S}
5 *2 S2s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "XSR4J_DS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 Cs  u0 {3,S} {5,S}
5 *2 S2s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "XSR4J_DD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *4 R!H u0 {2,D} {4,S}
4 *1 Cs  u0 {3,S} {5,S}
5 *2 S2s  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "XSR5J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *4 R!H u0 {3,[S,D]} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "XSR5J_SSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "XSR5J_SSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "XSR5J_SDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "XSR5J_DSS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "XSR5J_DDS",
    group = 
"""
1 *3 R!H u1 {2,S}
2 *5 R!H u0 {1,S} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "XSR5J_DSD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "XSR5J_SDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "XSR5J_DDD",
    group = 
"""
1 *3 R!H u1 {2,D}
2 *5 R!H u0 {1,D} {3,D}
3 *6 R!H u0 {2,D} {4,D}
4 *4 R!H u0 {3,D} {5,S}
5 *1 Cs  u0 {4,S} {6,S}
6 *2 S2s  u0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "XSR6J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *7 R!H u0 {3,[S,D]} {5,[S,D]}
5 *4 R!H u0 {4,[S,D]} {6,S}
6 *1 Cs  u0 {5,S} {7,S}
7 *2 S2s  u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "XSR7J",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *5 R!H u0 {1,[S,D]} {3,[S,D]}
3 *6 R!H u0 {2,[S,D]} {4,[S,D]}
4 *7 R!H u0 {3,[S,D]} {5,[S,D]}
5 *8 R!H u0 {4,[S,D]} {6,[S,D]}
6 *4 R!H u0 {5,[S,D]} {7,S}
7 *1 Cs  u0 {6,S} {8,S}
8 *2 S2s  u0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "CJ",
    group = "OR{CsJ, CdsJ, CdsJ-2}",
    kinetics = None,
)

entry(
    index = 25,
    label = "CdsJ",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *5 C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "CdsJ-H",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *5 C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "CdsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *5 C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "CdsJ-S2s",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *5 C  u0 {1,D}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "CdsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *5 C  u0 {1,D}
3    Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "CdsJ-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    R u0 {1,D}
3 *5 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "CdsJ_C-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3 *5 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "CdsJ_C-Cs2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *5 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "CdsJ_C-S2s2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *5 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "CdsJ_C-Cd2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *5 Cd u0 {1,S} {4,D}
4    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "CdsJ_S-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3 *5 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "CsJ",
    group = 
"""
1 *3 C u1 {2,S} {3,S} {4,S}
2 *5 R u0 {1,S}
3    R u0 {1,S}
4    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "CsJ-Cs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "CsJ-CsHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "CsJ-CsCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "CsJ-CsCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "CsJ-CsS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "CsJ-CsS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "CsJ-CsCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "CsJ-CsOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "CsJ-CsOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "CsJ-CsCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "CsJ-CsOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "CsJ-CsCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "CsJ-CsOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "CsJ-CsCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cs u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "CsJ-CsTwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cs            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "CsJ-Cd",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "CsJ-CdHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "CsJ-CdCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "CsJ-CdCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "CsJ-CdS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "CsJ-CdS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "CsJ-CdCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "CsJ-CdOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "CsJ-CdOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "CsJ-CdCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "CsJ-CdOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "CsJ-CdCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "CsJ-CdOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "CsJ-CdCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 Cd u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "CsJ-CdTwoDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 Cd            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "CsJ-S2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "CsJ-S2sHH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "CsJ-S2sCsH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "CsJ-S2sCsCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "CsJ-S2sS2sH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    S2s u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "CsJ-S2sS2sS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    S2s u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "CsJ-S2sCsS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cs u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "CsJ-S2sOneDe",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "CsJ-S2sOneDeH",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "CsJ-S2sCdH",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "CsJ-S2sOneDeCs",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    Cs            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "CsJ-S2sCdCs",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cd u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "CsJ-S2sOneDeS2s",
    group = 
"""
1 *3 C             u1 {2,S} {3,S} {4,S}
2 *5 S2s            u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    S2s            u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "CsJ-S2sCdS2s",
    group = 
"""
1 *3 C  u1 {2,S} {3,S} {4,S}
2 *5 S2s u0 {1,S}
3    Cd u0 {1,S}
4    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "SJ",
    group = 
"""
1 *3 S u1 {2,S}
2 *5 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "S2sJ",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *5 R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "S2sJ-Cs",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *5 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "S2sJ-S2s",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *5 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "S2sJ-OneDe",
    group = 
"""
1 *3 S2s            u1 {2,S}
2 *5 [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "S2sJ-Cd",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *5 Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "CJ-3",
    group = "OR{CsJ-3, CdsJ-3, CdsJ-3-2}",
    kinetics = None,
)

entry(
    index = 88,
    label = "CdsJ-3",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "CdsJ-3-H",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2 *4 C u0 {1,D}
3    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "CdsJ-3-Cs",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "CdsJ-3-S2s",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2 *4 C  u0 {1,D}
3    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "CdsJ-3-Cd",
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
    index = 93,
    label = "CdsJ-3-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    R u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "CdsJ_C-3-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    C u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "CdsJ_C-3-Cs2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *4 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "CdsJ_C-3-S2s2",
    group = 
"""
1 *3 C  u1 {2,D} {3,S}
2    C  u0 {1,D}
3 *4 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "CdsJ_C-3-Cd2",
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
    index = 98,
    label = "CdsJ_S-3-2",
    group = 
"""
1 *3 C u1 {2,D} {3,S}
2    S u0 {1,D}
3 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "CsJ-3",
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
    index = 100,
    label = "CsJ-3-Cs",
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
    index = 101,
    label = "CsJ-3-CsHH",
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
    index = 102,
    label = "CsJ-3-CsCsH",
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
    index = 103,
    label = "CsJ-3-CsCsCs",
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
    index = 104,
    label = "CsJ-3-CsS2sH",
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
    index = 105,
    label = "CsJ-3-CsS2sS2s",
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
    index = 106,
    label = "CsJ-3-CsCsS2s",
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
    index = 107,
    label = "CsJ-3-CsOneDe",
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
    index = 108,
    label = "CsJ-3-CsOneDeH",
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
    index = 109,
    label = "CsJ-3-CsCdH",
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
    index = 110,
    label = "CsJ-3-CsOneDeCs",
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
    index = 111,
    label = "CsJ-3-CsCdCs",
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
    index = 112,
    label = "CsJ-3-CsOneDeS2s",
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
    index = 113,
    label = "CsJ-3-CsCdS2s",
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
    index = 114,
    label = "CsJ-3-CsTwoDe",
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
    index = 115,
    label = "CsJ-3-Cd",
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
    index = 116,
    label = "CsJ-3-CdHH",
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
    index = 117,
    label = "CsJ-3-CdCsH",
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
    index = 118,
    label = "CsJ-3-CdCsCs",
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
    index = 119,
    label = "CsJ-3-CdS2sH",
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
    index = 120,
    label = "CsJ-3-CdS2sS2s",
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
    index = 121,
    label = "CsJ-3-CdCsS2s",
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
    index = 122,
    label = "CsJ-3-CdOneDe",
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
    index = 123,
    label = "CsJ-3-CdOneDeH",
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
    index = 124,
    label = "CsJ-3-CdCdH",
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
    index = 125,
    label = "CsJ-3-CdOneDeCs",
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
    index = 126,
    label = "CsJ-3-CdCdCs",
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
    index = 127,
    label = "CsJ-3-CdOneDeS2s",
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
    index = 128,
    label = "CsJ-3-CdCdS2s",
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
    index = 129,
    label = "CsJ-3-CdTwoDe",
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
    index = 130,
    label = "CsJ-3-S2s",
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
    index = 131,
    label = "CsJ-3-S2sHH",
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
    index = 132,
    label = "CsJ-3-S2sCsH",
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
    index = 133,
    label = "CsJ-3-S2sCsCs",
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
    index = 134,
    label = "CsJ-3-S2sS2sH",
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
    index = 135,
    label = "CsJ-3-S2sS2sS2s",
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
    index = 136,
    label = "CsJ-3-S2sCsS2s",
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
    index = 137,
    label = "CsJ-3-S2sOneDe",
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
    index = 138,
    label = "CsJ-3-S2sOneDeH",
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
    index = 139,
    label = "CsJ-3-S2sCdH",
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
    index = 140,
    label = "CsJ-3-S2sOneDeCs",
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
    index = 141,
    label = "CsJ-3-S2sCdCs",
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
    index = 142,
    label = "CsJ-3-S2sOneDeS2s",
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
    index = 143,
    label = "CsJ-3-S2sCdS2s",
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
    index = 144,
    label = "SJ-3",
    group = 
"""
1 *3 S u1 {2,S}
2 *4 R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "S2sJ-3",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "S2sJ-3-Cs",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "S2sJ-3-S2s",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "S2sJ-3-OneDe",
    group = 
"""
1 *3 S2s            u1 {2,S}
2 *4 [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "S2sJ-3-Cd",
    group = 
"""
1 *3 S2s u1 {2,S}
2 *4 Cd u0 {1,S} {3,D}
3    C  u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "C-RRC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 C  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "C-(NonDe)C",
    group = 
"""
1 *1 Cs           u0 {2,S} {3,S} {4,S}
2 *4 C            u0 {1,S}
3    [H,Cs,Os,S2s] u0 {1,S}
4    [H,Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "C-HHC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 C  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "C-CsHC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 C  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "C-CsCsC",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 C  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "C-(OneDe)C",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2 *4 C             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "C-(TwoDe)C",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2 *4 C             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "C-RRS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 S  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "C-(NonDe)S",
    group = 
"""
1 *1 Cs           u0 {2,S} {3,S} {4,S}
2 *4 S            u0 {1,S}
3    [H,Cs,Os,S2s] u0 {1,S}
4    [H,Cs,Os,S2s] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "C-HHS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 S  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "C-CsHS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 S  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "C-CsCsS",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S}
2 *4 S  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "C-(OneDe)S",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2 *4 S             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [H,Cs,Os,S2s]  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "C-(TwoDe)S",
    group = 
"""
1 *1 Cs            u0 {2,S} {3,S} {4,S}
2 *4 S             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "S-H",
    group = 
"""
1 *2 S u0 {2,S}
2    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "S-Cs",
    group = 
"""
1 *2 S  u0 {2,S}
2    Cs u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "S-S2s",
    group = 
"""
1 *2 S  u0 {2,S}
2    S2s u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "S-SJ",
    group = 
"""
1 *2 S  u0 {2,S}
2    S  u1 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: XSYJ
    L2: XSR3J
        L3: XSR3J_S
        L3: XSR3J_D
    L2: XSR4J
        L3: XSR4J_SS
        L3: XSR4J_SD
        L3: XSR4J_DS
        L3: XSR4J_DD
    L2: XSR5J
        L3: XSR5J_SSS
        L3: XSR5J_SSD
        L3: XSR5J_SDS
        L3: XSR5J_DSS
        L3: XSR5J_DDS
        L3: XSR5J_DSD
        L3: XSR5J_SDD
        L3: XSR5J_DDD
    L2: XSR6J
    L2: XSR7J
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
            L4: CdsJ-3-H
            L4: CdsJ-3-Cs
            L4: CdsJ-3-S2s
            L4: CdsJ-3-Cd
        L3: CdsJ-3-2
            L4: CdsJ_C-3-2
                L5: CdsJ_C-3-Cs2
                L5: CdsJ_C-3-S2s2
                L5: CdsJ_C-3-Cd2
            L4: CdsJ_S-3-2
        L3: CsJ-3
            L4: CsJ-3-Cs
                L5: CsJ-3-CsHH
                L5: CsJ-3-CsCsH
                L5: CsJ-3-CsCsCs
                L5: CsJ-3-CsS2sH
                L5: CsJ-3-CsS2sS2s
                L5: CsJ-3-CsCsS2s
                L5: CsJ-3-CsOneDe
                    L6: CsJ-3-CsOneDeH
                        L7: CsJ-3-CsCdH
                    L6: CsJ-3-CsOneDeCs
                        L7: CsJ-3-CsCdCs
                    L6: CsJ-3-CsOneDeS2s
                        L7: CsJ-3-CsCdS2s
                L5: CsJ-3-CsTwoDe
            L4: CsJ-3-Cd
                L5: CsJ-3-CdHH
                L5: CsJ-3-CdCsH
                L5: CsJ-3-CdCsCs
                L5: CsJ-3-CdS2sH
                L5: CsJ-3-CdS2sS2s
                L5: CsJ-3-CdCsS2s
                L5: CsJ-3-CdOneDe
                    L6: CsJ-3-CdOneDeH
                        L7: CsJ-3-CdCdH
                    L6: CsJ-3-CdOneDeCs
                        L7: CsJ-3-CdCdCs
                    L6: CsJ-3-CdOneDeS2s
                        L7: CsJ-3-CdCdS2s
                L5: CsJ-3-CdTwoDe
            L4: CsJ-3-S2s
                L5: CsJ-3-S2sHH
                L5: CsJ-3-S2sCsH
                L5: CsJ-3-S2sCsCs
                L5: CsJ-3-S2sS2sH
                L5: CsJ-3-S2sS2sS2s
                L5: CsJ-3-S2sCsS2s
                L5: CsJ-3-S2sOneDe
                    L6: CsJ-3-S2sOneDeH
                        L7: CsJ-3-S2sCdH
                    L6: CsJ-3-S2sOneDeCs
                        L7: CsJ-3-S2sCdCs
                    L6: CsJ-3-S2sOneDeS2s
                        L7: CsJ-3-S2sCdS2s
    L2: SJ-3
        L3: S2sJ-3
            L4: S2sJ-3-Cs
            L4: S2sJ-3-S2s
            L4: S2sJ-3-OneDe
                L5: S2sJ-3-Cd
L1: C
    L2: Cs
        L3: C-RRR
            L4: C-RRC
                L5: C-(NonDe)C
                    L6: C-HHC
                    L6: C-CsHC
                    L6: C-CsCsC
                L5: C-(OneDe)C
                L5: C-(TwoDe)C
            L4: C-RRS
                L5: C-(NonDe)S
                    L6: C-HHS
                    L6: C-CsHS
                    L6: C-CsCsS
                L5: C-(OneDe)S
                L5: C-(TwoDe)S
    L2: Cds
    L2: Ct 
   
L1: S
    L2: S-H
    L2: S-Cs
    L2: S-S2s
    L2: S-SJ
"""
)

forbidden(
    label = "1and3_bound",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 Cs  u0 {1,[S,D]}
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

