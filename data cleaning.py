import pandas as pd

def clean_data(file_path):

    df = pd.read_csv(file_path)

    # Fill missing numerical values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize city names
    if 'City' in df.columns:
        df['City'] = df['City'].str.title()

    # Generate summary
    summary = df.describe()

    # Save cleaned data
    df.to_csv("cleaned_data.csv", index=False)

    # Save report
    with pd.ExcelWriter("report.xlsx") as writer:
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)
        summary.to_excel(writer, sheet_name="Summary")

    print("Automation Complete")

# Function call
clean_data("sales_data.csv")