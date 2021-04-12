# Auto_splitimg
高分辨率小目标；图像分割
原图：![image](https://user-images.githubusercontent.com/57471141/114347201-2949c700-9b97-11eb-9e66-e94ea9157562.png)
图片来源：http://robotics.pkusz.edu.cn/resources/dataset/
图片分辨率：3034*1586
环境需要：
python3.6
xml
os
cv2
tqdm
自行pip/conda install [name]安装

一、通过auto_split_img_test05.py
通过解析XML文件在原图上进行显示，不修改xml文件，仅生成新图。
生成图片![image](https://user-images.githubusercontent.com/57471141/114347574-b856df00-9b97-11eb-83d8-bca20280f91e.png)

二、通过auto_split_img_test03.py
均匀切割成M*N张图片，不修改xml文件，仅生成新图。
生成图片：
![image](https://user-images.githubusercontent.com/57471141/114347773-12f03b00-9b98-11eb-8bb0-f2aee2eca161.png)

![image](https://user-images.githubusercontent.com/57471141/114347851-3a470800-9b98-11eb-99bc-fff04db14f81.png)

![image](https://user-images.githubusercontent.com/57471141/114347900-52b72280-9b98-11eb-9253-ef64da8569dd.png)

![image](https://user-images.githubusercontent.com/57471141/114347930-5e0a4e00-9b98-11eb-9c62-c78c719f0b83.png)

三、通过auto_split_img_test02.py
通过解析XML文件，寻找到原图缺陷目标所在位置，通过文件中设置的大小，生成当前缺陷目标所在的图片，并生成新的图片和XML文件。

![image](https://user-images.githubusercontent.com/57471141/114348277-e5f05800-9b98-11eb-86d7-b505e5603162.png)
![image](https://user-images.githubusercontent.com/57471141/114348292-eb4da280-9b98-11eb-9298-76b2e40a45da.png)
![image](https://user-images.githubusercontent.com/57471141/114348324-f274b080-9b98-11eb-81da-082e372d12d3.png)
![image](https://user-images.githubusercontent.com/57471141/114348350-fbfe1880-9b98-11eb-92f6-521373aef686.png)

xml:生成展示：
![image](https://user-images.githubusercontent.com/57471141/114348625-61520980-9b99-11eb-9587-ea0c5bf8e618.png)

四、使用建议
通过test02生成相应数据集合进行模型训练，通过03将检测图片进行分割后放入模型进行检测。
所有代码来源网络，本人仅负责收集并修改一部分。主要目的是为了像本人一样又菜又爱玩的同学可以进行基本的实验。

