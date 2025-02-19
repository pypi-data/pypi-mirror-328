import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

EMBED_DIM = 32
LSTM_UNITS = 64
BATCH_SIZE = 16
EPOCHS = 50
BEAM_WIDTH = 3
MODEL_PATH = os.path.join(PARENT_DIR, "models", "pretrained", "khmer_transliterator.keras")
ASSETS_PATH = os.path.join(PARENT_DIR, "data", "processed", "khmer_transliteration_assets.pkl")
