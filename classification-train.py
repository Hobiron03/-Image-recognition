import os
import re

def main():
    #学習に使う画像データのパス（トリミング後）
    train_data_path = "train_imagefile_path/train"
    #出力
    output_path = "training/train.txt"

    images = os.listdir(train_data_path)
    images.pop(0)

    with open(output_path, 'a', encoding='utf-8') as f:
        for image in images:
            path = os.path.join(train_data_path, image)
            if re.match('haruna', image):
                f.write(path + ' ' + str(0) + '\n')
            elif re.match('haronen', image):
                f.write(path + ' ' + str(1) + '\n')
            elif re.match('moore', image):
                f.write(path + ' ' + str(2) + '\n')


if __name__ == "__main__":
    main()
