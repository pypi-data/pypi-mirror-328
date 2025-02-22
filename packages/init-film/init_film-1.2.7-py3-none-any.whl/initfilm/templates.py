import os, sysconfig
import initfilm.config



python_sitepackages = sysconfig.get_path("purelib")
template_path_config = initfilm.config.get("templates", "path")

if template_path_config == "python":
    template_path = f"{python_sitepackages}/initfilm/templates"
    os.makedirs(template_path, exist_ok=True)
else:
    template_path = template_path_config
    os.makedirs(template_path, exist_ok=True)



def list(relative_path:str):
    """
    Lists all template files in desired folder.
    Args:  
        relative_path (str): Path to template files, relative to `template_path` (ex. "ASSETS/LOGOS").
    """

    path = os.path.join(template_path, relative_path)
    files = [f for f in os.listdir(path)]

    for id, template in enumerate(files, start=1):
        print(f"{id}) {template}")


def main(relative_path:str, destination_path:str):
    """
    Lists all template files in desired folder, let's user select files & copies files to destination.
    Args:
        relative_path (str): Path to template files, relative to `template_path` (ex. "ASSETS/LOGOS").
        destination_path (str): Full path to copy location.
    """

    list(relative_path)