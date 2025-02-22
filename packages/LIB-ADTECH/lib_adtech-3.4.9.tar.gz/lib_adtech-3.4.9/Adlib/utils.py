import sys
import time
import psutil
import chardet
import asyncio
import subprocess
import pandas as pd
from selenium.webdriver.remote.webelement import WebElement


meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

def detectEncoding(filePath, sample_size=10000):
    with open(filePath, 'rb') as f:
        raw_data = f.read(sample_size)
    result = chardet.detect(raw_data)
    return result['encoding']


async def aguardarTempo(intervalo: int = 900):

    async def countdown(intervalo: int):
        """
        Contagem assíncrona que mostra os minutos e segundos restantes
        
        Args:
            intervalo (int): A duração da contagem (em segundos).
        """
        tempo = 0
        while tempo < intervalo:
            for suffix in ["   ", ".  ", ".. ", "..."]:
                remaining = intervalo - tempo
                minutos, segundos = divmod(remaining, 60)
                print(f"Próxima checagem em {minutos:02}:{segundos:02} - Aguardando{suffix}", end="\r")
                await asyncio.sleep(1)
                tempo += 1
        print(f"                                                                           ", end="\r")

    await countdown(intervalo)




def convertHTMLTable2Dataframe(tableElement: WebElement) -> pd.DataFrame:
    """
    Converte um elemento <table> (Selenium WebElement) em um DataFrame

    Args:
        tableElemento (WebElement): O elemento do Selenium que representa a tabela em HTML <table>

    Returns:
        pd.DataFrame: A DataFrame containing the table data.
    """
    headers = [header.text for header in tableElement.find_elements("xpath", './/th')]
    
    rows = []
    for row in tableElement.find_elements("xpath", './/tr'):
        cells = row.find_elements("xpath", './/td')
        rows.append([cell.text for cell in cells])
    
    rows = [row for row in rows if row]
    
    if headers:
        return pd.DataFrame(rows, columns=headers)
    else:
        return pd.DataFrame(rows)


def executarPythonScripts(workingDirs: list[str], scripts: list[str], tabNames: list[str], delay: int = 10):
    def getTerminalsCount():
        return sum(1 for p in psutil.process_iter(attrs=['name']) if p.info['name'] == "powershell.exe")


    python = sys.executable
        
    subprocess.run(["wt"])
    time.sleep(1)  # Small delay to ensure the new window is created before opening tabs

    numWindows = getTerminalsCount()
    base_command = ["wt", "--window", f"{numWindows + 2}", "new-tab", "--title"]

    for workingDir, script, tabName in zip(workingDirs, scripts, tabNames):
        subprocess.run(base_command + [tabName] + ["cmd", "/k"] + ["cd", "/d", workingDir, "&&", python, script])
        time.sleep(delay)


# executarPythonScripts([], [], [])

if __name__=="__main__":
    scripts = ["teste2.py", "teste3.py"]

    workingDirs = [r"C:\Users\dannilo.costa\Desktop\Repos AD\Adlib", r"C:\Users\dannilo.costa\Desktop\Repos AD\Adlib"]

    executarPythonScripts(workingDirs, scripts, ["teste2", "teste3"])