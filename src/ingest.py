import os
import yaml
import zipfile

params = yaml.safe_load(open('params.yaml'))['ingest']

data_path = os.path.join('data', 'prepared', f"v{params['dcount']}")
origimg_path = os.path.join('data', 'store', f"v{params['dcount']}", 'images')
# print(data_path)
os.makedirs(data_path, exist_ok=True)
os.makedirs(origimg_path, exist_ok=True)

with zipfile.ZipFile(f'/Users/vaibhav/Desktop/boschdvc/MLOps_Pipeline/buffer/dataset{params["dcount"]}.zip',"r") as zipf:
    zipf.extractall(data_path)
    zipf.extractall(origimg_path)