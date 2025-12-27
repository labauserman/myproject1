import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    """Step 1: Ingest the data."""
    print("🚢 Loading Titanic dataset...")
    # This loads a real CSV as a Pandas 'DataFrame'
    return sns.load_dataset('titanic')

def analyze_data(df):
    """Step 2: Explore the statistics."""

    # what are the columns in the dataset?
    print(titanic_df.columns.tolist())
    
    print("\n--- Basic Stats ---")
    print(f"Total Passengers: {len(df)}")
    
    # Calculate survival rate by gender
    survival_by_sex = df.groupby('sex')['survived'].mean() * 100
    print(f"\nSurvival Rate by Gender:\n{survival_by_sex}")
    
    # Calculate survival rate by passenger class
    survival_by_class = df.groupby('pclass')['survived'].mean() * 100
    print(f"\nSurvival Rate by Class:\n{survival_by_class}")

def visualize_data(df):
    """Step 3: Create a professional chart."""
    print("\n📊 Generating visualization...")
    sns.set_theme(style="whitegrid")
    
    # Create a bar plot showing survival based on Class AND Gender
    plt.figure(figsize=(10, 6))
    plot = sns.barplot(data=df, x="pclass", y="survived", hue="sex")
    
    plt.title("Survival Rate by Class and Gender")
    plt.ylabel("Survival Probability")
    plt.xlabel("Passenger Class (1 = First, 3 = Third)")
    
    # Save the file to your folder
    plt.savefig("survival_analysis.png")
    print("✅ Success! Chart saved as 'survival_analysis.png'")
    plt.show()

if __name__ == "__main__":
    titanic_df = load_data()
    analyze_data(titanic_df)
    visualize_data(titanic_df)