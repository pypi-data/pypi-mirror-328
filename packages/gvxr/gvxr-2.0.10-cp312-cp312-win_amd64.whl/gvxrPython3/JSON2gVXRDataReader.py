import json # Load the JSON file
import os
import numpy as np

from cil.io import TIFFStackReader
from cil.framework import AcquisitionGeometry, AcquisitionData

# from gvxrPython3 import gvxr
# from gvxrPython3 import json2gvxr


def getUnitOfLength(aUnitOfLength: str) -> float:

    unit_of_length = 0.0;

    km  = 1000.0    / 0.001;
    hm  =  100.0    / 0.001;
    dam =   10.0    / 0.001;
    m   =    1.0    / 0.001;
    dm  =    0.1    / 0.001;
    cm  =    0.01   / 0.001;
    mm  =    0.001  / 0.001;
    um  =    1.0e-6 / 0.001;

    if ((aUnitOfLength == "kilometer") or (aUnitOfLength == "kilometre") or (aUnitOfLength == "km")):
        unit_of_length = km;
    elif ((aUnitOfLength == "hectometer") or (aUnitOfLength == "hectometre") or (aUnitOfLength == "hm")):
        unit_of_length = hm;
    elif ((aUnitOfLength == "decameter") or (aUnitOfLength == "decametre") or (aUnitOfLength == "dam")):
        unit_of_length = dam;
    elif ((aUnitOfLength == "meter") or (aUnitOfLength == "metre") or (aUnitOfLength == "m")):
        unit_of_length = m;
    elif ((aUnitOfLength == "decimeter") or (aUnitOfLength == "decimetre") or (aUnitOfLength == "dm")):
        unit_of_length = dm;
    elif ((aUnitOfLength == "centimeter") or (aUnitOfLength == "centimetre") or (aUnitOfLength == "cm")):
        unit_of_length = cm;
    elif ((aUnitOfLength == "millimeter") or (aUnitOfLength == "millimetre") or (aUnitOfLength == "mm")):
        unit_of_length = mm;
    elif ((aUnitOfLength == "micrometer") or (aUnitOfLength == "micrometre") or (aUnitOfLength == "um")):
        unit_of_length = um;
    else:
        raise ValueError("Unknown unit of length (" + aUnitOfLength + ")");

    return unit_of_length;

