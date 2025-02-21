import math

import cv2
import numpy as np


class Detector:
    def __init__(self, ratio_threshold=0.0001):
        self.ratio_threshold = ratio_threshold

    def inference(self, image: np.ndarray):
        assert image.ndim in [2, 3]
        if image.ndim == 3:
            assert image.shape[2] in [1, 3, 4]
            if image.shape[2] == 3:
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            elif image.shape[2] == 4:
                gray_image = cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)
            else:
                gray_image = image.squeeze(-1)
        else:
            gray_image = image
        
        # assume text pixels are black
        text_mask = gray_image < 255
        grid_size = max(1, int(min(image.shape[:2])/10))
        black_pixel_ratio = self.divide_into_grids(text_mask, grid_size)
        # filtered_black_pixel_ratio = self.get_max_connected_block(black_pixel_ratio, self.ratio_threshold)
        filtered_black_pixel_ratio = self.filter_connected_blocks_by_ratio(black_pixel_ratio, self.ratio_threshold)
        bounding_rect = self.find_bounding_rect_of_grids(filtered_black_pixel_ratio>0, grid_size)
        if bounding_rect is not None:
            h, w = image.shape[:2]
            bounding_rect[2] = min(bounding_rect[2], w)
            bounding_rect[3] = min(bounding_rect[3], h)

        return bounding_rect

    @staticmethod
    def divide_into_grids(image, grid_size):
        """
        将图像分成指定大小的网格，并计算每个网格中黑色像素的占比。

        :param image: 二值化图像, shape: [h, w], value: [0, 1]
        :param grid_size: 网格的大小 
        :return: 黑色像素占比矩阵 
        """
        rows, cols = image.shape 
        # print(rows, cols,grid_size)
        grid_rows = math.ceil(rows / grid_size) 
        grid_cols = math.ceil(cols / grid_size) 
        black_pixel_ratio = np.zeros((grid_rows, grid_cols))

        for i in range(grid_rows):
            for j in range(grid_cols):
                grid = image[i*grid_size:(i+1)*grid_size, j*grid_size:(j+1)*grid_size]
                black_pixel_ratio[i, j] = np.sum(grid) / (grid_size * grid_size)

        return black_pixel_ratio
    
    @staticmethod
    def get_max_connected_block(black_pixel_ratio, ratio_threshold):
        """
        首先对黑色像素占比矩阵作阈值操作，然后选择最大相连块

        :param black_pixel_ratio: 黑色像素占比矩阵 
        :param ratio_threshold: 黑色像素占比的阈值 
        :return: 过滤后的黑色像素占比矩阵 
        """
        # 创建一个二值矩阵，黑色像素占比大于阈值的设置为1，否则为0 
        binary_matrix = (black_pixel_ratio >= ratio_threshold).astype(np.uint8)
        
        # 使用连通组件标记算法 
        num_labels, labels_matrix = cv2.connectedComponents(binary_matrix, 8)

        # 找到最大的连通组件 
        max_label_id = 1 
        # max_area = 0 
        max_ratio = 0
        for label_id in range(1, num_labels):
            # area = np.sum(labels_matrix == label_id)
            # if area > max_area:
            #     max_area = area 
            #     max_label_id = label_id 
            ratio = np.sum(black_pixel_ratio[labels_matrix==label_id])
            if ratio > max_ratio:
                max_ratio = ratio
                max_label_id = label_id

        # 保留最大的连通组件 
        filtered_matrix = (labels_matrix == max_label_id).astype(np.float32) * black_pixel_ratio 

        return filtered_matrix
    
    @staticmethod
    def filter_connected_blocks_by_ratio(black_pixel_ratio, ratio_threshold, component_ratio_threshold=0.1):
        """
        首先对黑色像素占比矩阵作阈值操作，然后求取相连块，最后过滤面积较小的相连块

        :param black_pixel_ratio: 黑色像素占比矩阵 
        :param ratio_threshold: 黑色像素占比的阈值 
        :param component_ratio_threshold: 相连块与最大相连块黑色像素占比的比值的阈值, default 0.1
        :return: 过滤后的黑色像素占比矩阵 
        """
        # 创建一个二值矩阵，黑色像素占比大于阈值的设置为1，否则为0 
        binary_matrix = (black_pixel_ratio >= ratio_threshold).astype(np.uint8)
        
        # 使用连通组件标记算法 
        num_labels, labels_matrix = cv2.connectedComponents(binary_matrix, 8)
        
        # 计算每个连通组件的黑色像素总占比 
        component_ratios = []
        for label_id in range(1, num_labels):
            component = (labels_matrix == label_id)
            component_black_pixel_ratio = np.sum(black_pixel_ratio[component])
            component_ratios.append((label_id, component_black_pixel_ratio))
        
        if not component_ratios:
            # 如果 component_ratios 为空，返回一个与输入相同形状的空矩阵 
            return np.zeros_like(black_pixel_ratio)

        # 找到最大块的黑色像素总占比 
        max_ratio = max(component_ratios, key=lambda x: x[1])[1]
        
        # 过滤掉小于最大块component_ratio_threshold的块 
        filtered_matrix = np.zeros_like(black_pixel_ratio)
        for label_id, component_black_pixel_ratio in component_ratios:
            if component_black_pixel_ratio >= component_ratio_threshold * max_ratio:
                component = (labels_matrix == label_id)
                filtered_matrix[component] = black_pixel_ratio[component]
        
        return filtered_matrix 
    
    @staticmethod
    def find_bounding_rect_of_grids(mask, grid_size):
        if np.count_nonzero(mask) == 0:
            return None
        
        yx_arr = np.argwhere(mask)
        y_min, x_min = np.min(yx_arr, axis=0)
        y_max, x_max = np.max(yx_arr, axis=0)

        x_min *= grid_size
        y_min *= grid_size
        x_max *= grid_size
        y_max *= grid_size

        return [int(x_min), int(y_min), int(x_max + grid_size), int(y_max + grid_size)]
