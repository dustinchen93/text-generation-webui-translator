Code and test in Ubuntu 22.0.4.

Preparation:
1. Execute the command `pip install -r requirements.txt` to install the required dependencies.

Usage:
1. Obtain a multilngual model (e.g., OpenBuddy Vigogne (French), Chinese LLaMA / Alpaca, ).
2. Run the text-generation-webui with the `--extension api` argument.
3. Modify the "request" function in send_payload.py according to your requirements.(Make sure to change 'custom_stopping_strings' and 'prompt' to match your model's specifications.)
4. Run the program and wait. For example, I translated the book "https://www.gutenberg.org/ebooks/55805" in Chinese, and it took me approximately 5 hours using two decent CPUs and OpenBuddy GGML.
5. If you wish to translate additional HTML tags not included in ['p','div','strong','span','i','em'], add them to the translator.py file.
6. Modify your desired prompt in the translate function within the translator.py file.

Notes:
1. The translation of a large text wrapped in tags produces a better result.

TODO:
1. Rewrite as text-generation-webui extension
2. Improving translation speed(there would be some method to reduce waiting time like stream technique)
3. Enhancing translation quality
