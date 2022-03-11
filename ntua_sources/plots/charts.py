# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;
sns.set()
import pandas as pd



## Execution Times all Algorithms for the various Network Topologies ###################################################
########################################################################################################################
# Binomial Tree
def execution_time_all_Algorithms_Binomial():
    sns.set_style("ticks")


    data = [["2", 0.000121, 0.000130, 0.0096, 0.0594],
            ["4", 0.000162, 0.000161, 0.0174, 0.014],
            ["8", 0.000175, 0.000286, 0.0313, 0.0125],
            ["16", 0.000436, 0.000623, 2.61, 0.0141],
            ["32", 0.00132, 0.00182, 0.6649, 0.0223],
            ["64", 0.0227, 0.0204, 0.585, 0.0317],
            ["128", 0.0438, 0.0412, 2.1467, 0.0742],
            ["256", 0.0106, 0.102, 8.377, 0.1210],
            ["512", 0.406, 0.441, 36.002, 0.505],
            ["1024", 1.87, 1.836, 147.58, 1.32],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="line", figsize=(9, 8),color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    #plt.legend(loc=4)
    plt.title("Binomial Tree")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def execution_time_all_Algorithms_Binomial_LINE():
        y1 = [0.000121,0.000162 ,0.000175,0.000436,0.00132,0.0227,0.0438,0.0106,0.406,1.87]
        y2 = [0.000130,0.000161 ,0.000286,0.000623,0.00182,0.0204,0.0412,0.102,0.441,1.836]
        y3 = [0.0096,0.0174 ,0.0313,2.61,0.6649,0.585,2.1467,8.377,36.002,147.58]
        y4 = [0.0594,0.014 ,0.0125,0.0141,0.0223, 0.0317,0.0742,0.1210,0.505,1.32]
        x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

        sns.set_style("ticks")
        plt.plot(x, y1, "-+", label="Approximation", color="lightsteelblue")
        plt.plot(x, y2, "-o", label="Greedy", color="cornflowerblue")
        plt.plot(x, y3, "-*", label="Genetic", color="dimgray")
        plt.plot(x, y4, "--", label="ILP", color="peru")
        plt.legend(loc="upper left")
        plt.xlabel("Number of Vertices")
        plt.ylabel("Execution time (seconds)")
        plt.title("Binomial Tree")
        plt.tight_layout()
        plt.yscale('log')
        plt.tight_layout()
        plt.show()


# Star Graph
def execution_time_all_Algorithms_Star():

    sns.set_style("ticks")
    data = [["2",0.000131 ,0.000111,0.00921, 0.00853],
            ["4",0.00017 ,0.00011,0.0204,0.01267],
            ["8",0.00015 ,0.00023,0.0476, 0.01389],
            ["16",0.00036 ,0.00045,0.1268,0.0148],
            ["32",0.00110 ,0.00143,0.4633,0.0182],
            ["64",0.0207 ,0.0190,1.5824,0.0259],
            ["128",0.0342 ,0.03680,7.015,0.0677],
            ["256", 0.0913 ,0.0900,22.812,0.1094],
            ["512", 0.3236,0.3381,107.366,0.2276],
            ["1024",1.312 ,1.4089,443.81, 0.6835],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Star Graph")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

# Star Graph
def execution_time_all_Algorithms_Star_LINE():
    y1 = [0.000131,0.00017,0.00015,0.00036,0.00110,0.0207,0.0342,0.0913,0.3236,1.312]
    y2 = [0.000111,0.00011,0.00023,0.00045,0.00143,0.0190,0.03680,0.0900,0.3381,1.4089]
    y3 = [0.00921,0.0204,0.0476,0.1268,0.4633,1.5824,7.015,22.812,107.366,443.81]
    y4 = [0.00853,0.01267,0.01389,0.0148,0.0182,0.0259,0.0677,0.1094,0.2276,0.6835]
    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Approximation", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Greedy", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Genetic", color="dimgray")
    plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Star Graph")
    plt.tight_layout()
    plt.yscale('log')
    plt.tight_layout()
    plt.show()


# Barabasi-Albert Graph
def execution_time_all_Algorithms_BarabasiAlbert():
    # m=1

    sns.set_style("ticks")
    data = [["2", 0.00013,0.00011, 0.0117,0.0099],
            ["4", 0.00015,0.00018,0.028,0.0126],
            ["8",0.00015 ,0.0003,0.0549,0.0190],
            ["16",0.0005 ,0.0007,0.128,0.0215],
            ["32",0.0019 ,0.0022,0.388,0.0378],
            ["64",0.0213 ,0.0247,1.366,0.0363],
            ["128", 0.0413,0.0509,7.533,0.0782],
            ["256",0.122 ,0.142,22.392,0.1587],
            ["512",0.468 ,0.509,87.12,0.6933],
            ["1024",4.192 ,2.407,368.45,1.310],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Barabasi-Albert Graph")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_Algorithms_BarabasiAlbert_LINE():
    y1 = [0.00013,0.00015,0.00015,0.0005,0.0019,0.0213,0.0413,0.122,0.468,4.192]
    y2 = [0.00011,0.00018,0.0003,0.0007,0.0022,0.0247,0.0509,0.142,0.509,2.407]
    y3 = [0.0117,0.028,0.0549,0.128,0.388,1.366,7.533,22.392,87.12,368.45]
    y4 = [0.0099,0.0126,0.0190,0.0215,0.0378,0.0363,0.0782,0.1587,0.6933,1.310]
    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Approximation", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Greedy", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Genetic", color="dimgray")
    plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Barabasi-Albert Graph")
    plt.tight_layout()
    plt.yscale('log')
    plt.tight_layout()
    plt.show()


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


## Cost function all Algorithms for the various Network Topologies #####################################################
########################################################################################################################

def costfunction_all_Algorithms_BarabasiAlbert():
    # m=1
    sns.set_style("ticks")
    data = [["2",2.0,1.16,1.16,1.16 ],
            ["4",4.0,125.04,125.04,125.04],
            ["8",129.68,372.65,372.65,372.65 ],
            ["16",504.69,748.45,748.45,870.33 ],
            ["32",1264.73,1753.92,1753.92,1756.54 ],
            ["64",3752.51, 4732.42,4734.80,4854.30 ],
            ["128",6217.07,8244.56,8393.66,8280.75 ],
            ["256",12096.63,16346.34,17062.14,16260.24 ],
            ["512",25169.55,36592.49,39449.045,36950.95 ],
            ["1024",81269.18,116151.27,124501.55,117625.16 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Barabasi-Albert Graph")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def costfunction_all_Algorithms_Binomial():
    sns.set_style("ticks")
    data = [["2",2,1.16,1.16, 1.16 ],
            ["4",4,125.04,125.04,125.04 ],
            ["8",8,250.73,250.73,250.73],
            ["16",16,382.19,382.19,382.19 ],
            ["32",32,1500.48,1503.81,1503.81 ],
            ["64",64,3217.71,3623.29	,3371.40 ],
            ["128",128,6510.32	,7171.00	,6510.04 ],
            ["256",256,12099.31,14766.39,12099.31 ],
            ["512",512,27427.64,34354.79	,27427.64 ],
            ["1024",1024,84872.029,108433.52	,84872.03 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Binomial Tree")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def costfunction_all_Algorithms_Star():
    sns.set_style("ticks")
    data = [["2",2.0,	1.161,	1.161,		1.161 ],
            ["4",125.04	,246.92	,246.92	,246.92 ],
            ["8",372.097,493.97	,493.97	,493.97 ],
            ["16",990.11,1235.35,1235.35	,1235.35 ],
            ["32",2607.007	,2728.88	,2728.88	,2728.88 ],
            ["64",5630.31,5752.19,5752.19	,5752.19],
            ["128", 5630.31	,12639.10,	12639.10,		12639.10],
            ["256", 24003.90	,24125.78,	24125.78,		24125.78],
            ["512",  53895.35,	54017.23,	54017.23		,54017.23],
            ["1024",168392.52,	168556.29	,168556.29,		168556.29 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Star Graph")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

## NumberofNodesinVC all Algorithms for the various Network Topologies ###################################################
def  NumberofNodesinVC_all_Algorithms_BarabasiAlbert():
    #m=1
    sns.set_style("ticks")
    data = [["2",2 ,1,1,1],
            ["4",4,2,2,2 ],
            ["8",6,3,3,3 ],
            ["16",8,6,6,5 ],
            ["32",16,10,10,9 ],
            ["64",28,18,19,17 ],
            ["128",60,37,47,34 ],
            ["256",126,80,99,78 ],
            ["512",272,163,217,158 ],
            ["1024",534,321,433,312 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
    df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Barabasi-Albert Graph")
    plt.ylabel("Number of nodes in VC")
    # plt.yscale('log')
    plt.tight_layout()
    plt.show()

# TODO
# def NumberofNodesinVC_all_Algorithms_Balanced():
#     # r = 2 -- h = increased by 1 in every run, starts with 1
#     sns.set_style("ticks")
#     data = [["2",2,1,1,1 ],
#             ["4",2,1,1,1 ],
#             ["8",10,6,8,5 ],
#             ["16",20,10,16,10 ],
#             ["32",42,26,36,20 ],
#             ["64",,,, ],
#             ["128",,,, ],
#             ["256",,,, ],
#             ["512",,,, ],
#             ["1024",,,, ],
#             ]
#
#     df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
#     df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
#             kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
#     plt.xticks(rotation=0)
#     plt.title("Balanced Tree")
#     plt.ylabel("Number of nodes in VC")
#     # plt.yscale('log')
#     plt.tight_layout()
#     plt.show()


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################



## ApproximationRatio all Algorithms for the various Network Topologies ###################################################

def ApproximationRatio_all_Algorithms_Binomial():
    y1 = [2,2,2,2,2,2,2,2,2,2]
    y2 = [1,1,1,1,1,1,1,1,1,1]
    y3 = [1,1,1,1,1,1,1,1,1,1]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Approximation", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Greedy", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Genetic", color="dimgray")
    #plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Binomial Tree")
    plt.tight_layout()
    #plt.yscale('log')
    plt.tight_layout()
    plt.show()

def ApproximationRatio_all_Algorithms_Barabasi():
    y1 = [2, 2, 2, 1.6, 1.77, 1.64, 1.76, 1.61, 1.72, 1.71]
    y2 = [1, 1, 1, 1.2, 1.11, 1.05, 1.08, 1.02, 1.03, 1.02]
    y3 = [1, 1, 1, 1.2, 1.11, 1.11, 1.38, 1.26, 1.37, 1.38]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Approximation", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Greedy", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Genetic", color="dimgray")
    # plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Barabasi-Albert Graph")
    plt.tight_layout()
    # plt.yscale('log')
    plt.tight_layout()
    plt.show()


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################








#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------










## Execution Times all Network Structures for the various Algorithms ###################################################
########################################################################################################################
def execution_time_all_NetworkStructures_for_Approximation():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2", 0,       0.000131, 0.000121, 0,       0.00013, 0.00013],
            ["4", 0.00012, 0.00017,  0.000162, 0,        0.00014, 0.00015],
            ["8", 0.00013, 0.00015,  0.000175, 0,         0.00022, 0.00015],
            ["16", 0.00034, 0.00036, 0.000436, 0.00046,   0.00051, 0.0005],
            ["32", 0.0012, 0.00110,  0.00132,  0.0013,    0.0029, 0.0019],
            ["64", 0.0221, 0.0207,   0.0227,   0.0216,    0.0243, 0.0213],
            ["128", 0.0387, 0.0342,     0.0438,  0.0379,    0.05640, 0.0413],
            ["256", 0.0977, 0.0913,  0.0106,    0.1936,     0.1614, 0.122],
            ["512", 0.444, 0.3236,   0.406,    1.3412,      0.5105, 0.468],
            ["1024", 1.993, 1.312,    1.87,     9.074,      2.4698, 4.192],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_NetworkStructures_for_Approximation_LINE():
    y1 = [0.00012,0.00012,0.00013,0.00034,0.0012,0.0221,0.0387,0.0977,0.444,1.993]
    y2 = [0.000131,0.00017,0.00015,0.00036,0.00110,0.0207,0.0342,0.0913,0.3236,1.312]
    y3 = [0.000121,0.000162,0.000175,  0.000436,0.00132 ,0.0227, 0.0438,0.0106,0.406, 1.87 ]
    y4 = [0,0,0,0.00046,0.0013,0.0216,0.0379,0.1936,1.3412,9.074 ]
    y5 = [0.00013,0.00014,0.00022,0.00051,0.0029,0.0243,0.05640,0.1614,0.5105,2.4698]
    y6 =[0.00013,0.00015,0.00015,0.0005,0.0019,0.0213, 0.0413, 0.122,0.468,4.192]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Approximation")
    plt.tight_layout()
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_NetworkStructures_for_Greedy():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",0,        0.000111,   0.000130,  0,       0.00011, 0.00011 ],
            ["4",0.00014,  0.00011,    0.000161 , 0 ,      0.00016, 0.00018],
            ["8",0.00021,   0.00023,   0.000286,  0,       0.00029, 0.0003 ],
            ["16",0.00080,  0.00045,   0.000623,  0.00053, 0.0007,  0.0007 ],
            ["32",0.0015,   0.00143,   0.00182,   0.0019,  0.0022,  0.0022 ],
            ["64",0.0223,   0.0190,    0.0204 ,   0.0288,  0.0283,  0.0247 ],
            ["128",0.04617, 0.03680,   0.0412 ,   0.0736,  0.0504,  0.0509 ],
            ["256",0.113,   0.0900,    0.102 ,    0.3496,  0.162,   0.142 ],
            ["512",0.4588,  0.3381,    0.441,     2.479,   0.5051,  0.509 ],
            ["1024",1.96,   1.4089,    1.836 ,    22.3394, 2.368,   2.407 ],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial", "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Greedy")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_NetworkStructures_for_Greedy_LINE():
    y1 = [0.00014,0.00014,0.00021,0.00080,0.0015,0.0223,0.04617,0.113,0.4588,1.96]
    y2 = [0.000111,0.00011,0.00023,0.00045,0.00143,0.0190,0.03680,0.0900,0.3381,1.4089]
    y3 = [0.000130,0.000161,0.000286,0.000623,0.00182,0.0204,0.0412,0.102,0.441,1.836]
    y4 = [0,0,0,0.00053,0.0019,0.0288,0.0736,0.3496,2.479,22.3394]
    y5 = [0.00011,0.00016,0.00029,0.0007,0.0022,0.0283,0.0504,0.162,0.5051,2.368]
    y6 = [0.00011,0.00018,0.0003,0.0007,0.0022,0.0247,0.0509,0.142,0.509,2.407]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Greedy")
    plt.tight_layout()
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_NetworkStructures_for_Genetic():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")
    data = [["2",0 ,         0.00921 ,   0.0096 ,   0 ,       0.0106 ,    0.0117  ],
            ["4",0.0176 ,     0.0204 ,   0.0174 ,   0 ,       0.0168 ,    0.028 ],
            ["8",0.03386,    0.0476 ,    0.0313,    0 ,       0.0308 ,    0.0549 ],
            ["16",0.0940,    0.1268 ,    2.61 ,     0.0842 ,  0.05177 ,   0.128 ],
            ["32",0.3064,    0.4633 ,    0.6649 ,   0.145 ,   0.1502 ,    0.388 ],
            ["64",0.9414,    1.5824 ,    0.585 ,    0.3792 ,  0.4967 ,    1.366 ],
            ["128",3.997,    7.015 ,     2.1467 ,   1.116 ,   1.399 ,     7.533],
            ["256",16.495,   22.812 ,    8.377 ,    3.635 ,   5.2896 ,    22.392 ],
            ["512",76.28,    107.366 ,   36.002 ,   16.013 ,  25.899 ,    87.12],
            ["1024",310.96,  443.81 ,    147.58,    56.665 ,  110.31 ,    368.45 ],
            ]
    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi", "Watts–Strogatz",
                                     "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial", "Erdo-Renyi",
               "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Genetic")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()
    plt.show()

def execution_time_all_NetworkStructures_for_Genetic_LINE():
    y1 = [0.0176,0.0176,0.03386,0.0940,0.3064,0.9414,3.997,16.495,76.28,310.96]
    y2 = [0.00921,0.0204,0.0476,0.1268,0.4633,1.5824,7.015,22.812,107.366,443.81]
    y3 = [0.0096,0.0174,0.0313,2.61,0.6649,0.585,2.1467,8.377,36.002,147.58]
    y4 = [0,0,0,0.0842,0.145,0.3792,1.116,3.635,16.013,56.665]
    y5 = [0.0106,0.0168,0.0308,0.05177, 0.1502,0.4967,1.399,5.2896,25.899,110.31]
    y6 = [0.0117,0.028,0.0549,0.128,0.388, 1.366,7.533,22.392,87.12,368.45]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="Balanced Tree", color="lightsteelblue")
    plt.plot(x, y2, "-o", label="Star", color="cornflowerblue")
    plt.plot(x, y3, "-*", label="Binomial", color="dimgray")
    plt.plot(x, y4, "--", label="Erdo-Renyi", color="peru")
    plt.plot(x, y5, "-p", label="Watts-Strogatz", color="powderblue")
    plt.plot(x, y6, "-.", label="Barabasi-Albert", color="silver")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Execution time (seconds)")
    plt.title("Genetic")
    plt.tight_layout()
    plt.yscale('log')
    plt.tight_layout()
    plt.show()
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


## Cost Function all Network Structures for the various Algorithms #####################################################
########################################################################################################################
def costfunction_all_NetworkStructures_for_Approximation():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",0 ,2.0,2,0,2.0,2.0],
            ["4",2.16,125.04,4,0,4.0,4.0 ],
            ["8",250.083 ,372.097,8,0,8.0,129.68],
            ["16",379.86,372.097,8,259.76,16.0,504.69 ],
            ["32",886.69,2607.007,32,519.52,32.0,1264.73 ],
            ["64",1903.46,5630.31,64,307.76,64.0,3752.51 ],
            ["128",4433.25,5630.31,128,1162.52,128.0,6217.07 ],
            ["256",7342.22,24003.90,256,6552.64,256.0,12096.63 ],
            ["512",17542.49 , 53895.35,512,8951.86,512.0,25169.55],
            ["1024",56812.17,168392.52,1024,68618.70,1024.0,81269.18 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def costfunction_all_NetworkStructures_for_Greedy():
    sns.set_style("ticks")

    data = [["2",124.04,1.161,1.16,0,1.161,1.16 ],
            ["4",124.04,246.92,125.04,0,125.52,125.04 ],
            ["8",371.28,493.97,250.73,0,252.75, 372.65],
            ["16",745.11,1235.35,382.19,388.85,747.28,748.45 ],
            ["32",1746.77,2728.88,1500.48,1158.90,1388.81,1753.92 ],
            ["64",3269.75,5752.19,3217.71,1708.70,2821.53, 4732.42 ],
            ["128",8583.57,12639.10,6510.32,5041.98,5147.98,8244.56 ],
            ["256",13074.54,24125.78,12099.31,23343.71,11187.54,16346.34 ],
            ["512", 36131.69,54017.23,27427.64,110230.25,27571.52,36592.49],
            ["1024",98694.95,168556.29,84872.029,440389.58,109849.121,116151.27 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Greedy")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def costfunction_all_NetworkStructures_for_Genetic():
    sns.set_style("ticks")

    data = [["2", 124.04,1.161,1.16,0,1.161,1.16 ],
            ["4",124.04,246.92,125.04,0,3.3233,125.04 ],
            ["8",249.40,493.97,250.73,0,129.09,372.65 ],
            ["16",624.23,1235.35,382.19,147.86,148.84,748.45 ],
            ["32",1506.15,2728.88,1503.81,1086.42,1273.89, 1753.92],
            ["64",3400.336,5752.19,3623.29,3498.15,2514.96,4734.80 ],
            ["128",8012.42,12639.10,7171.00,23480.76,6212.21,8393.66 ],
            ["256",15039.79,24125.78,14766.39,229235.27,14206.98,17062.14 ],
            ["512",35542.64,54017.23,34354.79,1942119.08,35845.13,39449.045 ],
            ["1024",114932.21,168556.29,108433.52,16359885.61,149304.38,124501.55 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Genetic")
    plt.ylabel("Cost Function")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


## NumberofNodesinVC all Network Structures for the various Algorithms #################################################
########################################################################################################################
def NumberofNodesinVC_all_NetworkStructures_for_Approximation():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",2,2,2,0,2,2 ],
            ["4",2,2,4,0,4,4 ],
            ["8",4,2,8,0,8,6 ],
            ["16",10,2,8,14,16,8 ],
            ["32",20,2,32,28,32,16 ],
            ["64",42,2,64,62,64,28 ],
            ["128",84,2,128,124,128,60 ],
            ["256",170,2,256,250,256,126 ],
            ["512",340,2,512,510,512,272 ],
            ["1024",682,2,1024,1020,1024,534 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Number of nodes in VC")
    #plt.yscale('log')
    plt.tight_layout()

    plt.show()

def NumberofNodesinVC_all_NetworkStructures_for_Greedy():
    sns.set_style("ticks")

    data = [["2",1,1,1,0,1,1 ],
            ["4",1,1,1,0,2,2 ],
            ["8",2,1,4,0,4,3 ],
            ["16",6,1,4,9,10,6 ],
            ["32",10,1,8,21,18,10 ],
            ["64",26,1,32,48,35,18 ],
            ["128",42,1,64,109,72,37 ],
            ["256",106,1,128,234,154,80 ],
            ["512",170,1,256,486,290,163 ],
            ["1024",426,1,512,998,580,321 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Greedy")
    plt.ylabel("Number of nodes in VC")
    # plt.yscale('log')
    plt.tight_layout()

    plt.show()

def NumberofNodesinVC_all_NetworkStructures_for_Genetic():
    sns.set_style("ticks")

    data = [["2", 1,1,1,0,1,1],
            ["4",1 ,1,2,0,3,2],
            ["8", 3,1,4,0,6,3],
            ["16", 8,1,8,11,12,6],
            ["32", 16,1,8,25,21,10],
            ["64", 36,1,32,55,41,19],
            ["128", 69,1,64,114,81,47],
            ["256", 138,1,128,239,330,99],
            ["512", 285,1,256,490,330,217],
            ["1024", 532,1,512,999,659,433],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Genetic")
    plt.ylabel("Number of nodes in VC")
    # plt.yscale('log')
    plt.tight_layout()

    plt.show()

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

def barabasi_m1_lineplot():
    y1 = [0.0, 4.2890500561491636e-07, 8.168520167021456e-06, 0.0006840970466301425, 0.002968398304070831, 0.010820133691660136, 0.020537727870590716, 0.033848750430619974, 0.06615712790862845]
    y2 = [0.0, 3.1018789989484965e-07, 1.1210901861362055e-05, 0.0005034537244778701, 0.0036717190225163594, 0.011833814620475218, 0.026913243426464246, 0.04015625335753356, 0.07426527672877568]
    y3 = [0.0, 8.165135101144238e-07, 1.3862742632150508e-05, 0.0005794497529813799, 0.0032250649126290536, 0.010424094710856056, 0.024221169788849733, 0.04241752383575692, 0.06898042185489739]
    y4 = [0.0, 5.769751375117644e-06, 5.273421260696626e-05, 0.00032454236977170147, 0.0009135026822509431, 0.002277970112297533, 0.0038858616632962625, 0.006518912622161126, 0.019311201284674305]
    y5 = [0.0013131183721436651, 0.0036316845723471315, 0.007868525571247717, 0.012531054722519171, 0.016867087534156396, 0.02229009987394849, 0.029151047924838264, 0.03964331694773781, 0.058777678832860725]
    y6 = [0.0, 4.879709628389587e-06, 8.25009863921149e-05, 0.0027426985019762995, 0.007687178656051101, 0.013656987609191127, 0.021142212454545603, 0.03432470636603896, 0.05738864072212276]
    y7 = [0.0, 1.1854602970564363e-06, 2.3245747529395028e-05, 0.00028770747821812184, 0.0015391739315053713, 0.00838389333457478, 0.019191642111776635, 0.033690322082075466, 0.06137062549175342]
    y8 = [0.0, 7.008801169271505e-07, 2.1767092581602114e-05, 0.0006294753320454894, 0.0026643574121340855, 0.009592051784066602, 0.020603423507313628, 0.0379943318767833, 0.06890334027194403]
    y9 = [9.806251688984512e-08, 5.284608762859658e-06, 8.79045903792615e-05, 0.0014385582576960914, 0.005971444882609147, 0.015567865311283749, 0.02672211743074454, 0.044079704427644424, 0.06752622619189436]
    x = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    plt.plot(x, y1, "-+", label="DP")
    plt.plot(x, y2, "-o", label="TR")
    plt.plot(x, y3, "-*", label="SP")
    plt.plot(x, y4, "--", label="HD")
    plt.plot(x, y5, "-p", label="TSH")
    plt.plot(x, y6, "-.", label="SQ")
    plt.plot(x, y7, ":", label="DR")
    plt.plot(x, y8, "-v", label="STT")
    plt.plot(x, y9, label="OW")
    plt.legend(loc="upper left")
    plt.xlabel("Percentiles")
    plt.ylabel("DTW distance")
    plt.tight_layout()
    plt.savefig("dtw_per.pdf", dpi=300)


def vertices_and_edges_of_various_graph_topologies():
    sns.set_style("ticks")

    data = [["2", 1, 1, 1,                  0,     1, 1],
            ["4", 2, 3, 3,                  0,     5, 3],
            ["8", 6, 7, 7,                  0,     12, 7],
            ["16", 14, 15, 15,              25,    23, 15],
            ["32", 30, 31, 31,              105,   48, 31],
            ["64", 62, 63, 63,              394,   99, 63],
            ["128", 126, 127, 127,          1612,  191, 127],
            ["256", 254, 255, 255,          6522,  400, 255],
            ["512", 510, 511, 511,          26207, 763, 511],
            ["1024", 1022, 1023, 1023,      104927,1528, 1023],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Balanced Tree", "Star",
                                     "Binomial", "Erdo-Renyi",
                                     "Watts–Strogatz", "Barabasi-Albert"])
    df.plot(x="Number of Vertices",
            y=["Balanced Tree", "Star", "Binomial",
               "Erdo-Renyi", "Watts–Strogatz", "Barabasi-Albert"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Vertices and Edges")
    plt.ylabel("Edges")
    plt.ylim(0, 1700)
    #plt.yscale('log')
    plt.tight_layout()

    plt.show()


def vertex_edges_ErdosRenyi_probability():
    y1 = [1,3,7, 25, 105, 394, 1612, 6522, 26207, 104927]
    y2 = [1,3,11,66,248,1003, 4054, 16331, 65574, 262255]
    y3 = [1,4,20,94,360,1417,5712,22951,91762,366916]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="p=0.2", color="gray")
    plt.plot(x, y2, "-o", label="p=0.5", color="gray")
    plt.plot(x, y3, "-*", label="p=0.7", color="gray")
    # plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Number of Edges")
    plt.title("Erdo-Renyi")
    plt.tight_layout()
    # plt.yscale('log')
    plt.tight_layout()
    plt.show()


def vertex_edges_WattsStrogatz_degree():
    y1 = [1,5,12,23,48,99,191,400,763,1528]
    y2 = [0,6,24,49,101,194,389,764,1529,3072]
    y3 = [0,0,28,76,146,287,580,1144,2303,4635]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="k(L)=2", color="gray")
    plt.plot(x, y2, "-o", label="k(L)=4", color="gray")
    plt.plot(x, y3, "-*", label="k(L)=7", color="gray")
    # plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Number of Edges")
    plt.title("Watts-Strogatz")
    plt.tight_layout()
    # plt.yscale('log')
    plt.tight_layout()
    plt.show()

def vertex_edges_Barabasi_degree():
    y1 = [1,3,7,15,31,63,127,255,511,1023]
    y2 = [0,3,15,39,87,183,375,759,1527,3063]
    y3 = [0,3,15,64,192,448,960,1984,4032,8128]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    sns.set_style("ticks")
    plt.plot(x, y1, "-+", label="m=1", color="gray")
    plt.plot(x, y2, "-o", label="m=3", color="gray")
    plt.plot(x, y3, "-*", label="m=8", color="gray")
    # plt.plot(x, y4, "--", label="ILP", color="peru")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Number of Edges")
    plt.title("Barabasi-Albert")
    plt.tight_layout()
    # plt.yscale('log')
    plt.tight_layout()
    plt.show()

# def vertex_edges_BalancedTree():
#     y1 = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]
#     y2 = [0, 3, 15, 39, 87, 183, 375, 759, 1527, 3063]
#     y3 = [0, 3, 15, 64, 192, 448, 960, 1984, 4032, 8128]
#
#     x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
#
#     sns.set_style("ticks")
#     plt.plot(x, y1, "-+", label="BT-r_{2}", color="gray")
#     plt.plot(x, y2, "-o", label="BT-r_{3}", color="gray")
#     plt.plot(x, y3, "-*", label="BT-r_{5}", color="gray")
#     plt.plot(x, y4, "--", label="BT-h_{2}", color="gray")
#     plt.plot(x, y5, "-v", label="BT-h_{4}", color="gray")
#     plt.legend(loc="upper left")
#     plt.xlabel("Number of Vertices")
#     plt.ylabel("Number of Edges")
#     plt.title("Balanced Tree")
#     plt.tight_layout()
#     # plt.yscale('log')
#     plt.tight_layout()
#     plt.show()



if __name__ == '__main__':
    # miscellaneous
    #vertices_and_edges_of_various_graph_topologies()
    #vertex_edges_ErdosRenyi_probability()
    #vertex_edges_WattsStrogatz_degree()
    #vertex_edges_Barabasi_degree()
    #barabasi_m1_lineplot()
    vertex_edges_BalancedTree()


    #---------------------------------------------------------------------------------------------------------------------------


    ## Execution Times all Algorithms for the various Network Topologies ###################################################
    #execution_time_all_Algorithms_Binomial()
    #execution_time_all_Algorithms_Binomial_LINE()
    # execution_time_all_Algorithms_Balanced()
    #execution_time_all_Algorithms_Star()
    #execution_time_all_Algorithms_Star_LINE()
    # execution_time_all_Algorithms_BarabasiAlbert()
    #execution_time_all_Algorithms_BarabasiAlbert_LINE()
    ########################################################################################################################
    ########################################################################################################################

    ## Cost Function all Algorithms for the various Network Topologies ###################################################
    #costfunction_all_Algorithms_BarabasiAlbert()
    #costfunction_all_Algorithms_Binomial()
    #costfunction_all_Algorithms_Star()
    ########################################################################################################################
    ########################################################################################################################

    ## NumberofNodesinVC all Algorithms for the various Network Topologies ###################################################
    #NumberofNodesinVC_all_Algorithms_BarabasiAlbert()
    #NumberofNodesinVC_all_Algorithms_Balanced()
    # NumberofNodesinVC_all_Algorithms_Star() -> DOES NOT NEED
    # NumberofNodesinVC_all_Algorithms_Binomial() -> DOES NOT NEED
    ########################################################################################################################
    ########################################################################################################################

    ## ApproximationRatio all Algorithms for the various Network Topologies ###################################################
    #ApproximationRatio_all_Algorithms_Binomial()
    #ApproximationRatio_all_Algorithms_Star() -> Not needed, it is the same as binomial
    #ApproximationRatio_all_Algorithms_Barabasi()
    ########################################################################################################################
    ########################################################################################################################









    #-------------------------------------------------------------------------------------------------------------------










    ## Execution Times all Network Structures for the various Algorithms ###################################################
    # execution_time_all_NetworkStructures_for_Approximation()
    #execution_time_all_NetworkStructures_for_Approximation_LINE()
    # execution_time_all_NetworkStructures_for_Greedy()
    #execution_time_all_NetworkStructures_for_Greedy_LINE()
    # execution_time_all_NetworkStructures_for_Genetic()
    #execution_time_all_NetworkStructures_for_Genetic_LINE()
    ########################################################################################################################
    ########################################################################################################################

    ## Cost Function all Network Structures for the various Algorithms #####################################################
    #costfunction_all_NetworkStructures_for_Approximation()
    #costfunction_all_NetworkStructures_for_Greedy()
    #costfunction_all_NetworkStructures_for_Genetic()
    ########################################################################################################################
    ########################################################################################################################

    # NumberofNodesinVC all Network Structures for the various Algorithms ###############################################
    # NumberofNodesinVC_all_NetworkStructures_for_Approximation()
    # NumberofNodesinVC_all_NetworkStructures_for_Greedy()
    # NumberofNodesinVC_all_NetworkStructures_for_Genetic()
    ########################################################################################################################
    ########################################################################################################################







