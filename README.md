This repository is based on research that suggests that education can be improved by a carefully designed AI system.
The AI must be able to nudge the student forward, but not give the answer. For simplicity's sake, I will be using
existing LLMs with prompt engineering instead of building a model from scratch or fine tuning one.

Please note, this program uses anthropic AI, rather than openAI, due to moral concerns with openai's "nonprofit" goals.
if ANTHROPIC_API_KEY is defined in your environment, you won't need to type it in every time.

The teacher will look at what the student is trying to learn, and try to find an appropriate lesson in the 'lessons' directory. These lessons are designed by humans, but presented as examples to the AI. Since all AIs are lazy when it comes to complex tasks, it will rely heavily on the example, but still be able to follow any tangents the student wants to go down.


In order to install you'll need:
anthropic
