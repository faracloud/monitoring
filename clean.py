import pandas as pd

def jtest(a):
   print(a*3)

def do_clean(my_data):
    my_data = my_data.replace({'گیگابایت': 'GB'}, regex=True)
    my_data = my_data.replace({'مگابیت': 'Mb'}, regex=True)
    my_data = my_data.replace({'لینوکس': 'Linux'}, regex=True)
    my_data = my_data.replace({'ویندوز': 'Windows'}, regex=True)
    my_data = my_data.replace({'پارس‌آنلاین/افرانت': 'IR'}, regex=True)
    my_data = my_data.replace({'۰': '0'}, regex=True)
    my_data = my_data.replace({'۱': '1'}, regex=True)
    my_data = my_data.replace({'۲': '2'}, regex=True)
    my_data = my_data.replace({'۳': '3'}, regex=True)
    my_data = my_data.replace({'۴': '4'}, regex=True)
    my_data = my_data.replace({'۵': '5'}, regex=True)
    my_data = my_data.replace({'۶': '6'}, regex=True)
    my_data = my_data.replace({'۷': '7'}, regex=True)
    my_data = my_data.replace({'۸': '8'}, regex=True)
    my_data = my_data.replace({'۹': '9'}, regex=True)
    my_data["RAM"] = my_data["RAM"].replace({'/': '.'}, regex=True)
    my_data["BW"] = my_data["BW"].replace({'Gbit/s-Port': 'Gb'}, regex=True)
    
    
    return (my_data)


def aggregator(dataframe):
    versionFile = open('file_version', 'r')
    version= versionFile.read().strip("\n")
    newVersion=int(version)+1
    
    if(int(version) == 0):
        dataframe.to_csv('cleanData-{}.csv'.format(newVersion), header=True,index=True)
        return dataframe
        
    else:
        main = pd.read_csv('cleanData-{}.csv'.format(version), index_col = 0)
        
        aggDataFram = main.append(dataframe)
        aggDataFram=aggDataFram.reset_index(drop=True)
        aggDataFram.to_csv('cleanData-{}.csv'.format(newVersion), header=True,index=True)
        return aggDataFram
        

    versionFile = open('file_version', 'w')
    versionFile.write('{}'.format(newVersion))
    
    


