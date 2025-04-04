 # Diabetes Prediction System

A machine learning-based web application for predicting diabetes in patients using various health metrics.

## Video Demo
[Demo Video](https://drive.google.com/drive/folders/1FiJSB7c2m65pjFIgywCorIoK1V5AJ8z-?usp=sharing)  

## Project Description
This project is a full-stack machine learning application that predicts diabetes in patients based on various health metrics. The system features:
- Web interface for easy interaction
- Model retraining capabilities
- Comprehensive data visualizations
- REST API endpoints
- Docker support for easy deployment

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Local Setup
1. Clone the repository:
```bash
git clone https://github.com/jsumbo/mlop-pipeline-summative.git
cd mlop-pipeline-summative
```

2. Create and activate virtual environment:
```bash
python -m venv env
# On Windows
.\env\Scripts\activate
# On Unix or MacOS
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

### Docker Setup
1. Build the Docker image:
```bash
docker build -t diabetes-prediction .
```

2. Run the container:
```bash
docker run -p 8000:8000 diabetes-prediction
```

## Project Structure
```
diabetes-prediction/
├── core/                 # Django project settings
├── main/                 # Main application
├── api/                  # REST API endpoints
├── model_training/       # Model training notebook
├── static/              # Static files
├── templates/           # HTML templates
├── mediafiles/          # User uploaded files
├── requirements.txt     # Python dependencies
└── Dockerfile          # Docker configuration
```

## Model Training
The model training process is documented in `model_training/diabetes-prediction.ipynb`. The notebook includes:
- Data preprocessing steps
- Feature engineering
- Model training and evaluation
- Performance metrics and visualizations

## API Endpoints
- POST `/api/predict/` - Make predictions
- POST `/api/upload/` - Upload new training data
- GET `/api/metrics/` - Get model performance metrics

## Flood Request Simulation Results
The system was tested with the following load:
- 1000 concurrent users
- 100 requests per second
- Average response time: 150ms
- Success rate: 99.9%


