import os, glob
from pathlib import Path
import matplotlib.colors as mcolors
import sys
import numpy as np
from PIL import Image

import json # Load the JSON file
from gvxrPython3 import gvxr # Simulate X-ray images
from gvxrPython3.utils import getTextFileSpectrum
from gvxrPython3.utils import getSpectrumSpekpy
from gvxrPython3.utils import getSpectrumXpecgen
from gvxrPython3.utils import has_spekpy
from gvxrPython3.utils import has_xpecgen
from gvxrPython3.utils import has_skimage

# Define the NoneType
NoneType = type(None);
params  = None;
JSON_path = None
context_created = False
scan_params = {}
scan_setup = False
white_image = None
detector_loaded = False
source_loaded = False
kV_loaded = False
mAs_loaded = False

# Print the libraries' version
print (gvxr.getVersionOfSimpleGVXR())
print (gvxr.getVersionOfCoreGVXR())


def updatePath(fname:str):
    """
    Store the absolute path of the directory that contains the JSON file in a global variable called `JSON_path`.

    :param fname: The file name of the JSON file.
    """
    global JSON_path

    file_abs_path = os.path.abspath(fname)
    JSON_path = os.path.dirname(file_abs_path)


def getFilePath(fname:str):
    """
    Accessor on the absolute path of the file given as a parameter.
    This function supports both absolute and relative paths.
    If a relative path is given, it is relative to the JSON file
    (i.e. not to the Python script or notebook)

    :param fname: The file name of the file to access.
    :return: the absolute path of `fname`
    """
    global JSON_path

    file_absolute_path = ""

    # Is an absolute path?
    # Unix
    if fname[0] == "/":
        file_absolute_path = fname
    # Windows
    elif len(fname) >= 3:
        if fname[1] == ":" and fname[2] == "\\":
            file_absolute_path = fname

    # It is a relative path
    if file_absolute_path == "":
        file_absolute_path = JSON_path + "/" + fname

    return file_absolute_path


def initGVXR(fname:str, renderer:str="OPENGL", major:int=3, minor:int=2):
    """
    Create a simulation environment from a JSON file.

    :param fname: The file name of the JSON file. The filename will be cached for further use.
    :param renderer: The renderer (e.g. OPENGL, or EGL) (default: "OPENGL")
    :param major: The major version of the OpenGL context to create (default: 3)
    :param minor: The minor version of the OpenGL context to create (default: 2)
    """

    global params, context_created

    # Load the JSON file
    with open(fname) as f:
        params = json.load(f)

    # Update the absolute path of the JSON file
    updatePath(fname)

    # Create an OpenGL context
    if "WindowSize" in params:
        window_size = params["WindowSize"]
    elif "Window size" in params:
        window_size = params["Window size"]
    
    print("Create an OpenGL context:",
        str(window_size[0]) + "x" + str(window_size[1])
    )

    if not context_created:
        if renderer.upper() == "OPENGL":
            visibility = True
        else:
            visibility = False

        gvxr.createWindow(-1,
            True,
            renderer,
            major,
            minor)

    gvxr.setWindowSize(
        window_size[0],
        window_size[1]
    )

    context_created = True


def initSourceGeometry(fname:str="", verbose=0):
    """
    Initialise the X-ray source from a JSON file.

    :param fname: The file name of the JSON file. If no file name is provided, use the cached one. (default: "")
    """

    global params;
    global detector_loaded, source_loaded, kV_loaded, mAs_loaded;

    source_loaded = False

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f)

        # Update the absolute path of the JSON file
        updatePath(fname)

    # Set up the beam
    print("Set up the beam")
    source_position = params["Source"]["Position"];
    print("\tSource position:", source_position)
    gvxr.setSourcePosition(
        source_position[0],
        source_position[1],
        source_position[2],
        source_position[3]
    );
    source_shape = params["Source"]["Shape"]
    print("\tSource shape:", source_shape);

    if type(source_shape) == str:

        if source_shape.upper() == "PARALLELBEAM" or source_shape.upper() == "PARALLEL":
            gvxr.useParallelBeam();

        elif source_shape.upper() == "POINTSOURCE" or source_shape.upper() == "POINT" or source_shape.upper() == "CONE" or source_shape.upper() == "CONEBEAM":
            gvxr.usePointSource();

        else:
            raise ValueError("Unknown source shape:" + source_shape)

    elif type(source_shape) == type([]):
        if source_shape[0].upper() == "FOCALSPOT":
            spot_size = source_shape[1] * gvxr.getUnitOfLength(source_shape[2]) / gvxr.getUnitOfLength(source_position[3])
            gvxr.setFocalSpot(
                source_position[0], source_position[1], source_position[2], # Source position
                spot_size,
                source_position[3], # Units
                source_shape[3])

        else:
            raise ValueError("Unknown source shape:" + source_shape)

    else:
        raise ValueError("Unknown source shape:" + source_shape)

    source_loaded = True

    if kV_loaded and mAs_loaded and detector_loaded:
        if verbose:
            print("Update the beam spectrum as the source position may have changed, and kV and mAs are already in use")

        initSpectrum(fname, verbose)


def getTargetEnergy(input_unit: str,
                    input_energy: float,
                    target_unit: str):

    if input_unit == target_unit:
        target_energy = input_energy
    else:
        if type(input_energy) == list:
            target_energy = np.array(input_energy) * (gvxr.getUnitOfEnergy(input_unit) / gvxr.getUnitOfEnergy(target_unit))
        else:
            target_energy = input_energy * (gvxr.getUnitOfEnergy(input_unit) / gvxr.getUnitOfEnergy(target_unit))

    return target_energy


