import wave
from typing import Union, BinaryIO
from pathlib import Path

def validate_wav(file_input: Union[str, Path, BinaryIO]) -> bool:
    """
    Validate if a file is a proper WAV file by checking its format and properties.

    Args:
        file_input: Can be a file path (str or Path) or a file-like object

    Returns:
        bool: True if the file is a valid WAV file, False otherwise

    Examples:
        >>> from snaketools.audio import validate_wav_file
        >>> validate_wav_file("path/to/audio.wav")
        True
        >>> with open("audio.wav", "rb") as f:
        ...     validate_wav_file(f)
        True
    """
    try:
        # Handle different input types
        if isinstance(file_input, (str, Path)):
            wav_file = wave.open(str(file_input), 'rb')
        else:  # Assume file-like object
            wav_file = wave.open(file_input, 'rb')

        with wav_file:
            # Check basic WAV properties
            if wav_file.getnchannels() == 0:
                return False
            if wav_file.getframerate() == 0:
                return False
            if wav_file.getsampwidth() == 0:
                return False

            # Try to read a small portion of the file
            wav_file.readframes(1)

            return True

    except (wave.Error, EOFError, OSError) as e:
        return False
    except Exception as e:
        return False