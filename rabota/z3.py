var1=float(input("введите массу конфет в граммах:"))
if var1>2000:
   var2=var1*0.2
   print(f"{var1}гр = {var2}руб")
else:
    var2=var1*0.25
    print(f"{var1}гр = {var2}руб")