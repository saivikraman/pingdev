# import pandas as pd
# import os

# def reset_down_time(data_file_path):
#     data = pd.read_csv(data_file_path)
#     ips = data.ip_address

#     for ip_address in ips:
#         data.loc[data['ip_address'] == ip_address, 'Down_Time'] = 0

#     data.to_csv(data_file_path, index=False)

# # Call the function with the path to the CSV file you want to update
# data_file_path1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'data.csv')
# reset_down_time(data_file_path1)
