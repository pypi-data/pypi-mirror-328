# type: ignore
# Adapted from https://github.com/patrickvonplaten/controlnet_aux/blob/master/src/controlnet_aux/open_pose/hand.py
import cv2
import numpy as np
import torch

from scipy.ndimage import gaussian_filter
from skimage.measure import label

from .util import smart_resize, smart_resize_k, padRightDownCorner, npmax
from .model import handpose_model

class Hand(object):
    def __init__(self):
        self.model = handpose_model()

    def to(self, device, dtype=None):
        self.model.to(device, dtype=dtype)
        return self

    @property
    def dtype(self):
        return next(iter(self.model.parameters())).dtype

    def __call__(self, oriImgRaw):
        device = next(iter(self.model.parameters())).device
        scale_search = [0.5, 1.0, 1.5, 2.0]
        # scale_search = [0.5]
        boxsize = 368
        stride = 8
        padValue = 128
        thre = 0.05
        multiplier = [x * boxsize for x in scale_search]

        wsize = 128
        heatmap_avg = np.zeros((wsize, wsize, 22))

        Hr, Wr, Cr = oriImgRaw.shape

        oriImg = cv2.GaussianBlur(oriImgRaw, (0, 0), 0.8)

        for m in range(len(multiplier)):
            scale = multiplier[m]
            imageToTest = smart_resize(oriImg, (scale, scale))

            imageToTest_padded, pad = padRightDownCorner(
                imageToTest, stride, padValue
            )
            im = (
                np.transpose(
                    np.float32(imageToTest_padded[:, :, :, np.newaxis]), (3, 2, 0, 1)
                )
                / 256
                - 0.5
            )
            im = np.ascontiguousarray(im)

            data = torch.from_numpy(im).to(device, dtype=self.dtype)

            with torch.no_grad():
                output = self.model(data).cpu().float().numpy()

            # extract outputs, resize, and remove padding
            heatmap = np.transpose(
                np.squeeze(output), (1, 2, 0)
            )  # output 1 is heatmaps
            heatmap = smart_resize_k(heatmap, fx=stride, fy=stride)
            heatmap = heatmap[
                : imageToTest_padded.shape[0] - pad[2],
                : imageToTest_padded.shape[1] - pad[3],
                :,
            ]
            heatmap = smart_resize(heatmap, (wsize, wsize))

            heatmap_avg += heatmap / len(multiplier)

        all_peaks = []
        for part in range(21):
            map_ori = heatmap_avg[:, :, part]
            one_heatmap = gaussian_filter(map_ori, sigma=3)
            binary = np.ascontiguousarray(one_heatmap > thre, dtype=np.uint8)

            if np.sum(binary) == 0:
                all_peaks.append([0, 0])
                continue
            label_img, label_numbers = label(
                binary, return_num=True, connectivity=binary.ndim
            )
            max_index = (
                np.argmax(
                    [
                        np.sum(map_ori[label_img == i])
                        for i in range(1, label_numbers + 1)
                    ]
                )
                + 1
            )
            label_img[label_img != max_index] = 0
            map_ori[label_img == 0] = 0

            y, x = npmax(map_ori)
            y = int(float(y) * float(Hr) / float(wsize))
            x = int(float(x) * float(Wr) / float(wsize))
            all_peaks.append([x, y])
        return np.array(all_peaks)
