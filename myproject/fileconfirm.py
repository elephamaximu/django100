import os

f = os.path.abspath(__file__)
print("filename:", f)
f2 = os.path.dirname(f)
print("폴더:", f2)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(f2)
print("BASE_DIR :", BASE_DIR )

