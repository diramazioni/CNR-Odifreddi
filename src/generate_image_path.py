import os

def read_images(directory):
    image_list = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            image_list.append({'src': directory.split('/')[-1]+"/"+filename, 'text': ''})
    return image_list

if __name__ == "__main__":
    images_directory = '../static/src-img'
    image_list = read_images(images_directory)
    image_list = image_list[:10]
    output_list = "export const imgArray = [" + ",\n".join(map(str, image_list)) + "]"

    with open('lib/img_path.js', 'w') as f:
        f.write(output_list)

    print(output_list)

