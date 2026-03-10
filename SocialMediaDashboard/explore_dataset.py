import pandas as pd
import numpy as np

# ========================================
# YOUR DATASET FILE
# ========================================
DATASET_FILE = 'twitter_dataset.csv'

print("🚀 Starting Data Exploration...")
print("="*70)

try:
    # Load the dataset
    print(f"\n📂 Loading dataset: {DATASET_FILE}")
    df = pd.read_csv(DATASET_FILE, encoding='utf-8')
    print("✅ Dataset loaded successfully!")
    
except UnicodeDecodeError:
    print("⚠️  Encoding issue detected. Trying 'latin-1' encoding...")
    df = pd.read_csv(DATASET_FILE, encoding='latin-1')
    print("✅ Dataset loaded with latin-1 encoding!")
    
except FileNotFoundError:
    print(f"❌ File '{DATASET_FILE}' not found!")
    exit()

# ========================================
# 1. BASIC INFORMATION
# ========================================
print("\n" + "="*70)
print("📊 BASIC DATASET INFORMATION")
print("="*70)

print(f"\n📏 Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"💾 Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# ========================================
# 2. FIRST LOOK AT DATA
# ========================================
print("\n" + "="*70)
print("👀 FIRST 5 ROWS")
print("="*70)
print(df.head())

# ========================================
# 3. COLUMN NAMES & TYPES
# ========================================
print("\n" + "="*70)
print("📋 COLUMN DETAILS")
print("="*70)
print(f"\nTotal Columns: {len(df.columns)}")
print("\nColumn Names:")
for i, col in enumerate(df.columns, 1):
    print(f"   {i}. {col}")

# ========================================
# 4. DATA TYPES
# ========================================
print("\n" + "="*70)
print("🏷️  DATA TYPES")
print("="*70)
print(df.dtypes)

# ========================================
# 5. MISSING VALUES
# ========================================
print("\n" + "="*70)
print("🔍 MISSING VALUES ANALYSIS")
print("="*70)

missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Percentage': missing_percent
})

print("\nColumns with missing values:")
if missing_df['Missing Count'].sum() == 0:
    print("   ✅ No missing values found!")
else:
    print(missing_df[missing_df['Missing Count'] > 0].to_string())

# ========================================
# 6. BASIC STATISTICS
# ========================================
print("\n" + "="*70)
print("📈 STATISTICAL SUMMARY (Numeric Columns)")
print("="*70)
print(df.describe())

# ========================================
# 7. DETAILED INFO
# ========================================
print("\n" + "="*70)
print("ℹ️  DETAILED INFORMATION")
print("="*70)
df.info()

# ========================================
# 8. SAMPLE DATA FROM EACH COLUMN
# ========================================
print("\n" + "="*70)
print("🔬 SAMPLE VALUES FROM EACH COLUMN")
print("="*70)

for col in df.columns:
    print(f"\n📌 Column: {col}")
    print(f"   Type: {df[col].dtype}")
    print(f"   Unique values: {df[col].nunique():,}")
    print(f"   Sample values:")
    
    # Show 3 non-null sample values
    samples = df[col].dropna().head(3).tolist()
    for sample in samples:
        # Truncate long text
        sample_str = str(sample)[:150]
        print(f"      • {sample_str}")

# ========================================
# 9. SAVE SUMMARY TO FILE
# ========================================
print("\n" + "="*70)
print("💾 SAVING SUMMARY")
print("="*70)

with open('dataset_summary.txt', 'w', encoding='utf-8') as f:
    f.write(f"Dataset: {DATASET_FILE}\n")
    f.write(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns\n")
    f.write(f"\nColumns:\n")
    for col in df.columns:
        f.write(f"  - {col} ({df[col].dtype})\n")
    f.write(f"\nMissing Values:\n")
    f.write(missing_df[missing_df['Missing Count'] > 0].to_string())

print("✅ Summary saved to 'dataset_summary.txt'")

print("\n" + "="*70)
print("✅ EXPLORATION COMPLETE!")
print("="*70)