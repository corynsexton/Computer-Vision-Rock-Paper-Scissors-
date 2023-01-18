import cv2                                                      # Library in python to access camera
from keras.models import load_model                             # Keras makes easier to use tensorflow
import numpy as np

model = load_model('keras_model.h5')                            # Loads model created on Teaching-Machine
cap = cv2.VideoCapture(0)                                       # Assigns first camera available to 'cap' - not capturing any image here yet
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)     # Creates an empty array/matrix with 4 dimensions. 1 image passed in, H=224, W=224, 3 number of channels (RGB)
list_options = ['Rock', 'Paper', 'Scissors', 'Nothing']

while True: 
    ret, frame = cap.read()                                     # Takes first capture from line 5. Ret = Boolean (whether we could get an image or not (maybe no camera))
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # Re-sizes image that model is asking for
    image_np = np.array(resized_frame)                          # Turns image into a numpy array. Changes data
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image. 
    data[0] = normalized_image                                  # Feeds normalized image into `cap` ready to pass to model.
    prediction = model.predict(data)                            # Pass data to model to make a prediction. (This is what we can see in each line in terminal)
    cv2.imshow('frame', frame) 
                                                                
    print(prediction)
    max_index = np.argmax(prediction[0])                        # Gives us the highest probability of action 
    print(list_options[max_index])                              # Gives the corresponding element to the index in the list
    if cv2.waitKey(1) & 0xFF == ord('q'):                       # Press q to close the window
        break
            
cap.release()                                                   # After the loop release the cap object
cv2.destroyAllWindows()                                         # Destroy all the windows


