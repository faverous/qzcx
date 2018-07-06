'''
预测温度
'''
import data_process
import random
import csv
import os

def IT_w(it_w):
    if it_w <= 3185.3:
        return random.random() + 0.8
    if 3185.3 < it_w <= 3205.75:
        return random.random() + 1.8
    if 3205.75 < it_w <= 3224.10:
        return random.random() + 2.8
    if 3224.10 < it_w <= 3240.485:
        return random.random() + 3.8
    if 3240.485 < it_w <= 3255.67:
        return random.random() + 4.8
    if 3255.67 < it_w <= 3268.95:
        return random.random() + 5.8
    if 3268.95 < it_w <= 3279.06:
        return random.random() + 6.8
    if 3279.06 < it_w <= 3290:
        return random.random() + 7.8
    if 3290 < it_w <= 3302.70:
        return random.random() + 8.8
    if it_w > 3302.70:
        return 9.5

def BR_w(br_w):
    if br_w > 351.205:
        return random.random() + 0.8
    if 350.745 < br_w <= 351.205:
        return random.random() + 1.8
    if 350.185 < br_w <= 350.745:
        return random.random() + 2.8
    if 349.725 < br_w <= 350.185:
        return random.random() + 3.8
    if 349.345 < br_w <= 349.725:
        return random.random() + 4.8
    if 348.885 < br_w <= 349.345:
        return random.random() + 5.8
    if 348.425 < br_w <= 348.885:
        return random.random() + 6.8
    if 347.835 < br_w <= 348.425:
        return random.random() + 7.8
    if 346.975 < br_w <= 347.835:
        return random.random() + 8.8
    if br_w <= 346.975:
        return 9.5

def WIND_w(wind_w):
    if wind_w > 618.85:
        return random.random() + 0.8
    if 597.08 < wind_w <= 618.85:
        return random.random() + 1.8
    if 575.50 < wind_w <= 597.08:
        return random.random() + 2.8
    if 370.80 < wind_w <= 575.50:
        return random.random() + 3.8
    if 310.15 < wind_w <= 370.80:
        return random.random() + 4.8
    if 286.20 < wind_w <= 310.15:
        return random.random() + 5.8
    if 272.40 < wind_w <= 286.20:
        return random.random() + 6.8
    if 258.75 < wind_w <= 272.40:
        return random.random() + 7.8
    if 244.9 < wind_w <= 258.75:
        return random.random() + 8.8
    if wind_w <= 244.9:
        return 9.5

if __name__ == '__main__':
    output = data_process.input_com("pre_Tem.xlsx",0)
    hei = len(output)
    wei = len(output[0])
    pre_t = ['温度']
    for i in range(hei):
        br = BR_w(output[i][0])
        wind = WIND_w(output[i][1])
        it = IT_w(output[i][2])
        temper = (br + wind + it) * 0.002 + br * wind * it * 0.005 + 20
        pre_t.append(temper)
    data_process.out_excel(pre_t, "pred_Tem.xlsx")
    print("--写入csv--")
    with open(os.path.join(os.path.dirname(__file__), "clean_data.csv")) as csvFile:
        rows_T = csv.reader(csvFile)
        with open(os.path.join(os.path.dirname(__file__), "clean_data_T.csv"), 'w') as f:
            writer = csv.writer(f)
            i=0
            for row in rows_T:
                row.append(pre_t[i])
                writer.writerow(row)
                i = i+1
    print("--写入完成--")