import  jieba
__author__ = 'suwk'

FILE_PATH = '../data/keywords_user.log'

def split_data(path=FILE_PATH):
    print path
    with open(path) as data:
        for line in data:
            print line.split('\t')
            break

if __name__ == '__main__':
    split_data()