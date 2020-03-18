import os
import pandas

#ディレクトリをMainに移動
main_dir = 'VOCDevkit/VOC2007/ImageSets/Main'
os.chdir(main_dir)

#現在のディレクトリを出力
pwd = os.getcwd()
print(pwd)


def make_train_files():
    suffixs = ['_train','_val','_test']

    for suffix in suffixs:
        #suffix:添え字
        print('suffix',suffix)
        #replace(a,b):aをｂで置換する
        #'w':書き込み用で新規ファイルをopen
        new_file = open('{}.txt'.format(suffix.replace('_','')),'w')
        text = ""
        for file in os.listdir():
            #.find:検索してインデックスをかえす、ないときは-1
            #train.txt,val.txt,test.txt以外のファイルは実行しない
            if file.find(suffix) == -1:continue
            with open(file) as f:
                if text == "":text = f.read()
                text =text +'\n'+ f.read()
        new_file.write(text)

#valの33%をテストに
def split_val_test(rate:float):
    val = pandas.read_csv('val.txt')
    val = val.sample(frac=1)
    print('len',len(val))
    split = int(len(val) * rate)
    test = val.values
    val[:split].to_csv('val.txt',index=False)
    val[split:].to_csv('test.txt',index=False)
    print('val.txt',split)
    print('test.txt',len(val) - split)

if __name__ == '__main__':
    val_rate = 0.33
    make_train_files()
    split_val_test(val_rate)
