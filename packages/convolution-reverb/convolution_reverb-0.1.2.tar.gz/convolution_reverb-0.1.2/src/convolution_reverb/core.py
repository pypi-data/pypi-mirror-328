# import typing as tp
# import torch
# import torchaudio

# def normalize_audio(audio: torch.Tensor) -> torch.Tensor:  # is this necessary?
#     """Normalize the audio tensor so that its maximum absolute value is 1."""
#     max_val = audio.abs().max()
#     if max_val > 0:
#         audio = audio / max_val
#     return audio

# def apply_reverb(*, 
#          audio_path: tp.Union[str, None] = None, 
#          audio_wav: tp.Union[torch.Tensor, None] = None, 
#          audio_wav_sr: tp.Union[int, None] = None,
#          ir_path: tp.Union[str, None] = None,
#          ir_wav: tp.Union[torch.Tensor, None] = None, 
#          ir_wav_sr: tp.Union[int, None] = None,
#          output_path: tp.Union[str, None] = None,
#          normalize:bool=False,
#          ) -> tp.Tuple[torch.Tensor, torch.Tensor, int]:
#     """
#     Apply convolution reverb to an audio file or tensor.

#     Args:
#         audio_path: Path to the input audio file
#         audio_wav: Input audio as a torch.Tensor (n_channels, n_samples)
#         audio_wav_sr: Sampling rate of the input audio tensor
#         ir_path: Path to the impulse response file
#         ir_wav: Impulse response as a torch.Tensor (n_channels, n_samples)
#         ir_wav_sr: Sampling rate of the impulse response tensor
#         output_path: Path where the output audio will be saved

#     Returns:
#         Tuple containing:
#         - Original audio waveform (torch.Tensor)
#         - Convolved audio waveform (torch.Tensor)
#         - Sample rate (int)
#     """
#     if isinstance(audio_path, type(None)) and isinstance(audio_wav, type(None)):
#         raise ValueError("Either audio_path or audio_wav must be provided.")
#     if isinstance(audio_path, str) and isinstance(audio_wav, torch.Tensor):
#         raise ValueError("Only one of audio_path or audio_wav can be provided.")

#     # Load the audio and impulse response using torchaudio
#     if isinstance(audio_path, str):
#         audio_waveform, sr_audio = torchaudio.load(audio_path)
#     else:
#         audio_waveform, sr_audio = audio_wav, audio_wav_sr

#     if isinstance(ir_path, str):
#         ir_waveform, sr_ir = torchaudio.load(ir_path)
#     else:
#         ir_waveform, sr_ir = ir_wav, ir_wav_sr
    
#     # Ensure the sampling rates match
#     if sr_audio != sr_ir:
#         ir_waveform = torchaudio.functional.resample(ir_waveform, sr_ir, sr_audio)
    
#     # If multi-channel, convert to mono by averaging all channels
#     if audio_waveform.shape[0] > 1:
#         print("Input audio is multi-channel. Converting to mono by averaging channels.")
#         audio_waveform = audio_waveform.mean(dim=0, keepdim=True)
#     if ir_waveform.shape[0] > 1:
#         print("Impulse response is multi-channel. Converting to mono by averaging channels.")
#         ir_waveform = ir_waveform.mean(dim=0, keepdim=True)
    
#     audio = audio_waveform[0]
#     ir = ir_waveform[0]

#     # Convert to float32 (if not already) for processing
#     audio = audio.float()
#     ir = ir.float()
    
#     # Determine the length of the convolution result
#     n = audio.numel() + ir.numel() - 1
#     # Compute next power-of-two for efficient FFT computation
#     n_fft = 2 ** ((n - 1).bit_length())
    
#     # Compute FFT of both signals (using real FFT)
#     A = torch.fft.rfft(audio, n=n_fft)
#     B = torch.fft.rfft(ir, n=n_fft)
    
#     # Element-wise multiply in frequency domain (this is equivalent to convolution)
#     C = A * B
    
#     # Compute the inverse FFT to get the convolved signal and slice to the expected length
#     convolved = torch.fft.irfft(C, n=n_fft)[:n]
    
#     # Normalize to avoid clipping
#     if normalize:
#         convolved = normalize_audio(convolved)

#     # length match
#     if audio_waveform.shape[-1] != convolved.shape[0]:
#         # print("Length mismatch. Padding or truncating convolved signal to match audio length.")
#         if audio_waveform.shape[-1] < convolved.shape[0]:
#             convolved = convolved[:audio_waveform.shape[-1]]
#         else:
#             raise ValueError("Convolved signal is shorter than the audio signal. Does this happen?")

#     # Save the output if path is provided. torchaudio expects shape (channels, samples)
#     if isinstance(output_path, str):
#         convolved = convolved.unsqueeze(0)
#         torchaudio.save(output_path, convolved, sr_audio)
#         print(f"Convolved audio saved as '{output_path}'.")

#     return audio_waveform.mean(dim=0), convolved, sr_audio 


import typing as tp
import torch
import torchaudio


