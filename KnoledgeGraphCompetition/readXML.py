# line = None
with open('../dataset/sample_follow_topics.xml', 'r') as f:
    # if line == None:
    #     line = f.read()
    # print(f.read())
    content = f.read()
    # with open(...) as f:
    #     for line in f:
    #         < do
    #         something
    #         with line >

    # for line in f:
    #     # print line
    #     # break
    #     if line.__contains__('ccc-zhao'):
    #         print line
    # for index in range(0, len(f)):
    #     if lines[index].find('ccc-zhao'):
    #         need += lines[index - 1] + lines[index] + lines[index + 1] + lines[index + 2]
    # print need

lines = content.split('<RECORD>')
# print lines[0]
# for line in lines:

keyword = 'dong-ji-zai-hang-zhou'
need = ""
for index in range(0, len(lines)):
    if lines[index].__contains__(keyword):
        need +='    <RECORD>\n'+lines[index].strip('\n')
        # break
#         need+=lines[index-1]+lines[index]+lines[index+1]+lines[index+2]
print need

