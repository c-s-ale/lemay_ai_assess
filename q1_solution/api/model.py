from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class ENtoFRModel:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
        self.translation_pipeline = pipeline("translation_en_to_fr", model=self.model, tokenizer=self.tokenizer)
        print('Model loaded.')
    
    def translate_en_to_fr(self, text: str) -> str:
        return self.translation_pipeline(text)[0]