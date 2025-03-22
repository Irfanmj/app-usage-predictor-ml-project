# check_features_list.py
import pickle

with open("features_list.pkl", "rb") as f:
    features = pickle.load(f)

print("✅ features_list.pkl content:\n", features)
