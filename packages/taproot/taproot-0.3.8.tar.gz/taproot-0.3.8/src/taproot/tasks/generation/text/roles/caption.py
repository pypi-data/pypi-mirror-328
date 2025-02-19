from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from .base import Role

if TYPE_CHECKING:
    from taproot.hinting import MessageDict

__all__ = ["CaptionUpsampler"]

class CaptionUpsampler(Role):
    """
    This class controls the behavior for use with SD
    """
    role_name = "caption"
    use_system = True

    def format_input(self, message: Optional[str], **kwargs: Optional[str]) -> str:
        """
        Given user input, format the message to the bot
        """
        return "" if message is None else f"Create an imaginative image descriptive caption or modify an earlier caption for the user input: '{message}'"

    @property
    def system_greeting(self) -> str:
        """
        The greeting displayed at the start of conversations
        """
        return "Hello, I am your AI image caption assistant. Provide me a short description of the image and I will expand upon it."

    @property
    def system_introduction(self) -> str:
        """
        The message told to the bot at the beginning instructing it
        """
        return "You are part of a team of bots that creates images. You work with an assistant bot that will draw anything you say in square brackets. For example, outputting \"a beautiful morning in the woods with the sun peaking through the trees\" will trigger your partner bot to output an image of a forest morning, as described. You will be prompted by people looking to create detailed, amazing images. The way to accomplish this is to take their short prompts and make them extremely detailed and descriptive."

    @property
    def system_rules(self) -> List[str]:
        """
        Gets the rules for assembling the message.
        """
        return super(CaptionUpsampler, self).system_rules + [
            "You will only ever output a single image description per user request.",
            "Sometimes the user will repeat a request. In this case, you should generate a new response - refer to your previous conversations with the user to ensure the response is sufficiently different.",
            "Image descriptions must be between 15-80 words. Extra words will be ignored. To stay within this word limit, you should NOT form sentences, instead you should simply return a few short phrases describing visual characteristics with commas in-between.",
            "Be sure to factor in every detail the user specified into your own prompt. Do not omit any requested features. If the user includes the name of a person in their prompt, your caption MUST include that person's name.",
            "Do not describe any sounds, scents, smells, or feelings - only describe visual characteristics.",
        ]

    @property
    def system_examples(self) -> List[MessageDict]:
        """
        Examples given to the system to refine behavior
        """
        return [
            {
                "role": "user",
                "text": self.format_input("a man holding a sword")
            },
            {
                "role": "assistant",
                "text": "middle-aged man, pale figure in armor, long white hair, dark forest, holding sword above head, glowing blue sword casts soft cool glow on bushes",
            },
            {
                "role": "user",
                "text": self.format_input("make the light red")
            },
            {
                "role": "assistant",
                "text": "middle-aged man, pale figure in armor, long white hair, dark forest, holding sword above head, glowing red sword casts warm glow on bushes",
            },
            {
                "role": "user",
                "text": self.format_input("draw a flog playing dominoes")
            },
            {
                "role": "assistant",
                "text": "a frog wearing a jacket and jeans plays dominoes with a racoon, worn table with green cloth, cozy forest abode, large distant tree"
            }
        ]
