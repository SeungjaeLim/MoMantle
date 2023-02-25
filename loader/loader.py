import os
import csv
import cv2
import numpy as np

def load_data(asset_path, categorical_cols=None):
    data = {}

    csv_file = os.path.join(asset_path, "data.csv")
    image_dir = os.path.join(asset_path, "images")

    if not os.path.isfile(csv_file) or not os.path.isdir(image_dir):
        return data

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for i, row in enumerate(reader):
            img_path = os.path.join(image_dir, f"{i+1}.png")
            if not os.path.isfile(img_path):
                continue

            label = row[0]
            features = [float(f) for f in row[1:]]
            cat_features = np.zeros(len(features), dtype=np.int)
            qty_features = np.zeros(len(features) - len(categorical_cols), dtype=np.float)

            if categorical_cols is not None:
                for j, val in enumerate(features):
                    if j in categorical_cols:
                        cat_features[j] = int(val)
                    else:
                        qty_features[j - sum(categorical_cols)] = val
            else:
                qty_features = np.array(features)

            img = cv2.imread(img_path)
            if img is None:
                continue

            data[dataset].append({
                "label": label,
                "cat_features": cat_features,
                "qty_features": qty_features,
                "image": img
            })

    return data
