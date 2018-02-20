import os
import cv2

positives = os.listdir('positives/')
negatives = os.listdir('negatives/')

if len(positives) > 0:
    continue_response = input("There are " + str(len(positives)) + " positive images detected, continue?(y/n): ")
    if continue_response == 'y' or continue_response == 'Y':
        if not os.path.exists('training_positives'):
            os.makedirs('training_positives')
        
        print('------POSITIVES------')
        for img in positives:
            image = cv2.imread(os.path.join('positives/',img))
            print(img)
            resized_image = cv2.resize(image, (50,50))
            cv2.imwrite('training_positives/' + img, resized_image)
else:
    print("There is no images in training_positives directory")
        
if len(negatives) > 0:
    continue_response = input("There are " + str(len(negatives)) + " negative images detected, continue?(y/n): ")
    if continue_response == 'y' or continue_response == 'Y':
        if not os.path.exists('training_negatives'):
            os.makedirs('training_negatives')
        
        print('------NEGATIVES------')
        for img in negatives:
            image = cv2.imread(os.path.join('negatives/',img))
            print(img)
            resized_image = cv2.resize(image, (100,100))
            cv2.imwrite('training_negatives/' + img, resized_image)
else:
    print("There is no images in the training_negatives directory")
