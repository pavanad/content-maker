# -*- coding: utf-8 -*-

from colorama import Fore
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def publish_content(content: dict):
    print(f"\n> {Fore.CYAN}[publish-content]{Fore.RESET} Starting...")

    # set path of the client secret
    client_secret_file = "src/credentials/client_secret.json"
    GoogleAuth.DEFAULT_SETTINGS["client_config_file"] = client_secret_file

    auth = GoogleAuth()
    drive = GoogleDrive(auth)

    # get filename
    search_term = content["search_term"].lower().replace(" ", "-")
    filename = f"data/{search_term}.pdf"

    # upload file to google drive
    print(f"\n> {Fore.CYAN}[publish-content]{Fore.RESET} Upload file to google drive")

    # id of the folder Contet Maker in my google drive
    file_drive = drive.CreateFile(
        {
            "title": "spiderman.pdf",
            "parents": [
                {"kind": "drive#fileLink", "id": "1q7bFqbvu8jzMeR3SJIDjniPfbzkG7N3R"}
            ],
        }
    )
    file_drive.SetContentFile(filename)
    file_drive.Upload()

    # get share link
    permission = file_drive.InsertPermission(
        {"type": "anyone", "value": "anyone", "role": "reader"}
    )

    print(f"\n> {Fore.CYAN}[publish-content]{Fore.RESET} Share link: {Fore.GREEN}{file_drive['alternateLink']}{Fore.RESET}")


