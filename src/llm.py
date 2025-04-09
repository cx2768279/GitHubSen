import openai
import os
class LLM:
    def __init__(self):
        token = os.environ.get('deepseek_key')
        self.api_key = token
        openai.api_key = self.api_key
        openai.api_base = "https://api.deepseek.ai/v1"
        openai.stream=False
        openai.model='deepseek-reasoner'

    def summarize_isssues_prs(self, issues, pull_requests):
        prompt = (
            "Summarize the following GitHub issues and pull requests in a formal report format:\n\n"
            "## Issues\n"
        )

        for issue in issues:
            prompt += f"- {issue['title']} #{issue['number']}: {issue['body']}\n"
        prompt += "\n## Pull Requests\n"

        for pr in pull_requests:
            prompt += f"- {pr['title']} #{pr['number']}: {pr['body']}\n"

        response = openai.Completion.create(
            prompt=prompt,
            max_tokens=500,
        )

        return response.choices[0].text.strip()