import glob
import os
import shutil
from PIL import Image

suffix = "AldoSpizzichino"
basewidth = 1024
images = glob.glob('../static/src-img/*.jpg')
images_cat = '../static/train-lora/img'
dest_dir = "../static/train-lora-XL"


def move():
    for root, _, files in os.walk(images_cat):
        for filename in files:
            if filename.endswith('.jpg'):
                category = os.path.split(root)[1]
                name = os.path.splitext(filename)[0] + '.txt'
                source_txt = os.path.join(root, name)
                dest_dir_ = os.path.join(dest_dir, "img", category)
                source = os.path.join(dest_dir, filename)
                os.makedirs(dest_dir_, exist_ok=True)
                destination = os.path.join(dest_dir_, filename)
                destination_txt = os.path.join(dest_dir_, name)
                if (os.path.exists(source)):
                    shutil.move(source, destination)
                if (os.path.exists(source_txt)):
                    shutil.copy(source_txt, destination_txt)
                else:
                    print("error not found", source_txt)
                print(source, destination)
    reg = os.path.join(dest_dir, "reg")
    os.makedirs(reg, exist_ok=True)
    images_reg = glob.glob(dest_dir + '/*.jpg')
    for img in images_reg:
        filename = os.path.basename(img)
        dest = os.path.join(reg, filename)
        shutil.move(img, dest)
        print(img, dest)
        
def resize():
    count = 1
    for img in images:
        if (not os.path.exists(dest_dir)):
            os.mkdir(dest_dir)
        outname = f"{dest_dir}/{suffix}_{count}.jpg"
        if (not os.path.exists(outname)):
            img = Image.open(img)
            width, height = img.size
            # rescale proportional to the basewidth and center crop
            wpercent = (basewidth / float(width))
            hsize = int((float(height) * float(wpercent)))
            img = img.resize((basewidth, hsize))
            cut = (hsize - basewidth)/2
            # img = img.crop((0, cut, basewidth, hsize - cut))
            img.convert("RGB").save(outname)
            print(outname)
            count += 1


def rename():    
    descrs = glob.glob('../static/train/*.txt')
    for descr in descrs:
        base = os.path.basename(descr)
        count = ''.join(filter(str.isdigit, base))
        outname = f"../static/train/{suffix}_{count}.txt"
        shutil.move(descr, outname)


resize()
move()