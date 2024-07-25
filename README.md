# psychopy-eyetracker-sr-research

Extension for PsychoPy which adds support for [SR Research](https://www.sr-research.com/) 
eyetrackers (via ioHub)

## Supported Devices

Installing this package alongside PsychoPy will enable support for the following devices:

* Supported SR Research EyeLink devices

## Installing

Install this package with the following shell command:

    pip install psychopy-eyetracker-sr-research

You may also use PsychoPy's built-in plugin/package manager to install this package.

## Alternative
There is a different plug-in package [`psychopy-eyelink`](https://pypi.org/project/psychopy-eyelink/) provided by SR Research that adds more EyeLink-specific Eyetracking components to the PsychoPy Builder view to interact with SR Research EyeLink devices directly (without using ioHub). Note that when [`psychopy-eyelink`] is used, its component implementations are independent of the [`EyeTracking` tab in the `Experiment Setting` window](https://psychopy.org/hardware/eyeTracking.html).

You may use either `psychopy-eyetracker-sr-research` or `psychopy-eyelink` (but not both) to communicate with a SR Research EyeLink eyetracker.

## Usage

Once the package is installed, PsychoPy will automatically load it when started and the `psychopy.iohub.devices.eyetracker.hw.sr_research` namespace will contain the loaded objects.