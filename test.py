from fer import FER
import matplotlib.pyplot as plt 
a={'angry': 'đ ','disgust': 'đ¤ĸ', 'fear': 'đą', 'happy':'đ', 'sad': 'âšī¸', 'surprise': 'đŽ', 'neutral' : 'đ'}

img = plt.imread('happy.jpeg')
detector = FER(mtcnn=True)
  #print(detector.detect_emotions(img))
emotion, score = detector.top_emotion(img)
ans=emotion
#plt.imshow(img)
print(ans)