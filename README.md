# Twitter Sentiment Analysis Using Machine Learning Techniques
## By TechTitans - Avi Ajmera, Steven Chang, Brahma Chilumula, Hasan Mhowwala


## Project Overview
This project focuses on sentiment analysis of Twitter data, leveraging advanced machine learning techniques, to classify tweets into positive or negative sentiments. It is part of a comprehensive study where we have applied the CRISP-DM methodology to analyze and model Twitter data. 

## Repository Contents
- `Analysis.ipynb`: A Jupyter notebook containing the detailed analysis process, following the CRISP-DM methodology.
- `app.py`: Python file to run the Flask web application for real-time tweet sentiment analysis.
- `LRmodel.pkl`: The pickled Logistic Regression model used in the backend for sentiment classification.

- `Project_Report.pdf`: An in-depth report describing the analysis procedure, methodology, and findings.
- `Presentation.pptx`: A PowerPoint presentation explaining the project process.
- `Demo_Video.mp4`: A video demonstration of the project, including a demo of the Flask application.


`Dataset`: The dataset used in this study can be accessed via the provided [Drive link](https://drive.google.com/file/d/1X7pxCfanGIlYKdxslbO_vZU7pX2Mscaa/view)
`vectorizer.pkl`: The pickled vecctorizer for text data preprocessing can be found at [Drive link](https://drive.google.com/file/d/1uNRxfLsaXwDyZuiWQsQihnFeceMSxVov/view?usp=sharing)

## Replicate the analysis
To replicate the analysis on your own , download the Dataset zipped file and put in the repository and run the analysis
## Application Setup


### Installation and Running the App
1. Clone the repository to your local machine.
2. Download the `vectorizer.pkl` file and put it in the same repository from [Drive link](https://drive.google.com/file/d/1uNRxfLsaXwDyZuiWQsQihnFeceMSxVov/view?usp=sharing)
3. Install the required Python packages: `pip install -r requirements.txt`
4. Run `app.py` to start the Flask application: `python app.py`
5. Open your web browser and go to `http://127.0.0.1:5000/` to use the application.

## Using the Application
Enter a tweet text into the provided input field and submit it. The app will display whether the sentiment of the tweet is positive or negative, based on the Logistic Regression model's analysis.

## Dataset
Due to the size of the dataset, it is hosted externally. You can access and download the dataset used in this study through [this Drive link](https://drive.google.com/file/d/1X7pxCfanGIlYKdxslbO_vZU7pX2Mscaa/view).