def getSpectrum(fname:str="", target_unit:str="keV", verbose:int=0):

    global params, has_speckpy, has_xpecgen;
    global detector_loaded, source_loaded, kV_loaded, mAs_loaded;

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f)

        # Update the absolute path of the JSON file
        updatePath(fname)

    min_energy = sys.float_info.max
    max_energy = -sys.float_info.max
    
    k = []
    f = []

    if type(params["Source"]["Beam"]) == list:

        for energy_channel in params["Source"]["Beam"]:
            input_energy = energy_channel["Energy"];
            input_unit = energy_channel["Unit"];

            target_energy = getTargetEnergy(input_unit, input_energy, target_unit)

            count = energy_channel["PhotonCount"];

            if verbose > 0:
                if count == 1:
                    print("\t", str(count), "photon of", target_energy, target_unit);
                else:
                    print("\t", str(count), "photons of", target_energy, target_unit);

            k.append(target_energy)
            f.append(count)

        k = np.array(k)
        f = np.array(f)

    else:
        if "GateMacro" in params["Source"]["Beam"]:

            if "GateMacro" in params["Source"]["Beam"]:
                fname = getFilePath(params["Source"]["Beam"]["GateMacro"]);
            elif "Gate macro" in params["Source"]["Beam"]:
                fname = getFilePath(params["Source"]["Beam"]["Gate macro"]);
            else:
                raise ValueError("The file name of the Gate macro is not specified");

            input_unit = params["Source"]["Beam"]["Unit"]
            k, f, input_unit = getTextFileSpectrum(fname, input_unit)
            k = getTargetEnergy(input_unit, k, target_unit)

        elif "TextFile" in params["Source"]["Beam"]:
            if "TextFile" in params["Source"]["Beam"]:
                fname = getFilePath(params["Source"]["Beam"]["TextFile"]);
            elif "Tex file" in params["Source"]["Beam"]:
                fname = getFilePath(params["Source"]["Beam"]["Text file"]);
            else:
                raise ValueError("The file name is not specified");

            input_unit = params["Source"]["Beam"]["Unit"]
            k, f, input_unit = getTextFileSpectrum(fname, input_unit)
            k = getTargetEnergy(input_unit, k, target_unit)

        else:
            
            kvp_in_kV = None;

            if not has_xpecgen and not has_spekpy:
                print("spekpy is not install, you won't be able to load a beam spectrum using spekpy")
                print("xpecgen is not install, you won't be able to load a beam spectrum using xpecgen")
                raise IOError("Please install spekpy and/or xpecgen")

            if "kvp" in params["Source"]["Beam"]:
                kvp_in_kV = params["Source"]["Beam"]["kvp"];
            elif "kVp" in params["Source"]["Beam"]:
                kvp_in_kV = params["Source"]["Beam"]["kVp"];
            elif "KVP" in params["Source"]["Beam"]:
                kvp_in_kV = params["Source"]["Beam"]["KVP"];
            elif "PeakKiloVoltage" in params["Source"]["Beam"]:
                kvp_in_kV = params["Source"]["Beam"]["PeakKiloVoltage"];
            elif "Peak kilo voltage" in params["Source"]["Beam"]:
                kvp_in_kV = params["Source"]["Beam"]["Peak kilo voltage"];

            if kvp_in_kV:
                gvxr.setVoltage(kvp_in_kV, "kV");
                kV_loaded = True

                th_in_deg = 12
                if "Tube angle" in params["Source"]["Beam"]:
                    th_in_deg = params["Source"]["Beam"]["Tube angle"];
                elif "tube angle" in params["Source"]["Beam"]:
                    th_in_deg = params["Source"]["Beam"]["tube angle"];
                elif "TubeAngle" in params["Source"]["Beam"]:
                    th_in_deg = params["Source"]["Beam"]["TubeAngle"];

                gvxr.setTubeAngle(th_in_deg);

                mAs = -1
                if "mAs" in params["Source"]["Beam"]:
                    mAs = params["Source"]["Beam"]["mAs"];
                    mAs_loaded = True
                
                exposure_time_in_sec = None;
                exposure_time_key = None;
                if "Exposure time" in params["Source"]["Beam"]:
                    exposure_time_key = "Exposure time"
                elif "ExposureTime" in params["Source"]["Beam"]:
                    exposure_time_key = "ExposureTime"

                if exposure_time_key:
                    exposure_time_in_sec = params["Source"]["Beam"][exposure_time_key][0];

                    if params["Source"]["Beam"][exposure_time_key][1] != "sec" and params["Source"]["Beam"][exposure_time_key][1] != "s":
                        if params["Source"]["Beam"][exposure_time_key][1] == "ms":
                            exposure_time_in_sec /= 1000.0;
                        elif params["Source"]["Beam"][exposure_time_key][1] == "msec":
                            exposure_time_in_sec /= 1000.0;
                        elif params["Source"]["Beam"][exposure_time_key][1] == "milliseconds":
                            exposure_time_in_sec /= 1000.0;
                        elif params["Source"]["Beam"][exposure_time_key][1] == "millisecond":
                            exposure_time_in_sec /= 1000.0;
                        elif params["Source"]["Beam"][exposure_time_key][1] == "Milliseconds":
                            exposure_time_in_sec /= 1000.0;
                        elif params["Source"]["Beam"][exposure_time_key][1] == "Millisecond":
                            exposure_time_in_sec /= 1000.0;
                        else:
                            raise ValueError("The unit of time " + params["Source"]["Beam"][exposure_time_key][1] + " is not currently managed. If this is something that should be reported, please contact me.")

                current = None;
                current_key = None;
                if "X-ray tube current" in params["Source"]["Beam"]:
                    current_key = "X-ray tube current";
                elif "XRayTubeCurrent" in params["Source"]["Beam"]:
                    current_key = "XRayTubeCurrent";
                elif "Current" in params["Source"]["Beam"]:
                    current_key = "Current";

                if current_key:
                    current = params["Source"]["Beam"][current_key][0];
                
                    if params["Source"]["Beam"][current_key][1] != "mA" and params["Source"]["Beam"][current_key][1] != "milliampere" and params["Source"]["Beam"][current_key][1] != "Milliampere" and params["Source"]["Beam"][current_key][1] != "milliamperes" and params["Source"]["Beam"][current_key][1] != "Milliamperes":
                        if params["Source"]["Beam"][current_key][1] == "A":
                            current *= 1000.0;
                        elif params["Source"]["Beam"][current_key][1] == "ampere":
                            current *= 1000.0;
                        elif params["Source"]["Beam"][current_key][1] == "Ampere":
                            current *= 1000.0;
                        elif params["Source"]["Beam"][current_key][1] == "amperes":
                            current *= 1000.0;
                        elif params["Source"]["Beam"][current_key][1] == "Amperes":
                            current *= 1000.0;
                        else:
                            raise ValueError("The unit of current " + params["Source"]["Beam"][current_key][1] + " is not currently managed. If this is something that should be reported, please contact me.")

                if mAs < 0 and exposure_time_in_sec and current:
                    print(type(exposure_time_in_sec), type(current))
                    print((exposure_time_in_sec), (current))
                    mAs = exposure_time_in_sec * current

                gvxr.setmAs(mAs)

                if verbose > 0:
                    print("kVp (kV):", gvxr.getVoltage("kV"))
                    print("tube angle (degrees):", gvxr.getTubeAngle())
                    print("mAs:", gvxr.getmAs())
                    print("Exposure time:", current);
                    print("X-ray tube current:", exposure_time_in_sec);

                # Add the filters if needed
                filters = None
                gvxr.clearFiltration();

                if "filter" in params["Source"]["Beam"]:
                    filters = params["Source"]["Beam"]["filter"]
                elif "Filter" in params["Source"]["Beam"]:
                    filters = params["Source"]["Beam"]["Filter"]
                elif "Filtration" in params["Source"]["Beam"]:
                    filters = params["Source"]["Beam"]["Filtration"]
                elif "filtration" in params["Source"]["Beam"]:
                    filters = params["Source"]["Beam"]["filtration"]

                if filters:
                    for f in filters:
                        if isinstance(f[0], int):
                            mat = gvxr.getElementSymbol(f[0])
                        elif isinstance(f[0], str):
                            mat = f[0]
                        else:
                            raise ValueError(str(f) + " is not a valid filter.")

                        if len(f) == 2:
                            gvxr.addFilter(mat, f[1], "mm");
                        elif len(f) == 3:
                            gvxr.addFilter(mat, f[1], f[2]);
                        else:
                            raise ValueError(str(f) + " is not a valid filter.")

                if verbose > 0:
                    print('filtration:', filters)

                if not source_loaded and mAs_loaded:
                    raise IOError("It is best to call initSource before initSpectrum when mAs is used")

                if not detector_loaded and mAs_loaded:
                    raise IOError("It is best to call initDetector before initSpectrum when mAs is used")

                if not has_spekpy and mAs_loaded:
                    raise IOError("Please install spekpy")

                # Adjust the number of bins if needed
                max_number_of_energy_bins = None;
                if "MaxNumberOfEnergyBins" in params["Source"]["Beam"]:
                    max_number_of_energy_bins = int(params["Source"]["Beam"]["MaxNumberOfEnergyBins"])

                # Must use spekpy for now when mAs is used
                if mAs_loaded:
                    source_detector_distance = np.linalg.norm(np.array(gvxr.getSourcePosition("cm")) - np.array(gvxr.getDetectorPosition("cm")))
                    k, f, input_unit = getSpectrumSpekpy(kvp_in_kV, 
                        filters=filters, 
                        th_in_deg=th_in_deg, 
                        max_number_of_energy_bins=max_number_of_energy_bins,
                        mAs=gvxr.getmAs(), 
                        z=source_detector_distance)
                    gvxr.enablePoissonNoise()
                # We favour xpecgen
                else:
                    if has_xpecgen:
                        k, f, input_unit = getSpectrumXpecgen(kvp_in_kV, 
                            filters=filters, 
                            th_in_deg=th_in_deg,
                            max_number_of_energy_bins=max_number_of_energy_bins)

                    # has_spekpy is True
                    else:
                        k, f, input_unit = getSpectrumSpekpy(kvp_in_kV, 
                            filters=filters, 
                            th_in_deg=th_in_deg, 
                            max_number_of_energy_bins=max_number_of_energy_bins)


                k = getTargetEnergy(input_unit, k, target_unit)

            # KVP unknown
            else:
                raise IOError("Invalid beam spectrum in JSON file")

    for energy, count in zip(k, f):

        if count > 1.0e-6:
            max_energy = max(max_energy, energy)
            min_energy = min(min_energy, energy)

    if verbose > 0:
        print("/gate/source/mybeam/gps/emin", min_energy, target_unit)
        print("/gate/source/mybeam/gps/emax", max_energy, target_unit)

    return k, f, target_unit


