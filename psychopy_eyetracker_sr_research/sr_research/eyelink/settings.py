from psychopy.localization import _translate
from psychopy.experiment import Param
from psychopy.experiment.components.settings.eyetracking import EyetrackerBackend


class EyeLinkEyetrackerBackend(EyetrackerBackend):
    """Experiment settings for EyeLink 1000 eyetrackers.
    """
    label = 'SR Research Ltd. EyeLink 1000 (iohub)'
    key = 'eyetracker.hw.sr_research.eyelink.EyeTracker'

    needsFullscreen = True
    needsCalibration = False

    @classmethod
    def getParams(cls):
        # define order
        order = [
            # other options
            "elModelName",
            "elSimulationMode",
            "elEnableInterfaceWithoutConnection",
            # network settings
            "elNetIP4Address",
            # runtime settings
            "elSamplingRate",
            "elTrackEyes",
            "elSampleFiltering",
            "elSampleFilterType",
            "elVOGPupilMeasureTypes",
            "elVOGTrackingMode",
            "elVOGPupilCenterAlgorithm"
        ]

        # network settings
        params = {}
        params['elNetIP4Address'] = Param(
            "10.0.0.1",   # default value
            valType='str', 
            inputType="single",
            hint=_translate("IP Address to connect to."),
            label=_translate("IP4 Address"), 
            categ="Eyetracking"
        )

        # other options
        params['elModelName'] = Param(
            'EYELINK 1000 DESKTOP', 
            valType='str', 
            inputType="choice",
            allowedVals=["EYELINK 1000 DESKTOP", "EYELINK 1000 TOWER", "EYELINK 1000 REMOTE", "EYELINK 1000 LONG RANGE"],
            hint=_translate("Eyetracker device model"),
            label=_translate("Model for the eyetracker in use."),
            categ="Eyetracking"
        )
        params['elSimulationMode'] = Param(
            False,
            valType='bool',
            inputType="bool",
            hint=_translate("Simulation mode."),
            label=_translate("Simulation mode?"),
            categ="Eyetracking"
        )
        params['elEnableInterfaceWithoutConnection'] = Param(
            False,
            valType='bool',
            inputType="bool",
            hint=_translate("Enable interface without connection."),
            label=_translate("Enable interface without connection?"),
            categ="Eyetracking"
        )

        # runtime settings
        params['elSamplingRate'] = Param(
            '250', 
            valType='str', 
            inputType="choice",
            allowedVals=['250', '500', '1000', '2000'],
            hint=_translate("Sampling rate for the eyetracker in Hz."),
            label=_translate("Tracker sampling rate (Hz)"),
            categ="Eyetracking"
        )
        params['elTrackEyes'] = Param(
            'LEFT_EYE', 
            valType='str', 
            inputType="choice",
            allowedVals=['LEFT_EYE', 'RIGHT_EYE', 'BOTH'],
            label=_translate("Track eyes"),
            hint=_translate("Which eyes to track."),
        )
        params['elSampleFiltering'] = Param(
            'FILTER_ALL', 
            valType='str', 
            inputType="choice",
            allowedVals=['FILTER_ALL', 'FILTER_FILE', 'FILTER_ONLINE'],
            hint=_translate("Sample filtering mode."),
            label=_translate("Sample filtering"),
            categ="Eyetracking"
        )
        params['elSampleFilterType'] = Param(
            'FILTER_LEVEL_OFF', 
            valType='str', 
            inputType="choice",
            allowedVals=['FILTER_LEVEL_OFF', 'FILTER_LEVEL_1', 'FILTER_LEVEL_2'],
            hint=_translate("Sample filter type."),
            label=_translate("Sample filter type"),
            categ="Eyetracking"
        )
        params['elVOGPupilMeasureTypes'] = Param(
            'PUPIL_AREA', 
            valType='str', 
            inputType="choice",
            allowedVals=['PUPIL_AREA', 'PUPIL_DIAMETER'],
            hint=_translate("Pupil measure type."),
            label=_translate("Pupil measure type"),
            categ="Eyetracking"
        )
        params['elVOGTrackingMode'] = Param(
            'PUPIL_CR_TRACKING', 
            valType='str', 
            inputType="choice",
            allowedVals=['PUPIL_CR_TRACKING', 'PUPIL_ONLY_TRACKING'],
            hint=_translate("Pupil tracking mode."),
            label=_translate("Pupil tracking mode"),
            categ="Eyetracking"
        )
        params['elVOGPupilCenterAlgorithm'] = Param(
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
            "    'model_name': %(elModelName)s,\n"
            "    'simulation_mode': %(elSimulationMode)s,\n"
            "    'enable_interface_without_connection': %(elEnableInterfaceWithoutConnection)s,\n"
            "    'network_settings': %(elNetIP4Address)s,\n"
            "    'runtime_settings': {\n"
            "        'sampling_rate': %(elSamplingRate)s,\n"
            "        'track_eyes': %(elTrackEyes)s,\n"
            "        'sample_filtering': {\n"
            "            %(elSampleFiltering)s: %(elSampleFilterType)s,\n"
            "        },\n"
            "        'vog_settings': {\n"
            "           'pupil_measure_types': %(elVOGPupilMeasureTypes)s,\n"
            "           'tracking_mode': %(elVOGTrackingMode)s,\n"
            "           'pupil_center_algorithm': %(elVOGPupilCenterAlgorithm)s,\n"
            "        },\n"
            "    },\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)

