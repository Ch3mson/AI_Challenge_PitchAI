# This challenge is designed for Wat.AI core member hiring process ( project name : Pitch.AI)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data(filepath):
    df = pd.read_csv(filepath, header=None)
    # rename last column to 'target' for clarity
    df = df.rename(columns={df.columns[-1]: 'target'})
    return df


def preprocess_data(df):
    # standardize the columns
    scaler = StandardScaler()
    features = df.columns[:-1]
    df[features] = scaler.fit_transform(df[features])
    return df


def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    return accuracy, report

if __name__ == "__main__":
    # Path to the dataset
    data_path = "data/spambase.csv"

    # Load and preprocess the data
    df = load_data(data_path)
    df = preprocess_data(df)

    # Split data into features and target
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Train and evaluate the model
    model = train_model(X_train, y_train)
    accuracy, report = evaluate_model(model, X_test, y_test)

    print(f"Model Accuracy: {accuracy:.2f}")
    print(f"Classification Report:\n{report}")


