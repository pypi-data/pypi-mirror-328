# Generated from /workspaces/dAngr/src/dAngr/cli/grammar/dAngr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import re as rex

def serializedATN():
    return [
        4,1,81,675,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,3,
        0,68,8,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,76,8,0,10,0,12,0,79,9,0,5,0,
        81,8,0,10,0,12,0,84,9,0,1,0,5,0,87,8,0,10,0,12,0,90,9,0,3,0,92,8,
        0,1,0,1,0,1,1,1,1,1,1,5,1,99,8,1,10,1,12,1,102,9,1,1,1,1,1,1,1,1,
        1,5,1,108,8,1,10,1,12,1,111,9,1,1,1,1,1,1,1,1,1,5,1,117,8,1,10,1,
        12,1,120,9,1,1,1,1,1,1,1,1,1,5,1,126,8,1,10,1,12,1,129,9,1,1,1,1,
        1,3,1,133,8,1,1,2,1,2,1,2,3,2,138,8,2,1,2,1,2,1,2,1,2,1,2,3,2,145,
        8,2,1,2,5,2,148,8,2,10,2,12,2,151,9,2,1,2,3,2,154,8,2,1,3,1,3,1,
        3,3,3,159,8,3,1,3,1,3,3,3,163,8,3,1,3,1,3,3,3,167,8,3,1,3,1,3,3,
        3,171,8,3,1,3,1,3,3,3,175,8,3,1,3,1,3,1,3,1,3,3,3,181,8,3,1,3,1,
        3,3,3,185,8,3,1,3,1,3,1,3,1,3,1,3,3,3,192,8,3,1,3,1,3,3,3,196,8,
        3,1,3,1,3,3,3,200,8,3,1,3,1,3,3,3,204,8,3,1,3,1,3,3,3,208,8,3,1,
        3,1,3,3,3,212,8,3,3,3,214,8,3,3,3,216,8,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,228,8,3,1,3,1,3,3,3,232,8,3,1,3,1,3,1,3,3,
        3,237,8,3,1,3,1,3,1,3,1,3,1,3,5,3,244,8,3,10,3,12,3,247,9,3,1,4,
        1,4,3,4,251,8,4,1,4,3,4,254,8,4,1,4,1,4,3,4,258,8,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,272,8,6,1,7,1,7,1,7,1,7,
        3,7,278,8,7,1,7,1,7,1,7,3,7,283,8,7,1,7,1,7,1,7,1,7,3,7,289,8,7,
        1,7,1,7,3,7,293,8,7,1,7,3,7,296,8,7,1,7,1,7,1,7,1,7,1,7,3,7,303,
        8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,312,8,7,1,7,1,7,1,7,3,7,317,
        8,7,1,8,1,8,3,8,321,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,330,8,9,
        1,9,1,9,3,9,334,8,9,1,9,1,9,3,9,338,8,9,1,9,1,9,1,9,1,10,1,10,1,
        10,3,10,346,8,10,4,10,348,8,10,11,10,12,10,349,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,3,11,360,8,11,1,12,1,12,1,13,1,13,3,13,366,
        8,13,1,13,1,13,3,13,370,8,13,1,13,5,13,373,8,13,10,13,12,13,376,
        9,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,400,8,15,
        1,16,1,16,3,16,404,8,16,1,16,1,16,3,16,408,8,16,1,16,5,16,411,8,
        16,10,16,12,16,414,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,
        423,8,17,10,17,12,17,426,9,17,1,17,4,17,429,8,17,11,17,12,17,430,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,440,8,18,10,18,12,18,443,
        9,18,1,19,1,19,1,19,1,19,3,19,449,8,19,1,19,1,19,1,19,1,19,3,19,
        455,8,19,1,19,1,19,3,19,459,8,19,1,19,1,19,3,19,463,8,19,1,19,3,
        19,466,8,19,1,19,1,19,3,19,470,8,19,3,19,472,8,19,1,20,3,20,475,
        8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,484,8,21,1,21,1,21,
        1,21,1,21,5,21,490,8,21,10,21,12,21,493,9,21,1,22,1,22,1,23,1,23,
        1,23,3,23,500,8,23,1,23,3,23,503,8,23,1,23,1,23,1,23,1,23,1,23,3,
        23,510,8,23,1,23,3,23,513,8,23,1,23,3,23,516,8,23,1,23,1,23,3,23,
        520,8,23,1,23,5,23,523,8,23,10,23,12,23,526,9,23,1,23,3,23,529,8,
        23,1,23,1,23,1,23,3,23,534,8,23,1,23,1,23,3,23,538,8,23,1,23,1,23,
        3,23,542,8,23,1,23,1,23,3,23,546,8,23,1,23,1,23,3,23,550,8,23,1,
        23,1,23,3,23,554,8,23,1,23,1,23,3,23,558,8,23,1,23,1,23,5,23,562,
        8,23,10,23,12,23,565,9,23,1,23,3,23,568,8,23,1,23,1,23,1,23,3,23,
        573,8,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,581,8,23,1,23,1,23,3,
        23,585,8,23,1,23,1,23,1,23,1,23,1,23,3,23,592,8,23,1,23,1,23,3,23,
        596,8,23,1,23,1,23,3,23,600,8,23,1,23,3,23,603,8,23,1,23,3,23,606,
        8,23,1,23,1,23,1,23,1,23,1,23,3,23,613,8,23,1,23,1,23,3,23,617,8,
        23,1,23,1,23,3,23,621,8,23,1,23,1,23,3,23,625,8,23,1,23,1,23,5,23,
        629,8,23,10,23,12,23,632,9,23,1,24,1,24,3,24,636,8,24,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,649,8,25,1,26,
        1,26,1,27,1,27,1,27,3,27,656,8,27,1,28,1,28,1,28,1,28,1,28,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,0,2,
        6,46,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,0,6,2,0,15,15,74,74,1,0,10,11,1,
        0,26,28,1,0,21,22,1,0,1,18,4,0,20,20,40,54,56,78,81,81,808,0,91,
        1,0,0,0,2,132,1,0,0,0,4,153,1,0,0,0,6,236,1,0,0,0,8,250,1,0,0,0,
        10,261,1,0,0,0,12,271,1,0,0,0,14,316,1,0,0,0,16,318,1,0,0,0,18,325,
        1,0,0,0,20,342,1,0,0,0,22,359,1,0,0,0,24,361,1,0,0,0,26,363,1,0,
        0,0,28,377,1,0,0,0,30,399,1,0,0,0,32,401,1,0,0,0,34,428,1,0,0,0,
        36,441,1,0,0,0,38,471,1,0,0,0,40,474,1,0,0,0,42,483,1,0,0,0,44,494,
        1,0,0,0,46,572,1,0,0,0,48,635,1,0,0,0,50,648,1,0,0,0,52,650,1,0,
        0,0,54,655,1,0,0,0,56,657,1,0,0,0,58,662,1,0,0,0,60,667,1,0,0,0,
        62,672,1,0,0,0,64,67,7,0,0,0,65,66,5,20,0,0,66,68,3,42,21,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,92,5,19,0,0,70,81,5,19,0,
        0,71,81,3,2,1,0,72,81,3,18,9,0,73,77,5,56,0,0,74,76,3,50,25,0,75,
        74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,81,1,0,0,
        0,79,77,1,0,0,0,80,70,1,0,0,0,80,71,1,0,0,0,80,72,1,0,0,0,80,73,
        1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,88,1,0,0,0,
        84,82,1,0,0,0,85,87,5,20,0,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,
        0,0,0,88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,64,1,0,0,0,91,
        82,1,0,0,0,92,93,1,0,0,0,93,94,5,0,0,1,94,1,1,0,0,0,95,133,3,14,
        7,0,96,100,3,8,4,0,97,99,5,20,0,0,98,97,1,0,0,0,99,102,1,0,0,0,100,
        98,1,0,0,0,100,101,1,0,0,0,101,103,1,0,0,0,102,100,1,0,0,0,103,104,
        5,19,0,0,104,133,1,0,0,0,105,109,3,4,2,0,106,108,5,20,0,0,107,106,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,
        1,0,0,0,111,109,1,0,0,0,112,113,5,19,0,0,113,133,1,0,0,0,114,118,
        3,10,5,0,115,117,5,20,0,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,
        1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,118,1,0,0,0,121,122,
        5,19,0,0,122,133,1,0,0,0,123,127,3,12,6,0,124,126,5,20,0,0,125,124,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,
        1,0,0,0,129,127,1,0,0,0,130,131,5,19,0,0,131,133,1,0,0,0,132,95,
        1,0,0,0,132,96,1,0,0,0,132,105,1,0,0,0,132,114,1,0,0,0,132,123,1,
        0,0,0,133,3,1,0,0,0,134,135,3,42,21,0,135,136,5,49,0,0,136,138,1,
        0,0,0,137,134,1,0,0,0,137,138,1,0,0,0,138,139,1,0,0,0,139,149,3,
        42,21,0,140,144,5,20,0,0,141,142,3,42,21,0,142,143,5,65,0,0,143,
        145,1,0,0,0,144,141,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        148,3,6,3,0,147,140,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,
        150,1,0,0,0,150,154,1,0,0,0,151,149,1,0,0,0,152,154,3,6,3,0,153,
        137,1,0,0,0,153,152,1,0,0,0,154,5,1,0,0,0,155,156,6,3,-1,0,156,158,
        5,2,0,0,157,159,5,20,0,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,
        1,0,0,0,160,162,3,28,14,0,161,163,5,20,0,0,162,161,1,0,0,0,162,163,
        1,0,0,0,163,164,1,0,0,0,164,166,5,3,0,0,165,167,5,20,0,0,166,165,
        1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,170,3,6,3,0,169,171,
        5,20,0,0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,174,
        5,4,0,0,173,175,5,20,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,
        1,0,0,0,176,177,3,6,3,10,177,237,1,0,0,0,178,180,5,38,0,0,179,181,
        5,20,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,184,
        3,4,2,0,183,185,5,20,0,0,184,183,1,0,0,0,184,185,1,0,0,0,185,186,
        1,0,0,0,186,187,5,39,0,0,187,237,1,0,0,0,188,189,5,5,0,0,189,191,
        5,38,0,0,190,192,5,20,0,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,
        1,0,0,0,193,195,3,6,3,0,194,196,5,20,0,0,195,194,1,0,0,0,195,196,
        1,0,0,0,196,215,1,0,0,0,197,199,5,45,0,0,198,200,5,20,0,0,199,198,
        1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,203,3,6,3,0,202,204,
        5,20,0,0,203,202,1,0,0,0,203,204,1,0,0,0,204,213,1,0,0,0,205,207,
        5,45,0,0,206,208,5,20,0,0,207,206,1,0,0,0,207,208,1,0,0,0,208,209,
        1,0,0,0,209,211,3,6,3,0,210,212,5,20,0,0,211,210,1,0,0,0,211,212,
        1,0,0,0,212,214,1,0,0,0,213,205,1,0,0,0,213,214,1,0,0,0,214,216,
        1,0,0,0,215,197,1,0,0,0,215,216,1,0,0,0,216,217,1,0,0,0,217,218,
        5,39,0,0,218,237,1,0,0,0,219,237,3,54,27,0,220,237,3,38,19,0,221,
        237,5,14,0,0,222,223,5,12,0,0,223,224,5,20,0,0,224,237,3,6,3,3,225,
        227,3,46,23,0,226,228,5,20,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,
        229,1,0,0,0,229,231,3,30,15,0,230,232,5,20,0,0,231,230,1,0,0,0,231,
        232,1,0,0,0,232,233,1,0,0,0,233,234,3,6,3,0,234,237,1,0,0,0,235,
        237,3,46,23,0,236,155,1,0,0,0,236,178,1,0,0,0,236,188,1,0,0,0,236,
        219,1,0,0,0,236,220,1,0,0,0,236,221,1,0,0,0,236,222,1,0,0,0,236,
        225,1,0,0,0,236,235,1,0,0,0,237,245,1,0,0,0,238,239,10,7,0,0,239,
        240,5,20,0,0,240,241,7,1,0,0,241,242,5,20,0,0,242,244,3,6,3,8,243,
        238,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,
        7,1,0,0,0,247,245,1,0,0,0,248,251,3,10,5,0,249,251,3,46,23,0,250,
        248,1,0,0,0,250,249,1,0,0,0,251,253,1,0,0,0,252,254,5,20,0,0,253,
        252,1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,255,257,5,65,0,0,256,
        258,5,20,0,0,257,256,1,0,0,0,257,258,1,0,0,0,258,259,1,0,0,0,259,
        260,3,4,2,0,260,9,1,0,0,0,261,262,5,1,0,0,262,263,5,20,0,0,263,264,
        3,42,21,0,264,11,1,0,0,0,265,266,5,40,0,0,266,272,3,32,16,0,267,
        268,5,41,0,0,268,272,3,4,2,0,269,270,5,42,0,0,270,272,3,36,18,0,
        271,265,1,0,0,0,271,267,1,0,0,0,271,269,1,0,0,0,272,13,1,0,0,0,273,
        274,5,7,0,0,274,275,5,20,0,0,275,277,3,28,14,0,276,278,5,20,0,0,
        277,276,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,5,43,0,0,
        280,282,3,20,10,0,281,283,3,16,8,0,282,281,1,0,0,0,282,283,1,0,0,
        0,283,317,1,0,0,0,284,285,5,9,0,0,285,286,5,20,0,0,286,295,3,42,
        21,0,287,289,5,20,0,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,
        0,0,0,290,292,5,45,0,0,291,293,5,20,0,0,292,291,1,0,0,0,292,293,
        1,0,0,0,293,294,1,0,0,0,294,296,3,42,21,0,295,288,1,0,0,0,295,296,
        1,0,0,0,296,297,1,0,0,0,297,298,5,20,0,0,298,299,5,10,0,0,299,300,
        5,20,0,0,300,302,3,24,12,0,301,303,5,20,0,0,302,301,1,0,0,0,302,
        303,1,0,0,0,303,304,1,0,0,0,304,305,5,43,0,0,305,306,3,20,10,0,306,
        317,1,0,0,0,307,308,5,13,0,0,308,309,5,20,0,0,309,311,3,28,14,0,
        310,312,5,20,0,0,311,310,1,0,0,0,311,312,1,0,0,0,312,313,1,0,0,0,
        313,314,5,43,0,0,314,315,3,20,10,0,315,317,1,0,0,0,316,273,1,0,0,
        0,316,284,1,0,0,0,316,307,1,0,0,0,317,15,1,0,0,0,318,320,5,8,0,0,
        319,321,5,20,0,0,320,319,1,0,0,0,320,321,1,0,0,0,321,322,1,0,0,0,
        322,323,5,43,0,0,323,324,3,20,10,0,324,17,1,0,0,0,325,326,5,6,0,
        0,326,327,5,20,0,0,327,329,3,42,21,0,328,330,5,20,0,0,329,328,1,
        0,0,0,329,330,1,0,0,0,330,331,1,0,0,0,331,333,5,38,0,0,332,334,3,
        26,13,0,333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,337,
        5,39,0,0,336,338,5,20,0,0,337,336,1,0,0,0,337,338,1,0,0,0,338,339,
        1,0,0,0,339,340,5,43,0,0,340,341,3,20,10,0,341,19,1,0,0,0,342,347,
        5,79,0,0,343,345,3,22,11,0,344,346,5,19,0,0,345,344,1,0,0,0,345,
        346,1,0,0,0,346,348,1,0,0,0,347,343,1,0,0,0,348,349,1,0,0,0,349,
        347,1,0,0,0,349,350,1,0,0,0,350,351,1,0,0,0,351,352,5,80,0,0,352,
        21,1,0,0,0,353,360,5,17,0,0,354,360,5,18,0,0,355,356,5,16,0,0,356,
        357,5,20,0,0,357,360,3,4,2,0,358,360,3,2,1,0,359,353,1,0,0,0,359,
        354,1,0,0,0,359,355,1,0,0,0,359,358,1,0,0,0,360,23,1,0,0,0,361,362,
        3,4,2,0,362,25,1,0,0,0,363,374,3,42,21,0,364,366,5,20,0,0,365,364,
        1,0,0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,369,5,45,0,0,368,370,
        5,20,0,0,369,368,1,0,0,0,369,370,1,0,0,0,370,371,1,0,0,0,371,373,
        3,42,21,0,372,365,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,
        1,0,0,0,375,27,1,0,0,0,376,374,1,0,0,0,377,378,3,4,2,0,378,29,1,
        0,0,0,379,400,5,59,0,0,380,400,5,78,0,0,381,400,5,58,0,0,382,400,
        5,60,0,0,383,400,5,57,0,0,384,400,5,64,0,0,385,400,5,66,0,0,386,
        400,5,67,0,0,387,400,5,69,0,0,388,400,5,68,0,0,389,400,5,70,0,0,
        390,400,5,71,0,0,391,400,5,72,0,0,392,400,5,55,0,0,393,394,5,73,
        0,0,394,400,5,61,0,0,395,400,5,62,0,0,396,400,5,63,0,0,397,400,5,
        41,0,0,398,400,5,50,0,0,399,379,1,0,0,0,399,380,1,0,0,0,399,381,
        1,0,0,0,399,382,1,0,0,0,399,383,1,0,0,0,399,384,1,0,0,0,399,385,
        1,0,0,0,399,386,1,0,0,0,399,387,1,0,0,0,399,388,1,0,0,0,399,389,
        1,0,0,0,399,390,1,0,0,0,399,391,1,0,0,0,399,392,1,0,0,0,399,393,
        1,0,0,0,399,395,1,0,0,0,399,396,1,0,0,0,399,397,1,0,0,0,399,398,
        1,0,0,0,400,31,1,0,0,0,401,403,3,42,21,0,402,404,5,20,0,0,403,402,
        1,0,0,0,403,404,1,0,0,0,404,405,1,0,0,0,405,407,5,38,0,0,406,408,
        5,20,0,0,407,406,1,0,0,0,407,408,1,0,0,0,408,412,1,0,0,0,409,411,
        3,34,17,0,410,409,1,0,0,0,411,414,1,0,0,0,412,410,1,0,0,0,412,413,
        1,0,0,0,413,415,1,0,0,0,414,412,1,0,0,0,415,416,5,39,0,0,416,33,
        1,0,0,0,417,429,3,38,19,0,418,429,3,54,27,0,419,429,3,48,24,0,420,
        424,5,38,0,0,421,423,3,34,17,0,422,421,1,0,0,0,423,426,1,0,0,0,424,
        422,1,0,0,0,424,425,1,0,0,0,425,427,1,0,0,0,426,424,1,0,0,0,427,
        429,5,39,0,0,428,417,1,0,0,0,428,418,1,0,0,0,428,419,1,0,0,0,428,
        420,1,0,0,0,429,430,1,0,0,0,430,428,1,0,0,0,430,431,1,0,0,0,431,
        35,1,0,0,0,432,440,3,38,19,0,433,440,3,54,27,0,434,440,3,48,24,0,
        435,436,5,38,0,0,436,437,3,36,18,0,437,438,5,39,0,0,438,440,1,0,
        0,0,439,432,1,0,0,0,439,433,1,0,0,0,439,434,1,0,0,0,439,435,1,0,
        0,0,440,443,1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,37,1,0,0,
        0,443,441,1,0,0,0,444,445,7,2,0,0,445,446,5,49,0,0,446,448,3,42,
        21,0,447,449,5,40,0,0,448,447,1,0,0,0,448,449,1,0,0,0,449,472,1,
        0,0,0,450,472,5,30,0,0,451,452,5,29,0,0,452,454,5,51,0,0,453,455,
        5,20,0,0,454,453,1,0,0,0,454,455,1,0,0,0,455,456,1,0,0,0,456,465,
        3,40,20,0,457,459,5,20,0,0,458,457,1,0,0,0,458,459,1,0,0,0,459,460,
        1,0,0,0,460,462,5,37,0,0,461,463,5,20,0,0,462,461,1,0,0,0,462,463,
        1,0,0,0,463,464,1,0,0,0,464,466,3,40,20,0,465,458,1,0,0,0,465,466,
        1,0,0,0,466,467,1,0,0,0,467,469,5,52,0,0,468,470,5,40,0,0,469,468,
        1,0,0,0,469,470,1,0,0,0,470,472,1,0,0,0,471,444,1,0,0,0,471,450,
        1,0,0,0,471,451,1,0,0,0,472,39,1,0,0,0,473,475,5,78,0,0,474,473,
        1,0,0,0,474,475,1,0,0,0,475,476,1,0,0,0,476,477,3,4,2,0,477,41,1,
        0,0,0,478,484,5,24,0,0,479,484,5,77,0,0,480,481,3,52,26,0,481,482,
        5,77,0,0,482,484,1,0,0,0,483,478,1,0,0,0,483,479,1,0,0,0,483,480,
        1,0,0,0,484,491,1,0,0,0,485,490,5,24,0,0,486,490,5,22,0,0,487,490,
        5,77,0,0,488,490,3,52,26,0,489,485,1,0,0,0,489,486,1,0,0,0,489,487,
        1,0,0,0,489,488,1,0,0,0,490,493,1,0,0,0,491,489,1,0,0,0,491,492,
        1,0,0,0,492,43,1,0,0,0,493,491,1,0,0,0,494,495,7,3,0,0,495,45,1,
        0,0,0,496,497,6,23,-1,0,497,499,3,42,21,0,498,500,5,40,0,0,499,498,
        1,0,0,0,499,500,1,0,0,0,500,573,1,0,0,0,501,503,5,78,0,0,502,501,
        1,0,0,0,502,503,1,0,0,0,503,504,1,0,0,0,504,573,3,44,22,0,505,573,
        5,14,0,0,506,573,3,38,19,0,507,509,5,51,0,0,508,510,5,20,0,0,509,
        508,1,0,0,0,509,510,1,0,0,0,510,512,1,0,0,0,511,513,3,46,23,0,512,
        511,1,0,0,0,512,513,1,0,0,0,513,524,1,0,0,0,514,516,5,20,0,0,515,
        514,1,0,0,0,515,516,1,0,0,0,516,517,1,0,0,0,517,519,5,45,0,0,518,
        520,5,20,0,0,519,518,1,0,0,0,519,520,1,0,0,0,520,521,1,0,0,0,521,
        523,3,46,23,0,522,515,1,0,0,0,523,526,1,0,0,0,524,522,1,0,0,0,524,
        525,1,0,0,0,525,528,1,0,0,0,526,524,1,0,0,0,527,529,5,20,0,0,528,
        527,1,0,0,0,528,529,1,0,0,0,529,530,1,0,0,0,530,573,5,52,0,0,531,
        533,5,53,0,0,532,534,5,20,0,0,533,532,1,0,0,0,533,534,1,0,0,0,534,
        563,1,0,0,0,535,537,5,31,0,0,536,538,5,20,0,0,537,536,1,0,0,0,537,
        538,1,0,0,0,538,539,1,0,0,0,539,541,5,43,0,0,540,542,5,20,0,0,541,
        540,1,0,0,0,541,542,1,0,0,0,542,543,1,0,0,0,543,545,3,46,23,0,544,
        546,5,20,0,0,545,544,1,0,0,0,545,546,1,0,0,0,546,547,1,0,0,0,547,
        549,5,45,0,0,548,550,5,20,0,0,549,548,1,0,0,0,549,550,1,0,0,0,550,
        551,1,0,0,0,551,553,5,31,0,0,552,554,5,20,0,0,553,552,1,0,0,0,553,
        554,1,0,0,0,554,555,1,0,0,0,555,557,5,43,0,0,556,558,5,20,0,0,557,
        556,1,0,0,0,557,558,1,0,0,0,558,559,1,0,0,0,559,560,3,46,23,0,560,
        562,1,0,0,0,561,535,1,0,0,0,562,565,1,0,0,0,563,561,1,0,0,0,563,
        564,1,0,0,0,564,567,1,0,0,0,565,563,1,0,0,0,566,568,5,20,0,0,567,
        566,1,0,0,0,567,568,1,0,0,0,568,569,1,0,0,0,569,573,5,54,0,0,570,
        573,5,31,0,0,571,573,5,32,0,0,572,496,1,0,0,0,572,502,1,0,0,0,572,
        505,1,0,0,0,572,506,1,0,0,0,572,507,1,0,0,0,572,531,1,0,0,0,572,
        570,1,0,0,0,572,571,1,0,0,0,573,630,1,0,0,0,574,575,10,8,0,0,575,
        576,5,49,0,0,576,629,3,42,21,0,577,578,10,7,0,0,578,580,5,51,0,0,
        579,581,5,20,0,0,580,579,1,0,0,0,580,581,1,0,0,0,581,582,1,0,0,0,
        582,584,3,40,20,0,583,585,5,20,0,0,584,583,1,0,0,0,584,585,1,0,0,
        0,585,586,1,0,0,0,586,587,5,52,0,0,587,629,1,0,0,0,588,589,10,6,
        0,0,589,591,5,51,0,0,590,592,5,20,0,0,591,590,1,0,0,0,591,592,1,
        0,0,0,592,593,1,0,0,0,593,595,3,40,20,0,594,596,5,20,0,0,595,594,
        1,0,0,0,595,596,1,0,0,0,596,597,1,0,0,0,597,599,5,43,0,0,598,600,
        5,20,0,0,599,598,1,0,0,0,599,600,1,0,0,0,600,602,1,0,0,0,601,603,
        3,40,20,0,602,601,1,0,0,0,602,603,1,0,0,0,603,605,1,0,0,0,604,606,
        5,20,0,0,605,604,1,0,0,0,605,606,1,0,0,0,606,607,1,0,0,0,607,608,
        5,52,0,0,608,629,1,0,0,0,609,610,10,5,0,0,610,612,5,51,0,0,611,613,
        5,20,0,0,612,611,1,0,0,0,612,613,1,0,0,0,613,614,1,0,0,0,614,616,
        3,40,20,0,615,617,5,20,0,0,616,615,1,0,0,0,616,617,1,0,0,0,617,618,
        1,0,0,0,618,620,5,37,0,0,619,621,5,20,0,0,620,619,1,0,0,0,620,621,
        1,0,0,0,621,622,1,0,0,0,622,624,3,40,20,0,623,625,5,20,0,0,624,623,
        1,0,0,0,624,625,1,0,0,0,625,626,1,0,0,0,626,627,5,52,0,0,627,629,
        1,0,0,0,628,574,1,0,0,0,628,577,1,0,0,0,628,588,1,0,0,0,628,609,
        1,0,0,0,629,632,1,0,0,0,630,628,1,0,0,0,630,631,1,0,0,0,631,47,1,
        0,0,0,632,630,1,0,0,0,633,636,3,50,25,0,634,636,5,19,0,0,635,633,
        1,0,0,0,635,634,1,0,0,0,636,49,1,0,0,0,637,649,5,24,0,0,638,649,
        5,22,0,0,639,649,3,62,31,0,640,649,5,31,0,0,641,649,5,32,0,0,642,
        649,5,20,0,0,643,644,5,38,0,0,644,645,3,48,24,0,645,646,5,39,0,0,
        646,649,1,0,0,0,647,649,3,52,26,0,648,637,1,0,0,0,648,638,1,0,0,
        0,648,639,1,0,0,0,648,640,1,0,0,0,648,641,1,0,0,0,648,642,1,0,0,
        0,648,643,1,0,0,0,648,647,1,0,0,0,649,51,1,0,0,0,650,651,7,4,0,0,
        651,53,1,0,0,0,652,656,3,56,28,0,653,656,3,58,29,0,654,656,3,60,
        30,0,655,652,1,0,0,0,655,653,1,0,0,0,655,654,1,0,0,0,656,55,1,0,
        0,0,657,658,5,41,0,0,658,659,5,38,0,0,659,660,3,4,2,0,660,661,5,
        39,0,0,661,57,1,0,0,0,662,663,5,42,0,0,663,664,5,38,0,0,664,665,
        3,36,18,0,665,666,5,39,0,0,666,59,1,0,0,0,667,668,5,40,0,0,668,669,
        5,38,0,0,669,670,3,34,17,0,670,671,5,39,0,0,671,61,1,0,0,0,672,673,
        7,5,0,0,673,63,1,0,0,0,110,67,77,80,82,88,91,100,109,118,127,132,
        137,144,149,153,158,162,166,170,174,180,184,191,195,199,203,207,
        211,213,215,227,231,236,245,250,253,257,271,277,282,288,292,295,
        302,311,316,320,329,333,337,345,349,359,365,369,374,399,403,407,
        412,424,428,430,439,441,448,454,458,462,465,469,471,474,483,489,
        491,499,502,509,512,515,519,524,528,533,537,541,545,549,553,557,
        563,567,572,580,584,591,595,599,602,605,612,616,620,624,628,630,
        635,648,655
    ]