def initSpectrum(fname:str="", verbose:int=0):
    """
    Initialise the X-ray spectrum from a JSON file.

    :param str fname: The file name of the JSON file. If no file name is provided, use the cached one. (default: "")
    :param int verbose: The level of verbosity (default: 0)
    :return: spectrum, unit (e.g. "keV", "MeV"), k, f
    """

    global params;

    kV_loaded = False
    mAs_loaded = False

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f)

        # Update the absolute path of the JSON file
        updatePath(fname)

    k, f, unit = getSpectrum(fname, verbose=verbose)
    gvxr.resetBeamSpectrum()

    spectrum = {}

    for energy, count in zip(k, f):
        if energy in spectrum.keys():
            spectrum[energy] += count
        else:
            spectrum[energy] = count

    for energy in spectrum.keys():
        count = spectrum[energy]
        gvxr.addEnergyBinToSpectrum(energy, unit, count);

        if verbose > 0:
            print("/gate/source/mybeam/gps/histpoint", energy / 1000, count)

    return spectrum, unit, k, f;


def initDetector(fname:str="", verbose=0):
    """
    Initialise the X-ray detector from a JSON file.

    :param str fname: The file name of the JSON file. If no file name is provided, use the cached one. (default: "")
    """

    global params;
    global detector_loaded, source_loaded, kV_loaded, mAs_loaded;

    detector_loaded = False

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f);

        # Update the absolute path of the JSON file
        updatePath(fname)

    assert params is not None
    # Set up the detector
    print("Set up the detector");

    detector_position = params["Detector"]["Position"];
    gvxr.setDetectorPosition(
        detector_position[0],
        detector_position[1],
        detector_position[2],
        detector_position[3]
    );
    print("\tDetector position:", detector_position)

    detector_up = params["Detector"]["UpVector"];
    gvxr.setDetectorUpVector(
        detector_up[0],
        detector_up[1],
        detector_up[2]
    );
    print("\tDetector up vector:", detector_up)

    if "RightVector" in params["Detector"]:
        detector_right = params["Detector"]["RightVector"];
        gvxr.setDetectorRightVector(
            detector_right[0],
            detector_right[1],
            detector_right[2]
        );
        print("\tDetector right vector:", detector_right)

    if "NumberOfPixels" in params["Detector"]:
        detector_number_of_pixels = params["Detector"]["NumberOfPixels"];
    elif "Number of pixels" in params["Detector"]:
        detector_number_of_pixels = params["Detector"]["Number of pixels"];
    else:
        raise ValueError("The number of pixels of the detector is unknown")
    
    print("\tNumber of pixels:", detector_number_of_pixels)
    gvxr.setDetectorNumberOfPixels(
        detector_number_of_pixels[0],
        detector_number_of_pixels[1]
    );
    print("\tDetector number of pixels:", detector_number_of_pixels)

    if "Oversampling" in params["Detector"].keys():
        gvxr.useLBufferOversamplingFactor(params["Detector"]["Oversampling"])

    if "Spacing" in params["Detector"].keys() == list and "Size" in params["Detector"].keys():
        raise ValueError("Cannot use both 'Spacing' and 'Size' for the detector")

    if "Spacing" in params["Detector"].keys():
        pixel_spacing = params["Detector"]["Spacing"];
    elif "Size" in params["Detector"].keys():
        detector_size = params["Detector"]["Size"];
        pixel_spacing = [];
        pixel_spacing.append(detector_size[0] / detector_number_of_pixels[0]);
        pixel_spacing.append(detector_size[1] / detector_number_of_pixels[1]);
        pixel_spacing.append(detector_size[2]);

    # Sanity check: Cannot use both 'Energy response' and 'Scintillator' for the detector
    if "Energy response" in params["Detector"].keys() and "Scintillator" in params["Detector"].keys():
        raise ValueError("Cannot use both 'Energy response' and 'Scintillator' for the detector")

    if "Energy response" in params["Detector"].keys():

        # Get the unit of energy
        unit_of_energy = "keV"
        if "Unit" in params["Detector"]["Energy response"]:
            unit_of_energy = params["Detector"]["Energy response"]["Unit"]

        elif "Energy" in params["Detector"]["Energy response"]:
            unit_of_energy = params["Detector"]["Energy response"]["Energy"]

        # The response is save in a separate text file
        if "File" in params["Detector"]["Energy response"]:
            print("\tEnergy response:", params["Detector"]["Energy response"]["File"], "in", unit_of_energy)
            gvxr.clearDetectorEnergyResponse()
            gvxr.loadDetectorEnergyResponse(getFilePath(params["Detector"]["Energy response"]["File"]), unit_of_energy)

        # The response is saved in the JSON file
        elif "LUT" in params["Detector"]["Energy response"]:
            gvxr.clearDetectorEnergyResponse()
            gvxr.setDetectorEnergyResponse(params["Detector"]["Energy response"]["LUT"], unit_of_energy)
            print("\tEnergy response:", len(params["Detector"]["Energy response"]["LUT"]), "entries in", unit_of_energy)

    # Set the energy response using the scintillator
    if "Scintillator" in params["Detector"].keys():
        gvxr.clearDetectorEnergyResponse();
        gvxr.setScintillator(params["Detector"]["Scintillator"]["Material"],
            params["Detector"]["Scintillator"]["Thickness"],
            params["Detector"]["Scintillator"]["Unit"]);

    gvxr.setDetectorPixelSize(
        pixel_spacing[0],
        pixel_spacing[1],
        pixel_spacing[2]
    );
    print("\tPixel spacing:", pixel_spacing)

    if "LSF" in params["Detector"].keys():
        print("LSF:", params["Detector"]["LSF"])
        if isinstance(params["Detector"]["LSF"], str) or isinstance(params["Detector"]["LSF"], list):
            # Load from a file
            if isinstance(params["Detector"]["LSF"], str):
                gvxr.setLSF(getFilePath(params["Detector"]["LSF"]))
            # Load from an array
            else:
                gvxr.setLSF(params["Detector"]["LSF"])
        else:
            raise ValueError("LSF must be a filepath or an array.")

    detector_loaded = True

    if kV_loaded and mAs_loaded and source_loaded:
        if verbose:
            print("Update the beam spectrum as the detector position may have changed, and kV and mAs are already in use")

        initSpectrum(fname, verbose)


