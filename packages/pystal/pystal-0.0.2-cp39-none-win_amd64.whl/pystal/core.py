import numpy as np
import platform
import matplotlib.pyplot as plt

plt.figure()

if platform.system() == "Windows":
    import win.pycrystal_core as ctlc
else:
    raise NotImplementedError("This platform is not yet supported")

ctlc.help()
ctlc.init()

ctlc.init_scene_from_dcm("D:/DataSets/DcmToolsTest/Thorax-Abdo/", renderer="realistic", res=(2048,2048))

ctlc.rotate_volume_x_y_axis(0, 0)
ctlc.rendering(128)

ctlc.rendered_result_save_to_png(png="demo1")

img = ctlc.get_final_result_uchar4_buffer()

plt.imshow(img)
plt.show()

#img = np.zeros((768,1024, 4), dtype=np.uint8, order='C')  # Ensure continuous memory
#img.flags.writeable = True

ctlc.rotate_volume_x_y_axis(180, 0)
ctlc.rendering(128)

ctlc.rendered_result_save_to_png(png="demo2")

ctlc.copy_final_result_uchar4_buffer(img)
plt.imshow(img)
plt.show()


ctlc.release()






