import plotly.plotly as py
import plotly.graph_objs as go

emp_id = ['A001','B002','C444','A222']
salary = [45000,25000,10000,35000]

trace = go.Pie(labels=emp_id, values=salary)

py.iplot([trace], filename='pie_chart')