def initSamples(fname:str="", verbose:int=0):
    """
    Initialise the scanned objects from a JSON file.

    :param str fname: The file name of the JSON file. If no file name is provided, use the cached one. (default: "")
    :param int verbose: The level of verbosity (default: 0)
    """

    global params;

    move_all_mesh_to_centre = False

    gvxr.removePolygonMeshesFromXRayRenderer()
    gvxr.removePolygonMeshesFromSceneGraph()

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f);

        # Update the absolute path of the JSON file
        updatePath(fname)

    # Load the data
    if verbose > 0:
        print("Load the 3D data\n");

    colours = list(mcolors.TABLEAU_COLORS);
    colour_id = 0;

    mesh_source = None
    mesh_unit = None

    if "SceneGraph" in params:
        mesh_source = params["SceneGraph"]["Samples"]
        gvxr.loadSceneGraph(getFilePath(params["SceneGraph"]["Path"]), params["SceneGraph"]["Unit"])

        if verbose > 0:
            print("Load the 3D objects from a scenegraph (" + getFilePath(params["SceneGraph"]["Path"]) + ")")

            for i, mesh in enumerate(mesh_source):
                print(i, mesh["Label"])

    if "Samples" in params:
        mesh_source = params["Samples"]

    for mesh in mesh_source:

        if "Cube" in mesh:
            if verbose == 1:
                print(mesh["Label"] + " is a cube")

            gvxr.makeCube(mesh["Label"], mesh["Cube"][0], mesh["Cube"][1]);

        elif "Cuboid" in mesh or "Parallelepiped" in mesh:
            if verbose == 1:
                print(mesh["Label"] + " is a cuboid")

            if "Cuboid" in mesh:
                gvxr.makeCuboid(mesh["Label"],
                            mesh["Cuboid"][0], mesh["Cuboid"][1], mesh["Cuboid"][2],
                            mesh["Cuboid"][3]);
            else:
                gvxr.makeCuboid(mesh["Label"],
                            mesh["Parallelepiped"][0], mesh["Parallelepiped"][1], mesh["Parallelepiped"][2],
                            mesh["Parallelepiped"][3]);

        elif "Cylinder" in mesh:
            if verbose == 1:
                print(mesh["Label"] + " is a cylinder")

            gvxr.makeCylinder(mesh["Label"], mesh["Cylinder"][0], mesh["Cylinder"][1], mesh["Cylinder"][2], mesh["Cylinder"][3]);

        elif "Step Wedge" in mesh or "StepWedge" in mesh:
            if verbose == 1:
                print(mesh["Label"] + " is a step wedge")

            if "Step Wedge" in mesh:
                dict_item = "Step Wedge";
            else:
                dict_item = "StepWedge";

            # Retrieve the parameters
            step_wedge_dict = mesh[dict_item];
            number_of_steps = step_wedge_dict["NumberOfSteps"];
            total_length = step_wedge_dict["TotalLength"];
            width = step_wedge_dict["Width"];
            first_step_height = step_wedge_dict["FirstStepHeight"];
            other_step_height = step_wedge_dict["OtherStepHeight"];
            unit = step_wedge_dict["Unit"];

            # Create the step wedge
            gvxr.makeStepWedge(mesh["Label"],
                number_of_steps, 
                total_length, 
                width,
                first_step_height,
                other_step_height,
                unit);

        elif "Path" in mesh and "Samples" in params:
            if verbose > 0:
                print("\tLoad", mesh["Label"], "in", getFilePath(mesh["Path"]), "using", mesh["Unit"]);

            gvxr.loadMeshFile(
                mesh["Label"],
                getFilePath(mesh["Path"]),
                mesh["Unit"],
                False
            );

        elif type(mesh) == str:
            if mesh == "MoveToCenter" or mesh == "MoveToCentre" or mesh == "moveToCenter" or mesh == "moveToCentre":
                move_all_mesh_to_centre = True

        elif "SceneGraph" not in params:
            raise IOError("Cannot find the geometry of Mesh " + mesh["Label"])

        if type(mesh) != str:
            material = mesh["Material"];

            if material[0].upper() == "ELEMENT":
                gvxr.setElement(
                    mesh["Label"],
                    material[1]
                );

            elif material[0].upper() == "MIXTURE":
                if type(material[1]) == str:
                    gvxr.setMixture(
                        mesh["Label"],
                        material[1]
                    );

                else:
                    elements = [];
                    weights = [];

                    if verbose == 2:
                        print(mesh["Label"] + ":",
                              "d="+str(mesh["Density"]), "g/cm3 ;",
                              "n=" + str(len(material[1][0::2])),
                              "; state=solid");

                    for Z, weight in zip(material[1][0::2], material[1][1::2]):
                        elements.append(Z);
                        weights.append(weight);

                        if verbose == 2:
                            print("        +el: name="+gvxr.getElementName(Z) + " ; f=" +str(weight) )

                    if verbose == 2:
                        print()

                    gvxr.setMixture(
                        mesh["Label"],
                        elements,
                        weights
                    );

            elif material[0].upper() == "COMPOUND":
                gvxr.setCompound(
                    mesh["Label"],
                    material[1]
                );

            elif material[0].upper() == "HU":
                gvxr.setHounsfieldValue(
                    mesh["Label"],
                    round(material[1])
                );

            elif material[0].upper() == "MU":
                gvxr.setLinearAttenuationCoefficient(
                    mesh["Label"],
                    material[1],
                    "cm-1"
                );

            else:
                raise IOError("Unknown material type: " + material[0]);

            if "Density" in mesh.keys():
                gvxr.setDensity(
                    mesh["Label"],
                    mesh["Density"],
                    "g/cm3"
                );

            if "MoveToCenter" in mesh.keys() or "MoveToCentre" in mesh.keys() or "moveToCenter" in mesh.keys() or "moveToCentre" in mesh.keys():
                move_mesh_to_centre = True
            else:
                move_mesh_to_centre = False

            if "Transform" in mesh.keys():
                # Centre the mesh first, then freeze its vertices
                if move_mesh_to_centre:
                    gvxr.moveToCenter(mesh["Label"])
                    gvxr.applyCurrentLocalTransformation(mesh["Label"])

                for transform in mesh["Transform"]:
                    if transform[0] == "Rotation":
                        if len(transform) == 5:
                            gvxr.rotateNode(mesh["Label"],
                                            transform[1],
                                            transform[2],
                                            transform[3],
                                            transform[4])

                        else:
                            raise IOError("Invalid rotation:", transform)

                    elif transform[0] == "Translation":
                        if len(transform) == 5:
                            gvxr.translateNode(mesh["Label"],
                                            transform[1],
                                            transform[2],
                                            transform[3],
                                            transform[4])

                        else:
                            raise IOError("Invalid translation:", transform)

                    elif transform[0] == "Scaling":
                        if len(transform) == 4:
                            gvxr.scaleNode(mesh["Label"],
                                            transform[1],
                                            transform[2],
                                            transform[3])

                        else:
                            raise IOError("Invalid scaling:", transform)

                    elif transform[0] == "Matrix":
                        if len(transform) == 2:
                            gvxr.setLocalTransformationMatrix(mesh["Label"],
                                [
                                    transform[1][ 0], transform[1][ 1], transform[1][ 2], transform[1][ 3], 
                                    transform[1][ 4], transform[1][ 5], transform[1][ 6], transform[1][ 7], 
                                    transform[1][ 8], transform[1][ 9], transform[1][10], transform[1][11], 
                                    transform[1][12], transform[1][13], transform[1][14], transform[1][15], 
                                ])

                    else:
                        raise IOError("Invalid transformation:", transform)

                # gvxr.applyCurrentLocalTransformation(mesh["Label"])

            # Add the mesh to the simulation
            if "Type" in mesh.keys():
                if mesh["Type"] == "inner":
                    gvxr.addPolygonMeshAsInnerSurface(mesh["Label"]);

                elif mesh["Type"] == "outer":
                    # gvxr.addPolygonMeshAsInnerSurface(mesh["Label"]);
                    gvxr.addPolygonMeshAsOuterSurface(mesh["Label"]);

            else:
                gvxr.addPolygonMeshAsInnerSurface(mesh["Label"]);

            # Flip the normal vectors if needed
            flip_normal_flag_string = None

            if "FlipNormal" in mesh.keys():
                flip_normal_flag_string = "FlipNormal"
            elif "FlipNormals" in mesh.keys():
                flip_normal_flag_string = "FlipNormals"
            elif "flipNormal" in mesh.keys():
                flip_normal_flag_string = "flipNormal"
            elif "flipNormals" in mesh.keys():
                flip_normal_flag_string = "flipNormals"
            elif "flipNormalVectors" in mesh.keys():
                flip_normal_flag_string = "flipNormalVectors"
            elif "invertNormal" in mesh.keys():
                flip_normal_flag_string = "invertNormal"
            elif "invertNormals" in mesh.keys():
                flip_normal_flag_string = "invertNormals"
            elif "invertNormalVectors" in mesh.keys():
                flip_normal_flag_string = "invertNormalVectors"

            if flip_normal_flag_string is not None:
                if mesh[flip_normal_flag_string] != False:
                    gvxr.invertNormalVectors(mesh["Label"])

            # Use the ambiant colour if possible
            has_ambient_colour = False
            if "AmbientColour" in mesh.keys():
                has_ambient_colour = True
                colour = mesh["AmbientColour"]
                gvxr.setColour(mesh["Label"], colour[0], colour[1], colour[2], colour[3]);

            # Use a LUT
            else:
                # Change the colour
                colour = mcolors.to_rgb(colours[colour_id]);

                # Get the opacity
                opacity = 1.0

                if "Opacity" in mesh.keys():
                    opacity = mesh["Opacity"]

                gvxr.setColour(mesh["Label"], colour[0], colour[1], colour[2], opacity);
                colour_id += 1;

                if colour_id == len(colours):
                    colour_id = 0;

            # Set other colour parameters if possible
            if "DiffuseColour" in mesh.keys():
                colour = mesh["DiffuseColour"]
                gvxr.setDiffuseColour(mesh["Label"], colour[0], colour[1], colour[2], colour[3]);

            if "SpecularColour" in mesh.keys():
                colour = mesh["SpecularColour"]
                gvxr.setSpecularColour(mesh["Label"], colour[0], colour[1], colour[2], colour[3]);

            if "Shininess" in mesh.keys():
                gvxr.setShininess(mesh["Label"], mesh["Shininess"]);

    # Move the samples on the centre
    if move_all_mesh_to_centre:
        gvxr.moveToCentre()