class JSON2gVXRDataReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self, verbose=0):

        # Load the JSON file
        with open(self.file_name) as f:
            gVXR_params = json.load(f)

        # Get the absolute path of the JSON file
        cmd = os.path.abspath(self.file_name)

        # Get the path where the projections are
        projection_path = gVXR_params["Scan"]["OutFolder"]

        # Where are the TIFF files?
        TIFF_file_name = ""

        # Is an absolute path? (Unix)
        if projection_path[0] == "/":
            TIFF_file_name = projection_path
        # Is an absolute path? (Windows)
        elif len(projection_path) > 3:
            if projection_path[1] == ":" and (projection_path[2] == "\\" or projection_path[2] == "/"):
                TIFF_file_name = projection_path

        # It is a relative path
        if len(TIFF_file_name) == 0:
            # Get the absolute path of the JSON file
            file_abs_path = os.path.abspath(self.file_name)
            file_path = os.path.dirname(file_abs_path)
            TIFF_file_name = file_path + "/" + projection_path

        # Get the rotation parameters
        if "RotationAxis" in gVXR_params["Scan"]:
            rotation_axis_direction = gVXR_params["Scan"]["RotationAxis"]
        else:
            rotation_axis_direction = np.array(gVXR_params["Detector"]["UpVector"])


        # rotation_axis_direction[2] *= -1

        if "CenterOfRotation" in gVXR_params["Scan"]:
            temp_rotation_axis_position = gVXR_params["Scan"]["CenterOfRotation"]
        elif "CentreOfRotation" in gVXR_params["Scan"]:
            temp_rotation_axis_position = gVXR_params["Scan"]["CentreOfRotation"]
        else:
            temp_rotation_axis_position = [0, 0, 0, "cm"]

        if len(temp_rotation_axis_position) == 4:
            temp_rotation_axis_position = np.array(temp_rotation_axis_position[0:3]) * getUnitOfLength(temp_rotation_axis_position[3]) / getUnitOfLength("cm")
        # temp_rotation_axis_position[2] *= -1
        # temp_rotation_axis_position += ???
        # temp_rotation_axis_position[1] = (181.75211882974276 +  36.786910286694045) / 2
        rotation_axis_position = temp_rotation_axis_position #[0, 0, 0]
        

        # Get the source position in mm
        temp = gVXR_params["Source"]["Position"]
        source_position_cm = np.array(temp[0:3]) * getUnitOfLength(temp[3]) / getUnitOfLength("cm")
        # source_position_cm[2] *= -1
        # source_position_cm -= temp_rotation_axis_position

        # Get the detector position in mm
        temp = gVXR_params["Detector"]["Position"]
        detector_position_cm = np.array(temp[0:3]) * getUnitOfLength(temp[3]) / getUnitOfLength("cm")
        # detector_position_cm[2] *= -1
        # detector_position_cm -= temp_rotation_axis_position

        # Compute the ray direction
        ray_direction = (detector_position_cm - source_position_cm)
        ray_direction /= np.linalg.norm(ray_direction)

        # Get the shape of the beam (parallel vs cone beam)
        source_shape = gVXR_params["Source"]["Shape"]

        # Is it a parallel beam
        use_parallel_beam = False
        if type(source_shape) == str:
            if source_shape.upper() == "PARALLELBEAM" or source_shape.upper() == "PARALLEL":
                use_parallel_beam = True

        # Get the pixel spacing in mm
        detector_number_of_pixels = gVXR_params["Detector"]["NumberOfPixels"]
        if "Spacing" in gVXR_params["Detector"].keys() == list and "Size" in gVXR_params["Detector"].keys():
            raise ValueError("Cannot use both 'Spacing' and 'Size' for the detector")

        if "Spacing" in gVXR_params["Detector"].keys():
            temp = gVXR_params["Detector"]["Spacing"]
            pixel_spacing_cm = [
                temp[0] * getUnitOfLength(temp[2]) / getUnitOfLength("cm"),
                temp[1] * getUnitOfLength(temp[2]) / getUnitOfLength("cm")
             ]
            if verbose > 0:
                print("Pixel spacing:", pixel_spacing_cm, "cm")

        elif "Size" in gVXR_params["Detector"].keys():
            detector_size = gVXR_params["Detector"]["Size"];
            pixel_spacing_cm = [
                (detector_size[0] / detector_number_of_pixels[0]) * getUnitOfLength(detector_size[2]) / getUnitOfLength("cm"),
                (detector_size[0] / detector_number_of_pixels[0]) * getUnitOfLength(detector_size[2]) / getUnitOfLength("cm")
            ]
            if verbose > 0:
                print("Detecotr size:", detector_size, "cm")
        else:
            raise ValueError("'Spacing' and 'Size' were not defined for the detector, we cannot determined the pixel spacing")

        # Get the angles
        include_final_angle = False
        if "IncludeFinalAngle" in gVXR_params["Scan"]:
            include_final_angle = gVXR_params["Scan"]["IncludeFinalAngle"]

        angle_set = np.linspace(
            0,
            gVXR_params["Scan"]["FinalAngle"],
            gVXR_params["Scan"]["NumberOfProjections"],
            include_final_angle
        )

        detector_direction_x = np.cross(ray_direction, rotation_axis_direction)
        detector_direction_y = rotation_axis_direction

        if "RightVector" in gVXR_params["Detector"]:
            detector_direction_x = gVXR_params["Detector"]["RightVector"]

        if "UpVector" in gVXR_params["Detector"]:
            detector_direction_y = gVXR_params["Detector"]["UpVector"]

        # source_position_cm -= rotation_axis_position
        # detector_position_cm -= rotation_axis_position
        # rotation_axis_position = [0, 0, 0]
        if verbose > 0:
            print("Source position:", source_position_cm, "cm")
            print("Detector position:", detector_position_cm, "cm")
            print("Ray direction:", ray_direction)
            print("Rotation axis:", rotation_axis_direction)
            print("Rotation axis position:", rotation_axis_position, "cm")
            print("detector_direction_x:", detector_direction_x)
            print("detector_direction_y:", detector_direction_y)
            print("Angles:", angle_set[0], "...", angle_set[-1], "degrees")


        # Parallel beam
        if use_parallel_beam:
            acquisition_geometry = AcquisitionGeometry.create_Parallel3D(ray_direction,
                detector_position_cm,
                detector_direction_x=detector_direction_x,
                detector_direction_y=detector_direction_y,
                rotation_axis_position=rotation_axis_position,
                rotation_axis_direction=rotation_axis_direction)
            print(ray_direction)
            print(detector_position_cm)
            print(rotation_axis_position)
            print(rotation_axis_direction)
        # It is cone beam
        else:
            acquisition_geometry = AcquisitionGeometry.create_Cone3D(source_position_cm,
                detector_position_cm,
                detector_direction_x=detector_direction_x,
                detector_direction_y=detector_direction_y,
                rotation_axis_position=rotation_axis_position,
                rotation_axis_direction=rotation_axis_direction)

        acquisition_geometry.set_angles(angle_set)
        acquisition_geometry.set_panel(detector_number_of_pixels, pixel_spacing_cm)
        acquisition_geometry.set_labels(['angle','vertical','horizontal'])
        print(detector_number_of_pixels)
        print(pixel_spacing_cm)

        # Create the reader
        TIFF_reader = TIFFStackReader(file_name=TIFF_file_name)

        # Load the image data
        TIFF_data = TIFF_reader.read()

        flat_field_correction = bool(gVXR_params["Scan"]["Flat-Field Correction"]) if "Flat-Field Correction" in gVXR_params["Scan"] else False

#         if flat_field_correction == False:
#             k, f, target_unit = json2gvxr.getSpectrum(self.file_name, "MeV")
#             total_energy_in_MeV = 0.0
#             for energy, count in zip(k, f):
#                 total_energy_in_MeV += energy * count

#             TIFF_data /= total_energy_in_MeV

        data = AcquisitionData(TIFF_data, deep_copy=False, geometry=acquisition_geometry)

        return data

