# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

name = os.environ.get("my_name") # 環境変数の値をAPに代入
print(dotenv_path)
print(name)