class dAngrParser ( Parser ):

    grammarFileName = "dAngr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'static'", "'IIF'", "'THEN'", "'ELSE'", 
                     "'range'", "'def'", "'if'", "'else'", "'for'", "'in'", 
                     "'not in'", "'not'", "'while'", "<INVALID>", "'help'", 
                     "'return'", "'break'", "'continue'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'&sym'", "'&reg'", "'&vars'", "'&mem'", 
                     "'&state'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'->'", "'('", 
                     "')'", "'!'", "'&'", "'$'", "':'", "';'", "','", "'\"'", 
                     "'''", "'@'", "'.'", "'|'", "'['", "']'", "'{'", "'}'", 
                     "'^'", "'#'", "'%'", "'*'", "'+'", "'/'", "'//'", "'<<'", 
                     "'>>'", "'**'", "'='", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'&&'", "'||'", "'?'", "'~'", "'`'", 
                     "'_'", "'-'" ]

    symbolicNames = [ "<INVALID>", "STATIC", "CIF", "CTHEN", "CELSE", "RANGE", 
                      "DEF", "IF", "ELSE", "FOR", "IN", "NOT_IN", "NOT", 
                      "WHILE", "BOOL", "HELP", "RETURN", "BREAK", "CONTINUE", 
                      "NEWLINE", "WS", "HEX_NUMBERS", "NUMBERS", "NUMBER", 
                      "LETTERS", "LETTER", "SYM_DB", "REG_DB", "VARS_DB", 
                      "MEM_DB", "STATE", "STRING", "BINARY_STRING", "ESCAPED_QUOTE", 
                      "ESCAPED_SINGLE_QUOTE", "SESC_SEQ", "ESC_SEQ", "ARROW", 
                      "LPAREN", "RPAREN", "BANG", "AMP", "DOLLAR", "COLON", 
                      "SCOLON", "COMMA", "QUOTE", "SQUOTE", "AT", "DOT", 
                      "BAR", "BRA", "KET", "BRACE", "KETCE", "XOR", "HASH", 
                      "PERC", "MUL", "ADD", "DIV", "FLOORDIV", "LSHIFT", 
                      "RSHIFT", "POW", "ASSIGN", "EQ", "NEQ", "LT", "GT", 
                      "LE", "GE", "AND", "OR", "QMARK", "TILDE", "TICK", 
                      "UNDERSCORE", "DASH", "INDENT", "DEDENT", "HAT" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_expression_part = 3
    RULE_assignment = 4
    RULE_static_var = 5
    RULE_ext_command = 6
    RULE_control_flow = 7
    RULE_else_ = 8
    RULE_function_def = 9
    RULE_body = 10
    RULE_fstatement = 11
    RULE_iterable = 12
    RULE_parameters = 13
    RULE_condition = 14
    RULE_operation = 15
    RULE_py_basic_content = 16
    RULE_py_content = 17
    RULE_bash_content = 18
    RULE_reference = 19
    RULE_index = 20
    RULE_identifier = 21
    RULE_numeric = 22
    RULE_object = 23
    RULE_anything = 24
    RULE_anything_no = 25
    RULE_special_words = 26
    RULE_range = 27
    RULE_dangr_range = 28
    RULE_bash_range = 29
    RULE_python_range = 30
    RULE_symbol = 31

    ruleNames =  [ "script", "statement", "expression", "expression_part", 
                   "assignment", "static_var", "ext_command", "control_flow", 
                   "else_", "function_def", "body", "fstatement", "iterable", 
                   "parameters", "condition", "operation", "py_basic_content", 
                   "py_content", "bash_content", "reference", "index", "identifier", 
                   "numeric", "object", "anything", "anything_no", "special_words", 
                   "range", "dangr_range", "bash_range", "python_range", 
                   "symbol" ]

    EOF = Token.EOF
    STATIC=1
    CIF=2
    CTHEN=3
    CELSE=4
    RANGE=5
    DEF=6
    IF=7
    ELSE=8
    FOR=9
    IN=10
    NOT_IN=11
    NOT=12
    WHILE=13
    BOOL=14
    HELP=15
    RETURN=16
    BREAK=17
    CONTINUE=18
    NEWLINE=19
    WS=20
    HEX_NUMBERS=21
    NUMBERS=22
    NUMBER=23
    LETTERS=24
    LETTER=25
    SYM_DB=26
    REG_DB=27
    VARS_DB=28
    MEM_DB=29
    STATE=30
    STRING=31
    BINARY_STRING=32
    ESCAPED_QUOTE=33
    ESCAPED_SINGLE_QUOTE=34
    SESC_SEQ=35
    ESC_SEQ=36
    ARROW=37
    LPAREN=38
    RPAREN=39
    BANG=40
    AMP=41
    DOLLAR=42
    COLON=43
    SCOLON=44
    COMMA=45
    QUOTE=46
    SQUOTE=47
    AT=48
    DOT=49
    BAR=50
    BRA=51
    KET=52
    BRACE=53
    KETCE=54
    XOR=55
    HASH=56
    PERC=57
    MUL=58
    ADD=59
    DIV=60
    FLOORDIV=61
    LSHIFT=62
    RSHIFT=63
    POW=64
    ASSIGN=65
    EQ=66
    NEQ=67
    LT=68
    GT=69
    LE=70
    GE=71
    AND=72
    OR=73
    QMARK=74
    TILDE=75
    TICK=76
    UNDERSCORE=77
    DASH=78
    INDENT=79
    DEDENT=80
    HAT=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(dAngrParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.NEWLINE)
            else:
                return self.getToken(dAngrParser.NEWLINE, i)

        def QMARK(self):
            return self.getToken(dAngrParser.QMARK, 0)

        def HELP(self):
            return self.getToken(dAngrParser.HELP, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.StatementContext)
            else:
                return self.getTypedRuleContext(dAngrParser.StatementContext,i)


        def function_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Function_defContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Function_defContext,i)


        def HASH(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.HASH)
            else:
                return self.getToken(dAngrParser.HASH, i)

        def anything_no(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Anything_noContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Anything_noContext,i)


        def getRuleIndex(self):
            return dAngrParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = dAngrParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 64
                _la = self._input.LA(1)
                if not(_la==15 or _la==74):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 65
                    self.match(dAngrParser.WS)
                    self.state = 66
                    self.identifier()


                self.state = 69
                self.match(dAngrParser.NEWLINE)
                pass

            elif la_ == 2:
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 83324573112598526) != 0) or _la==77 or _la==78:
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 70
                        self.match(dAngrParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        self.state = 71
                        self.statement()
                        pass

                    elif la_ == 3:
                        self.state = 72
                        self.function_def()
                        pass

                    elif la_ == 4:
                        self.state = 73
                        self.match(dAngrParser.HASH)
                        self.state = 77
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 74
                                self.anything_no() 
                            self.state = 79
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                        pass


                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 85
                    self.match(dAngrParser.WS)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 93
            self.match(dAngrParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control_flow(self):
            return self.getTypedRuleContext(dAngrParser.Control_flowContext,0)


        def assignment(self):
            return self.getTypedRuleContext(dAngrParser.AssignmentContext,0)


        def NEWLINE(self):
            return self.getToken(dAngrParser.NEWLINE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def static_var(self):
            return self.getTypedRuleContext(dAngrParser.Static_varContext,0)


        def ext_command(self):
            return self.getTypedRuleContext(dAngrParser.Ext_commandContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = dAngrParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.control_flow()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.assignment()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 97
                    self.match(dAngrParser.WS)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(dAngrParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.expression()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 106
                    self.match(dAngrParser.WS)
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 112
                self.match(dAngrParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.static_var()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 115
                    self.match(dAngrParser.WS)
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                self.match(dAngrParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.ext_command()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 124
                    self.match(dAngrParser.WS)
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(dAngrParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IdentifierContext,i)


        def DOT(self):
            return self.getToken(dAngrParser.DOT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def expression_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Expression_partContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Expression_partContext,i)


        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.ASSIGN)
            else:
                return self.getToken(dAngrParser.ASSIGN, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = dAngrParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 134
                    self.identifier()
                    self.state = 135
                    self.match(dAngrParser.DOT)


                self.state = 139
                self.identifier()
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 140
                        self.match(dAngrParser.WS)
                        self.state = 144
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                        if la_ == 1:
                            self.state = 141
                            self.identifier()
                            self.state = 142
                            self.match(dAngrParser.ASSIGN)


                        self.state = 146
                        self.expression_part(0) 
                    self.state = 151
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.expression_part(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dAngrParser.RULE_expression_part

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionRangeContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RANGE(self):
            return self.getToken(dAngrParser.RANGE, 0)
        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)
        def expression_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Expression_partContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Expression_partContext,i)

        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.COMMA)
            else:
                return self.getToken(dAngrParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionRange" ):
                listener.enterExpressionRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionRange" ):
                listener.exitExpressionRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionRange" ):
                return visitor.visitExpressionRange(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionInContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Expression_partContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Expression_partContext,i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)
        def IN(self):
            return self.getToken(dAngrParser.IN, 0)
        def NOT_IN(self):
            return self.getToken(dAngrParser.NOT_IN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionIn" ):
                listener.enterExpressionIn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionIn" ):
                listener.exitExpressionIn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionIn" ):
                return visitor.visitExpressionIn(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionNotContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(dAngrParser.NOT, 0)
        def WS(self):
            return self.getToken(dAngrParser.WS, 0)
        def expression_part(self):
            return self.getTypedRuleContext(dAngrParser.Expression_partContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionNot" ):
                listener.enterExpressionNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionNot" ):
                listener.exitExpressionNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionNot" ):
                return visitor.visitExpressionNot(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionObjectContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionObject" ):
                listener.enterExpressionObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionObject" ):
                listener.exitExpressionObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionObject" ):
                return visitor.visitExpressionObject(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBoolContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(dAngrParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBool" ):
                listener.enterExpressionBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBool" ):
                listener.exitExpressionBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBool" ):
                return visitor.visitExpressionBool(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionReferenceContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reference(self):
            return self.getTypedRuleContext(dAngrParser.ReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionReference" ):
                listener.enterExpressionReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionReference" ):
                listener.exitExpressionReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionReference" ):
                return visitor.visitExpressionReference(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionIfContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CIF(self):
            return self.getToken(dAngrParser.CIF, 0)
        def condition(self):
            return self.getTypedRuleContext(dAngrParser.ConditionContext,0)

        def CTHEN(self):
            return self.getToken(dAngrParser.CTHEN, 0)
        def expression_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Expression_partContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Expression_partContext,i)

        def CELSE(self):
            return self.getToken(dAngrParser.CELSE, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionIf" ):
                listener.enterExpressionIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionIf" ):
                listener.exitExpressionIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionIf" ):
                return visitor.visitExpressionIf(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionAltContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def range_(self):
            return self.getTypedRuleContext(dAngrParser.RangeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAlt" ):
                listener.enterExpressionAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAlt" ):
                listener.exitExpressionAlt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAlt" ):
                return visitor.visitExpressionAlt(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionParenthesisContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionParenthesis" ):
                listener.enterExpressionParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionParenthesis" ):
                listener.exitExpressionParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionParenthesis" ):
                return visitor.visitExpressionParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionOperationContext(Expression_partContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.Expression_partContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)

        def operation(self):
            return self.getTypedRuleContext(dAngrParser.OperationContext,0)

        def expression_part(self):
            return self.getTypedRuleContext(dAngrParser.Expression_partContext,0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionOperation" ):
                listener.enterExpressionOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionOperation" ):
                listener.exitExpressionOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionOperation" ):
                return visitor.visitExpressionOperation(self)
            else:
                return visitor.visitChildren(self)



    def expression_part(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = dAngrParser.Expression_partContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression_part, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = dAngrParser.ExpressionIfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 156
                self.match(dAngrParser.CIF)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 157
                    self.match(dAngrParser.WS)


                self.state = 160
                self.condition()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 161
                    self.match(dAngrParser.WS)


                self.state = 164
                self.match(dAngrParser.CTHEN)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 165
                    self.match(dAngrParser.WS)


                self.state = 168
                self.expression_part(0)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 169
                    self.match(dAngrParser.WS)


                self.state = 172
                self.match(dAngrParser.CELSE)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 173
                    self.match(dAngrParser.WS)


                self.state = 176
                self.expression_part(10)
                pass

            elif la_ == 2:
                localctx = dAngrParser.ExpressionParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.match(dAngrParser.LPAREN)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 179
                    self.match(dAngrParser.WS)


                self.state = 182
                self.expression()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 183
                    self.match(dAngrParser.WS)


                self.state = 186
                self.match(dAngrParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = dAngrParser.ExpressionRangeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(dAngrParser.RANGE)
                self.state = 189
                self.match(dAngrParser.LPAREN)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 190
                    self.match(dAngrParser.WS)


                self.state = 193
                self.expression_part(0)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 194
                    self.match(dAngrParser.WS)


                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 197
                    self.match(dAngrParser.COMMA)
                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 198
                        self.match(dAngrParser.WS)


                    self.state = 201
                    self.expression_part(0)
                    self.state = 203
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 202
                        self.match(dAngrParser.WS)


                    self.state = 213
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==45:
                        self.state = 205
                        self.match(dAngrParser.COMMA)
                        self.state = 207
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 206
                            self.match(dAngrParser.WS)


                        self.state = 209
                        self.expression_part(0)
                        self.state = 211
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 210
                            self.match(dAngrParser.WS)






                self.state = 217
                self.match(dAngrParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = dAngrParser.ExpressionAltContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 219
                self.range_()
                pass

            elif la_ == 5:
                localctx = dAngrParser.ExpressionReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 220
                self.reference()
                pass

            elif la_ == 6:
                localctx = dAngrParser.ExpressionBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 221
                self.match(dAngrParser.BOOL)
                pass

            elif la_ == 7:
                localctx = dAngrParser.ExpressionNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 222
                self.match(dAngrParser.NOT)
                self.state = 223
                self.match(dAngrParser.WS)
                self.state = 224
                self.expression_part(3)
                pass

            elif la_ == 8:
                localctx = dAngrParser.ExpressionOperationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 225
                self.object_(0)

                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 226
                    self.match(dAngrParser.WS)


                self.state = 229
                self.operation()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 230
                    self.match(dAngrParser.WS)


                self.state = 233
                self.expression_part(0)
                pass

            elif la_ == 9:
                localctx = dAngrParser.ExpressionObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 235
                self.object_(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = dAngrParser.ExpressionInContext(self, dAngrParser.Expression_partContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_part)
                    self.state = 238
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 239
                    self.match(dAngrParser.WS)
                    self.state = 240
                    _la = self._input.LA(1)
                    if not(_la==10 or _la==11):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.match(dAngrParser.WS)
                    self.state = 242
                    self.expression_part(8) 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(dAngrParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def static_var(self):
            return self.getTypedRuleContext(dAngrParser.Static_varContext,0)


        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = dAngrParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 248
                self.static_var()
                pass

            elif la_ == 2:
                self.state = 249
                self.object_(0)
                pass


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 252
                self.match(dAngrParser.WS)


            self.state = 255
            self.match(dAngrParser.ASSIGN)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 256
                self.match(dAngrParser.WS)


            self.state = 259
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(dAngrParser.STATIC, 0)

        def WS(self):
            return self.getToken(dAngrParser.WS, 0)

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_static_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_var" ):
                listener.enterStatic_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_var" ):
                listener.exitStatic_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_var" ):
                return visitor.visitStatic_var(self)
            else:
                return visitor.visitChildren(self)




    def static_var(self):

        localctx = dAngrParser.Static_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_static_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(dAngrParser.STATIC)
            self.state = 262
            self.match(dAngrParser.WS)
            self.state = 263
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ext_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(dAngrParser.BANG, 0)

        def py_basic_content(self):
            return self.getTypedRuleContext(dAngrParser.Py_basic_contentContext,0)


        def AMP(self):
            return self.getToken(dAngrParser.AMP, 0)

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def DOLLAR(self):
            return self.getToken(dAngrParser.DOLLAR, 0)

        def bash_content(self):
            return self.getTypedRuleContext(dAngrParser.Bash_contentContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_ext_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExt_command" ):
                listener.enterExt_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExt_command" ):
                listener.exitExt_command(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExt_command" ):
                return visitor.visitExt_command(self)
            else:
                return visitor.visitChildren(self)




    def ext_command(self):

        localctx = dAngrParser.Ext_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ext_command)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(dAngrParser.BANG)
                self.state = 266
                self.py_basic_content()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(dAngrParser.AMP)
                self.state = 268
                self.expression()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(dAngrParser.DOLLAR)
                self.state = 270
                self.bash_content()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_flowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(dAngrParser.IF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def condition(self):
            return self.getTypedRuleContext(dAngrParser.ConditionContext,0)


        def COLON(self):
            return self.getToken(dAngrParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(dAngrParser.BodyContext,0)


        def else_(self):
            return self.getTypedRuleContext(dAngrParser.Else_Context,0)


        def FOR(self):
            return self.getToken(dAngrParser.FOR, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IdentifierContext,i)


        def IN(self):
            return self.getToken(dAngrParser.IN, 0)

        def iterable(self):
            return self.getTypedRuleContext(dAngrParser.IterableContext,0)


        def COMMA(self):
            return self.getToken(dAngrParser.COMMA, 0)

        def WHILE(self):
            return self.getToken(dAngrParser.WHILE, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_control_flow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl_flow" ):
                listener.enterControl_flow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl_flow" ):
                listener.exitControl_flow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_flow" ):
                return visitor.visitControl_flow(self)
            else:
                return visitor.visitChildren(self)




    def control_flow(self):

        localctx = dAngrParser.Control_flowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_control_flow)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(dAngrParser.IF)
                self.state = 274
                self.match(dAngrParser.WS)
                self.state = 275
                self.condition()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 276
                    self.match(dAngrParser.WS)


                self.state = 279
                self.match(dAngrParser.COLON)
                self.state = 280
                self.body()
                self.state = 282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 281
                    self.else_()


                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(dAngrParser.FOR)
                self.state = 285
                self.match(dAngrParser.WS)
                self.state = 286
                self.identifier()
                self.state = 295
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 287
                        self.match(dAngrParser.WS)


                    self.state = 290
                    self.match(dAngrParser.COMMA)
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 291
                        self.match(dAngrParser.WS)


                    self.state = 294
                    self.identifier()


                self.state = 297
                self.match(dAngrParser.WS)
                self.state = 298
                self.match(dAngrParser.IN)
                self.state = 299
                self.match(dAngrParser.WS)
                self.state = 300
                self.iterable()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 301
                    self.match(dAngrParser.WS)


                self.state = 304
                self.match(dAngrParser.COLON)
                self.state = 305
                self.body()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.match(dAngrParser.WHILE)
                self.state = 308
                self.match(dAngrParser.WS)
                self.state = 309
                self.condition()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 310
                    self.match(dAngrParser.WS)


                self.state = 313
                self.match(dAngrParser.COLON)
                self.state = 314
                self.body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(dAngrParser.ELSE, 0)

        def COLON(self):
            return self.getToken(dAngrParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(dAngrParser.BodyContext,0)


        def WS(self):
            return self.getToken(dAngrParser.WS, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_else_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_" ):
                listener.enterElse_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_" ):
                listener.exitElse_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_" ):
                return visitor.visitElse_(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = dAngrParser.Else_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(dAngrParser.ELSE)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 319
                self.match(dAngrParser.WS)


            self.state = 322
            self.match(dAngrParser.COLON)
            self.state = 323
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(dAngrParser.DEF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(dAngrParser.COLON, 0)

        def body(self):
            return self.getTypedRuleContext(dAngrParser.BodyContext,0)


        def parameters(self):
            return self.getTypedRuleContext(dAngrParser.ParametersContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = dAngrParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(dAngrParser.DEF)
            self.state = 326
            self.match(dAngrParser.WS)
            self.state = 327
            self.identifier()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 328
                self.match(dAngrParser.WS)


            self.state = 331
            self.match(dAngrParser.LPAREN)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17301502) != 0) or _la==77:
                self.state = 332
                self.parameters()


            self.state = 335
            self.match(dAngrParser.RPAREN)
            self.state = 337
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 336
                self.match(dAngrParser.WS)


            self.state = 339
            self.match(dAngrParser.COLON)
            self.state = 340
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(dAngrParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(dAngrParser.DEDENT, 0)

        def fstatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.FstatementContext)
            else:
                return self.getTypedRuleContext(dAngrParser.FstatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.NEWLINE)
            else:
                return self.getToken(dAngrParser.NEWLINE, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = dAngrParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(dAngrParser.INDENT)
            self.state = 347 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 343
                self.fstatement()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 344
                    self.match(dAngrParser.NEWLINE)


                self.state = 349 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 11266979074146302) != 0) or _la==77 or _la==78):
                    break

            self.state = 351
            self.match(dAngrParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(dAngrParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(dAngrParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(dAngrParser.RETURN, 0)

        def WS(self):
            return self.getToken(dAngrParser.WS, 0)

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(dAngrParser.StatementContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_fstatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFstatement" ):
                listener.enterFstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFstatement" ):
                listener.exitFstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFstatement" ):
                return visitor.visitFstatement(self)
            else:
                return visitor.visitChildren(self)




    def fstatement(self):

        localctx = dAngrParser.FstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fstatement)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(dAngrParser.BREAK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(dAngrParser.CONTINUE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(dAngrParser.RETURN)
                self.state = 356
                self.match(dAngrParser.WS)
                self.state = 357
                self.expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = dAngrParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.COMMA)
            else:
                return self.getToken(dAngrParser.COMMA, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = dAngrParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.identifier()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==45:
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 364
                    self.match(dAngrParser.WS)


                self.state = 367
                self.match(dAngrParser.COMMA)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 368
                    self.match(dAngrParser.WS)


                self.state = 371
                self.identifier()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = dAngrParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(dAngrParser.ADD, 0)

        def DASH(self):
            return self.getToken(dAngrParser.DASH, 0)

        def MUL(self):
            return self.getToken(dAngrParser.MUL, 0)

        def DIV(self):
            return self.getToken(dAngrParser.DIV, 0)

        def PERC(self):
            return self.getToken(dAngrParser.PERC, 0)

        def POW(self):
            return self.getToken(dAngrParser.POW, 0)

        def EQ(self):
            return self.getToken(dAngrParser.EQ, 0)

        def NEQ(self):
            return self.getToken(dAngrParser.NEQ, 0)

        def GT(self):
            return self.getToken(dAngrParser.GT, 0)

        def LT(self):
            return self.getToken(dAngrParser.LT, 0)

        def LE(self):
            return self.getToken(dAngrParser.LE, 0)

        def GE(self):
            return self.getToken(dAngrParser.GE, 0)

        def AND(self):
            return self.getToken(dAngrParser.AND, 0)

        def XOR(self):
            return self.getToken(dAngrParser.XOR, 0)

        def OR(self):
            return self.getToken(dAngrParser.OR, 0)

        def FLOORDIV(self):
            return self.getToken(dAngrParser.FLOORDIV, 0)

        def LSHIFT(self):
            return self.getToken(dAngrParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(dAngrParser.RSHIFT, 0)

        def AMP(self):
            return self.getToken(dAngrParser.AMP, 0)

        def BAR(self):
            return self.getToken(dAngrParser.BAR, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = dAngrParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_operation)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(dAngrParser.ADD)
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(dAngrParser.DASH)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 381
                self.match(dAngrParser.MUL)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 4)
                self.state = 382
                self.match(dAngrParser.DIV)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 5)
                self.state = 383
                self.match(dAngrParser.PERC)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
                self.match(dAngrParser.POW)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 7)
                self.state = 385
                self.match(dAngrParser.EQ)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 8)
                self.state = 386
                self.match(dAngrParser.NEQ)
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 9)
                self.state = 387
                self.match(dAngrParser.GT)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 10)
                self.state = 388
                self.match(dAngrParser.LT)
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 11)
                self.state = 389
                self.match(dAngrParser.LE)
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 12)
                self.state = 390
                self.match(dAngrParser.GE)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 13)
                self.state = 391
                self.match(dAngrParser.AND)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 14)
                self.state = 392
                self.match(dAngrParser.XOR)
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 15)
                self.state = 393
                self.match(dAngrParser.OR)
                self.state = 394
                self.match(dAngrParser.FLOORDIV)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 16)
                self.state = 395
                self.match(dAngrParser.LSHIFT)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 17)
                self.state = 396
                self.match(dAngrParser.RSHIFT)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 18)
                self.state = 397
                self.match(dAngrParser.AMP)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 19)
                self.state = 398
                self.match(dAngrParser.BAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Py_basic_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def py_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Py_contentContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Py_contentContext,i)


        def getRuleIndex(self):
            return dAngrParser.RULE_py_basic_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPy_basic_content" ):
                listener.enterPy_basic_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPy_basic_content" ):
                listener.exitPy_basic_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPy_basic_content" ):
                return visitor.visitPy_basic_content(self)
            else:
                return visitor.visitChildren(self)




    def py_basic_content(self):

        localctx = dAngrParser.Py_basic_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_py_basic_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.identifier()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 402
                self.match(dAngrParser.WS)


            self.state = 405
            self.match(dAngrParser.LPAREN)
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 406
                self.match(dAngrParser.WS)


            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -36029613106790402) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 163839) != 0):
                self.state = 409
                self.py_content()
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 415
            self.match(dAngrParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Py_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(dAngrParser.ReferenceContext,i)


        def range_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.RangeContext)
            else:
                return self.getTypedRuleContext(dAngrParser.RangeContext,i)


        def anything(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.AnythingContext)
            else:
                return self.getTypedRuleContext(dAngrParser.AnythingContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.LPAREN)
            else:
                return self.getToken(dAngrParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.RPAREN)
            else:
                return self.getToken(dAngrParser.RPAREN, i)

        def py_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Py_contentContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Py_contentContext,i)


        def getRuleIndex(self):
            return dAngrParser.RULE_py_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPy_content" ):
                listener.enterPy_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPy_content" ):
                listener.exitPy_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPy_content" ):
                return visitor.visitPy_content(self)
            else:
                return visitor.visitChildren(self)




    def py_content(self):

        localctx = dAngrParser.Py_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_py_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 428
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        self.state = 417
                        self.reference()
                        pass

                    elif la_ == 2:
                        self.state = 418
                        self.range_()
                        pass

                    elif la_ == 3:
                        self.state = 419
                        self.anything()
                        pass

                    elif la_ == 4:
                        self.state = 420
                        self.match(dAngrParser.LPAREN)
                        self.state = 424
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & -36029613106790402) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 163839) != 0):
                            self.state = 421
                            self.py_content()
                            self.state = 426
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 427
                        self.match(dAngrParser.RPAREN)
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 430 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bash_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(dAngrParser.ReferenceContext,i)


        def range_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.RangeContext)
            else:
                return self.getTypedRuleContext(dAngrParser.RangeContext,i)


        def anything(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.AnythingContext)
            else:
                return self.getTypedRuleContext(dAngrParser.AnythingContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.LPAREN)
            else:
                return self.getToken(dAngrParser.LPAREN, i)

        def bash_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Bash_contentContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Bash_contentContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.RPAREN)
            else:
                return self.getToken(dAngrParser.RPAREN, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_bash_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBash_content" ):
                listener.enterBash_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBash_content" ):
                listener.exitBash_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBash_content" ):
                return visitor.visitBash_content(self)
            else:
                return visitor.visitChildren(self)




    def bash_content(self):

        localctx = dAngrParser.Bash_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_bash_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 439
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                    if la_ == 1:
                        self.state = 432
                        self.reference()
                        pass

                    elif la_ == 2:
                        self.state = 433
                        self.range_()
                        pass

                    elif la_ == 3:
                        self.state = 434
                        self.anything()
                        pass

                    elif la_ == 4:
                        self.state = 435
                        self.match(dAngrParser.LPAREN)
                        self.state = 436
                        self.bash_content()
                        self.state = 437
                        self.match(dAngrParser.RPAREN)
                        pass

             
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(dAngrParser.DOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def VARS_DB(self):
            return self.getToken(dAngrParser.VARS_DB, 0)

        def REG_DB(self):
            return self.getToken(dAngrParser.REG_DB, 0)

        def SYM_DB(self):
            return self.getToken(dAngrParser.SYM_DB, 0)

        def BANG(self):
            return self.getToken(dAngrParser.BANG, 0)

        def STATE(self):
            return self.getToken(dAngrParser.STATE, 0)

        def MEM_DB(self):
            return self.getToken(dAngrParser.MEM_DB, 0)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)

        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IndexContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IndexContext,i)


        def KET(self):
            return self.getToken(dAngrParser.KET, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def ARROW(self):
            return self.getToken(dAngrParser.ARROW, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = dAngrParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 445
                self.match(dAngrParser.DOT)
                self.state = 446
                self.identifier()
                self.state = 448
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                if la_ == 1:
                    self.state = 447
                    self.match(dAngrParser.BANG)


                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.match(dAngrParser.STATE)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(dAngrParser.MEM_DB)
                self.state = 452
                self.match(dAngrParser.BRA)
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 453
                    self.match(dAngrParser.WS)


                self.state = 456
                self.index()
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20 or _la==37:
                    self.state = 458
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 457
                        self.match(dAngrParser.WS)


                    self.state = 460
                    self.match(dAngrParser.ARROW)
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 461
                        self.match(dAngrParser.WS)


                    self.state = 464
                    self.index()


                self.state = 467
                self.match(dAngrParser.KET)
                self.state = 469
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                if la_ == 1:
                    self.state = 468
                    self.match(dAngrParser.BANG)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def DASH(self):
            return self.getToken(dAngrParser.DASH, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = dAngrParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.state = 473
                self.match(dAngrParser.DASH)


            self.state = 476
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTERS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.LETTERS)
            else:
                return self.getToken(dAngrParser.LETTERS, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.UNDERSCORE)
            else:
                return self.getToken(dAngrParser.UNDERSCORE, i)

        def special_words(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.Special_wordsContext)
            else:
                return self.getTypedRuleContext(dAngrParser.Special_wordsContext,i)


        def NUMBERS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.NUMBERS)
            else:
                return self.getToken(dAngrParser.NUMBERS, i)

        def getRuleIndex(self):
            return dAngrParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = dAngrParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 478
                self.match(dAngrParser.LETTERS)
                pass
            elif token in [77]:
                self.state = 479
                self.match(dAngrParser.UNDERSCORE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                self.state = 480
                self.special_words()
                self.state = 481
                self.match(dAngrParser.UNDERSCORE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 489
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 485
                        self.match(dAngrParser.LETTERS)
                        pass
                    elif token in [22]:
                        self.state = 486
                        self.match(dAngrParser.NUMBERS)
                        pass
                    elif token in [77]:
                        self.state = 487
                        self.match(dAngrParser.UNDERSCORE)
                        pass
                    elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
                        self.state = 488
                        self.special_words()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self):
            return self.getToken(dAngrParser.NUMBERS, 0)

        def HEX_NUMBERS(self):
            return self.getToken(dAngrParser.HEX_NUMBERS, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_numeric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric" ):
                listener.enterNumeric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric" ):
                listener.exitNumeric(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric" ):
                return visitor.visitNumeric(self)
            else:
                return visitor.visitChildren(self)




    def numeric(self):

        localctx = dAngrParser.NumericContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_numeric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dAngrParser.RULE_object

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SlideStartLengthObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)
        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IndexContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IndexContext,i)

        def ARROW(self):
            return self.getToken(dAngrParser.ARROW, 0)
        def KET(self):
            return self.getToken(dAngrParser.KET, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlideStartLengthObject" ):
                listener.enterSlideStartLengthObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlideStartLengthObject" ):
                listener.exitSlideStartLengthObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlideStartLengthObject" ):
                return visitor.visitSlideStartLengthObject(self)
            else:
                return visitor.visitChildren(self)


    class ReferenceObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reference(self):
            return self.getTypedRuleContext(dAngrParser.ReferenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReferenceObject" ):
                listener.enterReferenceObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReferenceObject" ):
                listener.exitReferenceObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReferenceObject" ):
                return visitor.visitReferenceObject(self)
            else:
                return visitor.visitChildren(self)


    class BinaryStringObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BINARY_STRING(self):
            return self.getToken(dAngrParser.BINARY_STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryStringObject" ):
                listener.enterBinaryStringObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryStringObject" ):
                listener.exitBinaryStringObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryStringObject" ):
                return visitor.visitBinaryStringObject(self)
            else:
                return visitor.visitChildren(self)


    class ListObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)
        def KET(self):
            return self.getToken(dAngrParser.KET, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)
        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.ObjectContext)
            else:
                return self.getTypedRuleContext(dAngrParser.ObjectContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.COMMA)
            else:
                return self.getToken(dAngrParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListObject" ):
                listener.enterListObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListObject" ):
                listener.exitListObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListObject" ):
                return visitor.visitListObject(self)
            else:
                return visitor.visitChildren(self)


    class IndexedPropertyObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)
        def index(self):
            return self.getTypedRuleContext(dAngrParser.IndexContext,0)

        def KET(self):
            return self.getToken(dAngrParser.KET, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexedPropertyObject" ):
                listener.enterIndexedPropertyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexedPropertyObject" ):
                listener.exitIndexedPropertyObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexedPropertyObject" ):
                return visitor.visitIndexedPropertyObject(self)
            else:
                return visitor.visitChildren(self)


    class DictionaryObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRACE(self):
            return self.getToken(dAngrParser.BRACE, 0)
        def KETCE(self):
            return self.getToken(dAngrParser.KETCE, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.STRING)
            else:
                return self.getToken(dAngrParser.STRING, i)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.COLON)
            else:
                return self.getToken(dAngrParser.COLON, i)
        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.ObjectContext)
            else:
                return self.getTypedRuleContext(dAngrParser.ObjectContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.COMMA)
            else:
                return self.getToken(dAngrParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionaryObject" ):
                listener.enterDictionaryObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionaryObject" ):
                listener.exitDictionaryObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionaryObject" ):
                return visitor.visitDictionaryObject(self)
            else:
                return visitor.visitChildren(self)


    class NumericObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numeric(self):
            return self.getTypedRuleContext(dAngrParser.NumericContext,0)

        def DASH(self):
            return self.getToken(dAngrParser.DASH, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericObject" ):
                listener.enterNumericObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericObject" ):
                listener.exitNumericObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericObject" ):
                return visitor.visitNumericObject(self)
            else:
                return visitor.visitChildren(self)


    class SliceStartEndObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)
        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dAngrParser.IndexContext)
            else:
                return self.getTypedRuleContext(dAngrParser.IndexContext,i)

        def COLON(self):
            return self.getToken(dAngrParser.COLON, 0)
        def KET(self):
            return self.getToken(dAngrParser.KET, 0)
        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(dAngrParser.WS)
            else:
                return self.getToken(dAngrParser.WS, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSliceStartEndObject" ):
                listener.enterSliceStartEndObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSliceStartEndObject" ):
                listener.exitSliceStartEndObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSliceStartEndObject" ):
                return visitor.visitSliceStartEndObject(self)
            else:
                return visitor.visitChildren(self)


    class StringObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(dAngrParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringObject" ):
                listener.enterStringObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringObject" ):
                listener.exitStringObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringObject" ):
                return visitor.visitStringObject(self)
            else:
                return visitor.visitChildren(self)


    class IDObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)

        def BANG(self):
            return self.getToken(dAngrParser.BANG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIDObject" ):
                listener.enterIDObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIDObject" ):
                listener.exitIDObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDObject" ):
                return visitor.visitIDObject(self)
            else:
                return visitor.visitChildren(self)


    class PropertyObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(dAngrParser.ObjectContext,0)

        def DOT(self):
            return self.getToken(dAngrParser.DOT, 0)
        def identifier(self):
            return self.getTypedRuleContext(dAngrParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyObject" ):
                listener.enterPropertyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyObject" ):
                listener.exitPropertyObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyObject" ):
                return visitor.visitPropertyObject(self)
            else:
                return visitor.visitChildren(self)


    class BoolObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dAngrParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(dAngrParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolObject" ):
                listener.enterBoolObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolObject" ):
                listener.exitBoolObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolObject" ):
                return visitor.visitBoolObject(self)
            else:
                return visitor.visitChildren(self)



    def object_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = dAngrParser.ObjectContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_object, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                localctx = dAngrParser.IDObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 497
                self.identifier()
                self.state = 499
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 498
                    self.match(dAngrParser.BANG)


                pass

            elif la_ == 2:
                localctx = dAngrParser.NumericObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==78:
                    self.state = 501
                    self.match(dAngrParser.DASH)


                self.state = 504
                self.numeric()
                pass

            elif la_ == 3:
                localctx = dAngrParser.BoolObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 505
                self.match(dAngrParser.BOOL)
                pass

            elif la_ == 4:
                localctx = dAngrParser.ReferenceObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 506
                self.reference()
                pass

            elif la_ == 5:
                localctx = dAngrParser.ListObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 507
                self.match(dAngrParser.BRA)
                self.state = 509
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
                if la_ == 1:
                    self.state = 508
                    self.match(dAngrParser.WS)


                self.state = 512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 11259007614844926) != 0) or _la==77 or _la==78:
                    self.state = 511
                    self.object_(0)


                self.state = 524
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 515
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 514
                            self.match(dAngrParser.WS)


                        self.state = 517
                        self.match(dAngrParser.COMMA)
                        self.state = 519
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 518
                            self.match(dAngrParser.WS)


                        self.state = 521
                        self.object_(0) 
                    self.state = 526
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

                self.state = 528
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 527
                    self.match(dAngrParser.WS)


                self.state = 530
                self.match(dAngrParser.KET)
                pass

            elif la_ == 6:
                localctx = dAngrParser.DictionaryObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 531
                self.match(dAngrParser.BRACE)
                self.state = 533
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 532
                    self.match(dAngrParser.WS)


                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==31:
                    self.state = 535
                    self.match(dAngrParser.STRING)
                    self.state = 537
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 536
                        self.match(dAngrParser.WS)


                    self.state = 539
                    self.match(dAngrParser.COLON)
                    self.state = 541
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 540
                        self.match(dAngrParser.WS)


                    self.state = 543
                    self.object_(0)

                    self.state = 545
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 544
                        self.match(dAngrParser.WS)


                    self.state = 547
                    self.match(dAngrParser.COMMA)
                    self.state = 549
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 548
                        self.match(dAngrParser.WS)


                    self.state = 551
                    self.match(dAngrParser.STRING)
                    self.state = 553
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 552
                        self.match(dAngrParser.WS)


                    self.state = 555
                    self.match(dAngrParser.COLON)
                    self.state = 557
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==20:
                        self.state = 556
                        self.match(dAngrParser.WS)


                    self.state = 559
                    self.object_(0)
                    self.state = 565
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 566
                    self.match(dAngrParser.WS)


                self.state = 569
                self.match(dAngrParser.KETCE)
                pass

            elif la_ == 7:
                localctx = dAngrParser.StringObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 570
                self.match(dAngrParser.STRING)
                pass

            elif la_ == 8:
                localctx = dAngrParser.BinaryStringObjectContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 571
                self.match(dAngrParser.BINARY_STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 630
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,106,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 628
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
                    if la_ == 1:
                        localctx = dAngrParser.PropertyObjectContext(self, dAngrParser.ObjectContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_object)
                        self.state = 574
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 575
                        self.match(dAngrParser.DOT)
                        self.state = 576
                        self.identifier()
                        pass

                    elif la_ == 2:
                        localctx = dAngrParser.IndexedPropertyObjectContext(self, dAngrParser.ObjectContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_object)
                        self.state = 577
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 578
                        self.match(dAngrParser.BRA)
                        self.state = 580
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 579
                            self.match(dAngrParser.WS)


                        self.state = 582
                        self.index()
                        self.state = 584
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 583
                            self.match(dAngrParser.WS)


                        self.state = 586
                        self.match(dAngrParser.KET)
                        pass

                    elif la_ == 3:
                        localctx = dAngrParser.SliceStartEndObjectContext(self, dAngrParser.ObjectContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_object)
                        self.state = 588
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 589
                        self.match(dAngrParser.BRA)
                        self.state = 591
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 590
                            self.match(dAngrParser.WS)


                        self.state = 593
                        self.index()
                        self.state = 595
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 594
                            self.match(dAngrParser.WS)


                        self.state = 597
                        self.match(dAngrParser.COLON)
                        self.state = 599
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
                        if la_ == 1:
                            self.state = 598
                            self.match(dAngrParser.WS)


                        self.state = 602
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 11266979074146302) != 0) or _la==77 or _la==78:
                            self.state = 601
                            self.index()


                        self.state = 605
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 604
                            self.match(dAngrParser.WS)


                        self.state = 607
                        self.match(dAngrParser.KET)
                        pass

                    elif la_ == 4:
                        localctx = dAngrParser.SlideStartLengthObjectContext(self, dAngrParser.ObjectContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_object)
                        self.state = 609
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 610
                        self.match(dAngrParser.BRA)
                        self.state = 612
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 611
                            self.match(dAngrParser.WS)


                        self.state = 614
                        self.index()
                        self.state = 616
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 615
                            self.match(dAngrParser.WS)


                        self.state = 618
                        self.match(dAngrParser.ARROW)
                        self.state = 620
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 619
                            self.match(dAngrParser.WS)


                        self.state = 622
                        self.index()
                        self.state = 624
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==20:
                            self.state = 623
                            self.match(dAngrParser.WS)


                        self.state = 626
                        self.match(dAngrParser.KET)
                        pass

             
                self.state = 632
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,106,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AnythingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anything_no(self):
            return self.getTypedRuleContext(dAngrParser.Anything_noContext,0)


        def NEWLINE(self):
            return self.getToken(dAngrParser.NEWLINE, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_anything

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnything" ):
                listener.enterAnything(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnything" ):
                listener.exitAnything(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnything" ):
                return visitor.visitAnything(self)
            else:
                return visitor.visitChildren(self)




    def anything(self):

        localctx = dAngrParser.AnythingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_anything)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 31, 32, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 81]:
                self.state = 633
                self.anything_no()
                pass
            elif token in [19]:
                self.state = 634
                self.match(dAngrParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Anything_noContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTERS(self):
            return self.getToken(dAngrParser.LETTERS, 0)

        def NUMBERS(self):
            return self.getToken(dAngrParser.NUMBERS, 0)

        def symbol(self):
            return self.getTypedRuleContext(dAngrParser.SymbolContext,0)


        def STRING(self):
            return self.getToken(dAngrParser.STRING, 0)

        def BINARY_STRING(self):
            return self.getToken(dAngrParser.BINARY_STRING, 0)

        def WS(self):
            return self.getToken(dAngrParser.WS, 0)

        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def anything(self):
            return self.getTypedRuleContext(dAngrParser.AnythingContext,0)


        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def special_words(self):
            return self.getTypedRuleContext(dAngrParser.Special_wordsContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_anything_no

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnything_no" ):
                listener.enterAnything_no(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnything_no" ):
                listener.exitAnything_no(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnything_no" ):
                return visitor.visitAnything_no(self)
            else:
                return visitor.visitChildren(self)




    def anything_no(self):

        localctx = dAngrParser.Anything_noContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_anything_no)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,108,self._ctx)
            if la_ == 1:
                self.state = 637
                self.match(dAngrParser.LETTERS)
                pass

            elif la_ == 2:
                self.state = 638
                self.match(dAngrParser.NUMBERS)
                pass

            elif la_ == 3:
                self.state = 639
                self.symbol()
                pass

            elif la_ == 4:
                self.state = 640
                self.match(dAngrParser.STRING)
                pass

            elif la_ == 5:
                self.state = 641
                self.match(dAngrParser.BINARY_STRING)
                pass

            elif la_ == 6:
                self.state = 642
                self.match(dAngrParser.WS)
                pass

            elif la_ == 7:
                self.state = 643
                self.match(dAngrParser.LPAREN)
                self.state = 644
                self.anything()
                self.state = 645
                self.match(dAngrParser.RPAREN)
                pass

            elif la_ == 8:
                self.state = 647
                self.special_words()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_wordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(dAngrParser.STATIC, 0)

        def DEF(self):
            return self.getToken(dAngrParser.DEF, 0)

        def IF(self):
            return self.getToken(dAngrParser.IF, 0)

        def ELSE(self):
            return self.getToken(dAngrParser.ELSE, 0)

        def FOR(self):
            return self.getToken(dAngrParser.FOR, 0)

        def IN(self):
            return self.getToken(dAngrParser.IN, 0)

        def NOT(self):
            return self.getToken(dAngrParser.NOT, 0)

        def NOT_IN(self):
            return self.getToken(dAngrParser.NOT_IN, 0)

        def WHILE(self):
            return self.getToken(dAngrParser.WHILE, 0)

        def BOOL(self):
            return self.getToken(dAngrParser.BOOL, 0)

        def HELP(self):
            return self.getToken(dAngrParser.HELP, 0)

        def CIF(self):
            return self.getToken(dAngrParser.CIF, 0)

        def CTHEN(self):
            return self.getToken(dAngrParser.CTHEN, 0)

        def CELSE(self):
            return self.getToken(dAngrParser.CELSE, 0)

        def RETURN(self):
            return self.getToken(dAngrParser.RETURN, 0)

        def BREAK(self):
            return self.getToken(dAngrParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(dAngrParser.CONTINUE, 0)

        def RANGE(self):
            return self.getToken(dAngrParser.RANGE, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_special_words

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_words" ):
                listener.enterSpecial_words(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_words" ):
                listener.exitSpecial_words(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecial_words" ):
                return visitor.visitSpecial_words(self)
            else:
                return visitor.visitChildren(self)




    def special_words(self):

        localctx = dAngrParser.Special_wordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_special_words)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 524286) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dangr_range(self):
            return self.getTypedRuleContext(dAngrParser.Dangr_rangeContext,0)


        def bash_range(self):
            return self.getTypedRuleContext(dAngrParser.Bash_rangeContext,0)


        def python_range(self):
            return self.getTypedRuleContext(dAngrParser.Python_rangeContext,0)


        def getRuleIndex(self):
            return dAngrParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = dAngrParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_range)
        try:
            self.state = 655
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.dangr_range()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 653
                self.bash_range()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 654
                self.python_range()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dangr_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AMP(self):
            return self.getToken(dAngrParser.AMP, 0)

        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(dAngrParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_dangr_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDangr_range" ):
                listener.enterDangr_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDangr_range" ):
                listener.exitDangr_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDangr_range" ):
                return visitor.visitDangr_range(self)
            else:
                return visitor.visitChildren(self)




    def dangr_range(self):

        localctx = dAngrParser.Dangr_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_dangr_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(dAngrParser.AMP)
            self.state = 658
            self.match(dAngrParser.LPAREN)
            self.state = 659
            self.expression()
            self.state = 660
            self.match(dAngrParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bash_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(dAngrParser.DOLLAR, 0)

        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def bash_content(self):
            return self.getTypedRuleContext(dAngrParser.Bash_contentContext,0)


        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_bash_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBash_range" ):
                listener.enterBash_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBash_range" ):
                listener.exitBash_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBash_range" ):
                return visitor.visitBash_range(self)
            else:
                return visitor.visitChildren(self)




    def bash_range(self):

        localctx = dAngrParser.Bash_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_bash_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(dAngrParser.DOLLAR)
            self.state = 663
            self.match(dAngrParser.LPAREN)
            self.state = 664
            self.bash_content()
            self.state = 665
            self.match(dAngrParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Python_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(dAngrParser.BANG, 0)

        def LPAREN(self):
            return self.getToken(dAngrParser.LPAREN, 0)

        def py_content(self):
            return self.getTypedRuleContext(dAngrParser.Py_contentContext,0)


        def RPAREN(self):
            return self.getToken(dAngrParser.RPAREN, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_python_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPython_range" ):
                listener.enterPython_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPython_range" ):
                listener.exitPython_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPython_range" ):
                return visitor.visitPython_range(self)
            else:
                return visitor.visitChildren(self)




    def python_range(self):

        localctx = dAngrParser.Python_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_python_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 667
            self.match(dAngrParser.BANG)
            self.state = 668
            self.match(dAngrParser.LPAREN)
            self.state = 669
            self.py_content()
            self.state = 670
            self.match(dAngrParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(dAngrParser.WS, 0)

        def BANG(self):
            return self.getToken(dAngrParser.BANG, 0)

        def AMP(self):
            return self.getToken(dAngrParser.AMP, 0)

        def DOLLAR(self):
            return self.getToken(dAngrParser.DOLLAR, 0)

        def COLON(self):
            return self.getToken(dAngrParser.COLON, 0)

        def SCOLON(self):
            return self.getToken(dAngrParser.SCOLON, 0)

        def COMMA(self):
            return self.getToken(dAngrParser.COMMA, 0)

        def QUOTE(self):
            return self.getToken(dAngrParser.QUOTE, 0)

        def SQUOTE(self):
            return self.getToken(dAngrParser.SQUOTE, 0)

        def AT(self):
            return self.getToken(dAngrParser.AT, 0)

        def DOT(self):
            return self.getToken(dAngrParser.DOT, 0)

        def BAR(self):
            return self.getToken(dAngrParser.BAR, 0)

        def BRA(self):
            return self.getToken(dAngrParser.BRA, 0)

        def KET(self):
            return self.getToken(dAngrParser.KET, 0)

        def BRACE(self):
            return self.getToken(dAngrParser.BRACE, 0)

        def KETCE(self):
            return self.getToken(dAngrParser.KETCE, 0)

        def HAT(self):
            return self.getToken(dAngrParser.HAT, 0)

        def HASH(self):
            return self.getToken(dAngrParser.HASH, 0)

        def PERC(self):
            return self.getToken(dAngrParser.PERC, 0)

        def MUL(self):
            return self.getToken(dAngrParser.MUL, 0)

        def ADD(self):
            return self.getToken(dAngrParser.ADD, 0)

        def DIV(self):
            return self.getToken(dAngrParser.DIV, 0)

        def POW(self):
            return self.getToken(dAngrParser.POW, 0)

        def ASSIGN(self):
            return self.getToken(dAngrParser.ASSIGN, 0)

        def EQ(self):
            return self.getToken(dAngrParser.EQ, 0)

        def NEQ(self):
            return self.getToken(dAngrParser.NEQ, 0)

        def LT(self):
            return self.getToken(dAngrParser.LT, 0)

        def GT(self):
            return self.getToken(dAngrParser.GT, 0)

        def LE(self):
            return self.getToken(dAngrParser.LE, 0)

        def GE(self):
            return self.getToken(dAngrParser.GE, 0)

        def AND(self):
            return self.getToken(dAngrParser.AND, 0)

        def OR(self):
            return self.getToken(dAngrParser.OR, 0)

        def QMARK(self):
            return self.getToken(dAngrParser.QMARK, 0)

        def TILDE(self):
            return self.getToken(dAngrParser.TILDE, 0)

        def TICK(self):
            return self.getToken(dAngrParser.TICK, 0)

        def UNDERSCORE(self):
            return self.getToken(dAngrParser.UNDERSCORE, 0)

        def DASH(self):
            return self.getToken(dAngrParser.DASH, 0)

        def FLOORDIV(self):
            return self.getToken(dAngrParser.FLOORDIV, 0)

        def LSHIFT(self):
            return self.getToken(dAngrParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(dAngrParser.RSHIFT, 0)

        def getRuleIndex(self):
            return dAngrParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = dAngrParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            _la = self._input.LA(1)
            if not(((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & 2882303727156330497) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_part_sempred
        self._predicates[23] = self.object_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_part_sempred(self, localctx:Expression_partContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

    def object_sempred(self, localctx:ObjectContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




