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
            kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
    plt.xticks(rotation=0)
    plt.title("Binomial Tree")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()


# Balanced Tree
# def execution_time_all_Algorithms_Balanced():
#     # r = 2 -- h = increased by 1 in every run, starts with 1
#     sns.set_style("ticks")
#
#     data = [["2",0.00012 ,0.00014,,],
#             ["4", ,,,],
#             ["8", ,,,],
#             ["16", ,,,],
#             ["32", ,,,],
#             ["64", ,,,],
#             ["128", ,,,],
#             ["256", ,,,],
#             ["512", ,,,],
#             ["1024", ,,,],
#             ]
#
#     df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation", "Greedy", "Genetic", "ILP"])
#     df.plot(x="Number of Vertices", y=["Approximation", "Greedy", "Genetic", "ILP"],
#             kind="bar", figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'cyan'])
#     plt.xticks(rotation=0)
#     plt.title("Balanced Tree")
#     plt.ylabel("Execution time (seconds)")
#     plt.yscale('log')
#     plt.tight_layout()
#
#     plt.show()

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

    data = [["2", 0, 0.000131, 0.000121, 0, 0.00013, 0.00013],
            ["4", 0.00012, 0.00017, 0.000162, 0, 0.00014, 0.00015],
            ["8", 0.00013, 0.00015, 0.000175, 0, 0.00022, 0.00015],
            ["16", 0.00034, 0.00036, 0.000436, 0.00046, 0.00051, 0.0005],
            ["32", 0.0012, 0.00110, 0.00132, 0.0013, 0.0029, 0.0019],
            ["64", 0.0221, 0.0207, 0.0227, 0.0216, 0.0243, 0.0213],
            ["128", 0.0387, 0.0438, 0.0379, 0.05640, 0.0413],
            ["256", 0.0977, 0.0913, 0.0106, 0.1936, 0.1614, 0.122],
            ["512", 0.444, 0.3236, 0.406, 1.3412, 0.5105, 0.468],
            ["1024", 1.993, 1.312, 1.87, 9.074, 2.4698, 4.192],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation (Balanced Tree)", "Approximation (Star)",
                                     "Approximation (Binomial)", "Approximation (Erdo-Renyi)",
                                     "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"])
    df.plot(x="Number of Vertices",
            y=["Approximation (Balanced Tree)", "Approximation (Star)", "Approximation (Binomial)",
               "Approximation (Erdo-Renyi)", "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def execution_time_all_NetworkStructures_for_Greedy():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",0,0.000111,0.000130,0,0.00011,0.00011 ],
            ["4",0.00014,0.00011,0.000161 ,0 ,0.00016,0.00018],
            ["8",0.00021,0.00023, 0.000286,0,0.00029,0.0003 ],
            ["16",0.00080,0.00045,0.000623 ,0.00053,0.0007,0.0007 ],
            ["32",0.0015,0.00143, 0.00182,0.0019,0.0022,0.0022 ],
            ["64",0.0223,0.0190,0.0204 ,0.0288,0.0283,0.0247 ],
            ["128",0.04617,0.03680,0.0412 ,0.0736,0.0504,0.0509 ],
            ["256",0.113,0.0900,0.102 ,0.3496,0.162,0.142 ],
            ["512",0.4588,0.3381, 0.441,2.479,0.5051,0.509 ],
            ["1024",1.96,1.4089,1.836 ,22.3394,2.368,2.407 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Greedy (Balanced Tree)", "Greedy (Star)",
                                     "Greedy (Binomial)", "Greedy (Erdo-Renyi)", "Greedy (Watts–Strogatz)", "Greedy (Barabasi-Albert)"])
    df.plot(x="Number of Vertices",
            y=["Greedy (Balanced Tree)", "Greedy (Star)", "Greedy (Binomial)", "Greedy (Erdo-Renyi)", "Greedy (Watts–Strogatz)", "Greedy (Barabasi-Albert)"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Greedy")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

def execution_time_all_NetworkStructures_for_Genetic():
    # Balanced Tree -> r = 2 -- h = increased by 1 in every run, starts with 1
    # Erdo Renyi -> p=0.2
    # Watts - Strogatz -> k=2
    # Barabasi-Albert -> m=1

    sns.set_style("ticks")

    data = [["2",0 ,0.00921 ,0.0096 ,0 ,0.0106 , 0.0117  ],
            ["4",0.0176 ,0.0204 ,0.0174 ,0 ,0.0168 ,0.028 ],
            ["8",0.03386,0.0476 , 0.0313,0 ,0.0308 ,0.0549 ],
            ["16",0.0940,0.1268 ,2.61 ,0.0842 ,0.05177 ,0.128 ],
            ["32",0.3064,0.4633 ,0.6649 ,0.145 ,0.1502 ,0.388 ],
            ["64",0.9414,1.5824 ,0.585 ,0.3792 ,0.4967 ,1.366 ],
            ["128",3.997,7.015 ,2.1467 ,1.116 ,1.399 , 7.533],
            ["256",16.495,22.812 ,8.377 ,3.635 ,5.2896 ,22.392 ],
            ["512",76.28,107.366 ,36.002 ,16.013 ,25.899 , 87.12],
            ["1024",310.96,443.81 , 147.58,56.665 ,110.31 ,368.45 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Genetic (Balanced Tree)", "Genetic (Star)",
                                     "Genetic (Binomial)", "Genetic (Erdo-Renyi)", "Genetic (Watts–Strogatz)",
                                     "Genetic (Barabasi-Albert)"])
    df.plot(x="Number of Vertices",
            y=["Genetic (Balanced Tree)", "Genetic (Star)", "Genetic (Binomial)", "Genetic (Erdo-Renyi)",
               "Genetic (Watts–Strogatz)", "Genetic (Barabasi-Albert)"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Genetic")
    plt.ylabel("Execution time (seconds)")
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

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation (Balanced Tree)", "Approximation (Star)",
                                     "Approximation (Binomial)", "Approximation (Erdo-Renyi)",
                                     "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"])
    df.plot(x="Number of Vertices",
            y=["Approximation (Balanced Tree)", "Approximation (Star)", "Approximation (Binomial)",
               "Approximation (Erdo-Renyi)", "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
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

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation (Balanced Tree)", "Approximation (Star)",
                                     "Approximation (Binomial)", "Approximation (Erdo-Renyi)",
                                     "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"])
    df.plot(x="Number of Vertices",
            y=["Approximation (Balanced Tree)", "Approximation (Star)", "Approximation (Binomial)",
               "Approximation (Erdo-Renyi)", "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"],
            kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Number of nodes in VC")
    #plt.yscale('log')
    plt.tight_layout()

    plt.show()
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


def barabasi_m1_lineplot():
    y1_m1 = [2.0, 4.0, 129.68, 504.69, 1264.73, 3752.51, 6217.07, 12096.63, 25169.55, 81269.18]
    # y1_m3 = [4.0, 8.0, 134.68, 604.69, 1664.73, 3952.51, 6917.07, 12996.63, 27169.55, 85269.18]
    y2 = [1.16, 125.04, 372.65, 748.45, 1753.92, 4732.42, 8244.56, 16346.34, 36592.49, 116151.27]
    y3 = [1.16, 125.04, 372.65, 748.45, 1753.92, 4734.80, 8393.66, 17062.14, 39449.045, 124501.55]
    y4 = [1.16, 125.04, 372.65, 870.33, 1756.54, 4854.30, 8280.75, 16260.24, 36950.95, 117625.16]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # y1 = [0.0, 4.2890500561491636e-07, 8.168520167021456e-06, 0.0006840970466301425, 0.002968398304070831, 0.010820133691660136, 0.020537727870590716, 0.033848750430619974, 0.06615712790862845]
    # y2 = [0.0, 3.1018789989484965e-07, 1.1210901861362055e-05, 0.0005034537244778701, 0.0036717190225163594, 0.011833814620475218, 0.026913243426464246, 0.04015625335753356, 0.07426527672877568]
    # y3 = [0.0, 8.165135101144238e-07, 1.3862742632150508e-05, 0.0005794497529813799, 0.0032250649126290536, 0.010424094710856056, 0.024221169788849733, 0.04241752383575692, 0.06898042185489739]
    # y4 = [0.0, 5.769751375117644e-06, 5.273421260696626e-05, 0.00032454236977170147, 0.0009135026822509431, 0.002277970112297533, 0.0038858616632962625, 0.006518912622161126, 0.019311201284674305]
    # y5 = [0.0013131183721436651, 0.0036316845723471315, 0.007868525571247717, 0.012531054722519171, 0.016867087534156396, 0.02229009987394849, 0.029151047924838264, 0.03964331694773781, 0.058777678832860725]
    # y6 = [0.0, 4.879709628389587e-06, 8.25009863921149e-05, 0.0027426985019762995, 0.007687178656051101, 0.013656987609191127, 0.021142212454545603, 0.03432470636603896, 0.05738864072212276]
    # y7 = [0.0, 1.1854602970564363e-06, 2.3245747529395028e-05, 0.00028770747821812184, 0.0015391739315053713, 0.00838389333457478, 0.019191642111776635, 0.033690322082075466, 0.06137062549175342]
    # y8 = [0.0, 7.008801169271505e-07, 2.1767092581602114e-05, 0.0006294753320454894, 0.0026643574121340855, 0.009592051784066602, 0.020603423507313628, 0.0379943318767833, 0.06890334027194403]
    # y9 = [9.806251688984512e-08, 5.284608762859658e-06, 8.79045903792615e-05, 0.0014385582576960914, 0.005971444882609147, 0.015567865311283749, 0.02672211743074454, 0.044079704427644424, 0.06752622619189436]
    # x = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    # plt.plot(x, y1, "-+", label="DP")
    # plt.plot(x, y2, "-o", label="TR")
    # plt.plot(x, y3, "-*", label="SP")
    # plt.plot(x, y4, "--", label="HD")
    # plt.plot(x, y5, "-p", label="TSH")
    # plt.plot(x, y6, "-.", label="SQ")
    # plt.plot(x, y7, ":", label="DR")
    # plt.plot(x, y8, "-v", label="STT")
    # plt.plot(x, y9, label="OW")
    # plt.legend(loc="upper left")
    # plt.xlabel("Percentiles")
    # plt.ylabel("DTW distance")
    # plt.tight_layout()
    # plt.savefig("dtw_per.pdf", dpi=300)
    sns.set_style("ticks")
    plt.plot(x, y1_m1, "-+", label="Approximation")
    # plt.plot(x, y1_m3, "-+", label="Approximation m=3", color="blue")
    plt.plot(x, y2, "-o", label="Greedy")
    plt.plot(x, y3, "-*", label="Genetic")
    plt.plot(x, y4, "--", label="ILP")
    plt.legend(loc="upper left")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Cost function")

    plt.tight_layout()
    plt.show()
    # plt.savefig("sspd_per.pdf", dpi=300)



if __name__ == '__main__':

    ## Execution Times all Algorithms for the various Network Topologies ###################################################
    #execution_time_all_Algorithms_Binomial()
    # execution_time_all_Algorithms_Balanced()
    # execution_time_all_Algorithms_Star()
    # execution_time_all_Algorithms_BarabasiAlbert()
    ########################################################################################################################
    ########################################################################################################################

    ## Cost Function all Algorithms for the various Network Topologies ###################################################
    costfunction_all_Algorithms_BarabasiAlbert()
    ########################################################################################################################
    ########################################################################################################################

    ## NumberofNodesinVC all Algorithms for the various Network Topologies ###################################################
    NumberofNodesinVC_all_Algorithms_BarabasiAlbert()
    ########################################################################################################################
    ########################################################################################################################


    #-------------------------------------------------------------------------------------------------------------------



    ## Execution Times all Network Structures for the various Algorithms ###################################################
    execution_time_all_NetworkStructures_for_Approximation()
    # execution_time_all_NetworkStructures_for_Greedy()
    # execution_time_all_NetworkStructures_for_Genetic()
    ########################################################################################################################
    ########################################################################################################################

    ## Cost Function all Network Structures for the various Algorithms #####################################################
    # costfunction_all_NetworkStructures_for_Approximation()
    ########################################################################################################################
    ########################################################################################################################

    # NumberofNodesinVC all Network Structures for the various Algorithms ###############################################
    #NumberofNodesinVC_all_NetworkStructures_for_Approximation()
    ########################################################################################################################
    ########################################################################################################################




    # barabasi_m1_lineplot()


