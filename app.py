"""A small Tkinter app for managers to review equipment requests."""

import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk


def load_requests():
    """Read the sample requests from the JSON file beside this script."""
    data_file = Path(__file__).with_name("requests.json")
    with data_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    # Create the main application window.
    root = tk.Tk()
    root.title("Equipment Requests")
    root.geometry("850x400")
    root.minsize(650, 280)

    # Add a heading so the purpose of the list is clear.
    heading = ttk.Label(root, text="Equipment Requests", font=("TkDefaultFont", 16, "bold"))
    heading.pack(anchor="w", padx=16, pady=(16, 8))

    # A Treeview displays each request as a row with clearly labeled columns.
    columns = ("request_id", "employee", "equipment", "priority", "status")
    requests_table = ttk.Treeview(root, columns=columns, show="headings")
    requests_table.heading("request_id", text="Request ID")
    requests_table.heading("employee", text="Employee")
    requests_table.heading("equipment", text="Equipment Item")
    requests_table.heading("priority", text="Priority")
    requests_table.heading("status", text="Status")

    requests_table.column("request_id", width=105, anchor="center")
    requests_table.column("employee", width=160)
    requests_table.column("equipment", width=250)
    requests_table.column("priority", width=110, anchor="center")
    requests_table.column("status", width=100, anchor="center")

    # The scrollbar lets the manager see every row in a smaller window.
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=requests_table.yview)
    requests_table.configure(yscrollcommand=scrollbar.set)
    requests_table.pack(side="left", fill="both", expand=True, padx=(16, 0), pady=(0, 16))
    scrollbar.pack(side="right", fill="y", padx=(0, 16), pady=(0, 16))

    try:
        # Add each request from the JSON file as one row in the table.
        for request in load_requests():
            requests_table.insert(
                "",
                "end",
                values=(
                    request["request_id"],
                    request["employee_name"],
                    request["equipment_item"],
                    request["priority"],
                    request["status"],
                ),
            )
    except (OSError, json.JSONDecodeError, KeyError) as error:
        # Show a helpful message if the data file is missing or malformed.
        messagebox.showerror("Could not load requests", f"Please check requests.json.\n\n{error}")
        root.destroy()
        return

    # Keep the window open and responsive until the manager closes it.
    root.mainloop()


if __name__ == "__main__":
    main()
