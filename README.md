# YOLOv8 Fruits Detection

## Abstract

This is a project on fruit detection in images using the deep learning model YOLOv8. The types of fruits used in this project include:

- Avocado (Vietnamese: Bo)

- Tomato (Vietnamese: Ca chua)

- Orange (Vietnamese: Cam)

- Guava (Vietnamese: Oi)

- Bell Pepper (Vietnamese: Ot chuong)

- Red Apple (Vietnamese: Tao do)

- Green Apple (Vietnamese: Tao xanh)

- Dragon Fruit (Vietnamese: Thanh long)

## Table of content

1. [Install](#Install)

2. [Train](#Train)

3. [Predict](#Predict)

## Install

### Virtual environment

- Please set up a virtual environment using either the [Anaconda](https://www.anaconda.com/download) or venv package of [Python](https://www.python.org/downloads/).

    - In this project, I created a virtual environtment named 「venv」

        1. venv package `python3 -m venv venv`

        2. anaconda `conda create --name venv python=3.11`

    - Then activate the enviroment.

        1. venv package `.\venv\Scripts\activate`

        2. anaconda `conda activate venv`

    - Change directory to this project `cd path\to\this\project`

### YOLOv8 model 
    pip install ultralytics

## Train

1. CLI

    - `yolo task=detect mode=train model=yolov8l.pt data=data.yaml device=0 epochs=100 patience=50 name=yolov8_fruits_detection workers=8 batch=8`

<table style="width: 100%; border: 1px solid; border-collapse: collapse">
                        <caption><h4>where:</h4></caption>
                        <tr>
                            <th style="border: 1px solid; border-collapse: collapse; text-align: center">Argument</th>
                            <th style="border: 1px solid; border-collapse: collapse; text-align: center">Description</th>
                            <th style="border: 1px solid; border-collapse: collapse; text-align: center">Default</th>
                            <th style="border: 1px solid; border-collapse: collapse; text-align: center">Example</th>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">model</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">The model that you want to use</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">-</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">model=yolov8l.pt</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">data</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">Data file</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">-</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">data=data.yaml</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">workers</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">The number of processes that generate batches in parralel</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">8</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">workers=4</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">device</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">Device to run training</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">-</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">device=0[,1,2,3] if you have many GPUs, else device=cpu</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">batch</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">The number of images processed before updating the model</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">16</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">batch=8</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">epochs</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">The number of times the learning algorithm will work to process the entire dataset</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">100</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">epochs=100</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">patience</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">Epochs to wait for no observable to improvement for early stopping of training</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">50</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">patience=50</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">name</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">Folder name</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">-</td>
                            <td style="border: 1px solid; border-collapse: collapse; text-align: center">name=fruits</td>
                        </tr>
                    </table>

2. Python 

    - `python train.py`

3. Result ![train image](https://scontent.fdad3-5.fna.fbcdn.net/v/t1.15752-9/370098902_1403036000423826_5983942292507589961_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=DKk9_v06JTkAX_l2S_4&_nc_ht=scontent.fdad3-5.fna&oh=03_AdQHsoGo76vA_iq3YARFVr-XG_8T_umwbLGutROvjlAVQg&oe=656846CF)

## Predict

1. CLI

    - `yolo task=detect mode=predict model=runs\detect\fruits\weights\best.pt source="test\images\1_tomato_31.jpg" save=True show=True`

     ![predict image](https://scontent.fdad3-6.fna.fbcdn.net/v/t1.15752-9/368101555_170382116152087_8042047449849574807_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=Yu4nN_56bmwAX8VgISq&_nc_ht=scontent.fdad3-6.fna&oh=03_AdRLyBg_5NkwkzCM4Yzmp7EDaZxUW4kmD3IT1TPSc4_d4A&oe=65685B93)
