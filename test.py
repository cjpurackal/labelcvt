import conf_generator.yolo as y
import os

a = y.YoloConf()

a.generate(os.getcwd())