def initScan(fname:str=""):

    """
    Initialise a CT scan acquisition from a JSON file.

    :param str fname: The file name of the JSON file. If no file name is provided, use the cached one. (default: "")
    """

    global params;
    global scan_setup
    global scan_params

    # Load the JSON file
    if fname != "":
        with open(fname) as f:
            params = json.load(f)

        # Update the absolute path of the JSON file
        updatePath(fname)

    assert params is not None
    print("Set up the CT Scan")

    if "OutFolder" in params["Scan"]: # Optional
        scan_params["OutFolder"] = Path(getFilePath(params["Scan"]["OutFolder"]))
    else:
        scan_params["OutFolder"] = Path(getFilePath("./output/"))

    if "GifPath" in params["Scan"]: # Optional
        scan_params["GifPath"] = getFilePath(params["Scan"]["GifPath"])

    # GVXR Supports multiple methods to define scanning, and will work out every
    # possible combination. As a result, we will parse all the scanning
    # paramaters first, and then do checks to see if anything is missing

    nop = int(params["Scan"]["NumberOfProjections"]) if "NumberOfProjections" in params["Scan"] else None
    angS = float(params["Scan"]["AngleStep"]) if "AngleStep" in params["Scan"] else None
    finA = float(params["Scan"]["FinalAngle"]) if "FinalAngle" in params["Scan"] else None
    staA = float(params["Scan"]["StartAngle"]) if "StartAngle" in params["Scan"] else 0.0
    ilA = bool(params["Scan"]["IncludeLastAngle"]) if "IncludeLastAngle" in params["Scan"] else False

    flat_field_correction = bool(params["Scan"]["Flat-Field Correction"]) if "Flat-Field Correction" in params["Scan"] else False

    # if AngleStep OR Number of projections is missing, they can be worked out
    # with FinalAngle
    if nop is None or angS is None:
        if (nop is None and angS is None) or finA is None:
            # Cannot work out params with both sets missing
            raise ValueError("FinalAngle and NumberOfProjections or AngleStep must exist in Scan key.")
        if nop is None and angS is not None:
            if ilA is not None and ilA == True:
                nop = int((finA - staA) / angS) + 1
            else:
                nop = int((finA - staA) / angS)

        elif angS is None and nop is not None:
            if ilA is not None and ilA == True:
                angS = (finA - staA) / (nop - 1)
            else:
                angS = (finA - staA) / nop
        elif nop is not None and angS is not None and finA is None:
            if ilA is not None and ilA == True:
                finA = staA + angS * (nop - 1)
            else:
                finA = staA + angS * nop
        else:
            # Somehow the logic is broken?
            raise ValueError("Unable to calculate NumberOfProjections or AngleStep, please report this error with your config.")


    scan_params["AngleStep"] = angS
    scan_params["NumberOfProjections"] = nop
    scan_params["FinalAngle"] = finA
    scan_params["StartAngle"] = staA
    scan_params["IncludeLastAngle"] = ilA
    scan_params["Flat-Field Correction"] = flat_field_correction
    scan_params["RotationAxis"] = params["Detector"]["UpVector"];

    if "CenterOfRotation" in params["Scan"]:
        scan_params["RotCentre"] = params["Scan"]["CenterOfRotation"]
    elif "CentreOfRotation" in params["Scan"]:
        scan_params["RotCentre"] = params["Scan"]["CentreOfRotation"]
    elif "Center of rotation" in params["Scan"]:
        scan_params["RotCentre"] = params["Scan"]["Center of rotation"]
    elif "Centre of rotation" in params["Scan"]:
        scan_params["RotCentre"] = params["Scan"]["Centre of rotation"]
    else:
        scan_params["RotCentre"] = [0, 0, 0, "mm"]

    if "RotationAxis" in params["Scan"]:
        scan_params["RotationAxis"] = params["Scan"]["RotationAxis"]
    elif "Rotation axis" in params["Scan"]:
        scan_params["RotationAxis"] = params["Scan"]["Rotation axis"]

    scan_setup = True

    save_gif = "GifPath" in scan_params

    if save_gif:
        # Start scene
        gvxr.displayScene()

        # Move scene
        dist = np.linalg.norm((np.asarray(gvxr.getDetectorPosition("mm")), np.asarray(gvxr.getSourcePosition("mm"))))
        gvxr.setZoom(dist * 1.5)

        # # This specific rotation matrix assume using cil standards
        # if params["Detector"]["UpVector"][2] != 0:
        #     gvxr.setSceneRotationMatrix((0.19488376379013062, 0.5883488655090332, -0.7847718000411987, 0.0, 0.9800633788108826, -0.1483602672815323, 0.13215424120426178, 0.0, -0.0386761911213398, -0.7948808670043945, -0.6055325865745544, 0.0, 0.0, 0.0, 0.0, 1.0))
        # elif params["Detector"]["UpVector"][1] != 0:
        #     gvxr.setSceneRotationMatrix((-0.24557003378868103, -0.35820719599723816, 0.9007686376571655, 0.0, -0.01915137656033039, -0.9272466897964478, -0.37395715713500977, 0.0, 0.9691887497901917, -0.10908106714487076, 0.2208413928747177, 0.0, 0.0, 0.0, 0.0, 1.0))
        # elif params["Detector"]["UpVector"][0] != 0:
        #     gvxr.setSceneRotationMatrix((-0.016064796596765518, -0.9035729169845581, -0.4281272888183594, 0.0, 0.40574967861175537, 0.38545310497283936, -0.8287299275398254, 0.0, 0.9138408303260803, -0.18702487647533417, 0.360431045293808, 0.0, 0.0, 0.0, 0.0, 1.0))



