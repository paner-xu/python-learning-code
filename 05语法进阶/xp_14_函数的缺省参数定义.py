# 指定参数的默认值
def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: 男生 True  女生  False
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))
# 假定班上的男生居多！
# 在指定缺省参数的默认值时，应该使用最常见的值作为默认值
print_info("小明")
print_info("老王")
print_info("小美", False)
