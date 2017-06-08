with open('../dataset/follow_topics.xml', 'r') as f:
    content = f.read()

lines = content.split('<RECORD>')

# print lines[1]
topics = {}
num = 0
for line in lines[1:]:
    top1 = line.split('<topic_id>')
    top2 = top1[1].split('</topic_id>')
    num+=1
    # print top2[0]
    topics[top2[0]] = ''
# print num
# print len(topics)

topic_ids = topics.keys()
# print topic_ids

with open('../dataset/topics.xml', 'r') as f:
    topic_content = f.read()

toco = topic_content.split('<RECORD>')

# keyword = 'dong-ji-zai-hang-zhou'
need = ""
for index in range(0, len(toco)):
    if any(ext in toco[index] for ext in topic_ids):
        # print(lines[index])
        need += '<RECORD>\n' + toco[index].strip('\n')+'\n'
    # if lines[index].__contains__(keyword):
    #     need +='    <RECORD>\n'+lines[index].strip('\n')
print need

