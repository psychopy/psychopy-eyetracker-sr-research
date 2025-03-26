from psychopy.localization import _translate
from psychopy.experiment import Param
from psychopy.experiment.components.settings.eyetracking import EyetrackerBackend


class EyeLinkEyetrackerBackend(EyetrackerBackend):
    """Experiment settings for EyeLink 1000 eyetrackers.
    """
    label = 'SR Research Ltd EyeLink 1000 (iohub)'
    key = 'eyetracker.hw.sr_research.eyelink.EyeTracker'

    needsFullscreen = True
    needsCalibration = False

    @classmethod
    def getParams(cls):
        # define order
        order = [
            # other options
            "srModelName",
            "srSimulationMode",
            "srNativeDataFileName",
            # network settings
            "srEnableInterfaceWithoutConnection",
            "srNetIP4Address",
            # runtime settings
            "srSamplingRate",
            "srTrackEyes",
            "srLiveSampleFiltering",
            "srFileSampleFiltering",
            "srVOGPupilMeasureTypes",
            "srVOGTrackingMode",
            "srVOGPupilCenterAlgorithm"
        ]

        params = {}

        # network settings
        params['srNetIP4Address'] = Param(
            "100.1.1.1",   # default value
            valType='str', 
            inputType="single",
            hint=_translate("IP4 address to connect to."),
            label=_translate("Device IP4 address"), 
            categ="Eyetracking"
        )

        # other options
        params['srModelName'] = Param(
            'EYELINK 1000 DESKTOP', 
            valType='str', 
            inputType="choice",
            allowedVals=["EYELINK 1000 DESKTOP", "EYELINK 1000 TOWER", "EYELINK 1000 REMOTE", "EYELINK 1000 LONG RANGE"],
            hint=_translate("Device model for the eyetracker."),
            label=_translate("Device model"),
            categ="Eyetracking"
        )
        params['srSimulationMode'] = Param(
            False,
            valType='bool',
            inputType="bool",
            hint=_translate("Use a mouse to simulate eye movements instead of real gaze data."),
            label=_translate("Mouse simulation mode?"),
            categ="Eyetracking"
        )
        params['srEnableInterfaceWithoutConnection'] = Param(
            False,
            valType='bool',
            inputType="bool",
            hint=_translate("Enable interface without eyetracker connection for testing."),
            label=_translate("Disable eyetracker connection?"),
            categ="Eyetracking"
        )
        params['srNativeDataFileName'] = Param(
            "et_data",
            valType='str',
            inputType="single",
            hint=_translate("Set the default name of the native eyetracker EDF data file (excluding the .edf extension)"),
            label=_translate("EDF data file name"),
            categ="Eyetracking"
        )

        # runtime settings
        params['srSamplingRate'] = Param(
            '250', 
            valType='str', 
            inputType="choice",
            allowedVals=['250', '500', '1000', '2000'],
            hint=_translate("Sampling rate for the eyetracker in Hz."),
            label=_translate("Tracker sampling rate (Hz)"),
            categ="Eyetracking"
        )
        params['srTrackEyes'] = Param(
            'RIGHT_EYE', 
            valType='str', 
            inputType="choice",
            allowedVals=['LEFT_EYE', 'RIGHT_EYE', 'BOTH'],
            label=_translate("Track eyes"),
            hint=_translate("Which eyes to track."),
        )
        params['srLiveSampleFiltering'] = Param(
            'FILTER_LEVEL_OFF', 
            valType='str', 
            inputType="choice",
            allowedVals=['FILTER_LEVEL_OFF', 'FILTER_LEVEL_1', 'FILTER_LEVEL_2'],
            hint=_translate("Set the native filter level to be applied to samples."),
            label=_translate("Live sample filter"),
            categ="Eyetracking"
        )
        params['srFileSampleFiltering'] = Param(
            'FILTER_LEVEL_OFF', 
            valType='str', 
            inputType="choice",
            allowedVals=['FILTER_LEVEL_OFF', 'FILTER_LEVEL_1', 'FILTER_LEVEL_2'],
            hint=_translate("Set the native filter level to be applied to samples written to file."),
            label=_translate("Save sample filter"),
            categ="Eyetracking"
        )
        params['srVOGPupilMeasureTypes'] = Param(
            'PUPIL_AREA', 
            valType='str', 
            inputType="choice",
            allowedVals=['PUPIL_AREA', 'PUPIL_DIAMETER'],
            hint=_translate("Pupil measure type."),
            label=_translate("Pupil measure type"),
            categ="Eyetracking"
        )
        params['srVOGTrackingMode'] = Param(
            'PUPIL_CR_TRACKING', 
            valType='str', 
            inputType="choice",
            allowedVals=['PUPIL_CR_TRACKING', 'PUPIL_ONLY_TRACKING'],
            hint=_translate("Pupil tracking mode."),
            label=_translate("Pupil tracking mode"),
            categ="Eyetracking"
        )
        params['srVOGPupilCenterAlgorithm'] = Param(
            'ELLIPSE_FIT', 
            valType='str', 
            inputType="choice",
            allowedVals=['ELLIPSE_FIT', 'CENTROID_FIT'],
            hint=_translate("Pupil center algorithm."),
            label=_translate("Pupil center algorithm"),
            categ="Eyetracking"
        )

        return params, order

    @classmethod
    def writeDeviceCode(cls, inits, buff):
        code = (
            "ioConfig[%(eyetracker)s] = {\n"
            "    'name': 'tracker',\n"
            "    'model_name': %(srModelName)s,\n"
            "    'simulation_mode': %(srSimulationMode)s,\n"
            "    'default_native_data_file_name': %(srNativeDataFileName)s,\n"
            "    'enable_interface_without_connection': %(srEnableInterfaceWithoutConnection)s,\n"
            "    'network_settings': %(srNetIP4Address)s,\n"
            "    'runtime_settings': {\n"
            "        'sampling_rate': %(srSamplingRate)s,\n"
            "        'track_eyes': %(srTrackEyes)s,\n"
            "        'sample_filtering': {\n"
            "              'FILTER_ONLINE': %(srLiveSampleFiltering)s,\n"
            "              'FILTER_FILE': %(srFileSampleFiltering)s,\n"
            "        },\n"
            "        'vog_settings': {\n"
            "           'pupil_measure_types': %(srVOGPupilMeasureTypes)s,\n"
            "           'tracking_mode': %(srVOGTrackingMode)s,\n"
            "           'pupil_center_algorithm': %(srVOGPupilCenterAlgorithm)s,\n"
            "        },\n"
            "    },\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)

