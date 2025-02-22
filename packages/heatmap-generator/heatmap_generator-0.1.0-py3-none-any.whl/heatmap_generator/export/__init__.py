from .rpcanet_plus_copy_yixuan import *


def get_model(name, net=None):

    if name == 'rpcanet':
        net = RPCANet(stage_num=6,slayers=6, llayers=4, mlayers=3, channel=32)
# ===========================================================

    elif name == 'rpcanet_lstm':
        net = RPCANet_LSTM(stage_num=3, slayers=6, mlayers=3, channel=32)

    elif name == 'rpcanet_lstm_s6':
        net = RPCANet_LSTM(stage_num=6, slayers=6, mlayers=3, channel=32)


    elif name == 'rpcanet_lstm1':
        net = RPCANet_LSTM1(stage_num=3, slayers=6, mlayers=3, channel=32)

    elif name == 'rpcanet_lstm2':
        net = RPCANet_LSTM2(stage_num=3, slayers=6, mlayers=3, channel=32)

    # ===========================================================
    elif name == 'rpcanet_exp_ma':
        net = RPCANetMA(stage_num=6,slayers=6, llayers=3, mlayers=3, channel=32)
    # ===========================================================


    elif name == 'rpcanet_exp_s1':
        net = RPCANet9(stage_num=1, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s2':
        net = RPCANet9(stage_num=2, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s3':
        net = RPCANet9(stage_num=3, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s4':
        net = RPCANet9(stage_num=4, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s5':
        net = RPCANet9(stage_num=5, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s6':
        net = RPCANet9(stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s7':
        net = RPCANet9(stage_num=7, slayers=6, llayers=3, mlayers=3, channel=32)
    elif name == 'rpcanet_exp_s8':
        net = RPCANet9(stage_num=8, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s9':
        net = RPCANet9(stage_num=9, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s10':
        net = RPCANet9(stage_num=10, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_s12':
        net = RPCANet9(stage_num=12, slayers=6, llayers=3, mlayers=3, channel=32)
    # ===========================================================


    elif name == 'rpcanet_exp_b4':
        net = RPCANet9(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_exp_b6':
        net = RPCANet9(stage_num=6, slayers=6, llayers=6, mlayers=3, channel=32)
    elif name == 'rpcanet_exp_b2':
        net = RPCANet9(stage_num=6, slayers=6, llayers=2, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_t1':
        net = RPCANet9(stage_num=6, slayers=1, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_t3':
        net = RPCANet9(stage_num=6, slayers=3, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_t6':
        net = RPCANet9(stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_t9':
        net = RPCANet9(stage_num=6, slayers=9, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanet_exp_t12':
        net = RPCANet9(stage_num=6, slayers=12, llayers=3, mlayers=3, channel=32)
    # ===========================================================

    elif name == 'rpcanet_experi_k3':
        net = RPCANet_Experi(stage_num=3, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_k5':
        net = RPCANet_Experi(stage_num=5, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_k6':
        net = RPCANet_Experi(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_k7':
        net = RPCANet_Experi(stage_num=7, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_k9':
        net = RPCANet_Experi(stage_num=9, slayers=6, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanet_experi_l2':
        net = RPCANet_Experi(stage_num=6, slayers=2, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_l4':
        net = RPCANet_Experi(stage_num=6, slayers=4, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_l6':
        net = RPCANet_Experi(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_l8':
        net = RPCANet_Experi(stage_num=6, slayers=8, llayers=4, mlayers=3, channel=32)
    elif name == 'rpcanet_experi_l10':
        net = RPCANet_Experi(stage_num=6, slayers=10, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanet_wo_merge':
        net = RPCANet_wo_Merge(stage_num=6, slayers=6, llayers=4, channel=32)
    elif name == 'rpcanet':
        net = RPCANet(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanet9':
        net = RPCANet9(stage_num=6, slayers=6, mlayers=3, channel=32)
    elif name == 'rpcanet9_cbam':
        net = RPCANet9_CBAM(stage_num=6, slayers=6,llayers=3, mlayers=3, channel=32)
    
    
    elif name == 'rpcanet_lstm_wop':
        net = RPCANet_LSTM_wop(stage_num=6, slayers=6, mlayers=3, channel=32)



    
    elif name == 'rpcanetma7':
        net = RPCANetMA7(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanetma8':
        net = RPCANetMA8(stage_num=6, slayers=6, mlayers=3, channel=32)
    elif name == 'rpcanetma9':
        net = RPCANetMA9(stage_num=6, slayers=6, mlayers=3, channel=32)

    elif name == 'rpcanetma10':
        net = RPCANetMA10(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanetma11':
        net = RPCANetMA11(stage_num=6, slayers=6, llayers=4, mlayers=3, channel=32)

    elif name == 'rpcanetma12':
        net = RPCANetMA12(stage_num=6, slayers=6, llayers=3, mlayers=3, channel=32)

    elif name == 'rpcanetma12_s3':
        net = RPCANetMA12(stage_num=3, slayers=6, llayers=3, mlayers=3, channel=32)



    else:
        raise NotImplementedError

    return net

