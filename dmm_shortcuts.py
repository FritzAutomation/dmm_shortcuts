import os
import shutil


def create_custom_file(directory, source_filepath):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    filename = os.path.basename(source_filepath)
    destination_filepath = os.path.join(directory, filename)
    shutil.copy(source_filepath, destination_filepath)
    print(f"File '{filename}' created in '{directory}'.")


if __name__ == "__main__":
    # Define a fancy header
    header = """
    ============================================
    |                                           |
    |      Welcome to the DMM Shortcut Tool     |
    |                                           |
    ============================================
    """
    # Print the header
    print(header)

    # Get the current user's username
    username = os.getenv("USERNAME") or os.environ["USERNAME"]
    user_directory = os.path.join(
        "C:\\Users", username, "AppData\\Roaming\\DMM\\Favorites v16\\Remote"
    )

    # Define plant options and corresponding file paths
    plant_files = {
        "benson": [
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Benson_Prod.4DLink",
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Benson_Test.4DLink",
        ],
        "burlington": [
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Burlington_Prod.4DLink",
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Burlington_Test.4DLink",
        ],
        "fargo": [
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Fargo_Prod.4DLink",
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Fargo_Test.4DLink",
        ],
        "wichita": [
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Wichita_Prod.4DLink",
            r"\\cnh1\bur\BUR_Kitting\FritzjunkerDeploy\DMM_Shortcuts\Wichita_Test.4DLink",
        ],
    }

    # Display options to the user
    print(f"Logged in as: {username}")
    print("\nAvailable plants:")
    for key in plant_files.keys():
        print(f" - {key.capitalize()}")

    # Prompt the user for a selection
    selection = input("\nEnter the name of your choice: ").strip().lower()

    if selection in plant_files:
        source_filepaths = plant_files[selection]
        if os.path.exists(user_directory):
            for source_filepath in source_filepaths:
                create_custom_file(user_directory, source_filepath)
        else:
            print(f"The directory '{user_directory}' does not exist.")
    else:
        print(
            "Invalid selection. Please run the script again and select a valid plant."
        )
