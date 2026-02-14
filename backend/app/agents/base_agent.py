class BaseAgent:
    def __init__(self, role: str):
        self.role = role

    def get_system_prompt(self):
        return f"You are an expert {self.role} engineer."