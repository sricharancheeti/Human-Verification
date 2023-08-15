def test_evaluate(img_test_left , aud_test_left , img_test_right , aud_test_right , labels_test, BATCH_SIZE):
 
  results = model.evaluate([np.asarray(img_test_left),np.asarray(aud_test_left),np.asarray(img_test_right),np.asarray(aud_test_right)], np.asarray(labels_test) , batch_size = BATCH_SIZE)

  print('Test Loss: '+str(results[0]))
  print('Test Accuracy: '+str(results[1]))

def process_image(path):
  
  array_bgr = cv2.imread(path)
  array = cv2.cvtColor(array_bgr , cv2.COLOR_BGR2RGB)
  img= cv2.resize(array , (IMAGE_HEIGHT,IMAGE_WIDTH))
  img= np.array(img).reshape(-1,IMAGE_HEIGHT,IMAGE_WIDTH,3)
  plt.imshow(array)
  plt.show()
  
  return img

# function to take the image and audio of two persons and verify whether they are the same person or not...

def one_shot_learning_task():

  person1_aud=image_processing('Set path to audio spectogram image of person 1')

  person1_img=image_processing('Set path to facial image of person 1')

  person2_aud=image_processing('Set path to audio spectogram image of person 2')

  person2_img=image_processing('Set path to facial image of person 2')

  preds = model.predict([np.asarray(person1_img) , np.asarray(person1_aud) , np.asarray(person2_img) , np.asarray(person2_aud)])

  print(str(preds))

  if preds[0]<0.5 :
    print("Different")
  else :
    print("Same")