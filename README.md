# CNN Image Classification: Cheetah vs Hyena
The project demonstrates a CNN image classifier model "cheetah vs hyena predictor" deployed via a web interface.
This project involved developing a convolutional neural network (CNN) model to classify images as either cheetahs or hyenas using a Kaggle dataset. Data preprocessing steps included resizing images to 200x200 pixels and normalizing pixel values to the 0-1 range. 
The CNN model architecture consisted of multiple convolutional and max pooling layers, followed by fully connected layers and a final sigmoid output layer to make a binary prediction. Model training was done for 100 epochs with early stopping to prevent overfitting, achieving over 94% validation accuracy. 
Key evaluation metrics on the test set were 50% accuracy, 50% precision, 52% recall and 51% F1-score. For model serving, a Flask web application was built to allow image uploads and display the cheetah vs hyena classification result in the browser. 
Overall, the project demonstrates an end-to-end implementation of a CNN image classifier deployed via a web interface.
# Download the model & add to directory 
https://drive.google.com/file/d/1AI07wK1d22hvBFNcWOse2BHO6lwnV21-/view?usp=sharing
# Dataset
https://www.kaggle.com/datasets/singhdatascientist/for-image-classification-of-cheetah-vs-hyena
# Notebook that I have Created
https://www.kaggle.com/code/mohaimenulshawon/cnn-image-classification-cheetah-vs-hyena
# Web interface that I have Created
http://cheetah-hyena-predictor.mislamshawon.repl.co/
