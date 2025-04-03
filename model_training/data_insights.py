import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_and_preprocess_data():
    # Load data
    df = pd.read_csv('../diabetes.csv')
    
    # Handle zero values
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[cols] = df[cols].replace({0: np.nan})
    
    # Fill null values with median based on outcome
    for col in cols:
        median_df = df.groupby('Outcome')[col].median()
        df.loc[(df['Outcome'] == 0) & (df[col].isnull()), col] = median_df[0]
        df.loc[(df['Outcome'] == 1) & (df[col].isnull()), col] = median_df[1]
    
    return df

def create_visualizations(df):
    # 1. Correlation Heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('static/images/correlation_heatmap.png')
    plt.close()
    
    # 2. Distribution of Features
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(df.columns[:-1], 1):
        plt.subplot(3, 3, i)
        sns.histplot(data=df, x=col, hue='Outcome', bins=30)
        plt.title(f'{col} Distribution')
    plt.tight_layout()
    plt.savefig('static/images/feature_distributions.png')
    plt.close()
    
    # 3. Box Plots
    plt.figure(figsize=(15, 6))
    df.boxplot(column=df.columns[:-1])
    plt.title('Feature Distributions (Box Plots)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/box_plots.png')
    plt.close()

def train_and_evaluate_model(df):
    # Prepare data
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=20, stratify=y)
    
    # Train model
    model = SVC(probability=True)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1 Score': f1_score(y_test, y_pred)
    }
    
    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig('static/images/confusion_matrix.png')
    plt.close()
    
    return metrics

if __name__ == "__main__":
    # Create static/images directory if it doesn't exist
    import os
    os.makedirs('static/images', exist_ok=True)
    
    # Load and preprocess data
    df = load_and_preprocess_data()
    
    # Create visualizations
    create_visualizations(df)
    
    # Train and evaluate model
    metrics = train_and_evaluate_model(df)
    
    # Print metrics
    print("\nModel Performance Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}") 