import argparse, webbrowser
from .scanner import RepositoryScanner
from .exporters import export_all

def main():
    p=argparse.ArgumentParser()
    p.add_argument("path",nargs="?",default=".")
    p.add_argument("--ui",action="store_true")
    args=p.parse_args()

    if args.ui:
        from linuxcmdscan.ui.app_window import launch_ui
        launch_ui(); return

    res=RepositoryScanner().scan(args.path)
    export_all(res)
    webbrowser.open("reports/linuxcmdscan_report.html")