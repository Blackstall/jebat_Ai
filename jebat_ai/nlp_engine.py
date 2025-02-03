from transformers import pipeline

class NLPEngine:
    def __init__(self, model_type="gpt-neo"):
        """Initializes GPT-Neo with dynamic response length."""
        if model_type == "gpt-neo":
            self.model = pipeline(
                "text-generation",
                model="EleutherAI/gpt-neo-125M",
                truncation=True,
                pad_token_id=50256
            )
        else:
            raise ValueError("Unsupported model type. Use 'gpt-neo'.")

    def get_dynamic_length(self, input_text):
        """Dynamically adjusts response length based on input complexity."""
        word_count = len(input_text.split())

        if word_count <= 5:
            return 30  # Short response
        elif word_count <= 15:
            return 80  # Medium response
        else:
            return 200  # Long response

    def generate_response(self, input_text):
        """Generates AI response with dynamically adjusted length."""
        max_length = self.get_dynamic_length(input_text)

        response = self.model(
            input_text,
            max_length=max_length,  # 🔥 Dynamically set length
            temperature=0.8,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            repetition_penalty=1.2
        )
        return response[0]['generated_text'].strip()


