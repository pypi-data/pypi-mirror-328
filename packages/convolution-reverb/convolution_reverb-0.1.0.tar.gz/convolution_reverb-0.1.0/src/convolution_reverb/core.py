import typing as tp
import torch
import torchaudio

def normalize_audio(audio: torch.Tensor) -> torch.Tensor:  # is this necessary?
    """Normalize the audio tensor so that its maximum absolute value is 1."""
    max_val = audio.abs().max()
    if max_val > 0:
        audio = audio / max_val
    return audio

def apply_reverb(*, 
         audio_path: tp.Union[str, None] = None, 
         audio_wav: tp.Union[torch.Tensor, None] = None, 
         audio_wav_sr: tp.Union[int, None] = None,
         ir_path: tp.Union[str, None] = None,
         ir_wav: tp.Union[torch.Tensor, None] = None, 
         ir_wav_sr: tp.Union[int, None] = None,
         output_path: tp.Union[str, None] = None,
         normalize:bool=False,
         ) -> tp.Tuple[torch.Tensor, torch.Tensor, int]:
    """
    Apply convolution reverb to an audio file or tensor.

    Args:
        audio_path: Path to the input audio file
        audio_wav: Input audio as a torch.Tensor (n_channels, n_samples)
        audio_wav_sr: Sampling rate of the input audio tensor
        ir_path: Path to the impulse response file
        ir_wav: Impulse response as a torch.Tensor (n_channels, n_samples)
        ir_wav_sr: Sampling rate of the impulse response tensor
        output_path: Path where the output audio will be saved

    Returns:
        Tuple containing:
        - Original audio waveform (torch.Tensor)
        - Convolved audio waveform (torch.Tensor)
        - Sample rate (int)
    """
    if isinstance(audio_path, type(None)) and isinstance(audio_wav, type(None)):
        raise ValueError("Either audio_path or audio_wav must be provided.")
    if isinstance(audio_path, str) and isinstance(audio_wav, torch.Tensor):
        raise ValueError("Only one of audio_path or audio_wav can be provided.")

    # Load the audio and impulse response using torchaudio
    if isinstance(audio_path, str):
        audio_waveform, sr_audio = torchaudio.load(audio_path)
    else:
        audio_waveform, sr_audio = audio_wav, audio_wav_sr

    if isinstance(ir_path, str):
        ir_waveform, sr_ir = torchaudio.load(ir_path)
    else:
        ir_waveform, sr_ir = ir_wav, ir_wav_sr
    
    # Ensure the sampling rates match
    if sr_audio != sr_ir:
        ir_waveform = torchaudio.functional.resample(ir_waveform, sr_ir, sr_audio)
    
    # If multi-channel, convert to mono by averaging all channels
    if audio_waveform.shape[0] > 1:
        print("Input audio is multi-channel. Converting to mono by averaging channels.")
        audio_waveform = audio_waveform.mean(dim=0, keepdim=True)
    if ir_waveform.shape[0] > 1:
        print("Impulse response is multi-channel. Converting to mono by averaging channels.")
        ir_waveform = ir_waveform.mean(dim=0, keepdim=True)
    
    audio = audio_waveform[0]
    ir = ir_waveform[0]

    # Convert to float32 (if not already) for processing
    audio = audio.float()
    ir = ir.float()
    
    # Determine the length of the convolution result
    n = audio.numel() + ir.numel() - 1
    # Compute next power-of-two for efficient FFT computation
    n_fft = 2 ** ((n - 1).bit_length())
    
    # Compute FFT of both signals (using real FFT)
    A = torch.fft.rfft(audio, n=n_fft)
    B = torch.fft.rfft(ir, n=n_fft)
    
    # Element-wise multiply in frequency domain (this is equivalent to convolution)
    C = A * B
    
    # Compute the inverse FFT to get the convolved signal and slice to the expected length
    convolved = torch.fft.irfft(C, n=n_fft)[:n]
    
    # Normalize to avoid clipping
    if normalize:
        convolved = normalize_audio(convolved)

    # length match
    if audio_waveform.shape[-1] != convolved.shape[0]:
        # print("Length mismatch. Padding or truncating convolved signal to match audio length.")
        if audio_waveform.shape[-1] < convolved.shape[0]:
            convolved = convolved[:audio_waveform.shape[-1]]
        else:
            raise ValueError("Convolved signal is shorter than the audio signal. Does this happen?")

    # Save the output if path is provided. torchaudio expects shape (channels, samples)
    if isinstance(output_path, str):
        convolved = convolved.unsqueeze(0)
        torchaudio.save(output_path, convolved, sr_audio)
        print(f"Convolved audio saved as '{output_path}'.")

    return audio_waveform.mean(dim=0), convolved, sr_audio 