class Config:
    @staticmethod
    def open_ai_api_key():
        from dotenv import load_dotenv
        import os
        load_dotenv(override=True)
        return os.getenv('OPENAI_API_KEY')

    @staticmethod
    def anthropic_api_key():
        from dotenv import load_dotenv
        import os
        load_dotenv(override=True)
        return os.getenv('ANTHROPIC_API_KEY')

    @staticmethod
    def huggingface_api_key():
        from dotenv import load_dotenv
        import os
        load_dotenv(override=True)
        return os.getenv('HF_TOKEN')

    @staticmethod
    def phi_model_url():
        from dotenv import load_dotenv
        import os
        load_dotenv(override=True)
        return os.getenv('PHI_MODEL_URL')

    @staticmethod
    def advisors_config():
        return [
            {"type": "openai", "enabled": True},
            {"type": "anthropic", "enabled": True},
            {"type": "microsoft", "enabled": False}
        ]