def doCTScan(verbose:bool=False):


    """
    Perform the CT scan acquisition as initialised with the JSON file.

    :return: The rotations angles in degrees
    """

    global params
    global scan_setup
    global scan_params
    global white_image

    # Ensure scan is setup first
    if not scan_setup or params is None:
        raise RuntimeError("initScan() must be called before doCTScan()")

    # save_gif = "GifPath" in scan_params
    # out_folder = Path(scan_params["OutFolder"])

    if verbose:
        print("Performing CT Scan")
        print("\tRotation Centre:",scan_params["RotCentre"])
        print("\tNumber of Projections:",scan_params["NumberOfProjections"])
        print("\tRotation axis:", scan_params["RotationAxis"])
        print("\tAngle Step:",scan_params["AngleStep"])
        print("\tStart Angle:",scan_params["StartAngle"])
        print("\tFinal Angle:",scan_params["FinalAngle"])
        print("\tLast Angle Included:","YES" if scan_params["IncludeLastAngle"] else "NO")
        print("\tFlat-field correction:","YES" if scan_params["Flat-Field Correction"] else "NO")
        print("\tOutput folder:", scan_params["OutFolder"])

    # # Prepare scene for making a gif
    # screenshots = []

    # Create the output directory if needed
    os.makedirs(scan_params["OutFolder"], exist_ok=True)

    # if "NumberOfWhiteImages" in params["Scan"]:
    #     number_of_white_images = int(params["Scan"]["NumberOfWhiteImages"])
    #     scan_params["Flat-Field Correction"] = True
    # else:
    #     number_of_white_images = 1

    # # Create the white image for flat-field correction
    # if scan_params["Flat-Field Correction"]:            
    #     white_image = np.zeros((gvxr.getDetectorNumberOfPixels()[1], gvxr.getDetectorNumberOfPixels()[0]), dtype=np.single)
        
    #     for i in range(number_of_white_images):
    #         white_image += gvxr.getWhiteImage()

    #     white_image /= number_of_white_images

    # old_files = glob.glob(f"{scan_params['OutFolder']}/projection-*.tiff")
    # for fname in old_files:
    #     if verbose:
    #         print("\tDelete", fname)

    #     os.remove(fname)

    # old_files = glob.glob(f"{scan_params['OutFolder']}/projection-*.mha")
    # for fname in old_files:
    #     if verbose:
    #         print("\tDelete", fname)

    #     os.remove(fname)

    # if verbose:
    #     print(f"\tProjections saved to '{scan_params['OutFolder']}/projection-xxxx.tiff'")

    # angles = []
    # backup = gvxr.getLocalTransformationMatrix("root")
    
    
    units = "mm" # default for backward compatibility
    if len(scan_params["RotCentre"]) == 4:
        units = scan_params["RotCentre"][3]
    
    # gvxr.translateNode("root", 
    #     scan_params["RotCentre"][0],
    #     scan_params["RotCentre"][1],
    #     scan_params["RotCentre"][2],
    #     units)

    # for i in range(scan_params["NumberOfProjections"]):
    #     angles.append(i*scan_params["AngleStep"])


    #     # Compute an X-ray image
    #     img = np.array(gvxr.computeXRayImage(), dtype=np.single)

    #     # Apply the flat-field correction
    #     if scan_params["Flat-Field Correction"]:            
    #         img /= white_image

    #     # Looks like convention is for 4 digits 0-padding, with inital projection starting at 1
    #     Image.fromarray(img).save(out_folder/f"projection-{i+1:04}.tiff")

    #     if save_gif:
    #         # Update scene
    #         gvxr.displayScene()
    #         scrn = (np.asarray(gvxr.takeScreenshot()) * 255).astype("uint8")
    #         screenshots.append(Image.fromarray(scrn))

    #     # Rotate around detector up vector
    #     gvxr.rotateNode("root", scan_params["AngleStep"], *scan_params["RotationAxis"])

    # gvxr.setLocalTransformationMatrix("root", backup)

    # if verbose:
    #     print("CT Complete")

    # if save_gif:
    #     # Create a gif image
    #     screenshots[0].save(scan_params["GifPath"], "gif", append_images=screenshots[1:], duration=50, save_all=True, loop=0)
    #     if verbose:
    #         print("\tAnimation Saved to ", scan_params["GifPath"])

    # # Create a single scene image of the setup environment
    # # screenshots[0].save(scan_params["OutFolder"]/"scene.png")

    # if verbose:
    #     print("Simulated", scan_params["NumberOfProjections"], "projections.")
    # return angles

    if scan_params["Flat-Field Correction"]:            
        if "NumberOfWhiteImages" in params["Scan"]:
            number_of_white_images = int(params["Scan"]["NumberOfWhiteImages"])
        else:
            number_of_white_images = 1
    else:
        number_of_white_images = 0

    output_path = ""
    if scan_params["OutFolder"] is not None:
        output_path = str(scan_params["OutFolder"])

    gif_path = ""
    if "GifPath" in scan_params:
        gif_path = str(scan_params["GifPath"])

    gvxr.computeCTAcquisition(output_path, gif_path,
        scan_params["NumberOfProjections"],
        scan_params["StartAngle"],
        scan_params["IncludeLastAngle"],
        scan_params["FinalAngle"],
        number_of_white_images,
        scan_params["RotCentre"][0], scan_params["RotCentre"][1], scan_params["RotCentre"][2],
        units,
        scan_params["RotationAxis"][0], scan_params["RotationAxis"][1], scan_params["RotationAxis"][2],
        True,
        int(verbose)
    );

    return gvxr.getAngleSetCT();