def apply_reverb(*, 
         audio_path: tp.Union[str, None] = None, 
         audio_wav: tp.Union[torch.Tensor, None] = None, 
         audio_wav_sr: tp.Union[int, None] = None,
         ir_path: tp.Union[str, None] = None,
         ir_wav: tp.Union[torch.Tensor, None] = None, 
         ir_wav_sr: tp.Union[int, None] = None,
         output_path: tp.Union[str, None] = None,
         ) -> tp.Tuple[torch.Tensor, torch.Tensor, int]:
    """
    Apply convolution reverb to an audio file or tensor.

    The audio input can now be provided as either:
      - A tensor of shape (n_channels, n_samples) (single example), or
      - A tensor of shape (batch_size, n_channels, n_samples).
      
    In the single-example case the tensor is automatically unsqueezed to add a batch dimension.

    Args:
        audio_path: Path to the input audio file.
        audio_wav: Input audio as a torch.Tensor (n_channels, n_samples) or (batch_size, n_channels, n_samples).
        audio_wav_sr: Sampling rate of the input audio.
        ir_path: Path to the impulse response file.
        ir_wav: Impulse response as a torch.Tensor (n_channels, n_samples).
        ir_wav_sr: Sampling rate of the impulse response.
        output_path: Path where the output audio will be saved.

    Returns:
        Tuple containing:
        - Original mono audio waveform (torch.Tensor) with shape (batch_size, n_samples)
        - Convolved audio waveform (torch.Tensor) with shape (batch_size, n_samples)
        - Sample rate (int)
    """
    # Validate audio input
    if audio_path is None and audio_wav is None:
        raise ValueError("Either audio_path or audio_wav must be provided.")
    if isinstance(audio_path, str) and audio_wav is not None:
        raise ValueError("Only one of audio_path or audio_wav can be provided.")

    # Load audio
    if audio_path is not None:
        audio_waveform, sr_audio = torchaudio.load(audio_path)  # shape: (n_channels, n_samples)
        # Add a batch dimension: (1, n_channels, n_samples)
        audio_waveform = audio_waveform.unsqueeze(0)
    else:
        audio_waveform = audio_wav
        sr_audio = audio_wav_sr
        # If provided as (n_channels, n_samples), unsqueeze to get (1, n_channels, n_samples)
        if audio_waveform.dim() == 2:
            audio_waveform = audio_waveform.unsqueeze(0)
        elif audio_waveform.dim() != 3:
            raise ValueError("audio_wav must be a 2D or 3D tensor.")

    # Load impulse response (IR)
    if ir_path is not None:
        ir_waveform, sr_ir = torchaudio.load(ir_path)  # shape: (n_channels, n_samples)
    else:
        if ir_wav is None:
            raise ValueError("Either ir_path or ir_wav must be provided.")
        ir_waveform, sr_ir = ir_wav, ir_wav_sr
        if ir_waveform.dim() != 2:
            raise ValueError("ir_wav must be a 2D tensor of shape (n_channels, n_samples).")

    # Ensure the sampling rates match
    if sr_audio != sr_ir:
        ir_waveform = torchaudio.functional.resample(ir_waveform, sr_ir, sr_audio)

    # Convert multi-channel audio to mono by averaging channels.
    # For audio_waveform: shape (batch_size, n_channels, n_samples)
    if audio_waveform.shape[1] > 1:
        # print("Input audio is multi-channel. Converting to mono by averaging channels.")
        audio_waveform = audio_waveform.mean(dim=1, keepdim=True)
    # For ir_waveform: shape (n_channels, n_samples)
    if ir_waveform.shape[0] > 1:
        # print("Impulse response is multi-channel. Converting to mono by averaging channels.")
        ir_waveform = ir_waveform.mean(dim=0, keepdim=True)
    
    # Remove the channel dimension for further processing.
    # audio_batch: shape (batch_size, n_samples)
    audio_batch = audio_waveform
    # Use the impulse response as a 1D tensor (assuming a single IR is used)
    ir = ir_waveform.squeeze(0).float()

    # Ensure signals are in float32
    audio_batch = audio_batch.float()

    # Determine the convolution length (assuming all audio samples have the same length)
    batch_size, audio_length = audio_batch.shape
    ir_length = ir.numel()
    n = audio_length + ir_length - 1
    # Compute next power-of-two for efficient FFT computation
    n_fft = 2 ** ((n - 1).bit_length())

    # Compute FFT of the audio batch along the last dimension
    A = torch.fft.rfft(audio_batch, n=n_fft, dim=-1)  # shape: (batch_size, n_fft//2 + 1)
    # Compute FFT of the impulse response
    B = torch.fft.rfft(ir, n=n_fft)  # shape: (n_fft//2 + 1)

    # Multiply in frequency domain (broadcasting IR across the batch)
    C = A * B
    # Compute the inverse FFT to get the convolved signal and trim to expected length
    convolved = torch.fft.irfft(C, n=n_fft, dim=-1)[:, :n]  # shape: (batch_size, n)

    # Truncate the convolved signal to match the original audio length if necessary.
    if audio_length < convolved.shape[1]:
        convolved = convolved[:, :audio_length]
    elif audio_length > convolved.shape[1]:
        raise ValueError("Convolved signal is shorter than the audio signal. Does this happen?")

    # Save the output if an output path is provided (only supported for batch size 1)
    if output_path is not None:
        if batch_size != 1:
            raise ValueError("Saving output audio is only supported for a batch size of 1.")
        # torchaudio expects shape (channels, n_samples)
        convolved_to_save = convolved[0].unsqueeze(0)
        torchaudio.save(output_path, convolved_to_save, sr_audio)
        print(f"Convolved audio saved as '{output_path}'.")

    # Return the original mono audio (batch_size, n_samples) and the convolved audio
    return audio_batch.unsqueeze(1), convolved.unsqueeze(1), sr_audio
