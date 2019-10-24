from python_modules.tqdm import tqdm
from python_modules import requests
import gzip
import shutil
import re


def fetch_index_file(mirror_url, architecture, output_location):
    contents_file_name = f"Contents-{architecture}.gz"
    file_url = f"{mirror_url}/{contents_file_name}"
    output_location = f"{output_location}/{contents_file_name}"
    print(f"Fetching file from {file_url}.")

    response = requests.get(file_url, stream=True)
    response.raise_for_status()  # error if 400

    # setup tdqm for nifty progress bar
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1K
    tdqm_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(output_location, 'wb') as handle:
        # tdqm adds a nifty progress bar
        for data in response.iter_content(block_size):
            tdqm_bar.update(len(data))
            handle.write(data)
    tdqm_bar.close()
    return output_location


def extract_gzip(input_file):
    output_file = re.sub(r'.gz$', '.txt', input_file)
    print(f"Extracting {input_file} to {output_file}")
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    return output_file

