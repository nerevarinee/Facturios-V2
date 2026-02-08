from facturis.app import run_app
from facturis.core.lisence_check import check_license_file, show_license_error_and_exit

if __name__ == "__main__":
    # Check license before running app
    if not check_license_file():
        show_license_error_and_exit()

    run_app()