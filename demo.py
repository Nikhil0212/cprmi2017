# Copyright (c) 2016, Oleg Puzanov
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os
import numpy as np
import cv2
import test_cv as tv
from matplotlib import pyplot as plt

DIR_NAME = '/home/nikhil/cprmi2/images'

# Demo for clustering a set of 20 images using 'imgcluster' module.
# To be executed in the standalone mode by default. IP[y] Notebook requires some minor adjustments.

""" True (reference) labels for the provided images - defined manually according to the semantic
    meaning of images. For example: bear, raccoon and fox should belong to the same cluster.
    Please feel free to change the true labels according to your perception of these images  :-)
"""
TRUE_LABELS = [0, 1, 2, 1, 0, 1, 3, 3, 3, 3, 3, 1, 0, 2, 2, 1, 2, 0, 2, 2]
#TRUE_LABELS = [0, 1, 2, 1, 0]

if __name__ == "__main__":
    c = tv.do_cluster(DIR_NAME, algorithm='SIFT', print_metrics=True, labels_true=TRUE_LABELS)
    d=c.tolist()
    print "c : ",d,type(d)
    num_clusters = len(set(c))
    images = os.listdir(DIR_NAME)
    print(images[0])
    for n in range(num_clusters):
        print("\n --- Images from cluster #%d ---" % n)

        for i in np.argwhere(c == n):
            print("printing i: \n",i)
            if i != -1:
                print("Image %s" % images[i[0]])
                #print(i[0])
                #print(type(i))
                #print(images[0])  
                img = cv2.imread('%s/%s' % (DIR_NAME, images[i[0]]))
                #plt.axis('off')
                cv2.imshow('image',img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                #plt.show()

