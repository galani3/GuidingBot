import os

print("Creating bg.txt and info.dat files")

positives = os.listdir('training_positives/')
negatives = os.listdir('training_negatives/')

if len(positives) > 0:
    print(str(len(positives)) + " positive images detected")
    info_file = open('info.dat', 'w+')
    for img in positives:
        line = 'training_positives/' + img + ' 1 0 0 50 50\n'
        info_file.write(line)
    info_file.close()

if len(negatives) > 0:
    print(str(len(negatives)) + " negative images detected")
    bg_file = open('bg.txt', 'w+')
    for img in negatives:
        line = 'training_negatives/' + img + '\n'
        bg_file.write(line)
    bg_file.close()

print("DONE")
