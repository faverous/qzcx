import numpy as np
import tensorflow as tf
import xlrd
import xlsxwriter


def batch_generator(path, batch_size, seq_len):
    """
    生成带有标签的数据集，并划分mini-batch
    """

    with xlrd.open_workbook(path) as get_data:
        table = get_data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols

        x = []
        X = []
        for i in range(nrows - seq_len + 1):
            for j in range(seq_len):
                rowValues1 = table.row_values(i + j)[:]
                x.append(rowValues1)
            X.append(x)
            x = []

        arrX = np.array(X)

    return arrX

    """
    # 可以分得的batch个数
    #n_batches = int(len(arrX) / (batch_size * seq_len))
    # print(n_batches)
    #arrX = arrX[:batch_size * n_batches, :, :]
    # print(arrX)

    # X表示划分的时序数据集，Y是最后一条X对应的PUE，即标签。

    # np.random.shuffle(arrX)
    # for n in range(0, arrX.shape[0], seq_len):
    n = random.randint(0, len(arrX) - batch_size)
    x_batch = arrX[n:n + seq_len, :, :-1]
    y_batch = arrX[n:n + seq_len, -1:, -1:]
    # print(x_batch)
    # print(y_batch)
    return x_batch, y_batch
    """


def out_excel(tmplist, outpath):
    print("----开始写入数据----")
    pos_data = xlsxwriter.Workbook(outpath)
    worksheet = pos_data.add_worksheet()
    # style = xlwt.XFStyle()
    # style.num_format_str = "[$-10804]0.00"
    rows_pos = len(tmplist)

    #print(rows_pos, col_pos)
    for i in range(rows_pos):
        worksheet.write(i, 0, tmplist[i])
    pos_data.close()
    print("----写入完成----")
