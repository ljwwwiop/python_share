'''
    test
'''
'''
    这个demo 主要是 测试图片转换为txt文件
    主要使用openCV3 + PIL 
    也是为了之后 视频转换为文字
'''
from PIL import Image
import numpy as np

'''
im = Image.open('one.png')

width = im.size[0]
height = im.size[1]

fh = open('1.txt','w')

# 遍历每个点的象素
# 黑色写1 其余写0
colorsum = 0

for i in range(height):
    for j in range(width):
        color = im.getpixel((j,i))
        colorsum = color[0] + color[1] + color[2]

        if(colorsum == 0):
            fh.write('1')
        else:
            fh.write('0')
    fh.write('\n')
fh.close()
print('ok')'''

'''
if __name__ == "__main__":
    image_file = 'one.png'
    height = 100

    img = Image.open(image_file)
    img_width, img_height = img.size
    width = int(1.8 * height * img_width//img_height)
    img = img.resize((width,height),Image.ANTIALIAS)
    pixels = np.array(img.convert('L'))
    chars = 'MNHQ$OC?&>!:-;.'
    N = len(chars)
    step = N//256
    print(N)
    result  = ''
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j]//step]
        result +='\n'
    with open('1.txt','w') as f:
        f.write(result)
    print("ok")
'''







