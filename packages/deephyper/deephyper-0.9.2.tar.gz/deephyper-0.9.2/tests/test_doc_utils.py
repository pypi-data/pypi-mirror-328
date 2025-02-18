import re


text0 = """# .. dropdown::
from deephyper.analysis._matplotlib import update_matplotlib_rc
from deephyper.hpo import HpProblem
from deephyper.hpo import ExperimentalDesignSearch
import matplotlib.pyplot as plt

update_matplotlib_rc()
"""

text1 = """# .. dropdown:: some title
from deephyper.analysis._matplotlib import update_matplotlib_rc
from deephyper.hpo import HpProblem
from deephyper.hpo import ExperimentalDesignSearch
import matplotlib.pyplot as plt

update_matplotlib_rc()
"""

text2 = """# .. dropdown:: some title
#     :key0:
#     :key1: value1
from deephyper.analysis._matplotlib import update_matplotlib_rc
from deephyper.hpo import HpProblem
from deephyper.hpo import ExperimentalDesignSearch
import matplotlib.pyplot as plt

update_matplotlib_rc()
"""

text3 = """from deephyper.analysis._matplotlib import update_matplotlib_rc
from deephyper.hpo import HpProblem
from deephyper.hpo import ExperimentalDesignSearch
import matplotlib.pyplot as plt

update_matplotlib_rc()
"""

def parse_dropdown(rst_text):
    pattern = re.compile(
        r"# \.\. dropdown::(.*?)\n"  # Match the title
        r"(?:    :(\w+):(?: (.*?))?\n)*",  # Match optional keys and values
        re.DOTALL
    )

    match = pattern.search(rst_text)
    if match:

        title = match.group(1).strip()

        # Extract options as key-value pairs
        options = re.findall(r"    :(\w+):(?: (.*))?", rst_text)
        options = dict(options)


        # Remove matched lines from rst_text

        cleaned_rst_text = pattern.sub("", rst_text)
        for value in options:
            i = cleaned_rst_text.index("\n")
            cleaned_rst_text = cleaned_rst_text[i+1:]

        return {"title": title, "options": options}, cleaned_rst_text

    return None, rst_text


results, cleaned_text = parse_dropdown(text0)
print(results)
print(cleaned_text)

results, cleaned_text = parse_dropdown(text1)
print(results)
print(cleaned_text)

results, cleaned_text = parse_dropdown(text2)
print(results)
print(cleaned_text)

results, cleaned_text = parse_dropdown(text3)
print(results)
print(cleaned_text)