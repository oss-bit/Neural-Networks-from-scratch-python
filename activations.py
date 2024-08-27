import numpy as np

class Relu:
    def forward(self, inputs):
        self.outputs = np.maximum(0,inputs)
        