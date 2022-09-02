import os


if not os.path.exists("new_test_dir"):
    os.mkdir('new_test_dir')

dir_strusct = os.listdir('/usr')
print(dir_strusct)