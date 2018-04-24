def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild) # 使用os模块与操作系统进行交互，同时做到交互方式是可以跨平台的。
        #sChildPath = sPath  + sChild  # 这个在Windows系统上可能会出错
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents('E:/杂项/')
