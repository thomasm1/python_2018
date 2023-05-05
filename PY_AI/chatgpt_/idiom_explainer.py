class AgentTom(Agent, BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._explainer = Explainer()

    def act(self, observation, reward, done):
        action = super().act(observation, reward, done)
        if action == 0:
            self._explainer.explain(observation)
        return action

    def reset(self):
        super().reset()
        self._explainer.reset()

# Path: explainer.py
# Path: model.py
  

# Path: agent.py
class Agent:
    """Base class for all agents."""
    """If you want you agent to be tool-based1, AgentTom(Agent, BaseAgent)."""

    """if you want agent to be chatty and personality-based, use class AgentTom(ChatAgent, BaseAgent)"""

    def is_verbose_logging_enabled(self) -> bool:
        return True

    def get_tools(self) -> List[Tool]:
        return [
            # SearchTool(self.client),
            # MyTool(self.client),
            # GenerateImageTool(self.client),
        ]
    
    def get_personality(self) -> str:
        """return string that completes sentence "The Agent acts like ..." """
        return """
        a kind, helpful French teacher that responds to every situation with "C'est la vie!". Also, explaining the definitions and meanings of 
        words. Speaks in English and explains the french words and phrases. Then provides a note of encouragement about learning French."""
