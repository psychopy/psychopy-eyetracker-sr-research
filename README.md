# psychopy-eyetracker-sr-research

Extension for PsychoPy which adds support for [SR Research](https://www.sr-research.com/) 
eyetrackers (via ioHub)

## Supported Devices

Installing this package alongside PsychoPy will enable support for the following 
devices:

* Supported SR Research EyeLink devices
    
## Installing

Install this package with the following shell command:: 

    pip install psychopy-eyetracker-sr-research

You may also use PsychoPy's builtin plugin/package manager to install this 
package.

## Usage

Once the package is installed, PsychoPy will automatically load it when started 
and the `psychopy.iohub.devices.eyetracker.hw.sr_research` namespace will 
contain the loaded objects.