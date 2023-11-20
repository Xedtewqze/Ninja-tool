
import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """
   _______  .__            __         ________  ________          _________
   \      \ |__| ____     |__|____    \______ \ \______ \   ____ /   _____/
   /   |   \|  |/    \    |  \__  \    |    |  \ |    |  \ /  _ \\_____  \ 
  /    |    \  |   |  \   |  |/ __ \_  |    `   \|    `   (  <_> )        \
  \____|__  /__|___|  /\__|  (____  / /_______  /_______  /\____/_______  /
          \/        \/\______|    \/          \/        \/              \/ 
  """

   os.system(f'echo "{show_logo}" | lolcat')    
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├───┐")
