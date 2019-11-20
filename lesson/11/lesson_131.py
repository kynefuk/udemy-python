from optparse import OptionParser


def main():

    # 使用方法の説明書き
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)

    # オプション追加
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='input file name')

    options, args = parser.parse_args()

    print(options.filename)
    print(args)


if __name__ == '__main__':
    main()
