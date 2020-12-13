# imports
import torch.nn.functional as F
import torch
from faceEmbeddingModel import faceEmbeddingModel
# from prep import load_and_transform_img, show_tensor_img
from reg_database import RegistrationDatabase
from prep import load_and_transform_img
import sys
import numpy as np

# to Cao, Simon and Thien: model.eval()!
# main results:
# - euclidean distance or inner product no difference
# - data augmentation so far no difference (-> look at images)
# - works bad for less persons
# - works a bit better for few-shot learning instead of one-shot learning (currently 3 images per person)

# What I have done since last time:
# - implemented adaptive threshold
# - added three images per person and per image 4 data augmentations -> 12 images per registered person
# - implemented similarity calculation with inner product and euclidean distance (both same results)


embedding_model = faceEmbeddingModel().eval()

# mode='euclidean_distance'
database = RegistrationDatabase()

# RegistrationDatabase Description:

# input: 128 dim embedding as tensor (convert it internally to numpy array)
#               - registration: embedding + name
#               - deregistration: name
#               - recognition: embedding
# ---------------------------------------------------------------------------
# functions:    - registration
#               - deregistration
#               - recognition
#               - clean_database
# ---------------------------------------------------------------------------
# output:       - registration: "registered successfully"
#               - deregistration: "deregistered successfully"
#               - recognition: closest person + access/intruder

# ----------------------------------------------------------------------------------
def register_people():

    paths = []
    paths.append('./test_registration_images/Aaron_01.ppm')
    # paths.append('./test_registration_images/Aaron_02.ppm')
    # paths.append('./test_registration_images/Aaron_03.ppm')
    paths.append('./test_registration_images/Abdoulaye_01.ppm')
    # paths.append('./test_registration_images/Abdoulaye_02.ppm')
    # paths.append('./test_registration_images/Abdoulaye_03.ppm')
    paths.append('./test_registration_images/George_01.ppm')
    # paths.append('./test_registration_images/George_02.ppm')
    # paths.append('./test_registration_images/George_03.ppm')
    paths.append('./test_registration_images/Hugo_01.ppm')
    # paths.append('./test_registration_images/Hugo_02.ppm')
    # paths.append('./test_registration_images/Hugo_03.ppm')
    paths.append('./test_registration_images/Ian_01.ppm')
    # paths.append('./test_registration_images/Ian_02.ppm')
    # paths.append('./test_registration_images/Ian_03.ppm')
    paths.append('./test_registration_images/Jennifer_01.ppm')
    # paths.append('./test_registration_images/Jennifer_02.ppm')
    # paths.append('./test_registration_images/Jennifer_03.ppm')
    paths.append('./test_registration_images/Kofi_01.ppm')
    # paths.append('./test_registration_images/Kofi_02.ppm')
    # paths.append('./test_registration_images/Kofi_03.ppm')
    paths.append('./test_registration_images/Lleyton_01.ppm')
    # paths.append('./test_registration_images/Lleyton_02.ppm')
    # paths.append('./test_registration_images/Lleyton_03.ppm')
    paths.append('./test_registration_images/Vladimir_01.ppm')
    # paths.append('./test_registration_images/Vladimir_02.ppm')
    # paths.append('./test_registration_images/Vladimir_03.ppm')
    paths.append('./test_registration_images/Yashwant_01.ppm')
    # paths.append('./test_registration_images/Yashwant_02.ppm')
    # paths.append('./test_registration_images/Yashwant_03.ppm')


    names = []
    names.append('Aaron')
    # names.append('Aaron')
    # names.append('Aaron')
    names.append('Abdoulaye')
    # names.append('Abdoulaye')
    # names.append('Abdoulaye')
    names.append('George')
    # names.append('George')
    # names.append('George')
    names.append('Hugo')
    # names.append('Hugo')
    # names.append('Hugo')
    names.append('Ian')
    # names.append('Ian')
    # names.append('Ian')
    names.append('Jennifer')
    # names.append('Jennifer')
    # names.append('Jennifer')
    names.append('Kofi')
    # names.append('Kofi')
    # names.append('Kofi')
    names.append('Lleyton')
    # names.append('Lleyton')
    # names.append('Lleyton')
    names.append('Vladimir')
    # names.append('Vladimir')
    # names.append('Vladimir')
    names.append('Yashwant')
    # names.append('Yashwant')
    # names.append('Yashwant')


    for i in range(len(names)):
        # data augmentation
        reg_img = load_and_transform_img(paths[i])
        img_embedding_tensor = embedding_model(reg_img)
        database.face_registration(names[i],img_embedding_tensor)

# ----------------------------------------------------------------------------------

# database.clean_database()
# register_people()

# print(database.database)


# Face Recognition with data augmentation
path = './test_recognition_images/Yashwant_04.ppm'
img = load_and_transform_img(path)
img_embedding_tensor = embedding_model(img)
closest_label, check = database.face_recognition(img_embedding_tensor)
print("Closest person: ", closest_label, " --- ", check)

# database.face_deregistration('Aaron')

# print(database.database)
