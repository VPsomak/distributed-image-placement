# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import pandas as pd


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


def execution_time_Binomial():
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

def execution_time_all_for_Approximation():
    sns.set_style("ticks")

    data = [["2", 0, 0.000131, 0.000121, 0, 0.00013, 0.00013],
            ["4", 0.00012, 0.00017 , 0.000162 , 0, 0.00014, 0.00015],
            ["8", 0.00013,0.00015 ,0.000175 ,0,0.00022,0.00015],
            ["16", 0.00034,0.00036 ,0.000436 ,0.00046,0.00051,0.0005 ],
            ["32",0.0012 ,0.00110 ,0.00132 ,0.0013,0.0029,0.0019 ],
            ["64",0.0221 ,0.0207 ,0.0227 ,0.0216,0.0243,0.0213 ],
            ["128",0.0387 ,0.0438 ,0.0379 ,0.05640,0.0413 ],
            ["256",0.0977 , 0.0913, 0.0106 ,0.1936,0.1614 ,0.122 ],
            ["512", 0.444, 0.3236,0.406 ,1.3412,0.5105,0.468 ],
            ["1024",1.993 ,1.312 ,1.87 ,9.074,2.4698,4.192 ],
            ]

    df = pd.DataFrame(data, columns=["Number of Vertices", "Approximation (Balanced Tree)", "Approximation (Star)", "Approximation (Binomial)", "Approximation (Erdo-Renyi)", "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"])
    df.plot(x="Number of Vertices", y=["Approximation (Balanced Tree)", "Approximation (Star)", "Approximation (Binomial)", "Approximation (Erdo-Renyi)", "Approximation (Watts–Strogatz)", "Approximation (Barabasi-Albert)"],kind="bar",
            figsize=(9, 8), color=['lightsteelblue', 'cornflowerblue', 'dimgray', 'peru', 'powderblue', 'silver'])
    plt.xticks(rotation=0)
    plt.title("Approximation")
    plt.ylabel("Execution time (seconds)")
    plt.yscale('log')
    plt.tight_layout()

    plt.show()

# def execution_time_all_for_Greedy():
#     "Greedy (Balanced Tree)", "Greedy (Star)", "Greedy (Binomial)", "Greedy (Erdo-Renyi)", "Greedy (Watts–Strogatz)", "Greedy (Barabasi-Albert)"

# def execution_time_all_for_Genetic():
    #"Genetic (Balanced Tree)", "Genetic (Star)", "Genetic (Binomial)", "Genetic (Erdo-Renyi)", "Genetic (Watts–Strogatz)", "Genetic (Barabasi-Albert)",

#def execution_time_all_for_ILP():
    # "ILP (Balanced Tree)", "ILP (Star)", "ILP (Binomial)", "ILP (Erdo-Renyi)", "ILP (Watts–Strogatz)", "ILP (Barabasi-Albert)"

def barabasi_m1_lineplot():
    y1_m1 = [2.0, 4.0, 129.68, 504.69, 1264.73, 3752.51, 6217.07, 12096.63, 25169.55, 81269.18]
    #y1_m3 = [4.0, 8.0, 134.68, 604.69, 1664.73, 3952.51, 6917.07, 12996.63, 27169.55, 85269.18]
    y2 = [1.16, 125.04, 372.65, 748.45, 1753.92, 4732.42, 8244.56, 16346.34, 36592.49, 116151.27]
    y3 = [1.16, 125.04, 372.65, 748.45, 1753.92, 4734.80, 8393.66, 17062.14, 39449.045, 124501.55]
    y4 = [1.16, 125.04, 372.65, 870.33, 1756.54, 4854.30, 8280.75, 16260.24, 36950.95, 117625.16]

    x = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
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
    #plt.savefig("sspd_per.pdf", dpi=300)


# barabasi_m1_lineplot()
execution_time_Binomial()
execution_time_all_for_Approximation()
# execution_time_all_for_Greedy()
# execution_time_all_for_Genetic()
# execution_time_all_for_ILP()