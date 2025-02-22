#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


import qrcode


def create_qrcode(data: str):
    # 创建一个二维码实例
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 添加数据
    qr.add_data(data)
    qr.make(fit=True)

    # 创建一个图像并保存二维码
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存二维码图像
    #  img.save("qrcode.png")

    # 显示二维码图像
    img.show()


if __name__ == "__main__":
    create_qrcode('')
