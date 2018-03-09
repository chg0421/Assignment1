import plotly.offline as pf
# import plotly.plotly as py
# import plotly.graph_objs as go
# import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

# our X values:
emp_id =['B001','A001','C001','D001','E001','A003','A005','A007','B005']
print(emp_id)
# our Y values:
sales_values = [450,560,480,500,280,345,345,400,800]
plt.plot(emp_id, sales_values, '-b', label="A simple line")
plt.legend(loc='upper left')
plt.title("Sales Value for Employees")
# plt.legend(['A simple line'])
plt.xlabel('Employee ID')
plt.ylabel('Sales')
plt.show()

plt.plot(emp_id, sales_values, 'bo')
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv("test.csv")
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.hist(df['Sales'], bins=10)
# plt.title('Employee Sales Details')
# plt.xlabel('Employee ID')
# plt.ylabel('Sales')
# plt.show()


#pie Chart

emp_data = {
    'data': [{'labels': ['A001','B002','C444','A222'],
              'values': [45000,25000,10000,35000],
              'type': 'pie'}],
    'layout': {
        'title': '---Employees salary details---'}
}

pf.plot(emp_data)
