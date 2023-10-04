from django.shortcuts import render, redirect
import os
import subprocess
import time
import threading
import pandas as pd
import threading
import time
import subprocess
import os
import pandas as pd


class PingApp:
    def __init__(self, ip_addresses):
        self.pings = {ip: "Initializing..." for ip in ip_addresses}

    def update_status(self, ip, status):
        if ip in self.pings:
            self.pings[ip] = status

csv_file_lock = threading.Lock()
file_lock = threading.Lock()

def ping_worker(ip_address, app):
    while True:
        try:
            with csv_file_lock:
                data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
                data = pd.read_csv(data_file_path)

                result = subprocess.run(["ping", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
                if result.returncode == 0:
                    app.update_status(ip_address, "UP")
                    data.loc[data['ip_address'] == ip_address, 'status'] = 'UP'
                else:
                    app.update_status(ip_address, "Down")
                    data.loc[data['ip_address'] == ip_address, 'status'] = 'Down'

                data.to_csv(data_file_path, index=False)
        except subprocess.TimeoutExpired:
            app.update_status(ip_address, "Timeout")
        except Exception as e:
            app.update_status(ip_address, f"Error: {str(e)}")

        time.sleep(1)


def reg(request):
    data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
    data = pd.read_csv(data_file_path)
    ip_addresses = list(data.ip_address)
    app = PingApp(ip_addresses)

    ping_threads = []
    for ip_address in ip_addresses:
        data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
        data=pd.read_csv(data_file_path)
        thread = threading.Thread(target=ping_worker, args=(ip_address, app))
        thread.start()
        ping_threads.append(thread)

    return render(request, 'reg.html', {'data': data})

###########################################################################################################################################

def reg1(request):
    if (request.method == "POST"):
        data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
        data=pd.read_csv(data_file_path)
        try:
            # Prompt the user for the name they want to update
            name_to_update = request.POST.get("name")

            # Define the new data as a DataFrame with a single row
            new_data = pd.DataFrame({"name": [name_to_update], "ip_address": [request.POST.get("ip")], "link_for_log": ["/data"], "email_id": [request.POST.get("email")], "status" : ["Down"]})

            # Acquire the file lock to prevent concurrent file access
            with csv_file_lock:
                data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
                data=pd.read_csv(data_file_path)

                # Check if the name already exists in 'data' and update email and IP if it does
                if name_to_update in data["name"].values:
                    data.loc[data["name"] == name_to_update, ["ip_address", "email_id"]] = new_data[["ip_address", "email_id"]].values
                else:
                    # If the name doesn't exist, concatenate the new data to the dataframe
                    data = pd.concat([data, new_data], ignore_index=True)

                # Save the updated data to the CSV file
                data.to_csv(data_file_path, index=False)
                print(data)
            return redirect('reg')
        
        except Exception as e:
            # Handle exceptions here (e.g., log the error)
            print(f"An error occurred: {str(e)}")
        # return redirect(reg)

# Print the updated 'data' DataFrame

    return render (request,'reg1.html')


def reg2(request):
    return render (request,'reg2.html')
    


# def home(request):
#     data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')

#     data=pd.read_csv(data_file_path)
    
#     return render (request,'home.html',{'data':data})
#     #return render(request, 'home.html')