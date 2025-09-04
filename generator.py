import os

dataset_dir = "captchas"

for file in os.listdir(dataset_dir):
    if file.endswith(".png"):
        label = os.path.splitext(file)[0]
        txt_path = os.path.join(dataset_dir, file.replace(".png", ".gt.txt"))
        with open(txt_path, "w") as f:
            f.write(label)