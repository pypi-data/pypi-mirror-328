import requests
from PIL import Image, ImageFont, ImageDraw

class NiuNiu(object):
    # 这是一个非常牛的库，这个库里面都是很牛很好玩的库
    @staticmethod
    def download_image(url, local_filename):
        # 发送HTTP GET请求下载图片
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 将内容保存到本地文件
            with open(f"./{local_filename}.jpg", 'wb') as f:
                f.write(response.content)
        else:
            print(f"下载失败，HTTP状态码：{response.status_code}")

    @staticmethod
    def niu_draw(filename, new_wight=100):

        NiuNiu.download_image(f"https://wjf-1300814601.cos.ap-nanjing.myqcloud.com/img_private/{filename}.jpg",filename)
        ascii_chars = "MNHQ$OC67+>!:-. "
        img = Image.open(f"./{filename}.jpg")
        img = img.convert("L")
        w, h = img.size
        img = img.resize((new_wight * 2, int(new_wight * h // w)))
        w, h = img.size
        data = img.load()
        result = []
        n = len(ascii_chars) - 1
        for y in range(h):
            line = "".join(ascii_chars[data[x, y] * n // 255] for x in range(w))
            line += "\n"
            result.append(line)
        with open(f"{filename}.txt", "w") as f:
            f.writelines(result)
if __name__ == '__main__':
        niuniu=NiuNiu()
        ascii_art = niuniu.niu_draw(r"537")
