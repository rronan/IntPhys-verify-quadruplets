import hashlib
import json
import sys
from io import BytesIO
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm


def main():
    res_list = []
    for block in sorted(Path(sys.argv[1]).glob("*")):
        print(block)
        for quadruplet in tqdm(block.glob("*")):
            if not quadruplet.is_dir():
                continue
            hlist_dict = {0: [], 1: []}
            for k in range(1, 5):
                video_path = quadruplet / str(k)
                with open(video_path / "status.json", "r") as f:
                    status = json.load(f)
                for frame_path in video_path.glob("scene/*.png"):
                    img = cv2.imread(str(frame_path))
                    _, buffer = cv2.imencode(".png", img)
                    hash_ = hashlib.sha256(buffer.tostring()).hexdigest()
                    if status["header"]["is_possible"]:
                        hlist_dict[1].append(hash_)
                    else:
                        hlist_dict[0].append(hash_)
            true_hash = sorted(hlist_dict[1])
            false_hash = sorted(hlist_dict[0])
            res = true_hash == false_hash
            res_list.append(res)
            if not res:
                print(true_hash)
                print(false_hash)
        print("Success:", np.mean(res_list))


if __name__ == "__main__":
    main()
