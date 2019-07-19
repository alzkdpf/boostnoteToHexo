import os

def file_base_name(file_name):
    if '.' in file_name:
        separator_index = file_name.index('.')
        base_name = file_name[:separator_index]
        return base_name
    else:
        return file_name

def path_base_name(path):
    file_name = os.path.basename(path)
    return file_base_name(file_name)

# 헥소 형식으로 기록하기
def writeHexoTypeMarkdown(fileName):

    originalFile = open( fileName, mode='r', encoding='utf-8')
    fixFileName = 'fix_'+file_base_name(fileName)+'.md'
    fixFile = open( fixFileName, mode='wt', encoding='utf-8')
    lines = originalFile.readlines()
    count = len(lines)
    print(count)
    for i in range(count):
        if i == 0:
            fixFile.write("---\n")
            fixFile.write("title: "+lines[i].replace("#",""))
            fixFile.write("tags: \n")
            fixFile.write("- Android\n")
            fixFile.write("- toptoon\n")
            fixFile.write("---\n")
        fixFile.write(lines[i])
    fixFile.close()
    originalFile.close()

def isIgnoreList(item):
    ignoreList = ['fix']
    result = False
    for ignoreItem in ignoreList:
        if item.__contains__(ignoreItem):
            return True
    return result


fileList = os.listdir()

for file in fileList:
    if file.__contains__('.md'):
        print('file name : '+file)

        if isIgnoreList(file) == False:
            writeHexoTypeMarkdown(file)

