def cal_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

vish_exp_list = [2100, 3400, 3500]
ak_exp_list = [300, 800, 700]

vish_total = cal_total(vish_exp_list)
ak_total = cal_total(ak_exp_list)

print("Vishalyacha kharch", vish_total)
print("AK cha kharch", ak_total)