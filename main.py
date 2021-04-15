from FileScanner import FileScanner
import hashlib
import requests
import os


def format_response(file, response):
    file_name = os.path.basename(open(file).name)
    print(f"filename: {file_name}")

    overall_status = response['scan_results']['scan_all_result_a'] if response[
        'scan_results']['scan_all_result_a'] == "Infected" else "Clean"
    print(f"overall_status: {overall_status}")

    scan_details = response["scan_results"]["scan_details"]
    for k in scan_details:
        print(f"engine: {k}")

        threat_found = scan_details[k]['threat_found'] if scan_details[k]['threat_found'] else "Clean"
        print(f"threat_found: {threat_found}")

        print(f"scan_result_i: {scan_details[k]['scan_result_i']}")
        print(f"def_time: {scan_details[k]['def_time']}")


if __name__ == "__main__":
    print("Welcome to the Opswat File Vulnerability Scanner")
    print("Available commands are: ")
    print("1. exit : End the program")
    print("2. upload_file <filepath> : Upload a file to scan\n")

    while True:
        command = input(">> ")
        if command == "exit":
            quit()
        elif len(command.split()) != 2 or command.split()[0] != "upload_file":
            print("Invalid command")
        else:
            scanner = FileScanner()
            args = command.split()
            try:
                # Hash file using SHA-256
                file_hash = scanner.hash(args[1])
                # Check if file has already been scanned
                response = scanner.hash_lookup(file_hash)
                if not response:
                    # Scan file if hash not found
                    response = scanner.scan(args[1])

                format_response(args[1], response)
            except Exception as e:
                print(e)
