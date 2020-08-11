import json
import shutil

search_terms = ['stop sign', 'car', 'fire hydrant', 'city bus', 'traffic light', 'motorcycle']
ids = {}
for term in search_terms:
    ids[term] = []
    
# load the annotations
file = open('captions_train2014.json', 'r')
annotations = json.loads(file.read())
file.close()

# go through the captions

for image in annotations['annotations']:
    for term in search_terms:
        if term in image['caption'] and image['image_id'] not in ids[term]:
            ids[term].append(image['image_id'])

# get the image paths and move the images
for term in search_terms:
    for i in range(len(ids[term])):
        image_num = str(i + 1)
        image_id = str(ids[term][i]).rjust(12, '0')

        src_path = 'train2014/COCO_train2014_' + image_id + '.jpg'
        dst_path = 'images/' + term.replace(' ', '_') + image_num + '.jpg'

        shutil.copyfile(src_path, dst_path)
