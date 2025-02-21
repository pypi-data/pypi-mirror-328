import numpy as np
import platform
import matplotlib.pyplot as plt

if platform.system() == "Windows":
    import win.pycrystal_core as ctlc
else:
    raise NotImplementedError("This platform is not yet supported")

ctlc.init()
ctlc.help()

ctlc.load_data_from_dcm("D:/DataSets/DcmToolsTest/Thorax-Abdo/", renderer="realistic")

ctlc.rotate_volume_x_y_axis(0, 0)
ctlc.rendering_and_save_to_png(128, png="demo1")

img = np.zeros((768,1024, 4), dtype=np.uint8, order='C')  # Ensure continuous memory
img.flags.writeable = True

ctlc.rendering_and_get_final_result_uchar4_buffer(img)
plt.figure()
plt.imshow(img)
plt.show()

ctlc.release()






