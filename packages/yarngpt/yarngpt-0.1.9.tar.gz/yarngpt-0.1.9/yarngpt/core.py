import os
import torch
import requests
from transformers import AutoModelForCausalLM
from audiotokenizer import AudioTokenizerV2 as AudioTokenizer
from tqdm import tqdm

#define model storage directory
MODEL_DIR = os.path.expanduser("~/.yarngpt/models")
os.makedirs(MODEL_DIR, exist_ok=True)

#define file paths
CONFIG_PATH = os.path.join(MODEL_DIR, "wavtokenizer_mediumdata_frame75_3s_nq1_code4096_dim512_kmeans200_attn.yaml")
MODEL_PATH = os.path.join(MODEL_DIR, "wavtokenizer_large_speech_320_24k.ckpt")

#urls from Hugging Face
CONFIG_URL = "https://huggingface.co/novateur/WavTokenizer-medium-speech-75token/resolve/main/wavtokenizer_mediumdata_frame75_3s_nq1_code4096_dim512_kmeans200_attn.yaml"
MODEL_URL = "https://huggingface.co/novateur/WavTokenizer-large-speech-75token/resolve/main/wavtokenizer_large_speech_320_24k.ckpt"

def download_file(url, dest_path):
    """Downloads a file with a progress bar if it doesn't already exist."""
    if os.path.exists(dest_path):
        print(f"{dest_path} already exists. Skipping download.")
        return

    print(f"Downloading {url} to {dest_path}...")

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(dest_path, "wb") as f, tqdm(
        total=total_size, unit="B", unit_scale=True, desc=os.path.basename(dest_path)
    ) as progress_bar:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            progress_bar.update(len(chunk))

    print("Download complete.")

#ensure model files are available
download_file(CONFIG_URL, CONFIG_PATH)
download_file(MODEL_URL, MODEL_PATH)

#list of available speakers by language
ENGLISH_SPEAKERS = [
    "idera", "chinenye", "jude", "emma", "umar", "joke", 
    "zainab", "osagie", "remi", "tayo"
]

YORUBA_SPEAKERS = [
    "yoruba_male2", "yoruba_female2", "yoruba_female1"
]

IGBO_SPEAKERS = [
    "igbo_female2", "igbo_male2", "igbo_female1"
]

HAUSA_SPEAKERS = [
    "hausa_female1", "hausa_female2", "hausa_male2", "hausa_male1"
]

# Mapping friendly names to model parameters
SPEAKER_MAPPING = {
    #english voices keep their names
    "idera": "idera",
    "chinenye": "chinenye",
    "jude": "jude",
    "emma": "emma",
    "umar": "umar",
    "joke": "joke",
    "zainab": "zainab",
    "osagie": "osagie",
    "remi": "remi",
    "tayo": "tayo",
    
    #yoruba voices with friendly names
    "abayomi": "yoruba_male2",
    "aisha": "yoruba_female2",
    "folake": "yoruba_female1",
    
    #igbo voices with friendly names
    "chioma": "igbo_female2",
    "obinna": "igbo_male2",
    "adanna": "igbo_female1",
    
    #hausa voices with friendly names
    "amina": "hausa_female1",
    "fatima": "hausa_female2",
    "ibrahim": "hausa_male2",
    "yusuf": "hausa_male1"
}

#combined list for validation
AVAILABLE_SPEAKERS = ENGLISH_SPEAKERS + YORUBA_SPEAKERS + IGBO_SPEAKERS + HAUSA_SPEAKERS

def load_model_and_tokenizer():
    """Loads the YarnGPT model and tokenizer."""
    # hf_path = "saheedniyi/YarnGPT"
    hf_path = "saheedniyi/YarnGPT2"


    #initialize tokenizer
    audio_tokenizer = AudioTokenizer(hf_path, MODEL_PATH, CONFIG_PATH)

    #load model using Hugging Face's caching system
    model = AutoModelForCausalLM.from_pretrained(hf_path, torch_dtype="auto")
    model = model.to(audio_tokenizer.device)

    return model, audio_tokenizer

def generate_speech(text, speaker="idera", language="english", temperature=0.1, repetition_penalty=1.1, max_length=4000):
    """Generate speech audio from input text using the selected speaker.
    
    This function converts text to speech using YarnGPT's text-to-speech model with
    Nigerian-accented speech. It supports multiple languages and preset voices, allowing 
    customization of generation parameters.

    Args:
        text (str): The input text to convert to speech.
        speaker (str, optional): The voice to use for speech generation.
            Available voices by language:
            - English: idera, chinenye, jude, emma, umar, joke, zainab, osagie, remi, tayo
            - Yoruba: abayomi, aisha, folake
            - Igbo: chioma, obinna, adanna
            - Hausa: amina, fatima, ibrahim, yusuf
            Defaults to "idera".
        language (str, optional): The language for speech generation.
            Must be one of: english, yoruba, igbo, hausa
            Defaults to "english".
        temperature (float, optional): Controls randomness in generation.
            Higher values (e.g., 0.8) make output more random,
            lower values (e.g., 0.1) make it more deterministic.
            Defaults to 0.1.
        repetition_penalty (float, optional): Penalizes repetition in generated speech.
            Values > 1.0 reduce repetition. Defaults to 1.1.
        max_length (int, optional): Maximum length of generated sequence.
            Longer text needs higher values. Defaults to 4000.

    Returns:
        torch.Tensor: A 2D tensor containing the generated audio waveform
            with shape (1, num_samples) and sample rate of 24kHz.

    Raises:
        ValueError: If speaker is not one of the available preset voices.
        ValueError: If language is not one of the supported languages.
        
    Example:
        >>> from yarngpt import generate_speech
        >>> import torchaudio
        >>> 
        >>> # Generate English speech with default settings
        >>> audio = generate_speech("Hello, how are you?", language="english")
        >>> 
        >>> # Save the generated audio
        >>> torchaudio.save("output.wav", audio, sample_rate=24000)
        >>> 
        >>> # Use a Yoruba voice with Yoruba text
        >>> audio = generate_speech(
        ...     "Bawo ni?",
        ...     speaker="abayomi",
        ...     language="yoruba",
        ...     temperature=0.2,
        ...     repetition_penalty=1.2
        ... )
    """
    #convert speaker name and language to lowercase
    speaker = speaker.lower()
    language = language.lower()
    
    #validate language
    supported_languages = ["english", "yoruba", "igbo", "hausa"]
    if language not in supported_languages:
        raise ValueError(f"Language must be one of: {', '.join(supported_languages)}")
    
    #get model parameter for speaker
    model_speaker = SPEAKER_MAPPING.get(speaker, speaker)
    
    if model_speaker not in AVAILABLE_SPEAKERS:
        friendly_names = sorted(SPEAKER_MAPPING.keys())  #sort names alphabetically
        raise ValueError(f"Speaker must be one of: {', '.join(friendly_names)}")
    
    model, audio_tokenizer = load_model_and_tokenizer()
    prompt = audio_tokenizer.create_prompt(text, language, model_speaker)
    input_ids = audio_tokenizer.tokenize_prompt(prompt)
    
    # Create attention mask (1 for real tokens, 0 for padding)
    attention_mask = torch.ones_like(input_ids)
    
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        do_sample=True,  # Enable sampling for temperature to take effect
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        max_length=max_length,
        pad_token_id=model.config.eos_token_id,
        eos_token_id=model.config.eos_token_id
    )
    
    codes = audio_tokenizer.get_codes(output)
    audio = audio_tokenizer.get_audio(codes)
    
    return audio
