import sys
import subprocess
from colorama import Fore, Style
# Will "from g4f.client import Client" if an error occurs


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1:]

        try:
            result = subprocess.Popen(
                arg, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True
            )
            stdout, stderr = result.communicate()  # Non-blocking
            exit_code = result.returncode

        except Exception:
            print(f"Check the spelling: {' '.join(arg)}")
            return

        # Print command outputs
        print(Fore.BLUE + "Output:" + Style.RESET_ALL, stdout.strip() if stdout.strip() else "None")
        print(Fore.GREEN + "Exit Code:" + Style.RESET_ALL, exit_code)
        print(Fore.RED + "Error:" + Style.RESET_ALL, stderr.strip() if stderr.strip() else "None")

        # If the command failed, ask GPT for help
        if exit_code != 0:
            from g4f.client import Client

            print(Fore.RED + "Whoops! Looks like something went wrong with that command. Asking AI..." + Style.RESET_ALL)
            message = f"""
Find the error and mention it with only a few keywords.
Suggest a full corrected command line adding the word "macun" at the start of the line if it's obvious.
If its not, suggest a possible fix or what might happened with a few keywords. Avoid using Markdown or any special formatting in your response.
$ {" ".join(arg)}
{stderr.strip()}
[Command exited with {exit_code}]
            """

            gpt_client = Client()
            response = gpt_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": message}],
                web_search=False
            )

            print(response.choices[0].message.content)

    else:
        print("No input provided. To use macun: macun <command line>")

if __name__ == "__main__":
    main()
