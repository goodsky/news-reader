import random
from semantic_kernel.skill_definition import sk_function


class GenerateNumberSkill:
    """
    Description: Generates numbers
    """

    @sk_function(description="Generates a random number between 1 - <input>", name="Random")
    def random_number(self, input: str) -> str:
        """
        Description: Generates a random number between 1 - <input>
        """
        try:
            return str(random.randint(1, int(input)))
        except ValueError as e:
            print(f"Invalid upper bound for random value: {input}")
            raise e
