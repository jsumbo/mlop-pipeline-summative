import requests
import os

def download_dataset():
    # URL of the dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    
    # Download the file
    print("Downloading diabetes dataset...")
    response = requests.get(url)
    
    if response.status_code == 200:
        # Save the file
        with open("diabetes.csv", "wb") as f:
            f.write(response.content)
        print("Dataset downloaded successfully as 'diabetes.csv'")
    else:
        print(f"Failed to download dataset. Status code: {response.status_code}")

if __name__ == "__main__":
    download_dataset() 