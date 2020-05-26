import matplotlib.pyplot as plt
import numpy as np
import datetime

def draw_pic(title, res_model, data, **kwargs):   
    tickFontSize = 15
    labelFontSize = 20
    titleFontSize = 25
    Font = 'Times New Roman'
    
    fig = plt.figure(**kwargs)
 
    ax1 = fig.add_subplot(111)
    ax1.plot(res_model.smoothed_marginal_probabilities[1],'r')
    
    ax1.set_ylabel('Regime-One Probability',fontsize = labelFontSize,
                   family = Font)
    ax1.set_ylim([-0.2, 2.4])
    ax1.set_yticks(np.array(range(-2,26,2))/10)
    ax1.set_yticklabels(np.array(range(-2,26,2))/10,fontsize = tickFontSize)

    ax2 = ax1.twinx()  
    ax2.plot(data.unc)
    
    ax2.set_ylim([-5, 5])
    ax2.set_ylabel('UNC',fontsize = labelFontSize,
                   family = Font)
    ax2.set_yticks(np.array(range(-5,6,1)))
    ax2.set_yticklabels(np.array(range(-5,6,1)),fontsize = tickFontSize)
    
    
    ax1.set_xlim(min(data.index),max(data.index))
    x_ticks = [datetime.datetime(year,6,1) for year in range(1986,2020)]
    ax1.set_xticks(x_ticks)
    ax1.set_xticklabels(range(1986,2020), rotation=90,
                        fontsize = tickFontSize, 
                        family = Font)
    
    ax1.set_title(title, fontsize = titleFontSize, pad = 13,
                  family = Font)
    plt.show()


def print_regime(data,res_model,title,width_list = [15, 10, 12, 12, 12, 12, 15]):
    main_tile = '{:^%ds}' % sum(width_list)
    print(main_tile.format(title))
    regime0_index = res_model.smoothed_marginal_probabilities.index \
                        [(res_model.smoothed_marginal_probabilities[0]>0.8)]
    regime1_index = res_model.smoothed_marginal_probabilities.index \
                        [(res_model.smoothed_marginal_probabilities[1]>0.8)]
    regime0_stock = data.loc[regime0_index].stock
    regime0_bond = data.loc[regime0_index].bond
    regime1_stock = data.loc[regime1_index].stock
    regime1_bond = data.loc[regime1_index].bond
    
    title_width_list = [width_list[0]+width_list[1],width_list[2]+width_list[3],
                        width_list[4]+width_list[5],width_list[6]]
    title_format = '{:^%ds}{:^%ds}{:^%ds}{:^%ds}' % tuple(title_width_list)
    header_format = '{:^%ds}{:^%ds}{:^%ds}{:^%ds}{:^%ds}{:^%ds}{:^%ds}' % tuple(width_list)
    body_format = '{:<%ds}{:<%ds}{:^%ds}{:^%ds}{:^%ds}{:^%ds}{:^%ds}' % tuple(width_list)
    
    titile = [' ','Stock Returns','T-Bond Returns',' ']
    header = ['Regime','Obs.','Mean','Std. Dev.','Mean','Std. Dev.','Corr.(Bt,St)']
    body1 = ['All obs.', 'n = {:d}'.format(len(data)),
           '{:.4f}'.format(data.stock.mean()), '{:.4f}'.format(data.stock.std()),
           '{:.4f}'.format(data.bond.mean()), '{:.4f}'.format(data.bond.std()),
           '{:.4f}'.format(data.stock.corr(data.bond))]
    body2 = ['Regime-zero', 'n = {:d}'.format(len(regime0_stock)),
           '{:.4f}'.format(regime0_stock.mean()), '{:.4f}'.format(regime0_stock.std()),
           '{:.4f}'.format(regime0_bond.mean()), '{:.4f}'.format(regime0_bond.std()),
           '{:.4f}'.format(regime0_stock.corr(regime0_bond))]
    body3 = ['Regime-one', 'n = {:d}'.format(len(regime1_stock)),
           '{:.4f}'.format(regime1_stock.mean()), '{:.4f}'.format(regime1_stock.std()),
           '{:.4f}'.format(regime1_bond.mean()), '{:.4f}'.format(regime1_bond.std()),
           '{:.4f}'.format(regime1_stock.corr(regime1_bond))]
    
    print(title_format.format(*titile))
    print(header_format.format(*header))
    print(body_format.format(*body1))
    print(body_format.format(*body2))
    print(body_format.format(*body3))